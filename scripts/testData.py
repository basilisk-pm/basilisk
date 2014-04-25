from code_viewer.models import Repo

r=Repo(repo_type="git",repo_url="https://github.com/nyxcharon/code-tracker.git",repo_name="Code-Tracker",repo_location="~/git/code-tracker")

r.save()

