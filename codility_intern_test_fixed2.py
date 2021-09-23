######################################################################################################
##################################  ORIGINAL #########################################################
######################################################################################################

A = [[5, 4, 4], [4, 3, 4], [3, 2, 4], [2, 2, 2], [3, 3, 4], [1, 4, 4], [4, 1, 1]]

def solution(A):
    countries=1
    rows = len(A)
    col = len(A[0])
    row_lim = rows-1
    col_lim = col-1
    country_dic={}
    for row_index, row in enumerate(A):
        for col_index, col_char in enumerate(row):
            if col_index < col_lim:
                if A[row_index][col_index] == A[row_index][col_index + 1]:
                    country1 = row_index, col_index
                    country = row_index, col_index + 1
                    if (country1 in country_dic)&(country in country_dic):
                        countries -= 1
                    if (country in country_dic):
                        countries += 0
                    else:
                        country_dic[country] = country

                if (A[row_index][col_index]) != (A[row_index][col_index + 1]):
                    country = row_index, col_index + 1
                    if (country in country_dic):
                        countries += 0
                    else:
                        country_dic[country] = country
                        countries += 1

            if row_index < row_lim:
                if (A[row_index][col_index]) == (A[row_index + 1][col_index]):
                    country1 = row_index, col_index
                    country = row_index + 1, col_index
                    if (country1 in country_dic)&(country in country_dic):
                        countries -= 1
                    if (country in country_dic):
                        countries += 0
                    else:
                        country_dic[country] = country

                if (A[row_index][col_index]) != (A[row_index + 1][col_index]):
                    country = row_index + 1, col_index
                    if (country in country_dic):
                        countries += 0
                    else:
                        country_dic[country] = country
                        countries += 1

    print(countries)

solution(A)

######################################################################################################
##################################  FIXED ############################################################
######################################################################################################

A = [[5, 4, 4], [4, 3, 4], [3, 2, 4], [2, 2, 2], [3, 3, 4], [1, 4, 4], [4, 1, 1]]

def solution(A):
    countries=1
    rows = len(A)
    col = len(A[0])
    row_lim = rows-1
    col_lim = col-1
    country_dic={}
    for row_index, row in enumerate(A):
        for col_index, col_char in enumerate(row):
            if col_index < col_lim:
                if A[row_index][col_index] == A[row_index][col_index + 1]:
                    country1 = row_index, col_index
                    country = row_index, col_index + 1
                    if (country1 in country_dic)&(country in country_dic):
                        countries -= 1
                    if (country in country_dic):
                        countries += 0
                    else:
                        country_dic[country] = country

                if (A[row_index][col_index]) != (A[row_index][col_index + 1]):
                    country = row_index, col_index + 1
                    if (country in country_dic):
                        countries += 0
                    else:
                        country_dic[country] = country
                        countries += 1

            if row_index < row_lim:
                if (A[row_index][col_index]) == (A[row_index + 1][col_index]):
                    country1 = row_index, col_index
                    country = row_index + 1, col_index
                    if (country1 in country_dic)&(country in country_dic):
                        countries -= 1
                    if (country in country_dic):
                        countries += 0
                    else:
                        country_dic[country] = country

                if (A[row_index][col_index]) != (A[row_index + 1][col_index]):
                    country = row_index + 1, col_index
                    if (country in country_dic):
                        countries += 0
                    else:
                        country_dic[country] = country
                        countries += 1

    print(countries)

solution(A)
