# 文物藏品保护修复平台

面向博物馆藏品建档、病害调查、修复方案编制、修复工序实施与展陈环境监控的一体化保护修复后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 藏品建档 | `collection` | 藏品档案 | 藏品编号、藏品名称、藏品类别 |
| 文物本体 | `relic` | 文物本体 | 文物编号、文物名称、文物级别 |
| 病害调查 | `disease` | 病害调查记录 | 调查编号、关联文物、病害类型 |
| 修复方案 | `scheme` | 修复方案 | 方案编号、关联文物、病害概况 |
| 修复工序 | `process` | 修复工序 | 工序编号、所属方案、工序名称 |
| 修复材料 | `material` | 修复材料 | 材料编号、材料名称、材料规格 |
| 环境监控 | `environment` | 环境监测记录 | 监测编号、监测点位、展厅名称 |
| 囊匣制作 | `box` | 囊匣 | 囊匣编号、关联文物、囊匣材质 |
| 三维扫描 | `scan` | 三维扫描记录 | 扫描编号、关联文物、扫描设备 |
| 拓片制作 | `rubbing` | 拓片 | 拓片编号、关联文物、拓片类型 |
| 展陈布置 | `exhibit` | 展陈项目 | 展陈编号、展览名称、展厅位置 |
| 借展运输 | `transport` | 借展运输单 | 运输编号、借展单位、展品清单 |
| 虫害防治 | `pest` | 虫害防治单 | 防治编号、防治区域、有害生物 |
| 保护验收 | `accept` | 保护验收单 | 验收编号、关联文物、验收项目 |
| 库房排架 | `shelf` | 库房排架 | 排架编号、库房名称、排架位置 |
| 提取使用 | `extract` | 提取单 | 提取编号、关联文物、提取事由 |
| 影像采集 | `photo` | 影像资料 | 影像编号、关联文物、拍摄视角 |
| 保护日志 | `log` | 保护日志 | 日志编号、记录对象、记录类型 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
