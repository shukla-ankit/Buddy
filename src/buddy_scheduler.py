from typing import List
from random import seed, random


class BuddyScheduler:
    def __init__(self, list_team_members_names: List[str], n_days: int):
        self.n_days = n_days
        self.list_team_members_names = list_team_members_names.copy()
        self.list_team_members_names.sort()
        self.all_unique_permutations = []

    def permuteUnique(self):
        list_member_names: List[str] = []
        used = [False] * len(self.list_team_members_names)
        self.permute(list_member_names, used)

    def permute(self, list_member_names: List[str], used: List[bool]):
        if len(self.list_team_members_names) == len(list_member_names):
            self.all_unique_permutations.append(list_member_names)
            return
        for i in range(len(self.list_team_members_names)):
            if used[i] is False:
                if i == 0 or self.list_team_members_names[i-1] != self.list_team_members_names[i] or used[i - 1]:
                    used[i] = True
                    list_member_names.append(self.list_team_members_names[i])
                    self.permute(list_member_names, used)
                    used[i] = False
                    list_member_names.pop(len(list_member_names) - 1)

    def random_pair_generator(self) -> List[List[str]]:
        schedule: List[List[str]] = []
        self.permuteUnique()
        seed(7)
        list_exists = []
        for i in range(self.n_days):
            if len(list_exists) == i:
                list_exists.clear()
            r = random() // len(self.list_team_members_names)
            while r in list_exists:
                r = random() // len(self.list_team_members_names)
            list_exists.append(r)
            schedule.append(self.all_unique_permutations[r])
        return schedule
