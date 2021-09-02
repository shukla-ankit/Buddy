from typing import Dict
from member import Member

# Team


class Team:
    def __init__(self, team_name: str):
        self.__t_name = team_name
        self.__map_emails_to_members: Dict[str, Member] = {}

    def get_name(self):
        return self.__t_name

    def set_name(self, team_name: str):
        self.__t_name = team_name

    def add_member(self, f_name: str, l_name: str, email: str):
        try:
            if self.__is_email_taken(email) is False:
                self.__map_emails_to_members[email] = Member(f_name, l_name, email)
            else:
                raise Exception('Entered email {' + email + '} already exists in employee pool!')
        except Exception as error:
            print('add_member : ' + repr(error))
            exit(0)

    def add_members_by_json(self, members_json: str):
        try:
            for elem in members_json['Members']:
                if elem is not None:
                    if self.__is_email_taken(elem['email']) is False:
                        self.add_member(elem['f_name'], elem['l_name'], elem['email'])
                    else:
                        raise Exception('Entered email {' + elem['email'] + '} already exists in employee pool!')
        except Exception as error:
            print('add_members_by_json : ' + repr(error))
            exit(0)

    def remove_by_email(self, email: str):
        try:
            if self.__is_email_taken(email):
                del self.__map_emails_to_members[email]
            else:
                raise Exception('Entered email {' + email + '} not found in employee pool!')
        except Exception as error:
            print('remove_by_email : ' + repr(error))
            exit(0)

    def __is_email_taken(self, email: str):
        if self.__map_emails_to_members.get(email) is None:
            return False
        return True

    def __get_member(self, key: str):
        try:
            if self.__map_emails_to_members.get(key) is None:
                raise Exception('Entered email {' + key + '} not found in employee pool!')
            return self.__map_emails_to_members[key]
        except Exception as error:
            print('get_member : ' + repr(error))
            exit(0)

    def unsubscribe_by_email(self, email: str):
        self.self.__get_member(email).unsubscribe()

    def resubscribe_by_email(self, email: str):
        self.self.__get_member(email).subscribe()

    def get_subscribed_team_members_names(self):
        list_team_members_names: str = []
        for email in self.__map_emails_to_members:
            if self.__get_member(email).has_subscribed():
                list_team_members_names.append(self.__get_member(email).get_full_name())
        return list_team_members_names

    def print_team(self):
        print('\nTeam ', self.__t_name, ' (', str(len(self.__map_emails_to_members)),')\n--------------------------------------')
        for email in self.__map_emails_to_members:
            subscription_status = ' x '
            if self.__get_member(email).has_subscribed():
                subscription_status = ' - '
            print(subscription_status + self.__get_member(email).get_full_name())

