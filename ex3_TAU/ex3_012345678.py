#########################################
# Question 1 - do not delete this comment
#########################################
TOMATO = "tomato"

def find_tomato(items):
    for i in range(len(items)):
        if items[i].lower() == TOMATO:
            return i
    
    return -1
        

#########################################
# Question 2 - do not delete this comment
#########################################

VOWELS = "AEIOU"

# Write the rest of the code for question 2 below here.

def even_vowels(sentence):
    counter = 0 
    for char in sentence.upper():
        if char in VOWELS:
            counter+=1
    
    if counter%2 == 0:
        return True
    
    return False
    
#########################################
# Question 3 - do not delete this comment
#########################################


def three_div(number):
    cnt = 0 
    num_in_str = str(number)
    for digit in num_in_str:
        if int(digit)%3 == 0:
            cnt+=1
            
    return cnt


    
#########################################
# Question 4 - do not delete this comment
#########################################

def is_name(test_string):
    splited_list = test_string.split()
    if len(splited_list) != 2:
        return False
    for word in splited_list:
        if not word.isalpha():
            return False
        if word[0].islower():
            return False
        for char in range(len(word)):
            if char != 0:
                if word[char].isupper():
                    return False
                
    return True
            



    
#########################################
# Question 5 - do not delete this comment
#########################################


# Write the rest of the code for question 5 below here.

##add functions below
##add functions above

def adjust_to_recession(grocery_list,maximal_budget):
    while not check_list(grocery_list,maximal_budget):
        if len(grocery_list) == 0:
            print("Empty list")
            break
        else: # list isn't empty
            max_index = find_max(grocery_list)
            msg = 'You cannot afford' + (grocery_list[max_index])[0]
            grocery_list.pop(max_index)
    print('Go Shop!')


def find_max(grocery_list):
    max_price = -1
    most_expenssive = -1
    for product in range(len(grocery_list)):
        if (grocery_list[product])[1]>max_price:
            max_price = (grocery_list[product])[1]
            most_expenssive = product
            
    return most_expenssive

def check_list(grocery_list,maximal_budget):
    total_price = 0
    for product in grocery_list:
        total_price+= product[1]
    
    if total_price<=maximal_budget:
        return True
    return False


#########################################
# Question 6 - do not delete this comment
#########################################

def max_column(mat):
    if mat == []:
        return -1
    max_col_sum = 0
    max_col_ind = 0
    cols = range(len(mat[0]))
    rows = range(len(mat))
    
    for n in  cols:
        cnt = 0 
        for m in rows:
            cnt += (mat[m])[n]
        if cnt > max_col_sum:
            max_col_sum = cnt
            max_col_ind = n
            
    return  max_col_ind


#########################################
# Question 7 - do not delete this comment
#########################################

def create_matrix(m,n):
    mat = []
    for row in range(m) :
        mat.append([])
        for col in range(n):
            mat[row].append(row*n+col+1)
            
    return mat
    
    
#########################################
# Question 8 - do not delete this comment
#########################################

MUL_ERROR = "Error, Matrices cannot be multiplied"

def multiply_matrix(A,B):
    
    A_rows = len(A)
    A_cols = len(A[0])
    B_rows = len(B)
    B_cols = len(B[0])
    if A_cols != B_rows:
        return (MUL_ERROR)
    
    mat = []
    
    for i in range(A_rows):
        mat.append([])
        for j in range(B_cols):
            cnt = 0
            for k in range (A_cols):
                cnt += A[i][k]*B[k][j]
            
            mat[i].append(cnt)
            
     
    return mat
    

'''
The next code block executes several tests of common scenarios for your aid. 
You are more than welcome to add tests of your own, but it's not mandatory.
'''

# assert sentence throws an error if the expression after it equals False.
assert find_tomato(["Bagel","TomatO","Cherry"]) == 1
assert find_tomato(["Bagel","Apple","Cherry"]) == -1
assert even_vowels("BRioTH SHoUld")
assert not even_vowels("Barry SHoUld")
assert three_div(123456)==2
assert is_name("Barry White")
assert not is_name("Brian de Palma")    
assert find_max([("bread",5),("bannana",16.5),("milk",7.9),("lettuce",12)]) == 1
assert not check_list([("bread",5),("bannana",16.5),("milk",7.9),("lettuce",12)],20)
assert check_list([("bread",5),("bannana",16.5),("milk",7.9),("lettuce",12)],50)
lst = [("bread",5),("bannana",16.5),("milk",7.9),("lettuce",12)]
adjust_to_recession(lst,20)
assert lst ==  [("bread",5),("milk",7.9)]

lst = [("bread",5),("bannana",16.5),("milk",7.9),("lettuce",12)]
adjust_to_recession(lst,4)
assert lst ==  []

assert max_column([[5,6,7],[17,3,9]])==0
assert max_column([[20,35],[17,5],[10,10]])==1
assert create_matrix(4,5)==[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
assert create_matrix(4,2)==[[1,2],[3,4],[5,6],[7,8]]
assert multiply_matrix([[1,0],[2,1]],[[5,4],[-5,1]])==[[5,4],[5,9]]
assert multiply_matrix([[5,4],[-5,1]],[[1,0],[2,1]])==[[13,4],[-3,1]]
assert multiply_matrix([[1,0,3],[2,1,5]],[[5,4],[-5,1]])=="Error, Matrices cannot be multiplied"
                    

print ('Congrats!!!')
print ('All preliminary tests passed!')

    
    
    
    
    
    
    
    
    
    
    
    
    