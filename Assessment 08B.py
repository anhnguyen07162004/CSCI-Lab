# Anh Nguyen
# CSCI 102 - Section B
# Assessment 08B
# References: https://www.geeksforgeeks.org/python-count-overlapping-substring-in-a-given-string/, https://www.geeksforgeeks.org/python-program-to-find-indices-of-overlapping-substrings/#:~:text=To%20count%20the%20number%20of,finditer()%20method.
# Time: 60 minutes

import re

index_list = []
replacer_word = ""
str1 = input()
substr = input()

if len(substr) > len(str1):
  print("OUTPUT ERROR")
else:
  def CountOccurrences(string, substring):
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
          start = pos + 1
          count += 1
        else:
          break
    return count
  print("OUTPUT", CountOccurrences(str1, substr))

def CountIndices(pattern, string):
  a = [m.start() for m in re.finditer(
  '(?={0})'.format(re.escape(pattern)), string)]
  return a
  
index_list = CountIndices(substr, str1)
index_string = " ".join(map(str, index_list))

print("OUTPUT", index_string)
