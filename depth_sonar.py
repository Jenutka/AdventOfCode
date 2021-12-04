data_sonar = open("input_data").read().splitlines()
data_int = list(map(int, data_sonar))
print(data_int)
enum_data_sonar = list(enumerate(data_int, start=0))
count = 0
previous=None
for i, d in enum_data_sonar:
    if not previous:
        print(f"{i+1} {d} (N/A - no previous measurement)")
        previous=True
    elif previous:
        if d > enum_data_sonar[i-1][1]:
            print(f"{i+1} {d} (increased)")
            count +=1
            previous=True
        elif d < enum_data_sonar[i-1][1]:
            print(f"{i+1} {d} (decreased)")
            previous=True
        if i+1 == len(enum_data_sonar):
            print(f"Jsem na konci, počet přírůstků: {count}")