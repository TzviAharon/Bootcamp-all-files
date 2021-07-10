#########################################
# Question 1 - do not delete this comment
#########################################

def sum_file_nums(infile):
    f = open(infile, "r") 
    cnt = 0.0 
    for line in f:
        cnt += float(line)
    
    f.close()
    return cnt


#########################################
# Question 2 - do not delete this comment
#########################################

def filter_file_nums(infile, outfile):
    f = open(infile, "r") 
    f2 = open(outfile, "w")
    for line in f:
        if (float(line)%3 == 0.0):
            f2.write(line)

            
    f.close()
    f2.close()

filter_file_nums('q2_in.txt', 'q2_out.txt')
    
#########################################
# Question 3 - do not delete this comment
#########################################


def get_x_freqs(infile, outfile, x):
    f = open(infile,"r")
    f2 = open (outfile, "w")
    word_freq_dict = {}
    above_the_min = 0
    for line in f:
        for word in line.lower().split():
            word_freq_dict[word] = word_freq_dict.get(word,0) + 1
            
            
    for key in word_freq_dict.keys():
        if word_freq_dict[key]>=x:
            above_the_min = 1
            f2.write(key)
            f2.write('\n')

    if not above_the_min :
        f2.write('no_words!')
        f.close()
        f2.close()
        
get_x_freqs('q3_in_2.txt', 'q3_out.txt', 2)       
#########################################
# Question 4 - do not delete this comment
#########################################


def get_csv_matrix(infile):
    
    mat = []
    i = 0
    d = -1 
    try:
        with open(infile,'r') as f:
            for line in f:
    
                mat.append([])
                striped = line.strip('\n').split(',')
        
                if i == 0 :
                    d = len(striped)
                else:
                    v = len(striped)
                    if d != v:
                        print('Inconsistent number of fields detected in line ' + str(i+1))
                        return None 
                for char in striped:
                    try:
                        mat[i].append(float(char))
                    except ValueError:
                        print('Non-numeric field encountered in line ' + str(i+1))
                        return None
            
            i+=1 
    finally:
        f.close()
    return(mat)


#########################################
# Question 5 - do not delete this comment
#########################################

def secret_dict(infile):
    
    with open(infile,'r') as f:
        sec_dict = {}
        for line in f:
            striped =  line.strip('\n').split(',')

            sec_dict[striped[0]] = striped[1]
    f.close()
    return sec_dict
    

def decode(input_text_file, code_mapping_file, output_text_file):
    
    try:
        sec_dict = secret_dict(code_mapping_file)
        f  = open(input_text_file,'r')
        f2 = open(output_text_file,'w')
    except IOError:
        print('IO error encountered, cannot decode, exiting!')
    
                
    for line in f:
        for number in line.split():
            suitable_char = sec_dict.get(number,-1)
            if suitable_char == -1:
                f.close()
                f2.close()
        
                    #raise ValueError('Missing decrypting for code ' + str(number))
                raise ValueError
            else:
                f2.write(suitable_char)
        f2.write('\n')       
        f.close()
        f2.close()
        return






















