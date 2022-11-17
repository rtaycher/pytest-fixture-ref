import pytest
from _pytest.tmpdir import tmp_path

from pytest_fixture_ref import using_fixtures_from_defaults, using_fixtures_from_kwargs


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


@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
@using_fixtures_from_defaults
def order(fe=first_entry):
    return [fe]


@using_fixtures_from_defaults
def test_bar1(_=fix_w_yield1, __=fix_w_yield2, tmp=tmp_path):
    assert tmp.exists()


@using_fixtures_from_kwargs(_=fix_w_yield1, __=fix_w_yield2, tmp=tmp_path)
def test_bar2(_, __, tmp):
    assert tmp.exists()


@using_fixtures_from_kwargs(fe=order)
def test_first_order(fe):
    assert fe == ["a"]


if __name__ == "__main__":
    pytest.main([__file__])
