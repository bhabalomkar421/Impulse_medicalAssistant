l = [1]*8
print(l)
zero_count = 1
for i in range(1, 8):
    for j in range(0, 9-i):
        if (zero_count == 1):
            l[j] = 0
        elif (zero_count == 2):
            l[j] = l[j+1] = 0
        elif (zero_count == 3):
            l[j] = l[j+1] = l[j+2] = 0
        elif (zero_count == 4):
            l[j] = l[j+1] = l[j+2] = l[j+3] = 0

        print(l)
        l = [1]*8

        print("\n")
    zero_count += 1
    print("-------------------------------------------")
    if (zero_count == 5):
        break

    #    for k in range(j, j+1):
    #        l[k] = 0
    #    print(l)
