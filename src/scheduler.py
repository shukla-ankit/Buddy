from typing import List
from random import seed, randint


class Scheduler:
    def __init__(self, list_team_members_names: List[str], n_days: int):
        if len(list_team_members_names) < 3:
            print('Please provide list team members count more than 3!')
            exit(0)
        self.__n_days = n_days
        self.__all_unique_permutations = []
        self.permuteUnique(list_team_members_names)

    def permuteUnique(self, list_team_members_names: List[str]):
        def permute(i: int):
            if i == len(list_team_members_names):
                self.__all_unique_permutations.append(list_team_members_names[:])

            for j in range(i, len(list_team_members_names)):
                list_team_members_names[i], list_team_members_names[j] = list_team_members_names[j], \
                                                                         list_team_members_names[i]
                permute(i + 1)
                list_team_members_names[i], list_team_members_names[j] = list_team_members_names[j], \
                                                                         list_team_members_names[i]

        permute(0)
        self.__all_unique_permutations = list(set(map(lambda x: tuple(x), self.__all_unique_permutations)))

    def generate_schedule(self) -> List[List[str]]:
        schedule: List[List[str]] = []
        seed(7) # 7 is prime, so chosen for seed generation
        list_existing_indices = []
        num_permutations = len(self.__all_unique_permutations)
        for i in range(self.__n_days):
            if len(list_existing_indices) == i:
                list_existing_indices.clear()
            r = randint(num_permutations)
            while r in list_existing_indices:
                r = randint(num_permutations)
            list_existing_indices.append(r)
            schedule.append(self.__all_unique_permutations[r])
        return schedule
