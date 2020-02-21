# Introduction to Quark
Quark is a cluster computing flow. 'Flow' meaning that it describes how to use cluster computing with Python, and the concepts behind it.

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

# Build and Test

## Building a cluster with Raspberry Pi 4s

## Building a simulated cluster

So you don't have multiple pis lying around. That's fine, we can virtualise a cluster with Virtual Machines. 

A virtual machine is a file, typically called an image, that behaves like an actual computer. In other words, creating a computer within a computer. It runs in a window, much like any other program, giving the end user the same experience on a virtual machine as they would have on the host operating system itself. The virtual machine is sandboxed from the rest of the system, meaning that the software inside a virtual machine can’t escape or tamper with the computer itself. Multiple virtual machines can run simultaneously on the same physical computer.

### Let's get started...

1) [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads) for your system (Supports Windows, MacOS, Linux & Solaris). Follow the installer instructions to install it.
2) [Download the Ubuntu Server 18.04.4 LTS image](https://ubuntu.com/download/server)  
3) Open VirtualBox and click **New**. We'll set up the *controller* node first.
4) Enter *simpy-controller* as the name, then select *Linux* as the type and *Ubuntu 64bit* as the version .
5) For all the following prompts, just click *continue* or *create* on each (unless you want custom settings). You'll be taken to  *memory size* , then *hard disk*  all the way back to the main screen where you have created the VM. 
6) Click **Start**.
7) Select the .iso file you downloaded from the Ubuntu website in the pop-up then click **Start**.
8) Follow the instructions on-screen to install the Ubuntu Server OS. When you create credentials, make sure **your server's name** is *simpy-controller*. When you get to the Install OpenSSH screen, select it and continue to install the system with default settings. It will download security updates, then press enter when it prompts for a reboot.
9) The VM will reboot, then press enter when it asks you to remove the boot medium/device.

### The next steps...
Congrats, you've set up the controller VM! 
To create the worker node, repeat the previous steps from step **3**, just changing the parts where you entered *simpy-controller* to *simpy-worker1*. 

### Cluster assemble!
Now we need to get our virtual cluster set up with Quark. 

1) Start both the *simpy-controller* and *simpy-worker1* machines. Log into both with the username and password you created.
The following steps need to be done on both nodes.
2) In the menu bar, go to **Devices > Network > Network Settings** and select from the dropdown **Bridged Adapter**. 
3) Type in the console: 
```sh
git clone https://dev.azure.com/Uncast/Quark/_git/quark
```
4) This will clone the code in this repository straight into your nodes. You're ready to move on!

### Setting up each node

The following steps need to be carried out on **all nodes**.

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
