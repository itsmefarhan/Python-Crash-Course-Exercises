'''4-1. Pizzas: Think of at least three kinds of your favorite pizza . Store these pizza names in a list, 
and then use a for loop to print the name of each pizza . 
•	Modify your for loop to print a sentence using the name of the pizza instead of printing 
just the name of the pizza . For each pizza you should have one line of output containing a simple statement
like I like pepperoni pizza . 
•	Add a line at the end of your program, outside the for loop, that states how much you like pizza . 
The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, 
such as I really love pizza!'''

# pizzas = ['chicken tikka', 'fijita', 'supreme']

# for pizza in pizzas:
    # print(pizza)
#     print(f'I like {pizza} pizza')
# print('\nI really love pizza')

'''4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive . '''

# for number in range(1, 21):
#     print(number)

'''4-4. One Hundred: Make a list of the numbers from one to one Hundred, and then use a for loop to print the numbers'''

# numbers = list(range(1, 101))
# for num in numbers:
#     print(num)

'''4-5. Summing a hundred: Make a list of the numbers from one to one hundred, 
and then use min() and max() to make sure your list actually starts at one and ends at one hundred . 
Also, use the sum() function to see how quickly Python can add a hundred numbers .'''

# numbers = list(range(1, 101))
# print('Smallest number:', min(numbers))
# print('Highest number:', max(numbers))
# print('Sum of 1 to 100:', sum(numbers))

'''4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20 . 
Use a for loop to print each number . '''

# odd_num = list(range(1, 20, 2))
# for num in odd_num:
#     print(num)

'''4-7. Threes: Make a list of the multiples of 3 from 3 to 30 . Use a for loop to print the numbers in your list .'''

# multiple_of_three = list(range(3, 31, 3))
# for num in multiple_of_three:
#     print(num)

'''4-8. Cubes: A number raised to the third power is called a cube . For example, the cube of 2 is written as 2**3 
in Python . Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
and use a for loop to print out the value of each cube .'''

# cubes = list(range(1, 11))
# for cube in cubes:
#     print(cube ** 3)

'''4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes .'''

# cubes = [cube ** 3 for cube in range(1, 11)]
# print(cubes)

'''4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program 
that do the following: 
•	Print the message, The first three items in the list are: . Then use a slice to print the first three items 
from that program’s list . 
•	Print the message, Three items from the middle of the list are: . Use a slice to print three items 
from the middle of the list . 
•	Print the message, The last three items in the list are: . Use a slice to print the last three items 
in the list .'''

# pizzas = ['chicken tikka', 'fijita', 'supreme', 'pepporoni', 'cheese']
# print('The first three items in the list are: ', pizzas[:3])
# print('Three items from the middle of the list are: ', pizzas[1:4])
# print('The last three items in the list are: ', pizzas[2:])

'''4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 60) . Make a copy of the list 
of pizzas, and call it friend_pizzas . Then, do the following: 
•	Add a new pizza to the original list . 
•	Add a different pizza to the list friend_pizzas . 
•	Prove that you have two separate lists . 
Print the message, My favorite pizzas are:, and then use a for loop to print the first list . 
Print the message, My friend’s favorite pizzas are:, and then use a for loop to print the second list . 
Make sure each new pizza is stored in the appropriate list .'''

# pizzas = ['chicken tikka', 'fijita', 'supreme']
# friend_pizzas = pizzas[:]
# pizzas.append('pepporoni')
# friend_pizzas.append('cheese')
# print('My favorite pizzas are', pizzas)
# print("My friend's favorite pizzas are", friend_pizzas)

'''4-12. More Loops: All versions of foods.py in this section have avoided using for loops 
when printing to save space . Choose a version of foods.py, and write two for loops to print each list of foods .'''

# my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
# friend_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']

# for my_food in my_foods:
#     print(my_food)
# for friend_food in friend_foods:
#     print(friend_food)


'''4-13. Buffet: A buffet-style restaurant offers only five basic foods . Think of five simple foods, 
and store them in a tuple . 
•	Use a for loop to print each food the restaurant offers . 
•	Try to modify one of the items, and make sure that Python rejects the change . 
•	The restaurant changes its menu, replacing two of the items with different foods . 
Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.'''

# basic_food = ('Pizza', 'Mutton', 'Chicken', 'Beef', 'Burger')
# for food in basic_food:
#     print(food)

# basic_food[0] = 'Sandwich'

basic_food = ('Sandwich', 'Mutton', 'Chicken', 'Beef', 'Burger')
for food in basic_food:
    print(food)