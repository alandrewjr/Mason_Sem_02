import random
import sys
import os

#print("hello world")
name = "world"
#print("hello", name)
#single comment
'''
multiline comment
'''
quote = "\"Always remember you are unique"
multi_line_quote = ''' just like
everyone else'''

new_string = quote + multi_line_quote
print(new_string)
print("\n" * 1)
print("%s %s %s" % ('I like the quote', quote, multi_line_quote))
print("\n" * 1)
print("I don't like " , end="")
print("newlines")