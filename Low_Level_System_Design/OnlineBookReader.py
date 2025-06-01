

class User:
    def __init__(self, name: str, address: str, date_of_birth: int, msc: dict, password: str):
        self.name = name
        self.address = address
        self.date_of_birth = date_of_birth
        self.msc = msc
        self.password = password

        self.books = {}


class Login:
    def __init__(self):
        self.curr_users = []
        self.logged_users = []


# class System:
#     def __init__(self):
#         self.curr_users = []
#         self.logged_users = []
#
#     def login(self, user_name, password):
#         if self.user_exist(user_name):
#             user = self.get_user(user_name)
#
#             if self.user_logged_in(user):
#
#         return True


class Book:
    def __init__(self, name, isbn):
        name = name
        isbn = isbn
