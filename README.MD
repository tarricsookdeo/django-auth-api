# django-auth-api

This is an example project on how to use `dj-rest-auth` along with `django-allauth`, `djangorestframework` to create a token authentication system.

## Requirements

- Django 3+
- Python 3.7+

## Setup

- Clone the repository
- Create a `.env` file in the `api` directory, the same directory where `settings.py` is located. Inside of the `.env` file add the following vars:
  - SECRET_KEY=`<django secret key>`
  - DEBUG=`<True if debug mode is on, leave blank if debug is off>`
  - ALLOWED_HOSTS=`<A comma seperate list of allowed hosts>`
  - EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
  - EMAIL_USE_TLS=True
  - EMAIL_HOST=`<smtp of the email host you want to use>`
  - EMAIL_HOST_USER=`<Email address of the host>`
  - EMAIL_HOST_PASSWORD=`<Password of the email address for the host>`
  - EMAIL_PORT=`<Email port number>`

Here is and example.env file for gmail accounts:

```
SECRET_KEY=django-insecure-oc5i6+x4jm9n)e5+i94$s#4txe6lcp+3(%30-&e?(!cz56&%5(
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
EMAIL_BACKEND =django.core.mail.backends.smtp.EmailBackend
EMAIL_USE_TLS=True
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=johndoe@gmail.com
EMAIL_HOST_PASSWORD=Pasword1234
EMAIL_PORT=587
```

Note that if you want a boolean vale to be false, leave the value in the `.env` file blank. eg:
``` 
DEBUG=
```
