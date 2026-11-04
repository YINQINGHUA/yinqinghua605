/**
 * ============================================================
 * yqh_tab.js —— 通用 Tab 选项卡组件（可复用）
 * ------------------------------------------------------------
 * 作者：尹清华（24002120605）   建立时间：2026-11-04   使用大模型：GLM-5.3-Flash
 *
 * 用法：页面上任意一个容器，内部包含若干 .yqh_tab（选项卡按钮）
 *       与数量一一对应的 .yqh_panel（内容面板），然后调用：
 *         yqh_initTabs(容器元素);
 *       容器加 data-yqh-tabs 属性时，页面加载后会自动初始化，
 *       同一页面可放多个选项卡组件，互不影响（可复用）。
 * ============================================================
 */

/**
 * 初始化一个选项卡组件，为选项卡绑定切换逻辑
 * @param {HTMLElement} yqh_root 选项卡组件的容器元素
 * @returns {{activate: Function}|null} 返回控制对象，可通过 activate(下标) 手动切换；容器无效时返回 null
 */
function yqh_initTabs(yqh_root) {
    if (!yqh_root) {
        return null;
    }

    var yqh_tabs = yqh_root.querySelectorAll(".yqh_tab");     // 所有选项卡按钮
    var yqh_panels = yqh_root.querySelectorAll(".yqh_panel"); // 所有内容面板

    /**
     * 切换到指定下标的选项卡：先清除所有选项卡与面板的选中状态，再设置当前元素的选中状态
     * @param {number} yqh_index 要选中的选项卡下标（从 0 开始）
     */
    function yqh_activate(yqh_index) {
        // 第一步：清除所有选项卡的选中状态，并隐藏所有面板
        yqh_tabs.forEach(function (yqh_tab, yqh_i) {
            yqh_tab.classList.remove("yqh_active");
            yqh_tab.setAttribute("aria-selected", "false");
            yqh_panels[yqh_i].classList.remove("yqh_active");
            yqh_panels[yqh_i].hidden = true;
        });

        // 第二步：设置当前元素的选中状态，并显示对应面板
        var yqh_curTab = yqh_tabs[yqh_index];
        var yqh_curPanel = yqh_panels[yqh_index];
        yqh_curTab.classList.add("yqh_active");
        yqh_curTab.setAttribute("aria-selected", "true");
        yqh_curPanel.classList.add("yqh_active");
        yqh_curPanel.hidden = false;
    }

    // 为每个选项卡按钮绑定点击监听事件，点击后切换到对应下标的面板
    yqh_tabs.forEach(function (yqh_tab, yqh_index) {
        yqh_tab.addEventListener("click", function () {
            yqh_activate(yqh_index);
        });
    });

    // 组件初始化时默认选中第一个选项卡（国内新闻）
    yqh_activate(0);

    // 返回控制对象，外部可调用 activate 手动切换，方便复用
    return { activate: yqh_activate };
}

// 页面加载完成后，自动初始化所有带 data-yqh-tabs 属性的选项卡组件
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-yqh-tabs]").forEach(function (yqh_root) {
        yqh_initTabs(yqh_root);
    });
});

