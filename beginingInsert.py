def after_insertion(list1):
    length = len(list1)

    value = int(input("\nHow much value you are want to insert: "))
    list1.append(None)
    for i in range(length-1,0-2,-1):

        list1[i+1] = list1[i]
    list1[0] = value
    return list1

list1 = []
last_num = int(input("Enter the last number: "))

for i in range(last_num):
    inputs = int(input(f"Enter the  list1[{i}] index element: "))
    list1.append(inputs)

print("\nBefore insertion list1")
for i in range(len(list1)):
    print(f"Enter the  list1[{i}] index element: ", list1[i])

list1 = after_insertion(list1)

print("\nUpdate list1")
for i in range(len(list1)):
    print(f"Enter the  list1[{i}] index element: ", list1[i])

