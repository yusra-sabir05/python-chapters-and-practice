a = "yusra"
t = type(a)
print(t)  # Output: <class 'str'>

a = 3
t = type(a)
print(t)  # Output: <class 'int'>

a = 3.33
t = type(a)
print(t)  # Output: <class 'float'>

a = True
t = type(a)
print(t)  # Output: <class 'bool'>

# we can chnage any variable into any type

a = "3.12"  #this is string   changed into fl
b = float(a)
t = type(b)
print(t)  # Output: <class 'float'>

a = "3.12"
b = float(a)
c = str(b)
t = type(c)
print(t)  # Output: <class 'str'>

a = "3.12"
b = float(a)
c = str(b)
t = type(a)
print(t)  # Output: <class 'str'>
