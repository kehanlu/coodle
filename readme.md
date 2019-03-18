## setup

### environment

```shell
# clone from GitHub
$ git clone https://github.com/kehanlu/coodle
$ cd coodle

# virtual environment
$ pip install virtualenv
$ virtualenv ENV
$ source ENV/bin/activate

# install pakages
(ENV) $ pip install -r requirements.txt
```

### django

```shell
(ENV) $ python manage.py migrate
(ENV) $ python manage.py collectstatic
(ENV) $ python manage.py createsuperuser
```

### django-allauth

> I only provide google login through django-allauth. You can use Django default User system instead of social login, adjust `account` app for your customized needs.

First, you should go to [Google console](https://console.developers.google.com) to create a credential for Oauth. The redirect URL is `http://127.0.0.1:8000/accounts/google/login/callback/`

Then, copy the `Client ID` and `Client secrect` and create a socialapp in Django admin page.

Finally, you can click the button on the site navbar and login with Google!

See document below for more details:
[Django-allauth Providers](https://django-allauth.readthedocs.io/en/latest/providers.html#google)
