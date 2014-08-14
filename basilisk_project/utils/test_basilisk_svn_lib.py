from basilisk_svn_lib import checkout_svn_repo

print "Testing checkout of password protected repo"

checkout_svn_repo(username="bmartin4",password="kseksekse!",repo="https://svn.adonislinux.com/eos/launcher",checkout_location="test-svn")

print "Test finished"


