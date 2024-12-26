import unittest
import runner_and_tournament
from pprint import pprint


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

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


if __name__ == '__main__':
    unittest.main()
