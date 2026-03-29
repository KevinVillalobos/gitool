from pathlib import Path
from git import Repo, InvalidGitRepositoryError

def get_repo(path: str = ".") -> Repo | None:
    """Returns the Git repo at the current path, or None if not found."""
    try:
        return Repo(path, search_parent_directories=True)
    except InvalidGitRepositoryError:
        return None

def find_all_repos(base_path: str) -> list[Repo]:
    """Finds all Git repos under a base directory."""
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