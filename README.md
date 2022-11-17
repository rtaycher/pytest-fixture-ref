# pytest fixture ref

[![PyPI](https://img.shields.io/pypi/v/pytest-fixture-ref?style=flat-square)](https://pypi.python.org/pypi/pytest-fixture-ref/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pytest-fixture-ref?style=flat-square)](https://pypi.python.org/pypi/pytest-fixture-ref/)
[![PyPI - License](https://img.shields.io/pypi/l/pytest-fixture-ref?style=flat-square)](https://pypi.python.org/pypi/pytest-fixture-ref/)
[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)


---

**Documentation**: [https://rtaycher.github.io/pytest-fixture-ref](https://rtaycher.github.io/pytest-fixture-ref)

**Source Code**: [https://github.com/rtaycher/pytest-fixture-ref](https://github.com/rtaycher/pytest-fixture-ref)

**PyPI**: [https://pypi.org/project/pytest-fixture-ref/](https://pypi.org/project/pytest-fixture-ref/)

---

## Let developers reference pytest fixtures without name matching magic.

Pass fixtures via default value or decorator args instead of magic strings.

Let me admit this is a bit of a hack.
It might be important to note that this still uses pytests usual magic string matching under the covers
by grabbing the function name and re-writing the function.
That means you do have to make sure pytest imports it by installing it/specifying it in pytest_plugins/etc
as well as importing it for reference.
It also means this technically works with fake/dummy functions with the same name
(in case you can't easily import some fixtures)



example:

    from pytest_fixture_ref import using_fixtures_from_defaults, using_fixtures_from_kwargs

    @using_fixtures_from_defaults
    def test_bar1(_=fix_w_yield1, __=fix_w_yield2, tmp=tmp_path):
        assert tmp.exists()


    @using_fixtures_from_kwargs(_=fix_w_yield1, __=fix_w_yield2, tmp=tmp_path)
    def test_bar2(_, __, tmp):
        assert tmp.exists()


You can also use it to reference fixtures from other fixtures

    @pytest.fixture
    def first_entry():
        return "a"


    @pytest.fixture
    @using_fixtures_from_defaults
    def order(fe=first_entry):
        return [fe]

## Installation

```sh
pip install git+https://github.com/rtaycher/pytest-fixture-ref.git

```

## Development

* Clone this repository
* Requirements:
  * [Poetry](https://python-poetry.org/)
  * Python 3.7+
* Create a virtual environment and install the dependencies

```sh
poetry install
```

* Activate the virtual environment

```sh
poetry shell
```

### Testing

```sh
pytest
```

### Documentation

The documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings
 of the public signatures of the source code. The documentation is updated and published as a [Github project page
 ](https://pages.github.com/) automatically as part each release.

### Releasing

Trigger the [Draft release workflow](https://github.com/rtaycher/pytest-fixture-ref/actions/workflows/draft_release.yml)
(press _Run workflow_). This will update the changelog & version and create a GitHub release which is in _Draft_ state.

Find the draft release from the
[GitHub releases](https://github.com/rtaycher/pytest-fixture-ref/releases) and publish it. When
 a release is published, it'll trigger [release](https://github.com/rtaycher/pytest-fixture-ref/blob/master/.github/workflows/release.yml) workflow which creates PyPI
 release and deploys updated documentation.

### Pre-commit

Pre-commit hooks run all the auto-formatters (e.g. `black`, `isort`), linters (e.g. `mypy`, `flake8`), and other quality
 checks to make sure the changeset is in good shape before a commit/push happens.

You can install the hooks with (runs for each commit):

```sh
pre-commit install
```

Or if you want them to run only for each push:

```sh
pre-commit install -t pre-push
```

Or if you want e.g. want to run all checks manually for all files:

```sh
pre-commit run --all-files
```

---

This project was generated using the [wolt-python-package-cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter) template.
