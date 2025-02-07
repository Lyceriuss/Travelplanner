import json

from backend.connect_to_api import ResRobot

resrobot = ResRobot()

# Fetch the data
stuff = resrobot.trips(740000002, 740025725, None, None, 0)

# Convert to JSON format and pretty-print
json_output = json.dumps(stuff, indent=4, ensure_ascii=False)

# Print JSON output
print(json_output)
