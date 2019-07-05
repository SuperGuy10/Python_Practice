stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
final_selected = []
while states_needed:
    states_covered = set()
    selected_station = None
    #check every items each time, to make sure selected the longest one.
    for station, state in stations.items():
        covered = state&states_needed
        #print("covered",covered)
        if len(covered) > len(states_covered):
            print(len(covered), len(states_covered))
            selected_station = station
            states_covered = covered
    states_needed-=states_covered
    #print("states_needed",states_needed)
    final_selected.append(selected_station)
print(final_selected)
