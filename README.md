# django_website_boilerplate

This is a simple boilerplate meant to speed up time-to-market for a basic website with the usual homepage, about, services, support and 
contact pages. I have realised I am wasting time doing the same things over and over again, same pages, same views, same urls with the 
only different thing being the project names and a little extra functionality.

To use this project, clone or download the zip file. Create a virtualenv and install required packages from requirements.txt. Run migrations
and run python manage.py test websites.tests. If all tests pass, you are good to go. Simply edit the frontend to suit your needs py playing
around with base.html located in templates/website and the css files located in static/website/css to achieve this.

Add content and you have a Django website ready to be deployed. Just make sure to change SECRET_KEY, email settings, database settings and 
DEBUG values before deployment.

Good luck!
