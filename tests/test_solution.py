from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        a = solution('./files/testfile.txt', 'Hello')
        fh = open('./files/testfile.txt').read()
        text = fh.split('\n')
        res = text[-1]
        res2 = text[0]

        self.assertEqual(res, 'Hello')
        self.assertEqual(res2, 'Python')
