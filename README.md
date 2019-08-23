# Ansible 2 for Configuration Management

This code repository contains examples from the video course Ansible 2 for
Configuration Management by Alan Hohn, published by Packt Publishing.

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

