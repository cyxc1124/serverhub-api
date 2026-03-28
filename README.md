# ServerHub API

ServerHub 服务器管理系统 — 后端 API 服务。

前端仓库：[serverhub-web](https://github.com/cyxc1124/serverhub-web)

## 技术栈

- **框架**: FastAPI
- **ORM**: SQLAlchemy 2.0
- **数据库迁移**: Alembic
- **认证**: JWT (python-jose + passlib)
- **数据库支持**: MySQL / MariaDB / PostgreSQL

## 项目结构

```
serverhub-api/
├── app/
│   ├── api/            # API 路由 (auth, users, servers)
│   ├── core/           # 配置、安全 (JWT, bcrypt)
│   ├── db/             # 数据库连接与 Base
│   ├── models/         # ORM 模型
│   ├── schemas/        # Pydantic 请求/响应模型
│   └── services/       # 业务逻辑
├── alembic/            # 数据库迁移脚本
├── .env.example        # 配置示例
├── requirements.txt    # Python 依赖
└── run.py              # 启动入口
```

## 快速开始

```bash
# 创建虚拟环境
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# 安装依赖
pip install -r requirements.txt

# 复制配置文件并修改数据库信息
copy .env.example .env       # Windows
# cp .env.example .env       # Linux/Mac

# 启动服务 (默认 http://localhost:8000)
python run.py
```

## 数据库配置

在 `.env` 中修改 `DB_TYPE` 切换数据库：

| DB_TYPE      | 默认端口 | 说明 |
|-------------|---------|------|
| `postgresql` | 5432    | PostgreSQL |
| `mysql`      | 3306    | MySQL |
| `mariadb`    | 3306    | MariaDB |

## API 文档

启动服务后访问：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
