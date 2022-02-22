import unittest
import script


class TestCap(unittest.TestCase):
    def test_one(self):
        text = 'python'
        result = script.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_two(self):
        text = 'python java kotlin'
        result = script.cap_text(text)
        self.assertEqual(result, 'Python Java Kotlin')


if __name__ == '__main__':
    unittest.main()
