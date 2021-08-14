#########################################
# Question 1 - do not delete this comment
#########################################

def reverse_string(s):
    if len(s) == 1 or len(s) == 0:
        return s
    else:
        return reverse_string(s[1:])+s[0]
    

#########################################
# Question 2 - do not delete this comment
#########################################

def sublist_sumV2(numbers,target,path_lenght): 
    if target<0:
        return float('inf')
    if target == 0:
        return path_lenght
    if len(numbers) == 0:
        return float('inf')

    
    option1 = sublist_sumV2(numbers[:-1], target - numbers[-1], path_lenght+1)
    option2 = sublist_sumV2(numbers[:-1], target,path_lenght)
    
    return min(option1,option2)
        


def min_sublist_sum(numbers, target):
    return sublist_sumV2(numbers,target,0)

#########################################
# Question 3 - do not delete this comment
#########################################

def uncover_cell(ms_board, ms_revealed, idx):
    if idx>=0 and idx<=len(ms_board)-1:
        if len(ms_revealed) == 1:
            if ms_board[idx] == "*":
                print('boom!')
            return [True]
        if ms_board[idx] == "*":
            print('boom!')
            ms_revealed[idx] = True
            return ms_revealed
        if ms_board[idx] == 1 or ms_board[idx] == 2:
            ms_revealed[idx] = True
            return ms_revealed
        else: # ms_board[idx]=0
            ms_revealed[idx] = True
            if (idx>0 and ms_revealed[idx-1]==False): # not in the start
                uncover_cell(ms_board, ms_revealed, idx-1) # go left
            if (idx<len(ms_revealed)-1 and ms_revealed[idx+1]==False): # not at the end
                uncover_cell(ms_board, ms_revealed, idx+1) # go right
    else:
         print('Number out of range')

        
        
    return ms_revealed

#########################################
# Question 4 - do not delete this comment
#########################################


def is_valid_paren(s, cnt=0):
    if cnt <0:
        return False
    if s == '':
        if cnt == 0:
            return True
        else:
            return False
        
    if s[-1] == '(':
        cnt-=1
    if s[-1] == ')':
            cnt+=1 
    return is_valid_paren(s[:-1], cnt)
        

print(is_valid_paren('(long)(string(with(text)right)()(use))'))


























