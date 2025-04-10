# ex:4
# write a program to print the content of  a directly using os module search online for the function which does that 

# # ex:5
# label the program written in problem 4 with comments 

import os
# specify the directory you want to list
directory_path = '/'
# list all the file and directories in the specified path 
content = os.listdir(directory_path)
# print each file and directory name 
for item in content:
    print(item)