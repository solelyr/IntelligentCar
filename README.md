# IntelligentCar
IntelligentCar/
│
├── backend/                # Python 后端项目
│   ├── app/                # 主要后端代码目录
│   │   ├── __init__.py
│   │   ├── routes/         # 路由模块
│   │   ├── services/       # 业务逻辑层
│   │   ├── models/         # 数据模型
│   │   └── utils/          # 工具函数
│   ├── tests/              # 后端测试代码
│   ├── requirements.txt    # Python依赖包列表
│   ├── .env                # 环境变量配置
│   └── main.py             # 后端入口文件
│
├── frontend/               # React 前端项目
│   ├── src/                # 前端源码
│   ├── public/             # 静态资源
│   ├── package.json        # npm 配置
│   ├── vite.config.ts      # 如果用 Vite
│   └── tsconfig.json       # TypeScript配置
│
├── docker-compose.yml      # 可选：用于统一启动前后端（推荐）
├── .gitignore              # Git忽略文件
└── README.md               # 项目说明

# backend
python -m venv venv
source venv/bin/activate   # Windows 用 venv\Scripts\activate
pip install fastapi uvicorn
pip freeze > requirements.txt
uvicorn main:app --reload
deactivate

# frontend


