# import functools
#
# user = {'username': 'julien123', 'access_level': 'admin'}
#
#
# def user_has_permission(func):
#     @functools.wraps(func)
#     def secure_func(*args, **kwargs):
#         if user.get('access_level') == 'admin':
#             return func(*args, **kwargs)
#     return secure_func
#
#
# @user_has_permission
# def my_function(panel):
#     """
#     Allowus to retrieve the password for the admin panel
#     """
#     return f'Password for {panel} panel is 1234.'
#
#
# @user_has_permission
# def another():
#     pass
#
#
# print(my_function.__name__)
# print(my_function('movies'))
# print(another())


# --------------------------


"""
Implement a @access_control decorator that can be used like this:
@access_control(access_level)
def delete_some_file(filename):
    # perform the deletion operation
    print('{} is deleted!'.format(filename))
Your decorator should meet the following requirements:
- It takes in an argument `access_level` and would compare the current user's role with the access level.
- You can get the current user's role, represented by an integer, by calling the `get_current_user_role()` function.
    You don't need to implement this function, we will take care of it for you.
- You may assume smaller access level value would have higher privilege. For example, 0 - admin, 1 - user, 2 - guest.
    So you can check if the user has proper access level like this:
if get_current_user_role() <= access_level:
    # do something
else:
    # forbid
- If the user has the proper access level, we allow the user to call the function (that has this decorator).
- If the user does not have a proper access level, we raise a `PermissionError` with the message:
    'You do not have the proper access level.'
- The decorator should be generic, which means it can be applied to any function that has any amount of
    arguments (or key word arguments).
- Your decorator should keep the original function's `__name__` and `__doc__` strings.
"""

# DO NOT CHANGE
# def get_current_user_role() -> int:
#     # return the current user's role, represented by an int
#     # for example, 0 - admin, 1 - user, 2 - guest
#     # You don't need to change this function, we will replace it with a real function that returns the user's role
#     return 0
from functools import wraps


def access_control(access_level: int):
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            if get_user_role() <= access_level:
                return func(*args, **kwargs)
            else:
                raise PermissionError('You do not have the proper access level.')

        return inner_wrapper

    return outer_wrapper


def get_user_role() -> int:
    return 0


@access_control(0)
def delete_file(filename):
    # perform the deletion operation
    print(f'{filename} is deleted')


delete_file('test')



