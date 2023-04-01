"""Code rom https://www.pythonguis.com/tutorials/python-classes/"""


class Color:
    representation = "RGB"

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def as_tuple(self):
        return self.red, self.green, self.blue

    @classmethod
    def from_tuple(cls, rgb):
        return cls(*rgb)

    @staticmethod
    def color_says(message):
        print(message)


if __name__ == '__main__':
    color_red = Color(255, 0, 0)
    print(color_red.as_tuple())
    print(f"type of as_tuple(): {type(color_red.as_tuple())}")

    for level in color_red.as_tuple():
        print(level)

    color_blue = Color.from_tuple((0, 0, 255))
    print(color_blue.as_tuple())

    color_red.color_says("Hello from the Color class.")
