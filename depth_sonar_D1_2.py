data_sonar = open("input_data").read().splitlines()
data_int = list(map(int, data_sonar))
enum_data_sonar = list(enumerate(data_int, start=0))
list_three=[]
for i, d in enum_data_sonar:
    if i < 2:
        continue
    else:
        depth_three=enum_data_sonar[i-2][1]+enum_data_sonar[i-1][1]+enum_data_sonar[i][1]
        list_three.append(depth_three)
enum_data_sonar_three = list(enumerate(list_three, start=0))
count = 0
for i, d in enum_data_sonar_three:
    if i < 1:
        print(f"{i+1} {d} (N/A - no previous measurement)")
    elif d > enum_data_sonar_three[i-1][1]:
        print(f"{i+1} {d} (increased)")
        count +=1
    elif d < enum_data_sonar_three[i-1][1]:
        print(f"{i+1} {d} (decreased)")
    elif d == enum_data_sonar_three[i-1][1]:
        print(f"{i+1} {d} (no change)")
    if i+1 == len(enum_data_sonar_three):
        print(f"Jsem na konci, počet přírůstků: {count}")