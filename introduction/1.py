new_list = [1, 2, 3, "Indonesia"]

for element in new_list:
    try:
        print(element / 2)
    except:
        print("The element is not a number")
