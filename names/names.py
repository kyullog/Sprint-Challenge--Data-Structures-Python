import time
from binary_search_tree import BinarySearchTree


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

start_time = time.time()

my_duplicates = []

name_tree_1 = BinarySearchTree(names_1[0])
name_tree_2 = BinarySearchTree(names_2[0])

for i in range(len(names_1)):
    name_tree_1.insert(names_1[i])

for i in range(len(names_2)):
    name_tree_2.insert(names_2[i])

dupes = []
for name in names_1:

    if name_tree_2.contains(name):
        my_duplicates.append(name)


end_time = time.time()
print(f"{len(my_duplicates)} duplicates:\n\n{', '.join(my_duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
