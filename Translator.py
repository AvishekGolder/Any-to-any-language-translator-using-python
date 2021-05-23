from googletrans import Translator
tl = Translator()
#Bangla to English
print("Enter any Bengali text below: ")
a = input()
out = tl.translate(a, dest='en')
print(out.text)
#English to Bangla
print("Enter any English text below: ")
b = input()
output = tl.translate(b, dest='bn')
print(output.text)
a = input()
