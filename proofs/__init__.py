import doctest
import unittest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocFileSuite("test_core.md"))
    tests.addTests(doctest.DocFileSuite("test_base.md"))
    tests.addTests(doctest.DocFileSuite("test_read.md"))
    return tests

if __name__ == "__main__":
    unittest.main()

