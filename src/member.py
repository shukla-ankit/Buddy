# Team Member

class Member:
    def __init__(self, f_name: str, l_name: str, email: str):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.is_subscribed = True

    def get_full_name(self):
        return self.f_name + ' ' + self.l_name

    def subscribe(self):
        self.is_subscribed = True

    def unsubscribe(self):
        self.is_subscribed = False

    def get_subscription_status(self):
        return self.is_subscribed

    def get_email(self):
        return self.email

