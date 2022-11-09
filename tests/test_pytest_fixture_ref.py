import pytest
from _pytest.tmpdir import tmp_path

from pytest_fixture_ref import make_test_with_fixtures


@pytest.fixture
def fix_w_yield1():
    print("before_yield_1")
    yield
    print("after_yield_1")


@pytest.fixture
def fix_w_yield2():
    print("before_yield_2")
    yield
    print("after_yield_2")


@make_test_with_fixtures()
def test_bar1(f1=fix_w_yield1, f2=fix_w_yield2, tmp=tmp_path):
    print("test_bar")
    print(f"{tmp}")
    assert tmp.exists()


@make_test_with_fixtures(f1=fix_w_yield1, f2=fix_w_yield2, tmp=tmp_path)
def test_bar2(f1, f2, tmp):
    print("test_bar")
    print(f"{tmp}")
    assert tmp.exists()
