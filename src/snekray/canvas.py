from typing import List, Tuple
import snekray
import math


class Canvas:
    def __init__(
        self, width: int, height: int, fill: snekray.Color = None, max_value=255
    ) -> None:
        self.width = width
        self.height = height
        self.max_value = max_value
        self.max_row_length = 70

        self.fill = fill if fill else snekray.Color(0, 0, 0)

        self.pixels: List[snekray.Color] = [self.fill for _ in range(width * height)]

    def write_pixel(self, x: int, y: int, color: snekray.Color) -> None:
        if x < 0:
            x = 0
        elif x >= self.width:
            x = self.width - 1
        if y < 0:
            y = 0
        elif y >= self.height:
            y = self.height - 1
        self.pixels[x + (y * self.width)] = color

    def get_pixel(self, x, y) -> snekray.Color:
        return self.pixels[x + (y * self.width)]

    def format_pixel(self, pixel: snekray.Color) -> str:
        attr_names = ["red", "green", "blue"]
        values = []
        for attr in attr_names:
            pixel_attr = getattr(pixel, attr)
            pixel_value = pixel_attr * self.max_value
            if pixel_value > self.max_value:
                pixel_value = self.max_value
            elif pixel_value < 0:
                pixel_value = 0
            values.append(pixel_value)
        return " ".join(str(math.ceil(v)) for v in values)

    def format_row(self, row: List[snekray.Color]) -> str:
        return " ".join(self.format_pixel(p) for p in row)

    def split_row(self, row) -> Tuple[str, str]:
        offsets = [0, 1, 2, 3]
        row_return = ""
        carry = ""

        for offset in offsets:
            if row[self.max_row_length - offset] == " ":
                row_return = row[: self.max_row_length - offset]
                carry = row[self.max_row_length - offset + 1 :]
        return row_return.strip(), carry.strip()

    def to_ppm(self, color_maximum=255) -> str:
        header = ["P3", f"{self.width} {self.height}", f"{color_maximum}"]
        rows = []
        carry = None
        for i in range(self.height):
            row_start = i * self.width
            row_end = row_start + self.width

            pix_row = self.pixels[row_start:row_end]
            row = self.format_row(pix_row)
            if len(row) > 70:
                row, carry = self.split_row(row)
            rows.append(row)
            if carry:
                rows.append(carry)
                carry = None

        return "\n".join([*header, *rows, "\n"])
