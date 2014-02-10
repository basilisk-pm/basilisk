Code-Tracker
============
An open source code management and bug tracking solution. 
Code-Tracker is currently using [Django](https://www.djangoproject.com/) and MySQL for the backend and is themed with [Bootstrap](http://getbootstrap.com/). It will support all common versioning systems as well as be public or private facing. It will have fine grained user control, backup settings, custom styling, etc.

###Goals
1. Easy to use code viewer
  * Syntax Highlighting
  * Highlight and Comment on Code
  * Link sections of codes to exisiting bugs
  * Support svn,git,etc
2. Fully Featured Bug Tracker
  * Easily reference exisiting code in a bug report
  * Upload videos 
  * Display syntax highlighted code snippets
  * Comprehensive comparison utlities - diff, unit test, etc
3. Easily store and keep track of media files
  * Keep a user specified number of backups of files
  * Easily store and retrieve media files
  * Change backup settings based on file size

###Pre-requisites 
####Packages:
On Fedora/RHEL/CentOS machines:
```bash
sudo yum install python-django python-devel python-pip mysql-devel mysql-server
```
On Ubuntu/Debian machines:
```
sudo apt-get install python-django python-pip mysql-client mysql-server
```
####Python lib:
Install the Mysql hook for python (all platforms):
```bash
sudo pip install MySQL-python
```
####Setup MySQL*
```mysql
mysql> create database codetracker;

mysql> grant all privileges on codetracker.* to 'django'@'localhost' identified by 'password';

mysql> exit;
```
*When you change the database/username/password, be sure to update the settings.py file with the correct information

