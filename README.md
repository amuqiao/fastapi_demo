# 项目结构
```
fastapi_demo/
├── .gitignore          # Git忽略配置（Python虚拟环境、IDE缓存等）
├── .python-version     # 指定Python版本为3.12
├── pyproject.toml      # 依赖管理配置文件（uv工具生成）
├── uv.lock             # 依赖版本锁定文件
├── requirements.txt    # 导出的依赖列表（包含生产和开发依赖）
├── htmlcov/            # 测试覆盖率报告目录（pytest-cov生成）
├── .pytest_cache/      # pytest测试缓存目录
├── scripts/            # 脚本工具目录
│   ├── input/          # 原始数据输入目录（示例：raw_data.csv）
│   ├── output/         # 清洗后数据输出目录
│   └── run_cleaning.py # 数据清洗执行脚本
├── src/                # 核心源代码目录
│   ├── api/            # API服务模块
│   │   └── main.py     # FastAPI应用入口（定义基础路由）
│   ├── scripts/        # 业务脚本模块（待扩展）
│   └── tools/          # 工具模块
│       ├── decorators.py # 功能装饰器（含`measure`执行时间测量装饰器）
│       └── __init__.py   # 模块导出配置
└── tests/              # 测试目录
    ├── conftest.py     # pytest全局配置（添加项目根路径到Python搜索路径）
    ├── t1.py           # 示例测试文件（待填充具体测试用例）
    ├── test_scripts/   # 脚本模块测试目录（待扩展）
    └── test_tools/     # 工具模块测试目录
        └── test_measure.py # `measure`装饰器测试用例
```

# 环境准备
- 已安装Python 3.12（通过 .python-version 指定）
- 推荐使用虚拟环境（可选）：
  ```
    uv sync
  ```
- 激活虚拟环境（可选）：
  ```
    source .venv/bin/activate
  ```
# 运行项目
- 启动FastAPI服务器：
  ```
    uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
  ```
- 访问API文档：
  ```
    http://localhost:8000/docs
  ```

# 测试项目
- 运行所有测试用例：
  ```
    pytest
  ```
- 生成测试覆盖率报告：
  ```
    pytest --cov=src --cov-report=html
  ```
- 打开测试覆盖率报告：
  ```
    open htmlcov/index.html
  ```
# 脚本工具
- 数据清洗脚本：
  ```
    python scripts/run_cleaning.py
  ```   
