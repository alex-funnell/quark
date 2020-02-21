So you don't have multiple RPis lying around. That's fine, we can virtualise a cluster with Virtual Machines. 

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

### Setting up each node

To setup each node, follow [these instructions](/docs/nodesetup.md).