import math
#MATH FUNCTIONS NECESSARY:
def gcd_list(integers):
    listToUse = [i for i in integers]
    if (len(listToUse) == 0):
        return 0
    if (len(listToUse) == 1):
        return listToUse[0]
    while (len(listToUse) > 2):
        listToUse.append(math.gcd(listToUse[0], listToUse[1]))
        listToUse.pop(0)
        listToUse.pop(0)
    return math.gcd(listToUse[0], listToUse[1])

def PrimeFactorization(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


#SEMIGROUP FUNCTIONS:
def SetAdd(L1, L2):
    L3 = []
    for a in L1:
        for b in L2:
            L3.append(a+b)
    L3 = list(set(L3))
    return L3

#CODE TAKEN FROM THE OLD SAGE PACKAGE
def FactorizationsInNN(gens, m):
    if len(gens) == 1:
        return [] if m % gens[0] != 0 else [[int(m/gens[0])]]

    facts = []
    lessgens = gens[:-1]
    for i in range(int(m/gens[-1])+1):
        facts = facts + [fact + [i] for fact in FactorizationsInNN(lessgens, m-(i*gens[-1]))]
    return facts

#CODE FOR THE ACTUAL PACKAGE
class NumericalSemigroup: 
    
    def __init__(self, generators = []):
        self.gens = generators
        if(type(self.gens) != list):
            raise Exception("The input generators must be in the form of a list")
        if(len(self.gens) == 0):
            raise Exception("There must be at least one generator")
        self.gens = sorted(list(self.gens))
        self.multiplicity = min(self.gens)
        self.elements = self.getElements(self.gens)
        self.gaps = [i*gcd_list(self.gens) for i in range(0, max(self.elements)) if ((i*gcd_list(self.gens) not in self.elements) and (i*gcd_list(self.gens) < max(self.elements)))]
        if (len(self.gaps) < 1):
            self.Frobenius = -1
        else:
            self.Frobenius = max(self.gaps)
        self.AperySetWithRespectToTheMultiplicity = self.AperySet(min(self.gens))
        self.__lengthsets = {0: [0]}
        self.__factorizations = {}
        p = [0]*len(self.gens)
        self.__factorizations[0] = []
        self.__factorizations[0].append(p)
        self.__structureTheoremLS = []
        self.LengthSetPeriodicityBound = "Not Initialized"
        self.__maxLengthB1s = []
        self.__minLengthC1s = []
        self.__structureTheoremInitialized = False
            
  
    def getElements(self, gens):
        currentCount = 0
        previousCount = 0
        newGennies = []
        List = [0]
        for t in range(0, len(gens)):
            isGen = True
            for y in range(0, len(gens)):
                if(gens[y] == gens[t]):
                    continue
                if(int(gens[t])%int(gens[y]) == 0):
                    isGen = False
                    break
            if(isGen):
                newGennies.append(int(gens[t]))
        if(gcd_list(newGennies) != 1):
            newGennies2 = [int(i/gcd_list(newGennies)) for i in newGennies]
            upTo = max(newGennies2)*min(newGennies2)
            listOfElements = [i for i in newGennies2]
            elementz = []
            weStillHaveTime = True
            while (weStillHaveTime):
                for a in listOfElements:
                    elementz.append(a)
                listOfElements = SetAdd(listOfElements, newGennies2)
                elementz = sorted(list(set(elementz)))
                if(upTo in elementz):
                    for r in elementz:
                        currentCount += 1
                        if(r >= upTo):
                            break
                    if(currentCount == previousCount):
                        weStillHaveTime = False
                    else:
                        previousCount = int(currentCount)
                        currentCount = 0
        else:
            upTo = max(newGennies)*min(newGennies)
            listOfElements = [i for i in newGennies]
            elementz = []
            weStillHaveTime = True
            while (weStillHaveTime):
                for a in listOfElements:
                    elementz.append(a)
                listOfElements = SetAdd(listOfElements, newGennies)
                elementz = sorted(list(set(elementz)))
                if(upTo in elementz):
                    for r in elementz:
                        currentCount += 1
                        if(r >= upTo):
                            break
                    if(currentCount == previousCount):
                        weStillHaveTime = False
                    else:
                        previousCount = int(currentCount)
                        currentCount = 0
        for i in elementz:
            if(i > upTo):
                break
            List.append(int(i*gcd_list(newGennies)))
        gaps = [j for j in range(0, max(List)) if j not in List]
        if(len(gaps) < 1):
            frob = -1
        else:
            frob = max(gaps)
        return [element for element in List if element <= frob + min(newGennies)]

    def AperySet(self, n = -1, j = 1):
        if((type(n) != int) or n < 0):
            raise Exception("The Apery Set must be called with respect to a non-negative integer")
        if (j < 1):
            raise Exception("The j-th Apery set starts with j = 1.")
        jthSet = []
        for i in range(0, n):
            jCount = 0
            current = 0
            if(math.gcd(n, gcd_list(self.gens)) != 1):
                if(math.gcd(n, i) != gcd_list(self.gens)):
                    if(0 not in jthSet):
                        jthSet.append(0)
                    continue
            while(jCount < j):
                if(((current in self.elements) or ((current > max(self.elements)) and (current%gcd_list(self.gens) == 0))) and (current % n == i)):
                    jCount += 1
                    if(jCount == j):
                        break
                current += 1
            jthSet.append(current)
        return jthSet
    
    def Contains(self, n):
        if (math.gcd(n, gcd_list(self.gens)) != gcd_list(self.gens)):
            return False
        if (gcd_list(self.gens) == 1):
            return (int(n) >= self.AperySetWithRespectToTheMultiplicity[int(n)%self.multiplicity])
        else:
            newGens = [int(i/gcd_list(self.gens)) for i in self.gens]
            temp = NumericalSemigroup(newGens)
            newN = int(n/gcd_list(self.gens))
            return temp.Contains(newN)

    def minimalGenerators(self):
        miniGens = [i for i in self.gens]
        i = 0
        end = len(miniGens)
        while(i < end):
            restart = False
            for j in range(i + 1, end):
                if((miniGens[j] - miniGens[i]) in self):
                    miniGens.pop(j)
                    end = len(miniGens)
                    i = 0
                    restart = True
                    break
            if(not restart):
                i += 1
        return miniGens
    
    def LengthSetsUpToElement(self, nmax):
        self.__lengthsets = {}
        self.__lengthsets[0] = [0]
        for n in range(0, nmax + 1):
            if n in self.__lengthsets:
                continue
            self.__lengthsets[n] = []
            for i in range(len(self.gens)):
                if n - self.gens[i] < 0:
                    continue
                self.__lengthsets[n] += [l + 1 for l in self.__lengthsets[n - self.gens[i]]]
            self.__lengthsets[n] = sorted(list(set(self.__lengthsets[n])))
    
    def LengthSet(self, n):
        if (n not in self):
            raise Exception("There is no length set for this integer as it is not in the semigroup.")
        if(self.__structureTheoremInitialized and n > self.LengthSetPeriodicityBound):
            return self.LSUsingSTLS(n)
        if (n > max(self.__lengthsets)):
            self.LengthSetsUpToElement(n)
        return self.__lengthsets[n]
    
    def FactorizationsUpToElement(self, nmax):
        for n in range(1, nmax+1):
            self.__factorizations[n] = set([])
            for i in range(len(self.gens)):
                if n - self.gens[i] < 0:
                    continue
                for a in self.__factorizations[n - self.gens[i]]:
                    s = list(a)
                    s[i] += 1
                    s = tuple(s)
                    if s not in self.__factorizations[n]:
                        self.__factorizations[n] = self.__factorizations[n].union(set([s]))
    
    def Factorizations(self, n):
        if (n not in self.__factorizations):
            return FactorizationsInNN(self.gens, n)
        return self.__factorizations[n]
        
    def structureTheoremLengthSet(self):
        if(len(self.__structureTheoremLS) == 0):
            M_i_dict = {}
            m_j_dict = {}
            for i in range(0, min(self.gens)):
                M_i_dict[i] = self.__M_i(i)
            for j in range(0, max(self.gens)):
                m_j_dict[j] = self.__m_i(j)
            self.__structureTheoremLS.append(M_i_dict)
            self.__structureTheoremLS.append(m_j_dict)
        return self.__structureTheoremLS
    
    def __M_i(self, i):
        Mi = []
        S_M = self.S_M()
        Ap = S_M.AperySet(self.multiplicity)
        j = 1
        while((Ap[i] + j*self.multiplicity) <= S_M.Frobenius):
            current = Ap[i] + j*self.multiplicity
            if current not in S_M:
                Mi.append(j)
            j += 1
        return Mi
    
    def __m_i(self, i):
        mi = []
        S_m = self.S_m()
        Ap = S_m.AperySet(max(self.gens))
        j = 1
        while((Ap[i] + j*max(self.gens)) <= S_m.Frobenius):
            current = Ap[i] + j*max(self.gens)
            if current not in S_m:
                mi.append(j)
            j += 1
        return mi
    
    def LSUsingSTLS(self, n):
        structure = self.structureTheoremLengthSet()
        maxLen = int((n - self.__maxLengthB1s[n%min(self.gens)])/min(self.gens))
        minLen = int((n + self.__minLengthC1s[-n%max(self.gens)])/max(self.gens))
        possibleLengths = {}
        for i in range(minLen, maxLen + 1):
            possibleLengths[i] = True
        for a in structure[0][n%min(self.gens)]:
            possibleLengths[maxLen - a] = False
        for b in structure[1][n%max(self.gens)]:
            possibleLengths[minLen + b] = False
        return [i for i in range(minLen, maxLen + 1) if possibleLengths[i]]
    
    def structureTheoremInitialization(self):
        try:
            self.__startOfLSPeriodicity()
            self.__maxLengthB1s = self.__maxFactLen()
            self.__minLengthC1s = self.__minFactLen()
            self.structureTheoremLengthSet()
            self.__structureTheoremInitialized = True
            print("Done")
        except:
            print("Something went wrong with the initialization")
    
    def __startOfLSPeriodicity(self):
        if(self.LengthSetPeriodicityBound != "Not Initialized"):
            return self.LengthSetPeriodicityBound
        S_M = self.S_M()
        S_m = self.S_m()
        g = 0
        gPrime = 0
        gSmall = True
        gPrimeSmall = True
        bothDone = False
        while(not bothDone):
            j = 1
            while(gSmall):
                al = True
                for i in S_M.AperySet(min(self.gens), j):
                    if(i < S_M.Frobenius):
                        al = False
                if(al):
                    g = int(j)
                    gSmall = False
                else:
                    j += 1
            j = 1
            while(gPrimeSmall):
                al = True
                for i in S_m.AperySet(max(self.gens), j):
                    if(i < S_m.Frobenius):
                        al = False
                if(al):
                    gPrime = int(j)
                    gPrimeSmall = False
                else:
                    j += 1
            if(not gSmall and not gPrimeSmall):
                bothDone = True
        currentMax = 0
        for t in range(1, g+1):
            tempMax = max(self.MApSet(t))
            if(tempMax > currentMax):
                currentMax = int(tempMax)
            else:
                continue
        for r in range(1, gPrime+1):
            temp2Max = max(self.mApSet(r))
            if(temp2Max > currentMax):
                currentMax = int(temp2Max)
            else:
                continue
        self.LengthSetPeriodicityBound = int(currentMax)
        
    #TODO: ADD FUNCTIONALITY FOR DELTA SET
    def deltaSet(self):
        totalDeltaSet = []
        if(self.LengthSetPeriodicityBound == "Not Initialized"):
            self.__startOfLSPeriodicity()
        self.LengthSetsUpToElement(self.LengthSetPeriodicityBound + 1)
        for n in self.__lengthsets:
            if(n > self.LengthSetPeriodicityBound):
                break
            if (len(self.__lengthsets[n]) < 2):
                continue
            else: 
                for i in range(0, len(self.__lengthsets[n]) - 1):
                    totalDeltaSet.append(self.__lengthsets[n][i + 1] - self.__lengthsets[n][i])
        return sorted(list(set(totalDeltaSet)))
    
    #TODO: ADD PERODICITY OF MAX AND MIN LENGTH START
    def MApSet(self, j = 1):
        if(j < 1 or type(j) != int):
            raise Exception("There is no MAp set for j < 1")
        G_M = self.S_M()
        ApSet = G_M.AperySet(min(self.gens), j)
        return [i + min(self.gens)*min(G_M.LengthSet(i)) for i in ApSet]
    
    def mApSet(self, j = 1):
        if(j < 1 or type(j) != int):
            raise Exception("There is no mAp set for j < 1")
        G_M = self.S_m()
        ApSet = G_M.AperySet(max(self.gens), j)
        return [i + max(self.gens)*min(G_M.LengthSet(i)) for i in ApSet]
    
    def S_M(self):
        if (len(self.gens) < 2):
            raise Exception("There is no S_M for a semigroup with only one generator")
        S_M_gens = [self.gens[i]-self.gens[0] for i in range(1, len(self.gens))]
        return NumericalSemigroup(S_M_gens)
    
    def S_m(self):
        if (len(self.gens) < 2):
            raise Exception("There is no S_m for a semigroup with only one generator")
        S_m_gens = [self.gens[len(self.gens) - 1]-self.gens[i] for i in range(0, len(self.gens) - 1)]
        return NumericalSemigroup(S_m_gens)
    
    def __maxFactLen(self):
        S_M = self.S_M()
        return S_M.AperySet(min(self.gens))
    
    def __minFactLen(self):
        S_m = self.S_m()
        return S_m.AperySet(max(self.gens))
    
    def isHarmonic(self):
        return (self.AperySetWithRespectToTheMultiplicity == self.MApSet())
    
    ### REDEFINING PROPERTIES ###
    def __eq__(self, other):
        return ((self.gaps == other.gaps) and (gcd_list(self.gens) == gcd_list(other.gens)))
    
    def __contains__(self, other):
        return self.Contains(other)
    
    def __repr__(self):
        return "Numerical semigroup generated by " + str(self.gens)
