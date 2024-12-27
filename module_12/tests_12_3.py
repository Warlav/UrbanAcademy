import unittest
from runner import Runner
import runner_and_tournament


class RunnerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.is_frozen = False

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


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        cls.is_frozen = True

    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner_2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner_3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        {print(f'\n{i}:'): [print(f'{k}: ', v) for k, v in j.items()] for i, j in cls.all_results.items()}

    def test_zabeg_1(self):
        run = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3).start()
        TournamentTest.all_results['test_zabeg_1'] = run
        keys = list(run.keys())
        self.assertTrue(run[keys[-1]].name == self.runner_3.name)

    def test_zabeg_2(self):
        run = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3).start()
        TournamentTest.all_results['test_zabeg_2'] = run
        keys = list(run.keys())
        self.assertTrue(run[keys[-1]].name == self.runner_3.name)

    def test_zabeg_3(self):
        run = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3).start()
        TournamentTest.all_results['test_zabeg_3'] = run
        keys = list(run.keys())
        self.assertTrue(run[keys[-1]].name == self.runner_3.name)

    def test_zabeg_fail(self):
        run = runner_and_tournament.Tournament(6, self.runner_1, self.runner_2, self.runner_3).start()
        TournamentTest.all_results['test_zabeg_fail'] = run
        keys = list(run.keys())
        self.assertTrue(run[keys[-1]].name == self.runner_3.name)
