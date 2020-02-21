# Introduction to Quark
Quark is the name of this project. It's a cluster computing flow meaning that it describes how to get started and use cluster computing, and explains some of the the concepts behind it.

**Objective:** Use multiple ARM-based computers to calculate pi in parallel to the highest amount of digits in 60 minutes.

Although the main objective is above, Quark also will be here for other students or users to learn and use parallel computing.

# Concepts

## How cluster computing works
Cluster computing is a type of computing in which a group of computers are linked together so that they can act like a single computer.

There are **two** types of computers in a cluster. A *controller*, which distributes the tasks and controlls the cluster and *workers*, which do what they say on the tin, carry out the task.
Controllers are sometimes called master nodes or governing nodes. 
A computer in a cluster is known as a **node** whether it is a controller or worker.

Tasks are distributed evenly across the nodes so that they can be ran with multiple processors. Tasks also have to be written and designed in a certain way that uses the cluster. 

Our nodes will run [Ubuntu Server](https://ubuntu.com/download/server) as the operating system and use [Python](https://www.python.org) as the high-level language that we will write the tasks in. 

## Visualisation of cluster computing

# Calculating primes in parallel

## Introduction 
prime.py is a Python task that calculates prime numbers up to a certain endpoint over a single or multiple processors in parallel. This was written as the first milestone test for Quark. It enables me to then move on to researching solutions to the final objective of calculating pi in parallel.

## Dependencies
- mpi4py
- time
- sys

## How prime.py works
The following steps show how the method of working the prime numbers out works, not Quark.  

1.	task works out its rank in the Quark cluster and works out which part of the range of numbers or candidates it needs to check for prime numbers.
2.	for loop goes through range of candidates...
3.	assumes the candidate is a prime
4.	goes through previous candidates and see if they divide without remainder, if so break loop
5.  if we get here, it is a prime number, add to primes array, else go to next candidate
6.	once complete, send results to the controller
7.	if processor is controller, show results

# Calculating Pi in parallel

# Build and Test

- [Get started with a Raspberry Pi cluster](docs/rpi4-cluster-tutorial.md)
- [Get started with a simulated cluster in VirtualBox](docs/simulated-cluster-tutorial.md)