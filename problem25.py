#problem-25

n = int(input("Enter the dimension of the square matrix (n): "))

user_matrix = []
print("Enter the elements of the matrix:")
for _ in range(n):
    row = list(map(int, input().split()))
    user_matrix.append(row)


major_diagonal_sum = 0
minor_diagonal_sum = 0


for i in range(n):
    major_diagonal_sum += user_matrix[i][i]


for i in range(n):
    minor_diagonal_sum += user_matrix[i][n - 1 - i]

print("\nMatrix:")
for row in user_matrix:
    print(row)


print("\nSum of major diagonal:", major_diagonal_sum)
print("Sum of minor diagonal:", minor_diagonal_sum)


if major_diagonal_sum > minor_diagonal_sum:
    print("Major aligned")
elif minor_diagonal_sum > major_diagonal_sum:
    print("Minor aligned")
else:
    print("Balance")