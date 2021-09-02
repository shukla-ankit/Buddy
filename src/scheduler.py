from typing import List
from random import seed, random


class Scheduler:
    def __init__(self, list_team_members_names: List[str], n_days: int):
        if len(list_team_members_names) < 3:
            print('Please provide list team members count more than 3!')
            exit(0)
        self.__n_days = n_days
        self.__all_unique_permutations = []
        self.permuteUnique(list_team_members_names)

    def permuteUnique(self, t_list_team_members_names: List[str]):
        list_team_members_names = t_list_team_members_names.copy()
        list_team_members_names.sort()
        list_member_names: List[str] = []
        used = [False] * len(list_team_members_names)
        self.permute(list_team_members_names, list_member_names, used)
        print('Total permutations = ' + len(self.__all_unique_permutations))

    def permute(self, list_team_members_names: List[str], permutation_list_members_names: List[str], list_members_used_status: List[bool]):
        if len(list_team_members_names) == len(permutation_list_members_names):
            self.__all_unique_permutations.append(permutation_list_members_names.copy())
            print(permutation_list_members_names)
            return
        for i in range(len(list_team_members_names)):
            if list_members_used_status[i] is False:
                if i == 0 or list_team_members_names[i - 1] != list_team_members_names[i] or list_members_used_status[i - 1]:
                    list_members_used_status[i] = True
                    permutation_list_members_names.append(list_team_members_names[i])
                    self.permute(list_team_members_names, permutation_list_members_names, list_members_used_status)
                    list_members_used_status[i] = False
                    permutation_list_members_names.pop(len(permutation_list_members_names) - 1)

    def generate_schedule(self) -> List[List[str]]:
        schedule: List[List[str]] = []
        seed(7) # 7 is prime, so chosen for seed generation
        list_existing_indices = []
        for i in range(self.__n_days):
            if len(list_existing_indices) == i:
                list_existing_indices.clear()
            r = random() // len(self.__all_unique_permutations[0])
            while r in list_existing_indices:
                r = random() // len(self.__all_unique_permutations[0])
            list_existing_indices.append(r)
            schedule.append(self.__all_unique_permutations[r])
        return schedule
