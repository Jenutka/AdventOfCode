def main():
    data_movement = open("binary_data").read().splitlines()
    delka_znaku = len(str(data_movement[0]))
    binaries_1=[]
    binaries_0=[]
    #oxygen_generator_rating
    for pozice in range(delka_znaku):
        for i in data_movement:
            if int(i[pozice]) == 1:
                binaries_1.append(i)
            if int(i[pozice]) == 0:
                binaries_0.append(i)
        if len(binaries_1)>len(binaries_0):
            data_movement.clear()
            data_movement.extend(binaries_1)
            binaries_1.clear()
            binaries_0.clear()
        elif len(binaries_1)<len(binaries_0):
            data_movement.clear()
            data_movement.extend(binaries_0)
            binaries_0.clear()
            binaries_1.clear()
        elif len(binaries_1)==len(binaries_0):
            data_movement.clear()
            data_movement.extend(binaries_1)
            binaries_1.clear()
            binaries_0.clear()
        if len(data_movement)==1:
            break
    print(data_movement)
    oxygen_dec=int(data_movement[0], 2)
    print(oxygen_dec)
    data_movement = open("binary_data").read().splitlines()
    #CO2_scruber_rating
    for pozice in range(delka_znaku):
        for i in data_movement:
            if int(i[pozice]) == 1:
                binaries_1.append(i)
            if int(i[pozice]) == 0:
                binaries_0.append(i)
        if len(binaries_1)>len(binaries_0):
            data_movement.clear()
            data_movement.extend(binaries_0)
            binaries_1.clear()
            binaries_0.clear()
        elif len(binaries_1)<len(binaries_0):
            data_movement.clear()
            data_movement.extend(binaries_1)
            binaries_0.clear()
            binaries_1.clear()
        elif len(binaries_1)==len(binaries_0):
            data_movement.clear()
            data_movement.extend(binaries_0)
            binaries_1.clear()
            binaries_0.clear()
        if len(data_movement)==1:
            break
    print(data_movement)
    CO2=int(data_movement[0], 2)
    print(CO2)
    life_support_rate = oxygen_dec*CO2
    print(life_support_rate)

main()