# Taking input as a list of strings
a = list(input("Enter strings separated by spaces: ").split())
print(a)
# Sorting the list alphabetically
sorted_list = sorted(a)
# Displaying the sorted list
print("Sorted list of strings:")
k=[]
for i in sorted_list:
    k.append(i)
print(k)
