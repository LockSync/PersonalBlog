from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # every time a user is created ,
    # the UsersConfig will run
    # and every time UserConfig class runs
    # the ready function will run automatically
    def ready(self):
        import users.signals

