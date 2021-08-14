#########################################
# Question 1 - do not delete this comment
#########################################

# Write the rest of the code for question 1 below here.
def catalan_rec(n):
    if n == 0:
        return 1
    
    cn = 0
    for i in range(n):
        cn += catalan_rec(i)*catalan_rec(n-i-1)
        
    return cn

def catalan_mem(n,memo=None):
    if n == 0:
        return 1
    
    if memo == None:
        memo = {}
        

    for i in range(n):
        if i not in memo:
            memo[i] = catalan_mem(i)
        if n-i-1 not in memo:
            memo[n-i-1] = catalan_mem(n-i-1)
            
        memo[n] = memo.get(n,0) + memo[i]*memo[n-i-1]
        
    return  memo[n]
    
    
    
    
    


def catalan_rec_with_count(n,cnt = 1):
    if n <= 1:
        return (1,cnt)
    
    cn = 0
    for i in range(n):
        ci, inside_cnt1 = catalan_rec_with_count(i)
        cnMinusi,inside_cnt2 = catalan_rec_with_count(n-i-1)
        cn += ci * cnMinusi
        cnt += inside_cnt1+inside_cnt2
    return (cn,cnt)



def catalan_mem_with_count(n,memo=None,cnt=1):
    if memo == None:
        memo = {}
    memo[0] = 1
    memo[1] = 1
    if n == 0 or n == 1:
        return (memo[n],cnt)

        
    for i in range(n):
        

        cnt0 = 0
        if i not in memo:
            memo[i],cnt0 = catalan_mem_with_count(i)
            
        cnt1 = 0    
        if n-i-1 not in memo:
            memo[n-i-1],cnt1 = catalan_mem_with_count(n-i-1)        
        
        cnt+= cnt1+cnt0 
        memo[n] = memo.get(n,0) + memo[i]*memo[n-i-1]
        
    return  (memo[n],cnt)
    

#########################################
# Question 2 - do not delete this comment
#########################################


def atm_rec(amount,bills,n):
    if amount<0:
        return False
    if amount == 0 and n==0:
        return True
    if amount == 0 and n!=0:
        return False
    if n == 0 and amount!= 0:
        return False
    if bills == ():
        return False
        


    optionChoose    = atm_rec(amount-bills[-1],bills,n-1)
    optionNotChoose = atm_rec(amount,bills[:-1],n)
    opt = optionChoose or optionNotChoose
    return opt

def atm_mem(amount, bills, n,memo = None):
    if amount<0:
        return False
    if amount == 0 and n==0:
        return True
    if amount == 0 and n!=0:
        return False
    if n == 0 and amount!= 0:
        return False
    if bills == ():
        return False
        
    if memo == None:
        memo = {}
    

    if (amount-bills[-1],n-1) not in memo:
        optionChoose    = atm_rec(amount-bills[-1],bills,n-1)
        memo[(amount-bills[-1],n-1)] = optionChoose
    if (amount,n) not in memo:
        optionNotChoose    = atm_rec(amount,bills[:-1],n)
        memo[(amount,n)] = optionNotChoose
        
   
    return memo[(amount,n)] or  memo[(amount-bills[-1],n-1)]



	
#########################################
# Question 3 - do not delete this comment
#########################################


# Write the rest of the code for question 3 below here.


def max_trail(pyramid,row=0,col=0):
    if row == len(pyramid)-1:
        return pyramid[row][col]
    
    
    option1 = pyramid[row][col] + max_trail(pyramid,row+1,col)
    option2 = pyramid[row][col] + max_trail(pyramid,row+1,col+1)
    return max(option1,option2)
    
def max_trail_mem(pyramid,row=0,col=0,memo = None):
    if row == len(pyramid)-1:
        return pyramid[row][col]
        
    if memo == None:
        memo = {}
    
    if (row,col,row+1,col) not in memo:
        option1 = pyramid[row][col] + max_trail(pyramid,row+1,col)
        memo[(row,col,row+1,col)] = option1
    if (row,col,row+1,col+1) not in memo:
        option2 = pyramid[row][col] + max_trail(pyramid,row+1,col+1)
        memo[(row,col,row+1,col+1)] = option2
        
    return max(memo[(row,col,row+1,col+1)],memo[(row,col,row+1,col)])


