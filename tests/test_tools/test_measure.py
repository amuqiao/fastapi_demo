import time
import pytest
from src.tools.decorators import measure
import sys
from pathlib import Path
# 将项目根目录添加到 Python 搜索路径（假设当前文件路径为 tests/test_tools/test_measure.py）
# project_root = Path(__file__).resolve().parent.parent.parent
# sys.path.insert(0, str(project_root))


# 测试用辅助函数（被装饰的目标函数）


def sample_func(seconds: float = 0.1):
    """示例函数：模拟耗时操作"""
    time.sleep(seconds)
    return "完成"


@measure
def decorated_sample_func(seconds: float = 0.1):
    """被装饰的示例函数"""
    time.sleep(seconds)
    return "完成"


def test_measure_decorator_execution_time(capsys):
    """测试装饰器是否正确测量函数执行时间"""
    # 执行被装饰的函数（模拟耗时 0.1 秒）
    result = decorated_sample_func(0.1)

    # 验证函数返回值正确
    assert result == "完成"

    # 捕获 print 输出
    captured = capsys.readouterr()
    output = captured.out.strip()

    # 验证输出格式（如 "函数 decorated_sample_func 执行时间: 0.1005 秒"）
    assert "执行时间:" in output
    assert "秒" in output

    # 提取时间值并验证合理性（允许 ±0.02 秒误差）
    time_str = output.split(": ")[-1].replace(" 秒", "")
    execution_time = float(time_str)
    assert 0.08 <= execution_time <= 0.12  # 0.1秒 ±20ms 误差


def test_measure_decorator_preserves_metadata():
    """测试装饰器保留原函数元信息（使用 functools.wraps）"""
    # 验证 __name__ 和 __doc__ 与原函数一致
    assert decorated_sample_func.__name__ == "decorated_sample_func"
    assert decorated_sample_func.__doc__ == "被装饰的示例函数"


def test_measure_decorator_edge_case():
    """测试边界情况（极短执行时间）"""
    # 执行几乎无耗时的函数（模拟 0.001 秒）
    @measure
    def fast_func():
        time.sleep(0.001)
        return "快速完成"

    result = fast_func()
    assert result == "快速完成"
