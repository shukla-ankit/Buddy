import time
import sys
from team import Team
from scheduler import Scheduler
import json


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 app.py <json-file-path>')
        sys.exit(1)
    start_time = time.time()
    json_file_path = sys.argv[1]
    team = Team('ASR')
    with open(json_file_path) as json_file:
        members_json = json.load(json_file)
    team.add_members_by_json(members_json)
    team.print_team()
    print("\n\n")
    list_members = team.get_subscribed_team_members_names()
    scheduler = Scheduler(len(list_members), 5)
    schedule = scheduler.generate_schedule()
    i = 0
    for pairs in schedule:
        i = i + 1
        print('Day ' + str(i) + ': ')
        for pair in pairs:
            if len(pair) == 2:
                print('    ['+ list_members[pair[0]]+ ', ' +  list_members[pair[1]] + ']')
            else:
                print('    ['+ list_members[pair[0]]+ ', ' +  list_members[pair[1]] + ', ' + list_members[pair[2]] + ']')
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
