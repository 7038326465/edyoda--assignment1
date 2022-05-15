# check the program for reverse of words mirror view


reverse = input("Input a word to reverse: ")

for words in range(len(reverse) - 1, -1,-1,):
  print(reverse[words], end="")
print("")
