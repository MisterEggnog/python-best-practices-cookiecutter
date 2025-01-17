import re
from functools import reduce


def _includes_precommit_file(result):
    return result.project_path / ".pre-commit-config.yaml"


def test_default_include_file(cookies):
    result = cookies.bake()
    assert _includes_precommit_file(result).is_file()


def test_arg_not_include_file(cookies):
    for i in ["n", "N"]:
        result = cookies.bake({"precommit": i})
        assert not _includes_precommit_file(result).is_file()


def _file_contains_precommit(result):
    rexp = re.compile(r'^pre-commit = "\*"$')
    pipfile = open(result.project_path / "Pipfile")
    pip_lines = pipfile.readlines()
    pip_result = map(lambda l: l.strip(), pip_lines)
    pip_result = map(lambda l: rexp.match(l), pip_result)
    pip_result = map(lambda l: l is not None, pip_result)
    pip_result = any(pip_result)
    pipfile.close()
    return pip_result


def test_no_precommit_dependency(cookies):
    result = cookies.bake({"precommit": "N"})
    assert not _file_contains_precommit(result)


def test_precommit_dependency(cookies):
    result = cookies.bake()
    assert _file_contains_precommit(result)
