import unittest
import tests_12_1
import tests_12_2

suite_test = unittest.TestSuite()
suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)


class MyRunnerTest(tests_12_1.RunnerTest):
    @classmethod
    def setUpClass(cls):
        cls.is_frozen = False


class MyTournamentTest(tests_12_2.TournamentTest):
    @classmethod
    def setUpClass(cls):
        cls.is_frozen = True

def skip_test(func):
    def wrapper():
        pass

# print(suite_test.countTestCases())
