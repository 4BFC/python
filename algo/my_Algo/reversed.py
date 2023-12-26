# original_list = input().split()
original_list = list(map(int, input().split()))
reversed_list = list(reversed(original_list))
sorted_list = list(sorted(original_list))

print(type(original_list[0]))
print("Reversed List:", reversed_list)
print("Sorted List:", sorted_list)
print("Original List:", original_list)
