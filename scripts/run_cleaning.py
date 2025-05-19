from pathlib import Path
import sys
# scripts/run_cleaning.py
from pathlib import Path
import sys

# 添加项目根目录到Python路径
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.scripts.data_cleaner import clean_csv


"""
fastapi_demo/scripts/input/raw_data.csv 示例内容：

姓名,年龄,注册时间,备注
张三,,2023/05/10,测试用户
李四,25,2023/06/15,有效用户
王五,30,,无效时间
赵六,28,2023/07/20,有效用户
"""

if __name__ == "__main__":
    input_path = "scripts/input/raw_data.csv"
    output_path = "scripts/output/cleaned_data.csv"

    # 创建输出目录（如果不存在）
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    clean_csv(input_path, output_path)


