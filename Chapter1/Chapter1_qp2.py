import unittest
from collections import Counter

def check_permutation_by_sort(s1, s2):
    s1 = list(s1)
    s2 = list(s2)

    s1.sort()
    s2.sort()

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

def check_permutation_by_count(s1, s2):
    if len(s1) != len(s2):
        return False

    counter = [0] * 256

    for c in s1:
        counter[ord(c)] += 1

    for c in s2:
        if counter[ord(c)] == 0:
            return False
        counter[ord(c)] -= 1


    return True



def check_permutation_pythonic(s1, s2):
    if len(s1) != len(s2):
        return False

    d1 = Counter(s1)
    d2 = Counter(s2)

    return d1 == d2






class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions = [
        check_permutation_by_sort,
        check_permutation_by_count,
        check_permutation_pythonic,
    ]

    def test_cp(self):
        i = 0
        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                print(i)
                assert check_permutation(str1, str2) == expected
                i += 1


if __name__ == "__main__":
    unittest.main()