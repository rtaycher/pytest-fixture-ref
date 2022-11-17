import inspect
import textwrap


def using_fixtures_from_defaults(fn):
    """
    Pass fixtures to test/fixture via default value

    example:

    @using_fixtures_from_defaults
    def test_bar1(_=fix_w_yield1, __=fix_w_yield2, tmp=tmp_path):
        assert tmp.exists()

    """

    signature = inspect.signature(fn)
    keyword_names_to_fixtures = {k: v.default for k, v in signature.parameters.items()}
    assert all(
        v is not inspect.Parameter.empty for v in keyword_names_to_fixtures.values()
    ), "every parameter should have a matching fixture function provided as the default value"
    keyword_names_to_fixture_names = {
        k: f.__name__ for (k, f) in keyword_names_to_fixtures.items()
    }
    fixture_names = keyword_names_to_fixture_names.values()

    z = textwrap.dedent(
        f"""\
    def test_func({', '.join(fixture_names)}):
        return fn({', '.join(kname + '=' + fname for (kname, fname) in keyword_names_to_fixture_names.items())})
    """
    )
    scope = dict(fn=fn)
    exec(z, scope)
    test_func = scope["test_func"]
    test_func.__name__ = fn.__name__
    return test_func


def using_fixtures_from_kwargs(**fixture_kwargs):
    """
    Pass fixtures to test/fixture via decorator kwargs

    example:

    @using_fixtures_from_kwargs(_=fix_w_yield1, __=fix_w_yield2, tmp=tmp_path)
    def test_bar2(_, __, tmp):
        assert tmp.exists()

    """

    def inner(fn):
        signature = inspect.signature(fn)
        keyword_names_to_fixtures = {
            k: fixture_kwargs.get(k, None) or v.default
            for k, v in signature.parameters.items()
        }
        assert all(
            v is not inspect.Parameter.empty for v in keyword_names_to_fixtures.values()
        ), (
            "every parameter should have a matching fixture function "
            "provided in either the decorator or default function"
        )
        keyword_names_to_fixture_names = {
            k: f.__name__ for (k, f) in keyword_names_to_fixtures.items()
        }
        fixture_names = keyword_names_to_fixture_names.values()

        z = textwrap.dedent(
            f"""\
        def test_func({', '.join(fixture_names)}):
            return fn({', '.join(kname + '=' + fname for (kname, fname) in keyword_names_to_fixture_names.items())})
        """
        )
        scope = dict(fn=fn)
        exec(z, scope)
        test_func = scope["test_func"]
        test_func.__name__ = fn.__name__
        return test_func

    return inner
