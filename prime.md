# Introduction 
prime.py is a Python program that calculates prime numbers up to a certain endpoint over a single or multiple processors in parallel. 
This was written as the first milestone test for my Quark. It enables me to then move on to researching solutions to the [final goal](/README.md)

# Dependencies
- mpi4py
- time
- sys

# How prime.py works
The following steps show how the method of working the prime numbers out works, not Quark. The concepts of parallel computing and how details of how Quark works are available [here](/README.md). 

1.	prime.py works out its rank in the Quark cluster and works out which part of the range of numbers or candidates it needs to check for prime numbers.
2.	for loop goes through range of candidates...
3.	assumes the candidate is a prime
4.	goes through previous candidates and see if they divide without remainder, if so break loop
5.  if we get here, it is a prime number, add to primes array, else go to next candidate
6.	once complete, send results to the controller
7.	if processor is controller, show results