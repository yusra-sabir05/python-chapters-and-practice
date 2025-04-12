# Sample string  
text = "  Hello, World!  "  
print(text)
# 1. Basic String Methods  
print("Original String:", repr(text)) 
 
print("Lowercase:", text.lower())        # "  hello, world!  "  
print("Uppercase:", text.upper())        # "  HELLO, WORLD!  "  
print("Title Case:", text.title())        # "  Hello, World!  "  
print("Capitalized:", text.capitalize())  # "  Hello, world!  "  # remove spaces to get the correct aswer  
print("Stripped:", text.strip())          # "Hello, World!"  

# 2. Searching and Replacing  
print("Find 'World':", text.find("World"))  # 9 count spaces too 
print("Replace 'World' with 'Python':", text.replace("World", "Python"))  # "  Hello, Python!  "  
print("Count of 'o':", text.count("o"))  # 2  

# 3. Splitting and Joining  
words = text.split()  # ['Hello,', 'World!']  
print("Split words:", words)  
joined_string = " - ".join(words)  # "Hello, - World!"  
print("Joined string:", joined_string)  

# 4. String Formatting  
name = "Alice"  
greeting = f"Hello, {name}!"  # Using f-string  
print("Formatted String:", greeting)  

# 5. Checking Properties  
print("Is Alpha:", text.isalpha())       # False  
print("Is Digit:", text.isdigit())       # False  
print("Is Alphanumeric:", text.isalnum()) # False  
print("Is Space:", text.isspace())       # False  

# 6. Other Useful Methods  
print("Starts with '  Hello':", text.startswith("  Hello"))  # True  
print("Ends with 'World!  ':", text.endswith("World!  "))    # True  
print("Split lines:", text.splitlines())  # ['  Hello, World!  ']  

# # Additional Example to demonstrate splitlines  
multi_line_text = "Hello, World!\nWelcome to Python.\nEnjoy coding!"  
print("Multi-line Splitting:", multi_line_text)
print("Multi-line Splitting:", multi_line_text.splitlines())