#task1
def grams_to_ounces(grams):
    print(28.3495231 * grams)
grams_to_ounces(5)

#task2
def Farenheit(F):
    print((5/9)*(F-32))
Farenheit(5)

#task3
def solve_puzzle(heads, legs):
    for chickens in range(heads + 1):
        rabbits = heads - chickens
        if (2 * chickens + 4 * rabbits) == legs:
            print(chickens, rabbits)
solve_puzzle(35, 94)

#task4
def is_prime(num):
    if num < 2: 
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

input_numbers = input("Enter a list of numbers separated by spaces: ")
numbers_list = [int(num) for num in input_numbers.split()]
prime_numbers = filter_prime(numbers_list)
print("Original List:", numbers_list)
print("Prime numbers:", prime_numbers)

#task5
from itertools import permutations

def print_all_permutations(input_string):
    all_permutations = permutations(input_string)
    for permutation in all_permutations:
        print(''.join(permutation))
        
user_input = input("Enter a string:")
print_all_permutations(user_input)

#task6
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
user_input = input("Enter a sentence:")
result = reverse_words(user_input)
print("Reversed Sentence:", result)

#task7
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
user_input = input("Enter a list of numbers seperated by space")
nums_list = [int(num) for num in user_input.split()]
result = has_33(nums_list)
print(result)

#task8
def spy(nums):
    found_0 = False
    found_0_ = False
    for num in nums:
        if num == 0 and found_0_0:
            return True
        elif num == 0 and found_0:
            return True
        elif num == 7 and found_0_0:
            return True
        elif num == 0:
            found_0 = True
            
    return False
user_input = input("Enter a list of integers separated by commas:")
user_list = [int(x) for x in user_input.split(',')]
result = spy(user_list)
print (result)
 
#task9
import math
def sphere_volume(radius):
    volume = (4 / 3) * math.pi * radius**3
    return volume
radius = float(input("Enter the radius of the sphere: "))
result = sphere_volume(radius)
print(result)

#task10
def unique_elements(input_list):
    unique_list=[]
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
        return unique_list
    
user_input = input("Enter a list of integers separated by commas: ")
user_list = [int(x) for x in user_input.split(',')]

result = unique_elements(user_lists)
print("Original list:", user_list)
print("List with unique elements:", result)

#task11
def is_palindrome(word):
    cleaned_word = ''.join(word.lower().split())
    return cleaned_word == cleaned_word[::-1]
user_input = input("Enter a word or phrase: ")
result = is_palindrome(user_input)
print(result)

#task12
def histogram(numbers):
    for num in numbers:
        print('*' * num)
        
#task13
import random 
def guess_number():
    print("Hello! What is your name?")
    name = input()
    print("Well, {name}, I am thinking of a number between 1 and 20.")
    
    secret_number = random.randint(1, 20)
    guesses_taken = 0
    while True:
        print("Take a guess")
        guess = int(input())
        guesses_taken +=1
        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            print("Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
        
guess_number() 
