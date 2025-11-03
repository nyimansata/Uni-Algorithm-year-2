activities = [
    {'name': 'A', 'start': 1, 'finish': 4},
    {'name': 'B', 'start': 3, 'finish': 5},
    {'name': 'C', 'start': 0, 'finish': 6},
    {'name': 'D', 'start': 5, 'finish': 7},
    {'name': 'E', 'start': 8, 'finish': 9},
    {'name': 'F', 'start': 5, 'finish': 9}
]

# --- Version 1: Based on earliest finish time ---
v1 = sorted(activities, key=lambda x: x['finish'])
selected_v1 = []
last_finish = 0

for act in v1:
    if act['start'] >= last_finish:
        selected_v1.append(act['name'])
        last_finish = act['finish']

# --- Version 2: Based on shortest duration ---
v2 = sorted(activities, key=lambda x: (x['finish'] - x['start']))
selected_v2 = []
last_finish = 0

for act in v2:
    if act['start'] >= last_finish:
        selected_v2.append(act['name'])
        last_finish = act['finish']

# --- Print results ---
print("Version 1 (Based on Finish Time):", selected_v1)
print("Number of activities:", len(selected_v1))

print("\nVersion 2 (Based on Duration):", selected_v2)
print("Number of activities:", len(selected_v2))

if len(selected_v1) == len(selected_v2):
    print("\n Both strategies select the same number of activities.")
else:
    print("\n Different results finish-time greedy usually performs better.")
