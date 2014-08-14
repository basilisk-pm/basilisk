Basilisk
============
[![Build Status](https://travis-ci.org/basiIisk/basilisk.svg?branch=master)](https://travis-ci.org/basiIisk/basilisk)
[![Build Status](https://readthedocs.org/projects/basilisk-django/badge/?version=latest)](https://readthedocs.org/projects/basilisk-django/)

Basilisk is an open source code management and bug tracking solution.  Still in initial development.    
Basilisk is currently using [Django](https://www.djangoproject.com/) with Postgres for the backend. It is themed with [Bootstrap](http://getbootstrap.com/) provided by [django-bootstrap3](https://github.com/dyve/django-bootstrap3). Git and SVN support is done via [GitPython](https://gitorious.org/git-python/) and [PySVN](http://pysvn.tigris.org/docs/pysvn_prog_guide.html) respectively. It will support all common versioning systems as well as be public or private facing. It will have fine grained user control, backup settings, custom styling, etc.

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
  * Easily store and retrieve media files, including support for Amazon S3
  * Change backup settings based on file size


