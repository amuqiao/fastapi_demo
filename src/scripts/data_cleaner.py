# src/scripts/data_cleaner.py
import csv
from typing import List, Dict

def clean_csv(input_path: str, output_path: str) -> None:
    """
    清洗 CSV 数据并保存到输出路径

    参数:
        input_path (str): 输入 CSV 文件路径
        output_path (str): 输出 CSV 文件路径
    """
    required_fields = ["姓名", "年龄", "注册时间"]
    cleaned_data: List[Dict[str, str]] = []

    with open(input_path, "r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)

        if not set(required_fields).issubset(reader.fieldnames or []):
            raise ValueError(f"输入文件缺少必要列: {required_fields}")

        for row in reader:
            if not row.get("年龄") or not row["年龄"].strip():
                continue

            raw_date = row["注册时间"]
            formatted_date = raw_date.replace("/", "-") if raw_date else ""
            row["注册时间"] = formatted_date

            cleaned_row = {k: row[k] for k in required_fields}
            cleaned_data.append(cleaned_row)

    with open(output_path, "w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=required_fields)
        writer.writeheader()
        writer.writerows(cleaned_data)

    print(f"数据清洗完成，结果保存至: {output_path}")
