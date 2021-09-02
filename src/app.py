from team import Team
from scheduler import Scheduler
import json


def main():
    team = Team('ASR')
    with open('../data/members.json') as json_file:
        members_json = json.load(json_file)
    team.add_members_by_json(members_json)
    team.print_team()
    print("\n\n")
    scheduler = Scheduler(team.get_team_members_names(), 5)
    print(scheduler.random_pair_generator())


if __name__ == '__main__':
    main()
