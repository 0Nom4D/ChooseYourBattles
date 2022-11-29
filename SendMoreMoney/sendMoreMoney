#!/usr/bin/env python3

from typing import List
from itertools import permutations
from sys import argv


class Solver:
    def __init__(self, equationToSolve: str) -> None:
        self._equation = equationToSolve
        self._wordList = []
        self._letterList = []

    @property
    def equation(self) -> str:
        return self._equation

    @property
    def wordList(self):
        return self._wordList

    @property
    def letterList(self):
        return self._letterList

    def getLettersFromEquation(self) -> bool:
        self._wordList = self._equation.split()

        for word in self._wordList:
            if not word.isalpha():
                self._wordList.remove(word)
        self._letterList = list(set(''.join(self._wordList)))
        if len(self._letterList) > 10:
            return False
        return True

    def transformValue(self, values: List[int]) -> int:
        """
        Computes the list of integer for each value of a word, into an integer, using power of ten.

        :param values: List of value for each word
        :return: Computed value for the word
        """
        tenPowersList = [10 ** i for i in range(len(values) - 1, -1, -1)]
        value = 0

        for i in range(len(values)):
            value += values[i] * tenPowersList[i]
        return value

    def findCorrectWordValues(self) -> int:
        it = 0
        resultBiggerLength = False

        def getAllPossibleAssociation():
            return list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(self._letterList)))

        associationList = getAllPossibleAssociation()
        if len(self._wordList[2]) > len(self._wordList[0]) and len(self._wordList[2]) > len(self._wordList[0]):
            resultBiggerLength = True

        for association in associationList:

            ## Checks if the result is bigger than the both operands. If true, we're checking
            ## if the element in the 'x' position of the permutation is not 1, we continue. Because that
            ## permutation will not be the right one.
            if resultBiggerLength and association[self._letterList.index(self._wordList[2][0])] != 1:
                continue

            ## Creates all values for each letter of each word. When created, we loop over those
            ## elements, and we're getting the indices of all letters in our main list and
            ## we're getting its value in the permutation.
            elementValues = [[0] * len(self._wordList[i]) for i in range(len(self._wordList))]
            for it in range(len(self._letterList)):
                for idx, wordValues in enumerate(elementValues):
                    letterIndices = [_k for _k, _j in enumerate(self._wordList[idx]) if _j == self._letterList[it]]
                    for index in letterIndices:
                        wordValues[index] = association[it]

            ## When done, we're computing the value for each word. Then, we're checking if the 2 firsts
            ## are equal to the last one. Then, we're creating the equation with the transformed words.
            resultList = [self.transformValue(values) for values in elementValues]
            if sum(resultList[:-1]) == resultList[-1]:
                result = ''
                for idx, value in enumerate(resultList[:-1]):
                    result += f'{value}{" + " if idx != len(resultList[:-1]) - 1 else " = "}'
                result += f"{resultList[-1]}"
                print(result)
        return 0

    def run(self) -> int:
        if not self.getLettersFromEquation():
            return 1
        return self.findCorrectWordValues()


def main() -> int:
    if len(argv) != 2:
        return 1
    equationSolver = Solver(argv[1])
    return equationSolver.run()


if __name__ == "__main__":
    exit(main())
