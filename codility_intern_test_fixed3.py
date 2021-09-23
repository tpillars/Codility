#######################################################################################################
###################################  ORIGINAL #########################################################
#######################################################################################################
A=[1, 12, 42, 70, 36, -4, 43, 15]
B=[5, 15, 44, 72, 36, 2, 69, 24]
nums=[]
dic = {}

def solution(A,B):

    for x,y in enumerate(A):
        for i,j in enumerate(B):
            if x == i:
                for l in range(y,j):
                    if l not in nums:
                        nums.append(l)

    sorted_nums = sorted(nums)
    counter = sorted_nums[0]
    dic_counter = 0

    for indx, digit in enumerate(sorted_nums):

        if counter == digit:
            if dic_counter in dic:
                dic[dic_counter].append(digit)
            else:
                dic[dic_counter] = []
                dic[dic_counter].append(digit)
            counter +=1

        else:
            counter = digit
            dic_counter += 1
            if dic_counter in dic:
                dic[dic_counter].append(digit)
            else:
                dic[dic_counter] = []
                dic[dic_counter].append(digit)
            counter +=1

    print(len(dic))


solution(A,B)
#######################################################################################################
###################################  FIXED  ###########################################################
#######################################################################################################
A=[1, 12, 42, 70, 36, -4, 43, 15]
B=[5, 15, 44, 72, 36, 2, 69, 24]
nums=[]
dic = {}

def solution(A,B):

    for x,y in enumerate(A):
        for i,j in enumerate(B):
            if x == i:
                for l in range(y,j):
                    if l not in nums:
                        nums.append(l)
                nums.append(j)          # FIXED to add last number in range() to nums list

    sorted_nums = sorted(nums)
    counter = sorted_nums[0]
    dic_counter = 0

    for indx, digit in enumerate(sorted_nums):

        if counter == digit:
            if dic_counter in dic:
                dic[dic_counter].append(digit)
            else:
                dic[dic_counter] = []
                dic[dic_counter].append(digit)
            counter +=1

        else:
            counter = digit
            dic_counter += 1
            if dic_counter in dic:
                dic[dic_counter].append(digit)
            else:
                dic[dic_counter] = []
                dic[dic_counter].append(digit)
            counter +=1

    print(len(dic))


solution(A,B)
