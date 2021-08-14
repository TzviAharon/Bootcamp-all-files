'''
The next code block executes several tests of common scenarios for your aid. 
You are more than welcome to add tests of your own, but it's not mandatory.
'''


# assert sentence throws an error if the expression after it equals False.
assert catalan_rec(3) == 5
assert catalan_mem(5) ==42

if 'catalan_rec_with_count' in globals():
	res= catalan_rec_with_count(7)
	assert  res[0] == 429
	assert res[1] <= 2500

if 'catalan_mem_with_count' in globals():
	res = catalan_mem_with_count(7)
	assert res[0] == 429
	assert res[1] <=110
 
assert atm_rec(100,(20,),5) == True
assert atm_mem (100,(13,17),7)==False
assert atm_mem (90,(13,17),6)==True


assert max_trail([[4],[5,7],[3,4,2],[8,3,6,1]]) == 21
assert max_trail_mem([[3],[6,12],[6,3,10],[4,65,5,6]]) == 83

print 'Congrats!!!'
print 'All preliminary tests passed!'
