#Exercise 10: Create a new list from two list using the following condition
#Create a new list from two list using the following condition

#Given two list of niumbers, wrte a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

def combine_list(first_list, second_list):
    final_list = []
    for i in range(0, 5, 1):
        if first_list[i] % 2 == 0:
            ""
        else:
            final_list.append(first_list[i])

    for i in range(0, 5, 1):
        if second_list[i] % 2 == 0:
            final_list.append(second_list[i])
    
    print("the result is", final_list)

first_list = [10, 20, 25, 30, 35]
second_list = [40, 45, 60, 75, 90]
combine_list(first_list, second_list)
    
