import math
from numericalSemigroup import*

def unitTesting():
    S = NumericalSemigroup([6, 9, 20])
    T = NumericalSemigroup([6, 9, 12, 20])
    U = NumericalSemigroup([5, 9, 12])
    V = NumericalSemigroup([1])
    W = NumericalSemigroup([5])
    X = NumericalSemigroup([8, 12])
    Y = NumericalSemigroup([9, 12, 15])
    Z = NumericalSemigroup([9, 12])
    #TESTING EQUALITY
    assert S == T, "Failed Equality 1"
    assert S != U, "Failed Equality 2"
    assert V != W, "Failed Equality 3"
    assert V != NumericalSemigroup([2, 3]), "Failed Equality 4"
    assert W != NumericalSemigroup([3, 4, 5]), "Failed Equality 5"
    
    #TESTING CONTAINMENT
    assert 6 in S, "Failed Containment 1"
    assert 12 in S, "Failed Containment 2"
    assert 15 in T, "Failed Containment 3"
    assert 0 in T, "Failed Containment 4"
    assert 0 in V, "Failed Containment 5"
    assert 0 in W, "Failed Containment 6"
    assert 5 not in S, "Failed Containment 7"
    assert 43 not in S, "Failed Containment 8"
    assert 6 not in U, "Failed Containment 9"
    assert 1 not in U, "Failed Containment 10"
    assert 4 in V, "Failed Containment 11"
    assert -1 not in V, "Failed Containment 12"
    assert 4 not in W, "Failed Containment 13"
    assert 15 in W, "Failed Containment 14"
    assert 1000 not in Y, "Failed Containment 15"
    assert 15 not in Z, "Failed Containment 16"
    assert 4 not in X, "Failed Containment 17"
    assert 8 not in Y, "Failed Containment 18"
    assert 6 not in Y, "Failed Containment 19"
    assert 101 not in X, "Failed Containment 20"
    
    
    #Apery set with respect to multiplicity Tests
    assert S.AperySetWithRespectToTheMultiplicity == [0, 49, 20, 9, 40, 29], "Failed base Apery 1"
    assert T.AperySetWithRespectToTheMultiplicity == [0, 49, 20, 9, 40, 29], "Failed base Apery 2"
    assert U.AperySetWithRespectToTheMultiplicity == [0, 21, 12, 18, 9], "Failed base Apery 3"
    assert V.AperySetWithRespectToTheMultiplicity == [0], "Failed base Apery 4"
    assert W.AperySetWithRespectToTheMultiplicity == [0], "Failed base Apery 5"
    assert X.AperySetWithRespectToTheMultiplicity == [0, 12], "Failed base Apery 6"
    assert Y.AperySetWithRespectToTheMultiplicity == [0, 12, 15], "Failed base Apery 7"
    
    #jth-Apery set Tests
    assert S.AperySet(6, 2) == [i + 6 for i in S.AperySet(6)], "Failed jthApery set 1"
    assert T.AperySet(6, 4) == [i + 18 for i in T.AperySet(6)], "Failed jthApery set 2"
    
    #Extended Apery set Tests
    assert U.AperySet(3) == [0, 10, 5], "Failed extended Apery set 1"
    assert V.AperySet(3) == [0, 1, 2], "Failed extended Apery set 2"
    
    #Testing length density
    a1 = S.LengthDensity(500)
    a2 = S.LengthDensity(1032)
    a3 = S.LengthDensity(432)
    a4 = S.LengthDensity(893)
    a5 = S.LengthDensity(171)
    b1 = U.LengthDensity(500)
    b2 = U.LengthDensity(1032)
    b3 = U.LengthDensity(432)
    b4 = U.LengthDensity(893)
    b5 = U.LengthDensity(171)
    S.structureTheoremInitialization()
    U.structureTheoremInitialization()
    assert S.LengthDensity(500) == a1, "Failed Length Density Check"
    assert S.LengthDensity(1032) == a2, "Failed Length Density Check"
    assert S.LengthDensity(432) == a3, "Failed Length Density Check"
    assert S.LengthDensity(893) == a4, "Failed Length Density Check"
    assert S.LengthDensity(171) == a5, "Failed Length Density Check"
    assert U.LengthDensity(500) == b1, "Failed Length Density Check"
    assert U.LengthDensity(1032) == b2, "Failed Length Density Check"
    assert U.LengthDensity(432) == b3, "Failed Length Density Check"
    assert U.LengthDensity(893) == b4, "Failed Length Density Check"
    assert U.LengthDensity(171) == b5, "Failed Length Density Check"
    
def runTests():
    try: 
        unitTesting()
    except:
        raise Exception("Failed certain tests")
    print("Success on all tests")
