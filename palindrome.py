def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]

def sum_of_digits(num):
    return sum(int(digit) for digit in str(abs(num)))

n = int(input("Enter an integer N: "))

digit_sum = sum_of_digits(n)

if is_palindrome(digit_sum):
    print("palindrome")
else:
    print("not palindrome")