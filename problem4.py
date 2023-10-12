import unittest
import contextlib
import io
from printing import print_range, print_reversed

class Test_print(unittest.TestCase):

    def test_print_range(self):
        with contextlib.redirect_stdout(io.StringIO()) as f:
            print_range(1, 5, 1)

        self.assertEqual(f.getvalue(), "1\n2\n3\n4\n")

        with contextlib.redirect_stdout(io.StringIO()) as g:
            print_range(2, 10, 2)

        self.assertEqual(g.getvalue(), "2\n4\n6\n8\n")

    def test_print_reversed(self):
        with contextlib.redirect_stdout(io.StringIO()) as f:
            print_reversed("ICS33-Oscar")

        self.assertEqual(f.getvalue(), "I\nC\nS\n3\n3\n-\nO\ns\nc\na\nr\n")

        with contextlib.redirect_stdout(io.StringIO()) as g:
            print_reversed("WRITING60")

        self.assertEqual(g.getvalue(), "W\nR\nI\nT\nI\nN\nG\n6\n0\n")




