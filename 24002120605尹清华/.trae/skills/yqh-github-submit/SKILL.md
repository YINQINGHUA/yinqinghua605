---
name: yqh-github-submit
description: 将本课程作业项目 git commit 并 push 到 GitHub 仓库 YINQINGHUA/yinqinghua605，SSH 公钥认证，免令牌。凡用户要求提交、推送到 GitHub、同步代码到 github.com 时使用；Gitee 推送流程不适用本技能。
---

# GitHub 提交推送流程

仓库远程（SSH，用已配置的公钥认证，不用 HTTPS+令牌）：

```
git@github.com:YINQINGHUA/yinqinghua605.git
```

本地 remote 名固定为 `github`，分支为 `master`。`origin` 是 Gitee，勿改动、勿混淆。

## SSH 密钥

- 私钥 `C:\Users\Lenovo\.ssh\id_ed25519`，公钥 `id_ed25519.pub`（注释 yinqinghua-gitee），空口令，已加入 GitHub 账户。
- 认证自检：`ssh -T git@github.com`，成功时返回 `Hi YINQINGHUA!`（退出码 1 属正常，GitHub 恒如此）。
- 首次连接若卡在 host key 确认，先执行 `ssh-keyscan -t ed25519 github.com | Add-Content C:\Users\Lenovo\.ssh\known_hosts`。

## 提交流程

1. `git --no-pager status` 与 `git --no-pager diff` 核对变更；含敏感内容的文件（令牌、密钥、`.env`）绝不提交。
2. `git add` 按文件名逐个添加；用户明确说"提交全部"时才可 `git add -A`，添加后复查 status。
3. 提交信息用中文一行，说清本次改动目的；提交前如 pre-commit 钩子失败，修复后新建提交，不用 `--amend`。
4. 推送：`git push github master`（首次加 `-u`）。被拒时先 `git --no-pager fetch github` 分析分叉原因，仅经用户同意才可强推。
5. 验证：`git --no-pager log --oneline -3` 确认提交，必要时 `git --no-pager ls-remote github master` 比对本地与远程。

## 环境注意

- PowerShell 5.1 不支持 `&&`，多条命令用 `;` 连接或分开执行；git 输出一律加 `--no-pager`。
- SSH 认证失败时优先怀疑 known_hosts 与密钥权限，不要退回 HTTPS 令牌方案；任何令牌/密钥不得写入仓库文件。
- 仅在用户明确要求时 commit/push。
