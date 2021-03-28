import math
from fullSemigroupPackage import*
import unittest

class testingNumericalSemigroups(unittest.TestCase):
    def setUp(self):
        self.S = NumericalSemigroup([6, 9, 20])
        self.T = NumericalSemigroup([6, 9, 12, 20])
        self.U = NumericalSemigroup([5, 9, 12])
        self.V = NumericalSemigroup([1])
        self.W = NumericalSemigroup([5])
        self.X = NumericalSemigroup([8, 12])
        self.Y = NumericalSemigroup([9, 12, 15])
        self.Z = NumericalSemigroup([9, 12])
        
    def test_Equality(self):
        #TESTING EQUALITY
        assert self.S == self.T, "Failed Equality 1"
        assert self.S != self.U, "Failed Equality 2"
        assert self.V != self.W, "Failed Equality 3"
        assert self.V != NumericalSemigroup([2, 3]), "Failed Equality 4"
        assert self.W != NumericalSemigroup([3, 4, 5]), "Failed Equality 5"

    def test_Cointainment(self):
        assert 6 in self.S, "Failed Containment 1"
        assert 12 in self.S, "Failed Containment 2"
        assert 15 in self.T, "Failed Containment 3"
        assert 0 in self.T, "Failed Containment 4"
        assert 0 in self.V, "Failed Containment 5"
        assert 0 in self.W, "Failed Containment 6"
        assert 5 not in self.S, "Failed Containment 7"
        assert 43 not in self.S, "Failed Containment 8"
        assert 6 not in self.U, "Failed Containment 9"
        assert 1 not in self.U, "Failed Containment 10"
        assert 4 in self.V, "Failed Containment 11"
        assert -1 not in self.V, "Failed Containment 12"
        assert 4 not in self.W, "Failed Containment 13"
        assert 15 in self.W, "Failed Containment 14"
        assert 1000 not in self.Y, "Failed Containment 15"
        assert 15 not in self.Z, "Failed Containment 16"
        assert 4 not in self.X, "Failed Containment 17"
        assert 8 not in self.Y, "Failed Containment 18"
        assert 6 not in self.Y, "Failed Containment 19"
        assert 101 not in self.X, "Failed Containment 20"


    def test_AperySet(self):
        assert self.S.AperySetWithRespectToTheMultiplicity == [0, 49, 20, 9, 40, 29], "Failed base Apery 1"
        assert self.T.AperySetWithRespectToTheMultiplicity == [0, 49, 20, 9, 40, 29], "Failed base Apery 2"
        assert self.U.AperySetWithRespectToTheMultiplicity == [0, 21, 12, 18, 9], "Failed base Apery 3"
        assert self.V.AperySetWithRespectToTheMultiplicity == [0], "Failed base Apery 4"
        assert self.W.AperySetWithRespectToTheMultiplicity == [0], "Failed base Apery 5"
        assert self.X.AperySetWithRespectToTheMultiplicity == [0, 12], "Failed base Apery 6"
        assert self.Y.AperySetWithRespectToTheMultiplicity == [0, 12, 15], "Failed base Apery 7"

    def test_jthApertSet(self):
        assert self.S.AperySet(6, 2) == [i + 6 for i in self.S.AperySet(6)], "Failed jthApery set 1"
        assert self.T.AperySet(6, 4) == [i + 18 for i in self.T.AperySet(6)], "Failed jthApery set 2"

    def test_ExtendedAperySet(self):
        assert self.U.AperySet(3) == [0, 10, 5], "Failed extended Apery set 1"
        assert self.V.AperySet(3) == [0, 1, 2], "Failed extended Apery set 2"

    def test_LengthDensity(self):
        a1 = self.S.LengthDensity(500)
        a2 = self.S.LengthDensity(1032)
        a3 = self.S.LengthDensity(432)
        a4 = self.S.LengthDensity(893)
        a5 = self.S.LengthDensity(171)
        b1 = self.U.LengthDensity(500)
        b2 = self.U.LengthDensity(1032)
        b3 = self.U.LengthDensity(432)
        b4 = self.U.LengthDensity(893)
        b5 = self.U.LengthDensity(171)
        self.S.structureTheoremInitialization()
        self.U.structureTheoremInitialization()
        assert self.S.LengthDensity(500) == a1, "Failed Length Density Check"
        assert self.S.LengthDensity(1032) == a2, "Failed Length Density Check"
        assert self.S.LengthDensity(432) == a3, "Failed Length Density Check"
        assert self.S.LengthDensity(893) == a4, "Failed Length Density Check"
        assert self.S.LengthDensity(171) == a5, "Failed Length Density Check"
        assert self.U.LengthDensity(500) == b1, "Failed Length Density Check"
        assert self.U.LengthDensity(1032) == b2, "Failed Length Density Check"
        assert self.U.LengthDensity(432) == b3, "Failed Length Density Check"
        assert self.U.LengthDensity(893) == b4, "Failed Length Density Check"
        assert self.U.LengthDensity(171) == b5, "Failed Length Density Check"

    def tearDown(self):
        pass
        
        
if __name__ == '__main__':
    unittest.main()