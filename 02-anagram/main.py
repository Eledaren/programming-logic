def anagram(str1, str2):
  if sorted(str1) == sorted(str2): print(True)
  else: print(False)

str1 = input('Enter the first word: ')
str2 = input('Enter the second word: ')

anagram(str1, str2)