SECRET_KEY = 'django-insecure-6so8s^h=a19!-af_)4ody80-lgxgx0alky#-mr+$wgefs!-uw9'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'Kristie89$!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}