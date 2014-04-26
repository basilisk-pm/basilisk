import git, os, shutil
 
REMOTE_URL = "https://github.com/nyxcharon/code-tracker.git"
 
if os.path.isdir(DIR_NAME):
    shutil.rmtree(DIR_NAME)
 
os.mkdir(DIR_NAME)
 
git.Git().clone(REMOTE_URL)
 
print "---- DONE ----"
