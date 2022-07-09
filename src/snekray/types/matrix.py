from __future__ import annotations
from typing import List, Tuple, cast, Union
import math
import snekray as sr


class Matrix:
    def __init__(self, data: Tuple[Tuple[float, ...], ...]) -> None:
        self.matrix: Tuple[Tuple[float, ...], ...] = data
        self.col_count = len(self.matrix[0])

    def __repr__(self) -> str:
        return "\n".join(str(row) for row in self.matrix)

    @classmethod
    def _identity(cls, dim: int = 4) -> List[List[float]]:

        return list(
            list((1.0 if i == j else 0.0) for j in range(dim)) for i in range(dim)
        )

    @classmethod
    def identity_matrix(cls, dim: int = 4) -> Matrix:
        return Matrix(tuple(tuple(row) for row in cls._identity(dim)))

    @classmethod
    def ll2m(cls, ll):
        return Matrix(tuple(tuple(row) for row in ll))

    @classmethod
    def translation(cls, x, y, z) -> Matrix:
        ident = cls._identity()
        ident[0][3] = x
        ident[1][3] = y
        ident[2][3] = z
        return cls.ll2m(ident)

    @classmethod
    def scaling(cls, x, y, z) -> Matrix:
        ident = cls._identity()
        ident[0][0] = x
        ident[1][1] = y
        ident[2][2] = z

        return cls.ll2m(ident)

    @classmethod
    def rotation_x(cls, r):
        ident = cls._identity()
        ident[1][1] = math.cos(r)
        ident[1][2] = -math.sin(r)
        ident[2][1] = math.sin(r)
        ident[2][2] = math.cos(r)
        return cls.ll2m(ident)

    @classmethod
    def rotation_y(cls, r):
        ident = cls._identity()
        ident[0][0] = math.cos(r)
        ident[0][2] = math.sin(r)
        ident[2][0] = -math.sin(r)
        ident[2][2] = math.cos(r)
        return cls.ll2m(ident)

    @classmethod
    def rotation_z(cls, r):
        ident = cls._identity()
        ident[0][0] = math.cos(r)
        ident[0][1] = -math.sin(r)
        ident[1][0] = math.sin(r)
        ident[1][1] = math.cos(r)
        return cls.ll2m(ident)

    @classmethod
    def shearing(cls, xy, xz, yx, yz, zx, zy):
        ident = cls._identity()
        ident[0][1] = xy
        ident[0][2] = xz
        ident[1][0] = yx
        ident[1][2] = yz
        ident[2][0] = zx
        ident[2][1] = zy
        return cls.ll2m(ident)

    def submatrix(self, row_i, col_j):
        return Matrix(
            [
                [col for j, col in enumerate(row) if j != col_j]
                for i, row in enumerate(self.matrix)
                if i != row_i
            ]
        )

    def get(self, row, column) -> float:
        return self.matrix[row][column]

    def get_row(self, row) -> Tuple[float, ...]:
        return self.matrix[row]

    def get_column(self, col) -> Tuple[float, ...]:
        return tuple(row[col] for row in self.matrix)

    @property
    def cols(self):
        for i in range(self.col_count):
            yield self.get_column(i)

    @property
    def is_invertible(self):
        return self.determinant() != 0

    def inverse(self):
        cofactor_matrix = Matrix(
            tuple(
                tuple(self.cofactor(i, j) for j, _ in enumerate(row))
                for i, row in enumerate(self.matrix)
            )
        )
        transpose_cofactors = cofactor_matrix.transpose()
        return transpose_cofactors / self.determinant()

    def determinant(self) -> float:
        if len(self.matrix) == 2:
            return (self.matrix[0][0] * self.matrix[1][1]) - (
                self.matrix[1][0] * self.matrix[0][1]
            )
        else:
            determinant = 0.0
            for i in range(len(self.matrix)):
                determinant += self.matrix[0][i] * self.cofactor(0, i)
            return determinant

    def transpose(self):
        return Matrix(tuple(self.cols))

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Matrix):
            return NotImplemented
        __o = cast(Matrix, __o)
        is_equal = True
        for i, row in enumerate(self.matrix):
            is_equal = is_equal and all(
                (
                    math.isclose(round(element, 5), __o.get(i, j))
                    for j, element in enumerate(row)
                )
            )

        return is_equal

    def cross(self, row, col) -> float:
        return sum(x[0] * x[1] for x in zip(row, col))

    def minor(self, row, col) -> float:
        return self.submatrix(row, col).determinant()

    def cofactor(self, row, col) -> float:
        minor_value = self.minor(row, col)

        if (row + col) % 2:
            minor_value *= -1

        return minor_value

    def to_point(self) -> sr.Point:
        return sr.Point(*self.get_column(0)[:3])

    def to_vector(self) -> sr.Vector:
        return sr.Vector(*self.get_column(0)[:3])

    def __mul__(self, other: Union[Matrix, tuple]) -> Matrix:
        if isinstance(other, tuple):
            other = cast(Tuple[float, ...], other)
            other = Matrix(tuple((x,) for x in other))
        elif isinstance(other, Matrix):
            other = cast(Matrix, other)

        result = Matrix(
            tuple(
                tuple((self.cross(row, col) for col in other.cols))
                for row in self.matrix
            )
        )
        return result

    def __truediv__(self, value: Union[int, float]) -> Matrix:
        return Matrix(tuple(tuple(col / value for col in row) for row in self.matrix))
