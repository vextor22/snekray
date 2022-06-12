from __future__ import annotations
from typing import Tuple, cast, Union
import math


class Matrix:
    def __init__(self, data: Tuple[Tuple[float]]) -> None:
        self.matrix: Tuple[Tuple[float]] = data
        self.col_count = len(self.matrix[0])

    @classmethod
    def identity_matrix(cls, dim: int = 4) -> Matrix:
        return Matrix(
            tuple(tuple((1 if i == j else 0) for j in range(dim)) for i in range(dim))
        )

    def get(self, row, column) -> float:
        return self.matrix[row][column]

    def get_row(self, row) -> Tuple[float]:
        return self.matrix[row]

    def get_column(self, col) -> Tuple[float]:
        return cast(Tuple[float], tuple(row[col] for row in self.matrix))

    @property
    def cols(self):
        for i in range(self.col_count):
            yield self.get_column(i)

    def transpose(self):
        return Matrix(tuple(self.cols))

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Matrix):
            return NotImplemented
        __o = cast(Matrix, __o)
        is_equal = True
        for i, row in enumerate(self.matrix):
            is_equal = is_equal and all(
                (math.isclose(element, __o.get(i, j)) for j, element in enumerate(row))
            )

        return is_equal

    def cross(self, row, col) -> float:
        return sum(x[0] * x[1] for x in zip(row, col))

    def __mul__(self, other: Union[Matrix, tuple]):
        if isinstance(other, tuple):
            other = Matrix(tuple((x,) for x in other))
        if isinstance(other, Matrix):
            other = cast(Matrix, other)

            return Matrix(
                tuple(
                    cast(
                        Tuple[float],
                        tuple((self.cross(row, col) for col in other.cols)),
                    )
                    for row in self.matrix
                )
            )
