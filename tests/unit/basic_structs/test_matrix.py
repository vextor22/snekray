from snekray import Matrix


def test_matrix_creation_4x4():
    data = (
        (1, 2, 3, 4),
        (5.5, 6.5, 7.5, 8.5),
        (9, 10, 11, 12),
        (13.5, 14.5, 15.5, 16.5),
    )
    m = Matrix(data)

    assert m.get(0, 0) == 1
    assert m.get(0, 3) == 4
    assert m.get(1, 0) == 5.5
    assert m.get(1, 2) == 7.5
    assert m.get(2, 2) == 11
    assert m.get(3, 0) == 13.5
    assert m.get(3, 2) == 15.5


def test_matrix_creation_2x2():
    data = (
        (
            -3,
            5,
        ),
        (1, -2),
    )
    m = Matrix(data)

    assert m.get(0, 0) == -3
    assert m.get(0, 1) == 5
    assert m.get(1, 0) == 1
    assert m.get(1, 1) == -2


def test_matrix_creation_3x3():
    data = (
        (-3, 5, 0),
        (1, -2, -7),
        (0, 1, 1),
    )
    m = Matrix(data)

    assert m.get(0, 0) == -3
    assert m.get(1, 1) == -2
    assert m.get(2, 2) == 1


def test_matrix_equality_with_identical_matrix():
    data = (
        (-3, 5, 0),
        (1, -2, -7),
        (0, 1, 1),
    )
    m1 = Matrix(data)
    m2 = Matrix(data)

    assert m1 == m2


def test_matrix_equality_with_different_matrix():
    data = (
        (-3, 5, 0),
        (1, -2, -7),
        (0, 1, 1),
    )
    data_2 = (
        (-3, 5, 0),
        (1, -1, -7),
        (0, 1, 1),
    )
    m1 = Matrix(data)
    m2 = Matrix(data_2)

    assert m1 != m2


def test_matrix_multiplication():

    data = ((1, 2, 3, 4), (5, 6, 7, 8), (9, 8, 7, 6), (5, 4, 3, 2))
    data_2 = ((-2, 1, 2, 3), (3, 2, 1, -1), (4, 3, 6, 5), (1, 2, 7, 8))
    data_3 = (
        (20, 22, 50, 48),
        (44, 54, 114, 108),
        (40, 58, 110, 102),
        (16, 26, 46, 42),
    )
    m1 = Matrix(data)
    m2 = Matrix(data_2)
    expected = Matrix(data_3)
    actual = m1 * m2
    assert actual == expected


def test_matrix_multiplication_by_tuple():

    data = ((1, 2, 3, 4), (2, 4, 4, 2), (8, 6, 4, 1), (0, 0, 0, 1))
    tup = (1, 2, 3, 1)
    data_3 = (
        (18,),
        (24,),
        (33,),
        (1,),
    )
    m1 = Matrix(data)
    expected = Matrix(data_3)
    actual = m1 * tup
    assert actual == expected


def test_get_identity_matrix():

    data = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
    data_2 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    m1 = Matrix(data)
    m2 = Matrix(data_2)

    identity = Matrix.identity_matrix()
    identity_2 = Matrix.identity_matrix(3)
    assert m1 == identity
    assert m2 == identity_2


def test_multiple_by_identity_matrix():
    data = ((0, 1, 2, 4), (1, 2, 4, 8), (2, 4, 8, 16), (4, 8, 16, 32))
    m = Matrix(data)
    assert m * Matrix.identity_matrix() == m


def test_matrix_transpose():
    data = ((0, 9, 3, 0), (9, 8, 0, 8), (1, 8, 5, 3), (0, 0, 5, 8))
    transpose_data = ((0, 9, 1, 0), (9, 8, 8, 0), (3, 0, 5, 5), (0, 8, 3, 8))

    m = Matrix(data)
    m_t = Matrix(transpose_data)

    assert m.transpose() == m_t


def test_matrix_transpose_of_identity():

    identity_matrix = Matrix.identity_matrix()

    assert identity_matrix == identity_matrix.transpose()


def test_2x2_determinant():
    data = ((1, 5), (-3, 2))

    m = Matrix(data)

    assert m.determinant() == 17


def test_3x3_submatrix():
    data = ((1, 5, 0), (-3, 2, 7), (0, 6, -3))
    m = Matrix(data)

    sub_data = ((-3, 2), (0, 6))
    sub_m = Matrix(sub_data)

    assert m.submatrix(0, 2) == sub_m


def test_4x4_submatrix():
    data = ((2, 1, 5, 0), (9, 9, 9, 9), (3, -3, 2, 7), (4, 0, 6, -3))
    m = Matrix(data)

    sub_data = ((1, 5, 0), (-3, 2, 7), (0, 6, -3))
    sub_m = Matrix(sub_data)

    assert m.submatrix(1, 0) == sub_m
    assert m.submatrix(2, 0) != sub_m


def test_3x3_minor():
    data = ((3, 5, 0), (2, -1, -7), (6, -1, 5))
    a = Matrix(data)
    b = a.submatrix(1, 0)
    assert b.determinant() == 25
    assert a.minor(1, 0) == 25


def test_3x3_cofactor():
    data = ((3, 5, 0), (2, -1, -7), (6, -1, 5))
    a = Matrix(data)
    assert a.minor(0, 0) == -12
    assert a.cofactor(0, 0) == -12

    assert a.minor(1, 0) == 25
    assert a.cofactor(1, 0) == -25
