# Team Member

class Member:
    def __init__(self, f_name: str, l_name: str, email: str):
        self.__f_name = f_name
        self.__l_name = l_name
        self.__email = email
        self.__is_subscribed = True

    def get_full_name(self):
        return self.__f_name + ' ' + self.__l_name

    def subscribe(self):
        self.__is_subscribed = True

    def unsubscribe(self):
        self.__is_subscribed = False

    def has_subscribed(self):
        return self.__is_subscribed

    def get_email(self):
        return self.__email
