def _docker_files(path):
    return map(lambda f: path / f, ["Dockerfile", ".dockerignore"])


def _test_docker_do_not_exists(result):
    for file in _docker_files(result.project_path):
        assert not file.is_file()


def _test_docker_exists(result):
    for file in _docker_files(result.project_path):
        assert file.is_file()


def test_does_not_include_docker_by_default(cookies):
    result = cookies.bake()
    _test_docker_do_not_exists(result)


def test_does_include_docker(cookies):
    for i in ["y", "Y"]:
        result = cookies.bake(extra_context={"add_docker": i})
        _test_docker_exists(result)
