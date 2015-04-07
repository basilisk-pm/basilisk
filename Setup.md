Setup Instructions
============================

Assumes you are using Ubuntu 14.04  
1. sudo apt-get install python-dev python-pip  
2. git clone this repo, setup your .profile to export your secret key to point to the variable secret_KEY*  
3. sudo pip install -r requirements.txt   
4. ./manage.py makemigrations   
5. ./manage.py migrate      
6. ./manage.py runserver  

*Like so:
```
export secret_KEY='somelongsecretkey'
```

For the admin user to be setup  
1. ./manage.py createsuperuser  
2. Login to the adminstrative panel (/admin) and add the superuser as a new UserProfile object.  
  


