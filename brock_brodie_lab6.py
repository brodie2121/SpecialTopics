try:
  file1 = open("firstFile.txt", "r")
  file2 = open("secondFile.txt", "r")
except:
  print("Error: opening file")
  exit()

set1 = set()
set2 = set()

for word in file1:
  set1.add(word.strip())

for word in file2:
  set2.add(word.strip())

print("A list of all the unique words contained in both files:\n")
set_union = set.union(set1, set2)
print(set_union, "\n")

print("--" * 30)
print("A list of the words that appear in both files:\n")
set_common = set.intersection(set1, set2)
print(set_common, "\n")

print("--" * 30)
print("A list of the words that appear in the first file but not in the second file:\n")
print(set1.difference(set2), "\n")

print("--" * 30)
print("A list of the words that appear in the second file but not in the first file:\n")
print(set2.difference(set1), "\n")

print("--" * 30)
print("A list of the words that appear in either the first or second file but not in both:\n")
print(set_union.difference(set_common), "\n")

file1.close()
file2.close()