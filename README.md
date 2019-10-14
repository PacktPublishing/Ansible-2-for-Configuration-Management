# Ansible 2 for Configuration Management [Video]
This is the code repository for [Ansible 2 for Configuration Management [Video]](https://www.packtpub.com/cloud-networking/ansible-2-for-configuration-management-video), published by [Packt](https://www.packtpub.com/?utm_source=github). It contains all the supporting project files necessary to work through the video course from start to finish.

## About the Video Course
Configuration management is complicated, with a need for high availability, failover, and continuous updates and maintenance. Ansible 2 is a powerful automation tool that can help you manage the configuration of all your servers, whether you work on-premise or in the cloud.

With this course, you can quickly start using Ansible to automate the installation, configuration, and updates, ensuring that your systems are configured the right way automatically. You will then customize Ansible's behavior with variables, and apply similar automation to groups of servers. Next, you will work with roles, which will give you the ability to perform any required automation on your servers when it comes to installing, configuring, and running software. You'll manage servers and other resources in Amazon Web Services, then build Docker containers to deploy them to Kubernetes. You will also work with Ansible's power-user features with custom facts and custom modules.

By the end of the course, you will have worked through hands-on examples of Ansible 2 configuration management, enabling you to immediately start automating your own systems.


<H2>What You Will Learn</H2>
<DIV class=book-info-will-learn-text>
<UL>
<LI><SPAN style="LINE-HEIGHT: 20px; BACKGROUND-COLOR: transparent">Install, configure, and maintain a group of servers by automatically managing system configurations using Ansible 2</SPAN> 
<LI><SPAN style="LINE-HEIGHT: 20px; BACKGROUND-COLOR: transparent">Simplify automatic configuration management by applying each automated step the same way, every time, thus guaranteeing reliability</SPAN> 
<LI><SPAN style="LINE-HEIGHT: 20px; BACKGROUND-COLOR: transparent">Quickly adapt and apply automated installations and configurations to your own systems by working on practical examples</SPAN> 
<LI><SPAN style="LINE-HEIGHT: 20px; BACKGROUND-COLOR: transparent">Download existing Ansible roles as reusable automation units so you can apply identical automation to large numbers of systems</SPAN> 
<LI><SPAN style="LINE-HEIGHT: 20px; BACKGROUND-COLOR: transparent">Build your own custom Ansible roles and modules so you can use Ansible to its full potential</SPAN>
<LI><SPAN style="LINE-HEIGHT: 20px; BACKGROUND-COLOR: transparent">Perform any automation task (no matter how complex) with ease using Ansible</SPAN></LI></UL></DIV>

## Instructions and Navigation
### Assumed Knowledge

To fully benefit from the coverage included in this course, you will need:
●	An understanding of installing and configuring software
●	Basic knowledge of editing files and using the command line.
You don’t need any prior experience with Ansible.


To fully benefit from the coverage included in this course, you will need:

This course has the following software requirements:

●	An editor (Atom suggested)

●	Recommended packages: atom-ide-ui, ide-yaml

●	Access to a physical or virtual machine running Linux

●	The videos demonstrate using Ubuntu 18.04

●	See the videos or README.md in the exercise files for setup instructions

●	Access to at least one other physical or virtual machine to practice automation

●	The videos demonstrate creating machines in Amazon Web Services

●	Other configurations will require some minor changes to the exercise files

This course has been tested on the following system configuration for the Ansible control machine:

●	OS: Ubuntu 18.04

●	Processor: Quad Core Intel

●	Memory: 8GB

●	Hard Disk Space: 100GB

The examples use Amazon Web Services to create the needed computing resources to try out Ansible automation, but other cloud providers or local hardware will work as well with some minor changes to the exercise files.

## Layout

This repository is laid out based on the course videos. The first video after
the course introduction includes a complete Ansible demo, so the
`section-1/video-1.2` folder contains a complete example of using Ansible to
install and configure software on a set of servers.

## Prerequisites

See the `section-1/video-1.3` folder for instructions on installing Ansible.
Then, install required roles using Ansible Galaxy:

```
ansible-galaxy install geerlingguy.java,1.9.5
ansible-galaxy install geerlingguy.elasticsearch,3.0.1
ansible-galaxy install geerlingguy.kibana,3.2.1
ansible-galaxy install geerlingguy.logstash,4.0.0
```

Finally, many of the course examples are configured to run Ansible against
three virtual machines in Amazon Web Services. See the `setup` folder for
creating these virtual machines using Ansible.

All of these prerequisites are needed *before* running the complete example in
`section-1/video-1.2`.

## Dynamic Inventory

Once the virtual machines are created in Amazon Web Services, Ansible dynamic
inventory is used to find the instances and obtain IP addresses. The `common`
folder contains the standard `ec2` dynamic inventory script `ec2.py` and
configuration file `ec2.ini`. The `ec2.ini` file is configured to use the
U.S. East 1 AWS region; if you wish to use another region, edit this file
(and update the associated variables in the `setup/group_vars/all.yaml` file).

Of course, using what you learn from these videos, you can also adapt these
examples to use regular static inventory to control other physical or virtual
machines.

## Related Products
* [Hands-On Machine Learning with Scala and Spark [Video]](https://www.packtpub.com/big-data-and-business-intelligence/hands-machine-learning-scala-and-spark-video?utm_source=github&utm_medium=repository&utm_campaign=9781789342468)

* [RESTful Services with Delphi [Video]](https://www.packtpub.com/application-development/restful-services-delphi-video?utm_source=github&utm_medium=repository&utm_campaign=9781789951882)

* [Federated Learning with TensorFlow [Video]](https://www.packtpub.com/big-data-and-business-intelligence/federated-learning-tensorflow-video?utm_source=github&utm_medium=repository&utm_campaign=9781838823658)
