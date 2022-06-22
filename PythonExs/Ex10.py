#looking at escape sequences 
tabby_cat = "\tI'm tabbed in." #creats an indent on the line
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat." #create two backslashes to create one. An escape sequence
#always put two backslashes, a way to esacpe issues w/ backslashes  

#\n\t creats an new line and indent 
big_cat = '''
I'll do a list: 
\t* Cat food 
\t* Fishies 
\t* Catnip\n\t* Grass       
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(big_cat)