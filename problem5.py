def reverseWord(w):
  return ' '.join(w.split()[::-1])
w=input("enter the string to reverse")
print(reverseWord(w))
