#!/usr/bin/env python3

from sys import argv
from math import sqrt

"""Output primes smaller than an integer
Given a single integer argument n, return a list containing all primes
numbers strictly less than n.
"""

def main(argv):
	print(eratosthenes(argv[1]))
	return 0

def gen_eratosthenes():
	"""Generator prime numbers"""
	'''
	usage:
	p=gen_eratosthenes()
	next(p)
	each time run next(p), it produces a new prime number, start from 2, without end.
	'''
	p = 1
	while True:
	    isprime = True
	    p += 1
	    for x in range(2,int(sqrt(p))+1):
	        if p%x == 0:
	            isprime = False
	            break
	    if isprime:
	        yield p



def gen_ints():
	"""Generator for positive integers strictly greater than 1."""
	n = 2   #Generator starts at 2, the smallest prime number
	while True:
	    yield n
	    n += 1

def eratosthenes(number):
	"""Enter a positive integer greater than 2; return the list 
	of prime numbers strictly less than that integer."""
	try:
	    number = int(number)
	except TypeError:
	    return 'Argument must not be a list'
	except ValueError:
	    return 'Argument must be an integer, not "%s"' % number

	if number < 2:
	    return 'Argument must be an integer greater than 2, not %d' % number
	else:
	    #generate list of integers 2 through n-1
	    g = gen_ints()
	    primes = [next(g) for _ in range (number-2)]
  
	    stopPoint = sqrt(number)
	    primePosition = 0
	    testPrime = primes[primePosition]
	    while testPrime < stopPoint:
	        #iterate backwards through list and remove multiples
	        for index in range(len(primes)-1,primePosition,-1):
	            if primes[index]%testPrime == 0:
	                del primes[index]
	        primePosition += 1
	        testPrime = primes[primePosition]
	    return primes

def test_primes():
	"""Check that the primes less than 100 are correct """
	number = 100
	computed = eratosthenes(number)
	expected = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,
				53,59,61,67,71,73,79,83,89,97]
	success = computed == expected
	message = 'Computed %s, expected %s' % (computed, expected) 
	assert success, message

def test_primes_negNum():
	"""eatosthenes(n) input is a negative number """
	number = -10
	computed = eratosthenes(number)	
	expected = 'Argument must be an integer greater than 2, not -10'
	success = computed == expected
	message = 'Computed %s, expected %s' % (computed, expected)
	assert success, message

def test_primes_char():
	"""eatosthenes(n) input is a char"""
	number = 'a'
	computed = eratosthenes(number)
	expected = 'Argument must be an integer, not "a"'
	success = computed == expected
	message = 'Computed %s, expected %s' % (computed, expected)
	assert success, message

if __name__ == "__main__":
	try:
	    main(argv)
	except IndexError:
	    #Accurate feedback for n==2 since the IndexError gets caught first
	    if len(argv) < 2: 
	        print('Missing command-line argument.')
	    else:
	        print('No prime number smaller than 2.')
	    exit(1)
	# test functions
	test_primes()
	test_primes_negNum()
	test_primes_char()
