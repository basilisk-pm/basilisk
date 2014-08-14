from git import Repo


def git_clone_repo(username,password,repo_url,checkout_dir):
    Repo.clone_from(repo_url,checkout_dir)
