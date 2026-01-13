# change in fix-branch

import os
from question_3 import write_random_numbers

def test_number_of_lines():
    filename = "test_numbers.txt"
    write_random_numbers(5, filename)

    with open(filename, "r") as f:
        lines = f.readlines()

    assert len(lines) == 5
    os.remove(filename)


def test_numbers_in_range():
    filename = "test_numbers.txt"
    write_random_numbers(10, filename)

    with open(filename, "r") as f:
        for line in f:
            num = int(line.strip())
            assert 1 <= num <= 500

    os.remove(filename)
