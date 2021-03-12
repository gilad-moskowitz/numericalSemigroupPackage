# numericalSemigroupPackage

The code in numericalSemigroupPackage.py creates a Python `NumericalSemigroup` class for working with Numerical Semigroups in pure Python. My hope is that those who want to work on Numerical Semigroups without using SageMath can utilize this package. 

## Important Notes
The class `NumericalSemigroup` takes in one argument, which is the generators in the form of a list of integers. Note that the numerical semigroup generatored will have properties based on the passed list of generators. What I mean by this is that if we create two numerical semigroups, `S = NumericalSemigroup([6, 9, 20])` and `T = NumericalSemigroup([6, 9, 12, 20])`, then we see that these are the same semigroup, as they have all the same elements. However, the way we have chosen to represent them is different, and therefore their factorizations and length sets would also be different. That is to say, a factorization of an element in `S` is a 3-tuple while a factorization of an element in `T` is a 4-tuple. In this way the class treats the two semigroups differently. However, if one was to check `S == T`, then they would get `True`. If you are unsure whether the generators can be written in a more minimal way, you can call the function `minimalGenerators()`. For instance, if we called `T.minimalGenerators()` we would get `[6, 9, 20]`.

Another thing to note, the class `NumericalSemigroup` is not required to be cofinite. That is, we can generator the numerical semigroup `R = NumericalSemigroup([5])` which is clearly just the multiples of 5. When looking at a semigroup that is not cofinite, the properties, such as `gaps` and `Frobenius` are examined with respect to the gcd of the semigroup. For instance, `R.gaps = []` and `R.Frobenius = -1` (this is by convention). This is because, with respect to 5, the gcd of `R`, we have every element in the natural numbers. Understandably, most people only look at cofinite Numerical Semigroups, but I add this functionality for my own benefit and hopefully some other people might get some use of it. 

I am aware that for large numerical semigroups the initialization of the class takes a while. This is becasue as part of the initialization, I find the Apery set with respect to the multiplicity, the gaps of the semgroup, and the Frobenius number. Below I describe several of the attributes and functions that can be called.

Lastly, this package is relatively new and will hopefully be updated with more and more funtionalities. This also means that there is the possibility of errors, so please let me know if you find any. 

## Functions and Attributes
For the description of the functions and attributes we will use an example numerical semigroup. 

Suppose we called `S = NumericalSemigroup([6, 9, 20])`. Once the class has finished it's initialization we will be able to immediately call:
* `S.gens` which provides the list of generators of the numerical semigroup, i.e. `[6, 9, 20]`.
* `S.multiplicity` which provides the multiplicity (smallest generator) of the numerical semigroup, i.e. `6`
* `S.elements` which provides a list of all the elements up to the conductor (first element after the Frobenius number) of the numerical semigroup
* `S.Frobenius` which provides the Frobenius number (largest gap), i.e. `43`
* `S.gaps` which provides a list of the gaps of the numerical semigroup
* `S.AperySetWithRespectToTheMultiplicity` which provides the Apery set of the numerical semigroup with respect to the smallest generator, i.e. `[0, 49, 20, 9, 40, 29]`

The following is a selection of the functions that can be used to examine properties of the numerical semigroup:
* `S.AperySet(n, j)` will give the j-th Apery set of the numerical semigroup with respect to the integer n. For those who don't know what that is, you can refer to my thesis which will eventually be hyperlinked somewhere (sorry it's not there yet).
* `S.LengthSet(n)` will give the length set of the integer n. 
* `S.structureTheoremInitialization()` this will save several attributes that will allow you to examine the structure theorem of sets of length for the numerical semigroup. One of the attributes initialized here is the `LengthSetPeriodicityBound` which gives the upper bound for the start of length set periodicity. Also, after this function is called, for an n greater than or equal to the `LengthSetPeriodicityBound` will use the structure theorem when calculating the length set. 
* `S.LengthSetsUpToElement(nmax)` will dynamically generate a dictionary with keys being the elements of S up to nmax and their corresponding value being the specific element's length set.
* `S.FactorizationsUpToElement(nmax)` will do the same thing as the above function, only for the factorizations

There are other functions available, but I will let you play with it and see what you find.



## Testing the package

If you would like to make changes to the package and test that the base functionality hasn't been effected, you can `from testingPackage import*` and then call the function `runTests()`. If there are now problems, the function will print `Done` twice (from the struture theorem initialization of two semigroups), and then print `Success on all tests`. If there are any issues, the function will raise an exception. 
