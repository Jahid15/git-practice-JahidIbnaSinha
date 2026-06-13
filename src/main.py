from datetime import date
from utils import add, subtract, multiply, divide

print("My name is: Jahid Ibna Sinha")
print("Today's date is:", date.today())

print("\n--- Calculator ---")
print("5 + 3 =", add(5, 3))
print("10 - 4 =", subtract(10, 4))
print("5 x 3 =", multiply(5, 3))

try:
    print("10 / 2 =", divide(10, 2))
    print("10 / 0 =", divide(10, 0))  # This will trigger the error
except ValueError as e:
    print(e)