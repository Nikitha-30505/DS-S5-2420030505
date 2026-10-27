def find_square(num):
    return num * num
numb_to_square = input()
squared_value = find_square(int(numb_to_square))
print(f"The square of{numb_to_square} is {squared_value}")

#evenORodd
def evenORodd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
n = int(input())
result = evenORodd(n)
print(f"The number {n} is {result}")    