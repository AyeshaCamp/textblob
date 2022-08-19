# import textblob
from textblob import TextBlob

#variable
a = TextBlob(input("Please neter here:"))

#using correct method
a = a.correct()

print(a)