#################################################################
# FILE : ex3.py
# WRITER : daniel_riazanov , daniel.rez , 336119300
# EXERCISE : intro2cs ex3 2024
# DESCRIPTION: Module for practising loops
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: None
#################################################################


def input_list():
    """
    function receives inputs from user until no numb entered, adds converted str to a list, adds a sum of all numbers
    as a last member and returns a final list. If no numbs entered returns 0.
    """
    users_nums = []
    total_sum = 0

    while True:
        string_from_user = input()
        if string_from_user == "":
            break
        converted_input = float(string_from_user)
        users_nums.append(converted_input)

    if len(users_nums) == 0:
        users_nums.append(0)
        return users_nums

    for num in users_nums:
        total_sum += num
    users_nums.append(total_sum)

    return users_nums


def inner_product(vec_1, vec_2):
    """
    function takes two vectors and returns their product. If vectors length are diff => returns None. If one of the
    lists is empty => returns 0
    """
    res = 0
    if len(vec_1) != len(vec_2):
        return None
    elif len(vec_1) == 0 or len(vec_2) == 0:
        return 0
    else:
        for i in range(len(vec_1)):  # Possible because vectors are of the same num of dimension (len)
            res += vec_1[i] * vec_2[i]
    return res


def sequence_monotonicity(sequence):
    """
    function takes a sequence and returns list of boolean values describing whether sequence is:
        monotonic increasing
        strictly monotonic increasing
        monotonic decreasing
        strictly monotonic decreasing
    If sequence contains 0 or 1 member => returns False, False, False, False
    """
    res = [True, True, True, True]
    if len(sequence) == 0 or len(sequence) == 1:
        return [False, False, False, False]
    for i in range(1, len(sequence)):
        if not (sequence[i - 1] <= sequence[i]):
            res[0] = False
        if not (sequence[i - 1] < sequence[i]):
            res[1] = False
        if not (sequence[i - 1] >= sequence[i]):
            res[2] = False
        if not (sequence[i - 1] > sequence[i]):
            res[3] = False

    return res


def monotonicity_inverse(def_bool):
    """
    function takes a list of 4 boolean values referring to monotonicity of a sequence and returns an example for each
    possible case, when case is not possible returns None.
    """
    if def_bool == [True, True, False, False]:
        return [50.1, 51.1, 58, 125]
    if def_bool == [True, False, False, False]:
        return [1, 2, 2, 3]
    if def_bool == [False, False, True, False]:
        return [250, 249, 248.9, 7]
    if def_bool == [False, False, True, True]:
        return [250, 249, 248.9, 248.9]
    if def_bool == [False, False, False, False]:
        return [-1, 1, 0, 1]
    else:
        return None


def convolve(mat):
    """
    function computes the 3x3 convolution of the given matrix. It operates by iteratively traversing the
    entire matrix, calculating the sum of each 3x3 square region, and storing the results in a list. After computing
    the sums, it constructs a new matrix based on the original matrix dimensions, where each element is the sum of
    the corresponding 3x3 square in the original matrix.
    """
    for lst in mat:  # Validation
        if len(lst) == 0:
            return None
    """ Declaring Func Scope Variables"""
    total_colums = len(mat[0])  # Ranges of matrix to work in
    total_rows = len(mat)  # Ranges of matrix to work in
    result = []  # List of square sums
    result_matrix = []  # Returned matrix (convolved)

    """Main matrix iteration"""
    for i in range(total_rows - 2):
        for j in range(total_colums - 2):
            square_sum = 0  # initial sum for each 3*3 square in matrix:
            """3*3 square iteration"""
            for row_set in range(3):
                for colum_set in range(3):
                    square_sum += mat[i + row_set][j + colum_set]
            result.append(square_sum)

    """Building matrix from the square sum list"""

    index = 0
    while index < (len(result)):
        row = []
        for i in range(total_colums - 2):
            row.append(result[index])
            index += 1
        result_matrix.append(row)
    return result_matrix


def sum_of_vectors(vec_lst):
    """
    function calculates the sum of a list of vectors. After validating the input, the function initializes a container
    (list) to store the result based on the dimensions (coordinates) of the vectors. It then efficiently iterates over
    each index in the list, summing the corresponding coordinates of all vectors in the input list in a single loop.
    """

    if len(vec_lst) == 0:
        return None
    for vec in vec_lst:
        if len(vec) == 0:
            return []

    num_of_coord = len(vec_lst[0])

    vec_sum = [0] * num_of_coord  # Since all vectors are same size we create container for the result

    for vec in vec_lst:
        for i in range(num_of_coord):
            vec_sum[i] += vec[i]
    return vec_sum


def num_of_orthogonal(vectors):
    """
    function calculates the number of orthogonal pairs of vectors based on given list of vectors. It uses 2 loops to
    choose each pair of vectors and compute their inner product. If the product is sero we increase the counter and
    after finishing the iteration func returns counter
    """
    total_orthogonal = 0
    num_vectors = len(vectors)
    for i in range(num_vectors):
        for j in range(i + 1, num_vectors):
            vectors_product = inner_product(vectors[i], vectors[j])
            if vectors_product == 0:
                total_orthogonal += 1

    return total_orthogonal
