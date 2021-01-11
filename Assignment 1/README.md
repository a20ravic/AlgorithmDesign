# AlgorithmDesign

Write a python3 subroutine, sformbnine, whose argument is a list of exactly two items, [n,d], where both n and d are positive integers. That is, n, d ∈ {1, 2, 3, . . .}.
The pair [n,d] is to be interpreted as the rational number n/d where each of n and d is in base-9. The return value from sformbnine should be a list that has two items,
i.e., a pair, [x,y], which is interpreted as the rational number x/y, where each of x and y is in base-9, such that x/y is n/d in simplest form. That is, x/y = n/d, but x
and y have no factor in common other than 1. For example, the return value from sformbnine([11,27]) should be [2,5], because (11/27)9 = (10/25)10 = (2/5)10 = (2/5)9. As another example, sformbnine([14,35]) should return [14,35] because (14/35)9 = (13/32)10, which is already in simplest form.
