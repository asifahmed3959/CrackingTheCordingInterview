import unittest


#bit vector algorithm has to be learned

def clean_space(s):
    new_str = ""

    for char in s:
        if char == " ":
            pass

        elif char.isalpha():
            new_str += char.lower()

    return new_str


def is_palindrome_permutation(s):
    d = {}

    s = clean_space(s)

    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] =1

    odd = 0

    for value in d.values():
        if value % 2 == 1:
            odd += 1

            if odd > 1:
                return False

    print(s)

    return True

def is_palindrome_permutation_char(s):
    l = ord("z") - ord("a") + 1
    char_arr = [0] * l # considering only ascii values


    s = clean_space(s)

    for char in s:
        print(s)
        char_arr[ord("a")- ord(char)] += 1

    odd = 0

    for value in char_arr:
        if value % 2 == 1:
            odd += 1

            if odd > 1:
                return False
    return True


class Test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    testable_functions = [
        is_palindrome_permutation,
        is_palindrome_permutation_char
        # is_palindrome_bit_vector,
        # is_palindrome_permutation_pythonic,
        # is_palindrome_bit_vector2,
    ]

    def test_pal_perm(self):
        for f in self.testable_functions:
            for [test_string, expected] in self.test_cases:
                assert f(test_string) == expected


if __name__ == "__main__":
    unittest.main()