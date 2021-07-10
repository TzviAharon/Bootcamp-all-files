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
                    

print 'Congrats!!!'
print 'All preliminary tests passed!'
