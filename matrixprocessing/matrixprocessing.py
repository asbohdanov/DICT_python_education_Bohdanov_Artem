def read_matrix(prompt_size, prompt_matrix):
    while True:
        try:
            dimensions = input(f"{prompt_size} > ").strip().split()
            if len(dimensions) == 2:
                n = int(dimensions[0])
                m = int(dimensions[1])
                if n > 0 and m > 0:
                    break
            print("Input must be two positive numeric digits!")
        except ValueError:
            print("Input must be two positive numeric digits!")
    # Частина функції для зчитування розмірів матриці

    print(prompt_matrix)
    matrix=[]
    while len(matrix) < n:
        try:
            row_input = input("> ").strip().split()
            row = list(map(float, row_input))
            if len(row) == m:
                matrix.append(row)
            else:
                print("Row must contain exactly", m, "numbers!")
        except ValueError:
            print("Input must be numeric values separated by spaces!")
    return matrix
    #Частина функції для зчитування самої матриці розміром n на m


def format_num(val):
    if val % 1 == 0:
        return int(val)
    return round(val, 2)
    #Функція, що округляє числа, до виду int


def print_result(matrix):
    print("The result is:")
    for row in matrix:
        print(*[format_num(x) for x in row])
    print()
    #функція для виведення результату


def transpose_matrix(matrix, method):
    n = len(matrix)
    m = len(matrix[0])
    if method == "1":
        return [[matrix[i][j] for i in range(n)] for j in range(m)]
    elif method == "2":
        return [[matrix[n - 1 - i][m - 1 - j] for i in range(n)] for j in range(m)]
    elif method == "3":
        return [row[::-1] for row in matrix]
    elif method == "4":
        return matrix[::-1]
    #Функція для транспонування матриці


def get_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(len(matrix)):
        minor = [row[:c] + row[c + 1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * get_determinant(minor)
    return det
    #Функція для визначення визначника


def get_inverse_matrix(matrix):
    det = get_determinant(matrix)
    if det == 0:
        return None
    n = len(matrix)
    if n == 1:
        return [[1 / det]]
    cofactors = []
    for r in range(n):
        cofactor_row = []
        for c in range(n):
            minor = [row[:c] + row[c + 1:] for row in (matrix[:r] + matrix[r + 1:])]
            cofactor_row.append(((-1) ** (r + c)) * get_determinant(minor))
        cofactors.append(cofactor_row)
    # Створення матриці алгебраїчних доповнень

    adjugate = transpose_matrix(cofactors, "1")
    # Транспонуємо матрицю доповненбь щодо головної діагоналі

    return [[adjugate[i][j] / det for j in range(n)] for i in range(n)]
    # Ділимо кожен елемент приєднаної матриці на визначник


def main():
    while True:
        print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
        choice = input("Your choice: > ").strip()
        if choice == "0":
            break
        elif choice == "1":
            matrix_a = read_matrix("Enter size of first matrix:", "Enter first matrix:")
            matrix_b = read_matrix("Enter size of second matrix:", "Enter second matrix:")
            if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
                print("The operation cannot be performed.\n")
                continue
            res = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
            print_result(res)
        #Частина функції для додавання матриць

        elif choice == "2":
            matrix = read_matrix("Enter size of matrix:", "Enter matrix:")
            while True:
                try:
                    constant = float(input("Enter constant: > ").strip())
                    break
                except ValueError:
                    print("Input must be a single numeric value!")
            res = [[elem * constant for elem in row] for row in matrix]
            print_result(res)
        #Частина функції для множення матриці на константу

        elif choice == "3":
            matrix_a = read_matrix("Enter size of first matrix:", "Enter first matrix:")
            matrix_b = read_matrix("Enter size of second matrix:", "Enter second matrix:")
            if len(matrix_a[0]) != len(matrix_b):
                print("The operation cannot be performed.\n")
                continue
            res = []
            for i in range(len(matrix_a)):
                res_row = []
                for j in range(len(matrix_b[0])):
                    cell_sum = sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_b)))
                    res_row.append(cell_sum)
                res.append(res_row)
            print_result(res)
        #Частина функції для множення матриць

        elif choice == "4":
            print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
            t_choice = input("Your choice: > ").strip()
            if t_choice in ["1", "2", "3", "4"]:
                matrix = read_matrix("Enter matrix size:", "Enter matrix:")
                res = transpose_matrix(matrix, t_choice)
                print_result(res)
            else:
                print("Incorrect choice.\n")
        #Частина функції для транспонування матриці

        elif choice == "5":
            matrix = read_matrix("Enter matrix size:", "Enter matrix:")
            if len(matrix) != len(matrix[0]):
                print("The operation cannot be performed. Matrix must be square.\n")
                continue
            det = get_determinant(matrix)
            print("The result is:")
            print(format_num(det))
            print()
        #Частина функції для визначення визначника

        elif choice == "6":
            matrix = read_matrix("Enter matrix size:", "Enter matrix:")
            if len(matrix) != len(matrix[0]):
                print("The operation cannot be performed. Matrix must be square.\n")
                continue
            inverse = get_inverse_matrix(matrix)
            if inverse is None:
                print("This matrix doesn't have an inverse.\n")
            else:
                print_result(inverse)
        #Частина функції для знаходження зворотної матриці

    #Основна функція з меню та його розділами

main()