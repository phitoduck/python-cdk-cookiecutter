"""
Execute after project is generated.

Learn about CookieCutter "hooks" like this one here:
https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html
"""

# from pathlib import Path


# def create_version_txt_symlinks():
#     repo_name = '{{ cookiecutter.repo_name }}'

#     # Create symlink for infrastructure/VERSION.txt
#     infra_version_source = Path('../VERSION.txt')
#     infra_version_target = Path(repo_name) / 'infrastructure' / 'VERSION.txt'
#     create_symlink(infra_version_source, infra_version_target)

#     # Create symlink for repo_name/VERSION.txt
#     repo_version_source = Path('../VERSION.txt')
#     repo_version_target = Path(repo_name) / repo_name / 'VERSION.txt'
#     create_symlink(repo_version_source, repo_version_target)


# def create_symlink(source_path: Path, target_path: Path):
#     # Remove the existing target_path if it exists
#     if target_path.exists():
#         target_path.unlink()

#     # Create a symlink from source_path to target_path
#     target_path.symlink_to(source_path)


# if __name__ == '__main__':
#     create_version_txt_symlinks()
print("ran post gen hook!")

from pathlib import Path
THIS_DIR = Path(__file__).parent

Path("/Users/ericriddoch/repos/extra/python-cdk-cookiecutter/hi.md").write_text("hello world")
