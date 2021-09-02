from typing import List
from random import seed, randint
import random_dice_roller as rand

class Scheduler:
    def __init__(self, size_team: int, n_days: int):
        if size_team < 3:
            print('Please provide team with more members than 3!')
            exit(0)
        self.__n_days = n_days
        self.__all_unique_permutations = []
        self.permuteUnique([i for i in range(size_team)])

    def permuteUnique(self, list_members_id: List[int]):
        def permute(i: int):
            if i == len(list_members_id):
                self.__all_unique_permutations.append(list_members_id[:])

            for j in range(i, len(list_members_id)):
                list_members_id[i], list_members_id[j] = list_members_id[j], list_members_id[i]
                permute(i + 1)
                list_members_id[i], list_members_id[j] = list_members_id[j], list_members_id[i]

        permute(0)
        self.__all_unique_permutations = list(set(map(lambda x: tuple(x), self.__all_unique_permutations)))

    def get_pairs(self, list_members_id: List[int]) -> List[List[int]]:
        list_pairs_id: List[List[int]] = []
        is_size_uneven = len(list_members_id) / 2 != 0
        pair = []
        for i in range(len(list_members_id)):
            if len(pair) == 2:
                pair.sort()
                list_pairs_id.append(pair)
                pair = []
            pair.append(list_members_id[i])
        if is_size_uneven:
            k = rand.roll_dice_MaxMin(minimum_number=0, maximum_number=len(list_pairs_id)-1)
            list_pairs_id[k].append(list_members_id[-1])
            list_pairs_id[k].sort()
        list_pairs_id.sort()
        return list_pairs_id

    def generate_schedule(self) -> List[List[str]]:
        schedule: List[List[List[int]]] = []
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
