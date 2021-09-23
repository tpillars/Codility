#######################################################################################################
###################################  ORIGINAL #########################################################
#######################################################################################################
#
# A=[2,2,3,4,3,3,2,2,1,1,2,5]
# A=[2,2,3,4,3,3,2,2,1,1,2,5,4,5,4] # fails to produce correct answer - this only accomplishes changing status
# A=[1,2,3,4,5,6,7,8,9,10,11] # fails to produce correct answer - k
#
# list_len = len(A)
# field = list_len-1
# status = "start"
# tally = 0
#
# for i in range(field):
#
#     if (A[i] <= A[i+1]) & (status == "up"):
#         status = "up"
#         tally += 1
#     if (A[i] <= A[i+1]) & (status != "up"):
#         status = "up"
#     if (A[i] >= A[i+1]) & (status == "down"):
#         status = "down"
#         tally += 1
#     if (A[i] >= A[i+1]) & (status != "down"):
#         status = "down"
#     elif (A[i] == A[i+1]):
#         tally += 0

#######################################################################################################
###################################  FIXED ############################################################
#######################################################################################################
#
# list_len = len(A)
# field = list_len-1
# status = "start"
# tally = 1
#
# for i in range(field):
#     if (A[i] < A[i+1]) & (status == "up"):
#         status = "up"
#
#     if (A[i] < A[i+1]) & (status != "up"):
#         status = "up"
#         tally += 1
#
#     if (A[i] > A[i+1]) & (status == "down"):
#         status = "down"
#
#     if (A[i] > A[i+1]) & (status != "down"):
#         status = "down"
#         tally += 1
#
#     elif (A[i] == A[i+1]):
#         tally += 0
#
# print(tally)

#######################################################################################################
###################################  ORIGINAL #########################################################
#######################################################################################################
# A=np.zeros(21)
# A.shape = (7,3)
# A[0][0] = 5
# A[0][1] = 4
# A[0][2] = 4
# A[1][0] = 4
# A[1][1] = 3
# A[1][2] = 4
# A[2][0] = 3
# A[2][1] = 2
# A[2][2] = 4
# A[3][0] = 2
# A[3][1] = 2
# A[3][2] = 2
# A[4][0] = 3
# A[4][1] = 3
# A[4][2] = 4
# A[5][0] = 1
# A[5][1] = 4
# A[5][2] = 4
# A[6][0] = 4
# A[6][1] = 1
# A[6][2] = 1
# A = [[5, 4, 4], [4, 3, 4], [3, 2, 4], [2, 2, 2], [3, 3, 4], [1, 4, 4], [4, 1, 1]]
#
# def solution(A):
#     countries=1
#     rows = len(A)
#     col = len(A[0])
#     row_lim = rows-1
#     col_lim = col-1
#     country_dic={}
#     for row_index, row in enumerate(A):
#         for col_index, col_char in enumerate(row):
#             if col_index < col_lim:
#                 if A[row_index][col_index] == A[row_index][col_index + 1]:
#                     country1 = row_index, col_index
#                     country = row_index, col_index + 1
#                     if (country1 in country_dic)&(country in country_dic):
#                         countries -= 1
#                     if (country in country_dic):
#                         countries += 0
#                     else:
#                         country_dic[country] = country
#
#                 if (A[row_index][col_index]) != (A[row_index][col_index + 1]):
#                     country = row_index, col_index + 1
#                     if (country in country_dic):
#                         countries += 0
#                     else:
#                         country_dic[country] = country
#                         countries += 1
#
#             if row_index < row_lim:
#                 if (A[row_index][col_index]) == (A[row_index + 1][col_index]):
#                     country1 = row_index, col_index
#                     country = row_index + 1, col_index
#                     if (country1 in country_dic)&(country in country_dic):
#                         countries -= 1
#                     if (country in country_dic):
#                         countries += 0
#                     else:
#                         country_dic[country] = country
#
#                 if (A[row_index][col_index]) != (A[row_index + 1][col_index]):
#                     country = row_index + 1, col_index
#                     if (country in country_dic):
#                         countries += 0
#                     else:
#                         country_dic[country] = country
#                         countries += 1
#
#     print(countries)
#
# solution(A)
#
# #######################################################################################################
#
# A=[1, 12, 42, 70, 36, -4, 43, 15]
# B=[5, 15, 44, 72, 36, 2, 69, 24]
# nums=[]
# dic = {}
#
# def solution(A,B):
#
#     for x,y in enumerate(A):
#         for i,j in enumerate(B):
#             if x == i:
#                 for l in range(y,j):
#                     if l not in nums:
#                         nums.append(l)
#
#     sorted_nums = sorted(nums)
#     counter = sorted_nums[0]
#     dic_counter = 0
#     print(sorted_nums)
#
#     for indx, digit in enumerate(sorted_nums):
#
#         if counter == digit:
#             if dic_counter in dic:
#                 dic[dic_counter].append(digit)
#             else:
#                 dic[dic_counter] = []
#                 dic[dic_counter].append(digit)
#             counter +=1
#             print("we got one!", digit)
#         else:
#             counter = digit
#             dic_counter += 1
#             if dic_counter in dic:
#                 dic[dic_counter].append(digit)
#             else:
#                 dic[dic_counter] = []
#                 dic[dic_counter].append(digit)
#             counter +=1
#             print("we got one!", digit)
#
#     print(len(dic))
#
#
# solution(A,B)
