import numpy as np

for tc in range(int(input())):
    lst = list(map(int, input().split()))
    ar = np.array(lst)
    my_max=0

    for i in range(10):
        if ar[i]> my_max:
            my_max=ar[i]
    
    print(my_max)