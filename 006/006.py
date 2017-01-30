sum_squares = 0
squares_sum = 0
for i in range(1, 101):
    sum_squares += i**2
    squares_sum += i
diff = (squares_sum**2) - sum_squares
print(diff)







