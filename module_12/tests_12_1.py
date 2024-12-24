import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = Runner('Stepan')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        walker = Runner('Stepan')
        for i in range(10):
            walker.run()
        self.assertEqual(walker.distance, 100)

    def test_challenge(self):
        walker_1 = Runner('Stepan')
        walker_2 = Runner('Oleg')
        for i in range(10):
            walker_1.walk()
        for i in range(10):
            walker_2.run()
        self.assertNotEqual(walker_1.distance, walker_2.distance)


