import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = Runner('Stepan')
        [walker.walk() for i in range(10)]
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        walker = Runner('Stepan')
        [walker.run() for i in range(10)]
        self.assertEqual(walker.distance, 100)

    def test_challenge(self):
        walker_1 = Runner('Stepan')
        walker_2 = Runner('Oleg')
        [walker_1.walk() for i in range(10)]
        [walker_2.run() for i in range(10)]
        self.assertNotEqual(walker_1.distance, walker_2.distance)


if __name__ == '__main__':
    unittest.main()
