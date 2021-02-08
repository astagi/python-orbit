import os
import json
from orbit import Orbit, OrbitException

client = Orbit(auth=os.environ['ORBIT_API_KEY'])

repo_activities = {}

activities = client.get_activities(
    '650',
    items=250,
    start_date='2020-12-01',
    end_date='2021-02-08',
    direction="ASC",
    auto_paginated=True
)

for activity in activities:
    repo = activity['attributes']['tags'][1]
    last_activity = activity['attributes']['occurred_at']
    print (activity['attributes']['type'])
    if not repo in repo_activities:
        repo_activities[repo] = {
            'count' : 0,
            'last_activity' : None
        }
    else:
        repo_activities[repo]['count'] += 1
        repo_activities[repo]['last_activity'] = last_activity

print (json.dumps(repo_activities, indent=4, sort_keys=True))
