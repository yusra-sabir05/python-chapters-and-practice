# Define a multi-line string with placeholders for name and date  
letters = '''Dear <|Name|>   
you are selected  
<|Date|>'''  

# Replace the placeholders with actual values  
# Replace '<|Name|>' with 'yusra' and '<|Date|>' with '20 feb 2050'  
formatted_letters = letters.replace('<|Name|>', 'yusra').replace('<|Date|>', '20 feb 2050')  

# Print the formatted letter  
print(formatted_letters)