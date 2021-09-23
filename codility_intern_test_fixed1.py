#######################################################################################################
###################################  ORIGINAL #########################################################
#######################################################################################################

A=[2,2,3,4,3,3,2,2,1,1,2,5]
# A=[2,2,3,4,3,3,2,2,1,1,2,5,4,5,4] # fails to produce correct answer - this only accomplishes changing status
# A=[1,2,3,4,5,6,7,8,9,10,11] # fails to produce correct answer - k

list_len = len(A)
field = list_len-1
status = "start"
tally = 0

for i in range(field):
    # print(A[i], A[i+1])

    if (A[i] <= A[i+1]) & (status == "up"):
        status = "up"
        tally += 1
    if (A[i] <= A[i+1]) & (status != "up"):
        status = "up"
    if (A[i] >= A[i+1]) & (status == "down"):
        status = "down"
        tally += 1
    if (A[i] >= A[i+1]) & (status != "down"):
        status = "down"
    elif (A[i] == A[i+1]):
        tally += 0

#######################################################################################################
###################################  FIXED ############################################################
#######################################################################################################

list_len = len(A)
field = list_len-1
status = "start"
tally = 1

for i in range(field):
    if (A[i] < A[i+1]) & (status == "up"):
        status = "up"

    if (A[i] < A[i+1]) & (status != "up"):
        status = "up"
        tally += 1

    if (A[i] > A[i+1]) & (status == "down"):
        status = "down"

    if (A[i] > A[i+1]) & (status != "down"):
        status = "down"
        tally += 1

    elif (A[i] == A[i+1]):
        tally += 0

print(tally)