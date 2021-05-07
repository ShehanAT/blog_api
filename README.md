### This app is now completed
* I have added these routes now:
    * /api/ping
    * /api/posts 
* I have added two unit tests in ```api/tests.py```
* Caching feature added to ```/api/ping``` route 

### Instructions for setting up locally:
* run ```pip install -r requirements.txt```
* go to ```{root_folder}\memcached-amd64``` and open ```memcached.exe``` to start caching server on Windows(if on other OS check out [this article](https://realpython.com/python-memcache-efficient-caching/))
* run ```python manage.py runserver```
