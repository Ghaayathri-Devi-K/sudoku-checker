'''
As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

~ each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
~ each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
~ each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.

Your task is to write a program which:
~ reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
~ outputs Yes if the Sudoku is valid, and No otherwise.

Test your code using the data we've provided.

--------------- Test data ---------------------
Sample input:
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672

Sample output:
Yes


Sample input:
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671

Sample output:
No
'''

def isSuduko(r1,r2,r3,r4,r5,r6,r7,r8,r9):
    
    l1 = list(r1)
    l1_new = []
    for i in l1:
        l1_new.append(int(i))

    l2 = list(r2)
    l2_new = []
    for i in l2:
        l2_new.append(int(i))

    l3 = list(r3)
    l3_new = []
    for i in l3:
        l3_new.append(int(i))


    l4 = list(r4)
    l4_new = []
    for i in l4:
        l4_new.append(int(i))

    l5 = list(r5)
    l5_new = []
    for i in l5:
        l5_new.append(int(i))

    l6 = list(r6)
    l6_new = []
    for i in l6:
        l6_new.append(int(i))

    l7 = list(r7)
    l7_new = []
    for i in l7:
        l7_new.append(int(i))

    l8 = list(r8)
    l8_new = []
    for i in l8:
        l8_new.append(int(i))

    l9 = list(r9)
    l9_new = []
    for i in l9:
        l9_new.append(int(i))
        
    l = [l1_new, l2_new,l3_new,l4_new,l5_new,l6_new,l7_new,l8_new,l9_new]
    
    # Find row sum
    row_sum = sum(l[0]) # initialization 
    for r in range(1,len(l)):
        if sum(l[r]) != row_sum:
            row_sum_con = False
            break
        else:
            row_sum_con = True # Row sum condition satisfied
        
    # Find column sum
    col_sum = 0
    for r in range(len(l)):
        col_sum += l[r][0]
    COL_SUM = col_sum # Column sum initialization

    for R in range(len(l)):
        C_S = 0
        for C in range(len(l)):
            C_S += l[R][C]
        if C_S != COL_SUM:
            col_sum_con = False
            break
        else:
            col_sum_con = True
        
    # Checking internal sub-squares
    sl = l[0:3]
    sub_list = []
    for i in sl:
        sub_list+= i[0:3]
    init_sub_list_sum = sum(sub_list) # Initializing the sum of the sublist

    for n in range(0,9,3):
        sl = l[n:n+3]
        for m in range(0,9,3):
            sub_list = []
            for i in sl:
                sub_list += i[m:m+3]
            sub_list_sum = sum(sub_list)
            if sub_list_sum == init_sub_list_sum:
                sublist_con = True
            else:
                sublist_con = False
                break
                
                
    if sublist_con == True and col_sum_con == True and row_sum_con == True:
        print('Yes')
    else:
        print('No')
        
# ------- Test case 1 ------------      
# INPUT 1
r1 = '295743861'
r2 = '431865927'
r3 = '876192543'
r4 = '387459216'
r5 = '612387495'
r6 = '549216738'
r7 = '763524189'
r8 = '928671354'
r9 = '154938672'

isSuduko(r1,r2,r3,r4,r5,r6,r7,r8,r9)

# ------- Test case  ------------ 
# INPUT 2
r1 = '195743862'
r2 = '431865927'
r3 = '876192543'
r4 = '387459216'
r5 = '612387495'
r6 = '549216738'
r7 = '763524189'
r8 = '928671354'
r9 = '254938671'

isSuduko(r1,r2,r3,r4,r5,r6,r7,r8,r9)


'''
Author:
    @ Ghaayathri Devi K
'''
