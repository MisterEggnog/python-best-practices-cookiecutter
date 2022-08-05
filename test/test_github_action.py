
def _get_github_dir(result):
	return result.project_path / ".github"

def test_remove_github_dir(cookies):
	result = cookies.bake()
	assert not _get_github_dir(result).is_dir()

def test_include_github_dir(cookies):
	result = cookies.bake({"github_action":"y"})
	assert _get_github_dir(result).is_dir()
