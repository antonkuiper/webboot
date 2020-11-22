# https://asdkazmi.medium.com/deploying-flask-app-with-wsgi-and-apache-server-on-ubuntu-20-04-396607e0e40f
import sys 
sys.path.insert(0, '/var/www/html/flaskapp')
from flaskapp import app as application
