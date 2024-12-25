import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner_2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner_3 = runner_and_tournament.Runner('Ник', 3)

    def tearDownClass(self):
        return [print(i) for i in TournamentTest.all_results]

    def zabeg_1(self):
        run = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3).start()
        TournamentTest.all_results.update(run)
        self.assertTrue(self.all_results[-1].value == self.runner_3.name)

    def zabeg_2(self):
        run = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3).start()
        TournamentTest.all_results.update(run)
        self.assertTrue(self.all_results[-1].value == self.runner_3.name)

    def zabeg_3(self):
        run = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3).start()
        TournamentTest.all_results.update(run)
        self.all_results = sorted(self.all_results)
        self.assertTrue(self.all_results[-1].value == self.runner_3.name)


if __name__ == '__main__':
    unittest.main()
