#!/usr/bin/env python3
"""Small independent checks of manuscript formulas; not large-N experiments."""
from collections import Counter
from fractions import Fraction as F
import math
import random


def reverse_bits(i, m):
    return int(f'{i:0{m}b}'[::-1], 2)


def rho(n, k):
    rem = n % (2**k)
    return n-rem + 2*max(rem-2**(k-1), 0)


def newo(q, m, permutations):
    # Input digits are indexed from the most significant fractional bit.
    a = [(q >> (m-1-k)) & 1 for k in range(m)]
    return sum((a[k] ^ permutations[k][tuple(a[k+1:])]) << (m-1-k)
               for k in range(m))


def kernel(v):
    product = 1
    for j, x in enumerate(v, 1):
        product *= 1 + (x*x-x+F(1, 6))/j**2
    return product


def check_binary_formulas():
    rng = random.Random(20261028)
    checked = 0
    for m in range(1, 6):
        size = 2**m
        vdc = [reverse_bits(i, m) for i in range(size)]
        for n in range(1, size+1):
            counts = Counter((vdc[i]-vdc[j]) % size
                             for i in range(n) for j in range(n))
            assert counts[0] == n
            for r in range(1, size):
                assert counts[vdc[r]] == rho(n, r.bit_length())
        for _ in range(20):
            permutations = []
            for k in range(m):
                suffixes = [tuple((s >> t) & 1 for t in range(m-k-1))
                            for s in range(2**(m-k-1))]
                permutations.append({s: rng.randrange(2) for s in suffixes})
            scrambled = [newo(q, m, permutations) for q in vdc]
            assert len(set(scrambled)) == size
            for i in range(size):
                assert Counter((scrambled[i]-scrambled[j]) % size for j in range(i)) == \
                       Counter((vdc[i]-vdc[j]) % size for j in range(i))
                checked += 1
        for h in range(1, size, 2):
            for q in range(size):
                a = [(q >> (m-1-k)) & 1 for k in range(m)]
                digits = []
                for k in range(m):
                    tail = sum(F(a[l], 2**(l-k)) for l in range(k+1, m))
                    digits.append(a[k] ^ (math.floor(h*tail) % 2))
                actual = sum(bit << (m-1-k) for k, bit in enumerate(digits))
                assert actual == (h*q) % size
    print(f'PASS: dyadic multiplicities, {checked} Newo difference rows, odd carries')


def check_lattice_aggregate():
    m = 4
    size = 2**m
    h = [1, 3, 7]
    values = [kernel([F((reverse_bits(r,m)*z) % size, size) for z in h])
              for r in range(size)]
    for horizon in (1, 7, size):
        direct = 0
        for n in range(1, horizon+1):
            pair_sum = sum(kernel([F(((reverse_bits(i,m)-reverse_bits(j,m))*z) % size, size)
                                         for z in h]) for i in range(n) for j in range(n))
            direct += n*(-1 + pair_sum/n**2)
        reduced = horizon*values[0]-F(horizon*(horizon+1),2)
        for k in range(1, m+1):
            qk = sum(F(rho(n,k),n) for n in range(1,horizon+1))
            reduced += qk*sum(values[r] for r in range(2**(k-1),2**k))
        assert direct == reduced
    print('PASS: exact lattice aggregate vs direct ordered-pair sums')


def check_kronecker_aggregate():
    z = [math.sqrt(2), math.sqrt(3)]
    def kv(k):
        return float(kernel([(k*t) % 1 for t in z]))
    for horizon in (1, 2, 7, 15):
        direct = 0.0
        for n in range(1, horizon+1):
            pair_sum = sum(kv(i-j) for i in range(n) for j in range(n))
            direct += n*(-1+pair_sum/n**2)
        reduced = -horizon*(horizon+1)/2 + horizon*kv(0)
        for k in range(1,horizon):
            harmonic_tail = sum(1/n for n in range(k+1,horizon+1))
            reduced += 2*(horizon-k-k*harmonic_tail)*kv(k)
        assert math.isclose(direct,reduced,rel_tol=1e-11,abs_tol=1e-11)
    print('PASS: Kronecker harmonic criterion vs direct ordered-pair sums')


if __name__ == '__main__':
    check_binary_formulas()
    check_lattice_aggregate()
    check_kronecker_aggregate()
