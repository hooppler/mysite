# mysite
This is DjangoCMS example repository

# Developer Loal Configuration

1. Clone the code.
   > git clone git@github.com:hooppler/mysite.git
2. Configure database settings.
3. Make migrations.
   > python manage.py migrate
4. Create supperuser.
   > python manage.py createsuperuser
6. Run server from paretn folder of mysite
   > python mysite/manage.py runserver

## Development
STATIC_ROOT is useless during development, it's only required for deployment.

While in development, STATIC_ROOT does nothing. You don't even need to set it. Django looks for static files inside each app's directory (myProject/appName/static) and serves them automatically.

This is the magic done by manage.py runserver when DEBUG=True.

## Deployment
When your project goes live, things differ. Most likely you will serve dynamic content using Django and static files will be served by Nginx. Why? Because Nginx is incredibly efficient and will reduce the workload off Django.

This is where STATIC_ROOT becomes handy, as Nginx doesn't know anything about your Django project and doesn't know where to find static files.

So you set STATIC_ROOT = '/some/folder/' and tell Nginx to look for static files in /some/folder/. Then you run manage.py collectstatic and Django will copy static files from all the apps you have to /some/folder/.

Extra directories for static files
STATICFILES_DIRS is used to include additional directories for collectstatic to look for. For example, by default, Django doesn't recognize /myProject/static/. So you can include it yourself.

## Example
STATIC_URL = '/static/'

if not DEBUG:
    STATIC_ROOT = '/home/django/www-data/example.com/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]
