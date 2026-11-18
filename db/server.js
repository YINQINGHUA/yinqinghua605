// 数据服务器：端口 3004，同时提供页面静态资源与 poems 数据接口
// 启动方式：在 db 目录下执行 node server.js，然后浏览器访问 http://localhost:3004/yqh-poems.html
const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const YQH_PORT = 3004;
// 站点根目录是 db 的上一级，这样根目录里的 html、图片都能被访问到
const YQH_ROOT = path.join(__dirname, '..');

// yqh_readPoems：同步读取 db.json，返回其中的 poems 数组
function yqh_readPoems() {
  const yqhRaw = fs.readFileSync(path.join(__dirname, 'db.json'), 'utf-8');
  const yqhData = JSON.parse(yqhRaw);
  return yqhData.poems || [];
}

// 静态资源：把仓库根目录当作站点根，html / css / 图片都能直接访问
app.use(express.static(YQH_ROOT));

// 接口：GET /api/poems 返回全部诗词数据（含 pic、title、content）
app.get('/api/poems', function (yqhReq, yqhRes) {
  try {
    const yqhPoems = yqh_readPoems();
    // 允许跨域，方便页面用 file:// 打开时也能调试
    yqhRes.setHeader('Access-Control-Allow-Origin', '*');
    yqhRes.json(yqhPoems);
  } catch (yqhErr) {
    yqhRes.status(500).json({ error: '读取 db.json 失败：' + yqhErr.message });
  }
});

app.listen(YQH_PORT, function () {
  console.log('数据服务器已启动：http://localhost:' + YQH_PORT);
  console.log('页面地址：http://localhost:' + YQH_PORT + '/yqh-poems.html');
  console.log('数据接口：http://localhost:' + YQH_PORT + '/api/poems');
});
