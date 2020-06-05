# Quark
Quark is the name of this project. It's a cluster computing flow meaning that it describes how to get started and use cluster computing, and explains some of the the concepts behind it.

**Objective:** Use multiple ARM-based computers to calculate pi in parallel to the highest amount of digits in 60 minutes.

Although the main objective is above, Quark also will be here for other students or users to learn and use parallel computing.

## Concepts

### Introduction to cluster computing
Cluster computing is a type of computing in which a group of computers are linked together so that they can act like a single computer. 

In its most basic form, a cluster is a system comprising two or more computers or systems (called nodes) which work together to execute applications or perform other tasks, so that users who use them, have the impression that only a single system responds to them, thus creating an illusion of a single resource (virtual machine). This concept is called transparency of the system. As key features for the construction of these platforms is included elevation : reliability, load balancing and performance.

### How cluster computing works

There are **two** types of nodes in a cluster. A *controller*, which distributes the tasks and controlls the cluster and *workers*, which do what they say on the tin, carry out the task.
Controllers are sometimes called master nodes or governing nodes. 
A computer in a cluster is known as a **node** whether it is a controller or worker.

Tasks are distributed evenly across the nodes so that they can be ran with multiple processors. Tasks also have to be written and designed in a certain way that uses the cluster. 

Our nodes will run [Ubuntu Server](https://ubuntu.com/download/server) as the operating system and use [Python](https://www.python.org) as the high-level language that we will write the tasks in. 

### Visualisation of cluster computing
![cluster](https://www.buzzle.com/images/diagrams/computer-networks/cluster-computing.jpg)
### Terms that we'll use and what they mean

| Term:          | Definition                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Node           | A computer in a cluster.                                                                                                                                                                                                                                                                                                                                                                                                 |
| Controller     | The master computer in a cluster. Distributes tasks amongst the worker nodes to carry out.                                                                                                                                                                                                                                                                                                                               |
| Worker         | A slave node in a cluster. Carries out work given by controller.                                                                                                                                                                                                                                                                                                                                                         |
| Task           | The top-level program written in Python for a Quark Cluster.                                                                                                                                                                                                                                                                                                                                                             |
| Network Switch | Networking hardware that connects devices on a computer network                                                                                                                                                                                                                                                                                                                                                          |
| VirtualBox     | Oracle VM VirtualBox is a cross-platform virtualisation application. What does that mean? For one thing, it installs on your existing Intel or AMD-based computers, whether they are running Windows, Mac OS X, Linux, or Oracle Solaris operating systems (OSes). Secondly, it extends the capabilities of your existing computer so that it can run multiple OSes, inside multiple virtual machines, at the same time. |
| ISO File       | An ISO image is a disk image of an optical disc. In other words, it is an archive file that contains everything that would be written to an optical disc, sector by sector, including the optical disc file system. ISO image files bear the.iso filename extension.                                                                                                                                                     |
| SSH            | Secure Shell (SSH) is a cryptographic network protocol for operating network services securely over an unsecured network. Typical applications include remote command-line, login, and remote command execution, but any network service can be secured with SSH.                                                                                                                                                        |
| Rank           | The position of a node in a cluster (controller is 0, worker 1 is 1, etc).                                                                                                                                                                                                                                                                                                                                               |
| Scattering     | Allocating data to each worker node by the controller.                                                                                                                                                                                                                                                                                                                                                                   |
| Gathering      | Data allocated back to controller from worker nodes.                                                                                                                                                                                                                                                                                                                                                                     |
| Dataset        | A collection of related sets of information that is composed of elements that can be manipulated as a unit by a computer                                                                                                                                                                                                                                                                                                 |
| Process        | A process is the instance of a computer program that is being executed by one or many threads.                                                                                                                                                                                                                                                                                                                           |

**More information about cluster computing is [available here](docs/cluster-indepth.md)**

## Build and Test

  - [Get started with a Raspberry Pi cluster](docs/rpi4-cluster-tutorial.md)
  - [Get started with a simulated cluster in VirtualBox](docs/simulated-cluster-tutorial.md)

## Calculating primes in parallel

### Introduction 
prime.py is a Python task that calculates prime numbers up to a certain endpoint over a single or multiple processors in parallel. This was written as the first milestone test for Quark. It enables me to then move on to researching solutions to the final objective of calculating pi in parallel.

### Dependencies
  - mpi4py
  - time
  - sys

### How prime.py works
The following steps show how the method of working the prime numbers out works, not Quark.  

1.	task works out its rank in the Quark cluster and works out which part of the range of numbers or candidates it needs to check for prime numbers.
2.	for loop goes through range of candidates...
3.	assumes the candidate is a prime
4.	goes through previous candidates and see if they divide without remainder, if so break loop
5.  if we get here, it is a prime number, add to primes array, else go to next candidate
6.	once complete, send results to the controller
7.	if processor is controller, show results

## Calculating Pi in parallel

### Why can't you use parallel computing to calculate pi?

Computing all the digits of Pi from 1 to N in an efficient manner is a coarse-grained parallelizable task. At the very top level, it is not parallelizable at all. All the parallelism is at the lower levels. Therefore, communication between all workers is very frequent - enough to become a bottleneck.

There exist algorithms like BBP to directly compute arbitrary binary digits without the memory cost of computing all the digits before it. These are called "digit-extraction" algorithms. However, these algorithms require roughly O(N*log(N)) time to compute a small number of digits at offset N. Using this approach to compute all the digits from 1 to N will result in a quadratic run-time algorithm. This alone makes it unsuitable for large N.*

To make things worse, the currently known digit-extraction algorithms for bases other than binary are much slower. And a radix conversion runs into the same all-to-all communication problem as the current methods to compute Pi.

*While there exists some potential ways that can make the algorithm sub-quadratic, they haven't been researched since because they don't solve the problem of the radix conversion.


**TL:DR**
That's not how it works. Computing the digits of Pi is like building a skyscraper. You cannot just assign different floors to different contractors to build at the same time and combine them at the end. You need to finish each floor before you can build the floor above it. The only way to parallelize is to have the different contractors work together within each floor. In other words, the parallelism is horizontal, not vertical.
