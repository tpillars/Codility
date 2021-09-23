##################################################### hackerrank
# find sum of an array
ar = [2,4,5,8,9,6,5,1]
sum=0
for item in ar:
    sum+=item
# print(sum)
##################################################### hackerrank
# alice vs bob, who has higher number each round, sum
a = [2,4,5,8]
b = [3,5,5,1]
alice = 0
bob = 0
for a_index,a_value in enumerate(a):
    for b_index,b_value in enumerate(b):
        if a_index == b_index:
            if a_value > b_value:
                alice += 1
            elif b_value > a_value:
                bob += 1
            else:
                pass
print(alice, bob)
##################################################### hackerrank
# add diagonals, find absolute difference of L and R diag
ar = [10,4,5,1],\
     [2,10,1,8],\
     [2,1,10,8],\
     [1,4,5,10]

x = 0
y = 0
a = -1
b = 0
# b = y-1
leftdiag = 0
rightdiag = 0

for i in ar:
    if x == y:
        rightdiag+=ar[x][y]
        x+=1
        y+=1
        leftdiag+=ar[a][b]
        a-=1
        b+=1
abs_difference=abs(rightdiag-leftdiag)
# print(abs_difference)
##################################################### leetcode
# First Unique Char
s = "HHHHEEEELLLO WORLD!"
class Solution:
    def firstUniqChar(s):
        dic = {}
        dic2 = {}

        for index, letter in enumerate(s):
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
            dic2[letter] = index
        for item in dic:
            if dic[item] == 1:
                return(item, dic2[item])
sol = Solution
test1 = sol.firstUniqChar(s)
# print(test1)
#####################################################
