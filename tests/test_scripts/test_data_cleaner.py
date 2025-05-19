import csv
import os
import pytest
from src.scripts.data_cleaner import clean_csv
from tempfile import NamedTemporaryFile


def test_clean_csv():
    # 创建临时输入文件
    input_data = [
        {"姓名": "张三", "年龄": "", "注册时间": "2023/05/10", "备注": "测试用户"},
        {"姓名": "李四", "年龄": "25", "注册时间": "2023/06/15", "备注": "有效用户"},
        {"姓名": "王五", "年龄": "30", "注册时间": "", "备注": "无效时间"},
        {"姓名": "赵六", "年龄": "28", "注册时间": "2023/07/20", "备注": "有效用户"}
    ]
    with NamedTemporaryFile(mode='w', encoding='utf-8', delete=False, newline='') as infile:
        writer = csv.DictWriter(infile, fieldnames=input_data[0].keys())
        writer.writeheader()
        writer.writerows(input_data)
        input_path = infile.name

    # 创建临时输出文件
    with NamedTemporaryFile(mode='w', encoding='utf-8', delete=False, newline='') as outfile:
        output_path = outfile.name

    try:
        # 调用 clean_csv 函数
        clean_csv(input_path, output_path)

        # 验证输出文件内容
        with open(output_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            output_data = list(reader)

        assert len(output_data) == 3
        for row in output_data:
            assert row["年龄"].strip() != ""
            if row["注册时间"]:
                assert "/" not in row["注册时间"]

    finally:
        # 删除临时文件
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)


def test_clean_csv_missing_columns():
    # 创建缺少必要列的临时输入文件
    input_data = [
        {"姓名": "张三", "备注": "测试用户"}
    ]
    with NamedTemporaryFile(mode='w', encoding='utf-8', delete=False, newline='') as infile:
        writer = csv.DictWriter(infile, fieldnames=input_data[0].keys())
        writer.writeheader()
        writer.writerows(input_data)
        input_path = infile.name

    # 创建临时输出文件
    with NamedTemporaryFile(mode='w', encoding='utf-8', delete=False, newline='') as outfile:
        output_path = outfile.name

    try:
        # 调用 clean_csv 函数，期望抛出 ValueError
        with pytest.raises(ValueError):
            clean_csv(input_path, output_path)
    finally:
        # 删除临时文件
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)
