import pysvn

def checkout_svn_repo(username,password,repo_url,checkout_dir):
    client=pysvn.Client()
    client.set_default_username(username)
    client.set_default_password(password)
    client.checkout(repo_url,checkout_dir)

def update_svn_repo():
    return True

