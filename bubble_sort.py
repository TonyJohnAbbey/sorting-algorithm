l = [float(x) for x in input("Enter a list of elements: \n").split()]
swap = 1
while swap != 0:
    swap = 0
    for j in range(len(l)-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            swap +=1
            print(l)
    print(" ")
