#  negative indices

name = 'yusra'
# name = 01234  #when positive indices
#name = -5 -4 -3 -2 -1  when negative indices

short_name = name[-4 : -1] #negative indice
print(short_name)

short_name = name[1 : 4] #positive
print(short_name)
short_name = name[ : -1]

print(short_name)

print(name[:5]) # is same as print(name[0:5]) 
print(name[0:]) # is same as print(name[0:5]) 
