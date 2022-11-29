from sources.main import Solver


class TestSolver:
    def test_solverCreation(self):
        solver = Solver('SEND + MORE = MONEY')
        assert solver.equation == 'SEND + MORE = MONEY'
        assert solver.wordList == []
        assert solver.letterList == []

    def test_getLettersFromEq(self):
        solver = Solver('SEND + MORE = MONEY')
        assert solver.getLettersFromEquation() == True
        assert solver.equation == 'SEND + MORE = MONEY'
        assert solver.wordList == ['SEND', 'MORE', 'MONEY']
        assert set(solver.letterList) == set(['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y'])

    def test_findCorrectEquation(self, capsys):
        solver = Solver('SEND + MORE = MONEY')
        assert solver.run() == 0
        stdout = capsys.readouterr()[0]
        assert stdout == "9567 + 1085 = 10652\n"

    def test_runWithTooMuchLetters(self):
        solver = Solver('ALED + PEUR = SIGNAL')
        assert solver.run() == 1

    def test_getTooManyLetters(self):
        solver = Solver('ALED + PEUR = SIGNAL')
        assert solver.getLettersFromEquation() == False

    def test_valueTransform(self):
        _ = Solver('SEND + MORE = MONEY')
        assert _.transformValue([9, 0, 5, 4]) == 9054
