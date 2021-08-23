import functools

user = {'username': 'julien123', 'access_level': 'admin'}


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user.get('access_level') == 'admin':
            return func(*args, **kwargs)
    return secure_func


@user_has_permission
def my_function(panel):
    """
    Allowus to retrieve the password for the admin panel
    """
    return f'Password for {panel} panel is 1234.'


@user_has_permission
def another():
    pass


print(my_function.__name__)
print(my_function('movies'))
print(another())
