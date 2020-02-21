The following steps need to be carried out on **all nodes**.

On each node, run the following:
```sh
git clone https://dev.azure.com/Uncast/Quark/_git/quark
```
This will clone the code in this repository straight into your nodes. 

On each node, run the following:
```sh
sudo apt -y update && sudo apt -y upgrade && sudo reboot
```
This will check for any updates, upgrade all packages on the system, then reboot to further install any packages.
Log back into the system after it has rebooted.

On each node, run the following:
```sh
ifconfig
```
This will return the IP address of the node. Make a note of the **eth0 inet addr**. This is the IP address of the node.

For the cluster to work, each worker node needs to be able to talk to the master node without needing a password to log in. To do this, we use SSH keys. This can be a little laborious, but only needs to be done once. On each node, run the following:
```sh
ssh-keygen -t rsa
```
This creates a unique identity and key pair for the node. Next, tell the controller (simpy-controller) about the keys by running the following on every other node:
```sh
ssh-copy-id <INSERT IP OF CONTROLLER NODE>
```
Finally, do the same on the controller node and copy its key to every other node in the cluster.

The magic that makes our cluster work is MPI (Message Passing Interface). This protocol allows multiple computers to delegate tasks amongst themselves and respond with results. We’ll install MPI on each node of our cluster and, at the same time, install the Python bindings that allow us to take advantage of its magical powers.
On each node, run the following:
```sh
sudo apt install mpich python3-mpi4py
```
Once complete, test MPI is working on each node:
```sh
mpiexec -n 1 hostname
```
You should just get the name of the node echoed back at you. The **-n** means ‘how many nodes to run this on’. If you say one, it’s always the local machine.

### Let's get together
Time for our first cluster operation. From *simpy-controller*, issue the following command:
```sh
mpiexec -n 2 --host <INSERT CONTROLLER IP>,<INSERT WORKER1 IP> hostname
```
We’re asking the master supervisor process, **mpiexec**, to start two processes (-n 2), one on each node. If you’re not using two hosts, you’ll need to change this
as needed. The command hostname just echoes the node’s name, so if all is well, you’ll get a list of the two nodes of the cluster. You’ve just done a bit of parallel computing!

### Is a cluster of one still a cluster?
Now we’ve confirmed the cluster is operational, let’s put it to work. The prime.py program is a simple task that identifies prime numbers. The code takes a single argument, the maximum number to reach before stopping, and will return how many prime numbers were identified during the run. Start by testing it on the master node:
```sh
mpiexec -n 1 python3 prime.py 1000
```
**Translation:** ‘Run a single instance on the local node that runs prime.py testing for prime numbers up to 1000.’ This should run pretty quickly, probably well under a second, and find 168 primes.

### Compute!
To start the supercomputer, run this command from the controller:
```sh
mpiexec -n 4 --host <INSERT CONTROLLER IP>,<INSERT WORKER1 IP> python3 prime.py 100000
```

Each node gets a ‘rank’: a unique ID. The controller is always 0. This is used in the script to allocate which range of numbers each node processes, so no node checks the same number if it is a prime. When complete, each node reports back to the controller detailing the primes found. This is known as ‘gathering’. Once complete, the controller pulls all the data together and reports the result. In more advanced applications, different data sets can be allocated to the nodes by the controller. This is called **scattering**.

## Conclusion

You may have noticed we asked for all the primes up to 1000 in the previous example. This isn’t a great test as it is so quick to complete. 100,000 takes a little longer. In our tests, we saw that a single node took 238.35 seconds, but a fournode cluster managed it in 49.58 seconds – nearly five times faster!

Cluster computing isn’t just about crunching numbers. Fault-tolerance and load-balancing are other concepts worth investigating. Some cluster types act as single web servers and keep working, even if you kill one.