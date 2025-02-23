import unittest
import time
from collections import OrderedDict


def compress_string(s1):
    new_s = ""
    d = OrderedDict()

    for char in s1:
        if char in d:
            d[char] +=1
        else:
            d[char] = 1

    for key in d.keys():
        new_s += key + str(d[key])

    print(new_s)
    return new_s


def compress_string_using_ord(s1):
    arr = [0] * (ord("z") - ord("a") + 1)


    for char in s1:
        arr[ord(char)] += 1

    new_s = ""
    for i in range(len(arr)):
        if arr[i] > 0:
            new_s += chr(i + ord("a")) + str(arr[i])

    return new_s



class Test(unittest.TestCase):
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]
    testable_functions = [
        compress_string,
        compress_string_using_ord
    ]

    def test_string_compression(self):
        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(1000):
                for test_string, expected in self.test_cases:
                    assert f(test_string) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()