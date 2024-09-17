import Foundation

// Easy Tasks
// 1. Создаем Array
let fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
print("The third fruit is: \(fruits[2])") // Третий фрукт

// 2. Создаем множества
var favoriteNumbers: Set = [3, 7, 13]
favoriteNumbers.insert(21) // Добавляем новое число
print("Updated set of favorite numbers: \(favoriteNumbers)")

// 3. Создаем словарь 
let languages = ["Swift": 2014, "Python": 1991, "Java": 1995]
if let swiftYear = languages["Swift"] {
    print("Swift was released in: \(swiftYear)")
}

// 4. Обновляем Array
var colors = ["Red", "Blue", "Green", "Yellow"]
colors[1] = "Purple" // Обновляем второй цвет
print("Updated colors array: \(colors)")

// Medium Tasks
// 1. Пересечение между сетами
let set1: Set = [1, 2, 3, 4]
let set2: Set = [3, 4, 5, 6]
let intersection = set1.intersection(set2)
print("Intersection of the two sets: \(intersection)")

// 2. Обновленный словарь
var studentScores = ["Alice": 85, "Bob": 90, "Charlie": 88]
studentScores["Bob"] = 95 // Обновляем оценку Боба
print("Updated student scores: \(studentScores)")

// 3. объединение массивов 
let array1 = ["apple", "banana"]
let array2 = ["cherry", "date"]
let mergedArray = array1 + array2
print("Merged array: \(mergedArray)")

// Hard Tasks
// 1. Добавляю ключи в словарь
var countryPopulations = ["USA": 331000000, "India": 1380000000, "Brazil": 213000000]
countryPopulations["Canada"] = 38000000 // Добавляем новую страну
print("Updated dictionary with country populations: \(countryPopulations)")

// 2. Объединение и вычитание множеств
let setA: Set = ["cat", "dog"]
let setB: Set = ["dog", "mouse"]
let unionSet = setA.union(setB) // Объединение множеств
let finalSet = unionSet.subtracting(setB) // Вычитание второго множества
print("Final set after union and subtraction: \(finalSet)")

// 3. Вложенная коллекция
let studentGrades = [
    "Alice": [85, 90, 78],
    "Bob": [88, 76, 95],
    "Charlie": [92, 84, 89]
]
if let bobGrades = studentGrades["Bob"] {
    print("Bob's second grade is: \(bobGrades[1])") // Доступ ко второму элементу массива оценок
}