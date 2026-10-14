def square_even_positive(nums):
    return [n * n for n in nums if n > 0 and n % 2 == 0]


numbers = [1, 2, 3, 4, 5, 6, -2, 8, 0]
print(square_even_positive(numbers))
