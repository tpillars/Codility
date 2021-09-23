import random

# find lowest positive number skipped in list
randlist = []
for i in range (50):
    n = random.randint(0, 100)
    randlist.append(n)
# print(randlist)

randlist = [2,3,4]
def solution(A):
    dic = {}
    counter = 1
    sorted_A = sorted(A)

    for digit in sorted_A:
        if digit > 0:
            if digit in dic:
                pass
            else:
                dic[digit] = digit

    for item,key in dic.items():
        while key >0:
            if counter == key:
            # print(counter)
                counter += 1
            else:
                break
    print(counter)


solution(randlist)
