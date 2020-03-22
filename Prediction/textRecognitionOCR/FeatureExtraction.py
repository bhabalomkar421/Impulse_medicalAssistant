import re

sentence = "Name : Abhishek Gupta"
pattern = ".* : (.*)"
result = re.search(pattern, sentence)
print(result.group(1))