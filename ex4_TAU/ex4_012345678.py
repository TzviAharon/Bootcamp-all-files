#########################################
# Question 1a - do not delete this comment
#########################################

def map_bin2dec(n):
    
    bin_to_dec = {}
    for i in range(2**n):
        bin_str = bin(i)[2:].zfill(n)
        bin_to_dec[bin_str] = str(i)
    
    return bin_to_dec
    
#########################################
# Question 1b - do not delete this comment
#########################################

def bin_triplets_to_decimal(bin_str):
    bin_to_dec_dict = map_bin2dec(3)
    output_str = ''
    for i in range(int(len(bin_str)/3)):
        cur_str = bin_str[i*3:i*3+3]
        cur_dec = bin_to_dec_dict[cur_str]
        output_str += cur_dec
    
    return output_str

#########################################
# Question 2a - do not delete this comment
#########################################

def swap_student_courses(students_dict):
    courses_dict = {}
    all_students = students_dict.keys()
    for student in all_students:
        for course in students_dict[student]:
            if not course in courses_dict:
                courses_dict[course] = [student]
            else: # course already in dict
                courses_dict[course].append(student)
                
    return courses_dict        

#########################################
# Question 2b - do not delete this comment
#########################################

def count_courses_intersection(courses_dict):
    courses_list = list(courses_dict.keys())
    common_students_dict = {}
    
    for i in range(len(courses_list)):
        for j in range(len(courses_list)):
            if j>i:
                tpl =(courses_list[i],courses_list[j])
                common_students_dict[tpl] = 0        
                for student in courses_dict[courses_list[j]]:
                    if student in courses_dict[courses_list[i]]:
                         common_students_dict[tpl] += 1
                         
    return common_students_dict  

#########################################
# Question 3a - do not delete this comment
#########################################

def find_following_words(text):
    list_of_words_sorted = text.lower().split()
    list_of_words_sorted.sort()
    words_dict = {}
    for word in list_of_words_sorted:
        words_dict[word] = []
        checked_words = []
        for word_to_compare in list_of_words_sorted:
            if word_to_compare not in checked_words:
                if word_to_compare[0] == word[-1]:
                    words_dict[word].append(word_to_compare)
                    checked_words.append(word_to_compare)
                    
    
    
    return words_dict 





#########################################
# Question 3b - do not delete this comment
#########################################

def play_word_chain(text, word):
    word_dict = find_following_words(text)
    list_of_words_sorted = text.lower().split()
    used = []
    not_used = list_of_words_sorted.copy()
    cur_word = word.lower()
    while True:
        there_was_procces = 0
        if len(word_dict[cur_word]) == 0:
            break
        
        else:
            for potential_next_word in word_dict[cur_word]:
                if potential_next_word not in used :
                    there_was_procces = 1
                    cur_word = potential_next_word
                    used.append(cur_word)
                    not_used.remove(cur_word)
                    break
        if not there_was_procces:
            break
    return not_used


    
    
#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################

# print map_bin2dec(1)
# print map_bin2dec(2)

# print bin_triplets_to_decimal("001111")
# print bin_triplets_to_decimal("110011")

# print swap_student_courses({"Yuval": ["Math", "Computer Science", "Statistics"],\
#                       "Gal": ["Algebra", "Statistics", "Physics"],\
#                       "Noam": ["Statistics", "Math", "Programming"]})
# print count_courses_intersection({'Bible': ['Daniel', 'Roni'],\
#                                   'Psychology': ['Roni'], 'Biology': ['Daniel']})

# print find_following_words("The little girl sings a Song")

# unused_words = play_word_chain("The little girl sings a Song", "sings")
# print unused_words

# unused_words = play_word_chain("The little girl sings a Song", "tHe")
# print unused_words
