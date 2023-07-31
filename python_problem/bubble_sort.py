# Bubble Sort


def bubble_Sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]

    return list
print(bubble_Sort([3,2,0,1,5,4]))