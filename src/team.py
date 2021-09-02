from typing import Dict
from member import Member

# Team


class Team:
    def __init__(self, team_name: str):
        self.name = team_name
        self.dict_members: Dict[str, Member] = {}

    def get_name(self):
        return self.name

    def set_name(self, team_name: str):
        self.name = team_name

    def add_member(self, f_name: str, l_name: str, email: str):
        idx = self.dict_members[email] = Member(f_name, l_name, email)

    def add_members_by_json(self, members_json: str):
        for elem in members_json['Members']:
            self.add_member(elem['f_name'], elem['l_name'], elem['email'])

    def remove_by_email(self, email: str):
        idx = self.dict_members.get(email)
        if idx is not None:
            del self.dict_members[email]

    def unsubscribe_by_email(self, email: str):
        try:
            idx = self.dict_members.get(email)
            if idx is not None:
                self.dict_members[email].unsubscribe()
            else:
                raise Exception('Entered email {' + email + '} not found in existing employee pool!')
        except Exception as error:
            print('unsubscribe_by_email : ' + repr(error))

    def resubscribe_by_email(self, email: str):
        try:
            idx = self.dict_members.get(email)
            if idx is not None:
                self.dict_members[email].subscribe()
            else:
                raise Exception('Entered email {' + email + '} not found in existing employee pool!')
        except Exception as error:
            print('resubscribe_by_email : ' + repr(error))

    def print_team(self):
        print('\nTeam ', self.name, '\n--------------------------------------')
        for key in self.dict_members:
            if self.dict_members[key].get_subscription_status() is True:
                subscription_status = ' - '
            else:
                subscription_status = ' x '
            print(subscription_status + self.dict_members[key].get_full_name())

    def get_subscribed_team_members_names(self):
        list_team_members_names: str = []
        for key in self.dict_members:
            if self.dict_members[key].get_subscription_status() is True:
                list_team_members_names.append(self.dict_members[key].get_full_name())
        return list_team_members_names

