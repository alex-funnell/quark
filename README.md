# Introduction to Quark
Quark is a cluster computing flow. 'Flow' meaning that it describes how to use cluster computing with Python, and the concepts behind it.

Objective: Use multiple ARM-based computers to calculate pi in parallel to the highest amount of digits in 60 minutes.

Although the main objective is above, Quark also will be here for other students or users to learn and use parallel computing.

# Concepts

## How cluster computing works
Cluster computing is a type of computing in which a group of computers are linked together so that they can act like a single computer.

There are **two** types of computers in a cluster. A *controller*, which distributes the tasks and controlls the cluster and *workers*, which do what they say on the tin, carry out the task.
Controllers are sometimes called master nodes or governing nodes. 
A computer in a cluster is known as a **node** whether it is a controller or worker.

Tasks are distributed evenly across the nodes so that they can be ran with multiple processors. Tasks also have to be written and designed in a certain way that uses the cluster. 

Our nodes will run [Ubuntu Server](https://ubuntu.com/download/server) as the operating system, use [Python](https://www.python.org) as the high-level language that we will write the task in. 

## Visualisation of cluster computing

# Build and Test
TODO: Describe and show how to build your code and run the tests. 

# Contribute

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:
- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)