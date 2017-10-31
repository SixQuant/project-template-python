import unittest

import project_template_python


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(project_template_python.smile(), ":)")


if __name__ == '__main__':
    unittest.main()
