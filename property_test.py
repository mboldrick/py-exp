"""Test use of @property decorator"""


class Ninja:
    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_value: int):
        if new_value < 0:
            raise ValueError("Score cannot be negative.")
        self._score = new_value


def set_and_print_score(value):
    n.score = value
    print(f"score = {n.score}")


if __name__ == '__main__':
    n = Ninja()

    # n.score = 1
    # print(f"score = {n.score}")
    #
    # n.score = -5
    # print(f"score = {n.score}")

    set_and_print_score(5)
    set_and_print_score(-5)
    