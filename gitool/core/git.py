from pathlib import Path
from git import Repo, InvalidGitRepositoryError

def find_all_repos(base_path: str) -> list[Repo]:
    repos = []
    base = Path(base_path)
    if not base.exists():
        return repos
    for git_dir in base.rglob(".git"):
        if git_dir.is_dir():
            try:
                repos.append(Repo(git_dir.parent))
            except Exception:
                continue
    return repos