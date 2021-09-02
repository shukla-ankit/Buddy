from typing import List
from random import seed, randint
import random_dice_roller as rand

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

    def get_pairs(self, list_members_names: List[str]) -> List[List[str]]:
        list_pairs: List[List[str]] = []
        is_size_uneven = len(list_members_names) / 2 != 0
        pair = []
        for i in range(len(list_members_names)):
            if len(pair) == 2:
                list_pairs.append(pair)
                pair = []
            pair.append(list_members_names[i])
        if is_size_uneven:
            list_pairs[- 1].append(list_members_names[-1])
        return list_pairs

    def generate_schedule(self) -> List[List[str]]:
        schedule: List[List[List[str]]] = []
        seed(7) # 7 is prime, so chosen for seed generation
        list_existing_indices = []
        num_permutations = len(self.__all_unique_permutations)
        for i in range(self.__n_days):
            if len(list_existing_indices) == i:
                list_existing_indices.clear()
            # r = randint(num_permutations)
            r = rand.roll_dice_MaxMin(minimum_number=0, maximum_number=num_permutations)
            while r in list_existing_indices:
                # r = randint(num_permutations)
                r = rand.roll_dice_MaxMin(minimum_number=0, maximum_number=num_permutations)
            list_existing_indices.append(r)
            schedule.append(self.get_pairs(self.__all_unique_permutations[r]))
        return schedule
