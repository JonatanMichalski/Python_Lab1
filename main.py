from list1 import divisible
from list1 import common

numbers = [1,2,3,4,5]
divisor = 3

try:
    result = divisible(numbers, divisor)
    print("Original list:", numbers)
    print("Divisor: ", divisor)
    print("Result: ", result)
except (TypeError, ValueError) as error:
    print("Error: ", error)
    
x = [7,5,2,1,8,5,6,8]
y = [8,6,8,3,4,5,2]

try:
    result = common(x, y)
    print("List x:", x)
    print("List y:", y)
    print("Common:", result)
except (TypeError) as error:
    print("Error: ", error)
