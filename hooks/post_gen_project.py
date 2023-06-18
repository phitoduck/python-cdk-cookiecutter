"""
Execute after project is generated.

Learn about CookieCutter "hooks" like this one here:
https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html

The current working directory is the root of the generated project when this runs.
"""

from pathlib import Path
import subprocess
import os
import sys


REPO_NAME = '{{ cookiecutter.repo_name }}'
REPO_ROOT_DIR = Path.cwd()

def main():
    run_git_init(repo_root_dir=REPO_ROOT_DIR)
    commit_all_files(repo_root_dir=REPO_ROOT_DIR)
    create_version_txt_symlinks(repo_root_dir=REPO_ROOT_DIR)
    execute_pre_commit(repo_root_dir=REPO_ROOT_DIR)


def run_git_init(repo_root_dir: Path):
    """
    Run `git init` in the root of the generated project.
    """
    subprocess.run(["git", "init"], check=True, stdout=subprocess.DEVNULL, cwd=repo_root_dir)


def commit_all_files(repo_root_dir: Path):
    """
    Run `git add -A` and `git commit -m "Initial commit"` in the root of the generated project.
    """
    subprocess.run(["git", "add", "--all"], check=True, stdout=subprocess.DEVNULL, cwd=repo_root_dir)
    

def create_version_txt_symlinks(repo_root_dir: Path):
    """
    Create the following symlinks:

    - `infrastructure/VERSION.txt` -> `../VERSION.txt`
    - `repo_name/VERSION.txt` -> `../VERSION.txt`
    """
    source_version_txt_fpath = "../VERSION.txt"

    # infrastructure/VERSION.txt -> ../VERSION.txt
    infra_version_target = repo_root_dir / 'infrastructure' / 'VERSION.txt'
    create_symlink(source_version_txt_fpath, infra_version_target)

    # repo_name/VERSION.txt -> ../VERSION.txt
    repo_version_target = repo_root_dir / REPO_NAME / 'VERSION.txt'
    create_symlink(source_version_txt_fpath, repo_version_target)


def create_symlink(source_path: Path, target_path: Path):
    if target_path.exists():
        target_path.unlink()

    os.symlink(source_path, target_path)


def execute_pre_commit(repo_root_dir: Path):
    """Execute `pre-commit install` in the root of the generated project."""
    # install pipx
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'pipx'], check=True, stdout=subprocess.DEVNULL, cwd=repo_root_dir)
    # install pre-commit with pipx and run it against all files
    subprocess.run([sys.executable, '-m', 'pipx', 'run', 'pre-commit', 'run', '--all-files'], stdout=subprocess.DEVNULL, cwd=repo_root_dir)
    subprocess.run(["git", "add", "--all"], check=True, stdout=subprocess.DEVNULL, cwd=repo_root_dir)


if __name__ == '__main__':
    main()
