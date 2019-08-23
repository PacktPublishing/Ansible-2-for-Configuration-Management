# Ansible 2 for Configuration Management, Video 2.4

At the beginning of each play, Ansible gathers "facts" about all of
the hosts in the play by running the `setup` module. These facts can
be used in the same way as variables. This folder demonstrates some of the
available facts.

## Prerequisites

Install Ansible per the instructions in `section-1/video-1.3`.

This example collects facts from a set of hosts. You can use the `setup`
directory to provision one server and two clients as virtual machines in AWS
or use what you learn in these videos to modify this example to work with
existing hosts.

Look at the variables in `group_vars/all.yaml` to make sure they match your
configuration (especially the location of your SSH private key).

## Facts

Facts provide useful information about hosts, including:

* Architecture: 32-bit or 64-bit
* Disks and partitions
* Operating system, distribution, and version
* Network devices and addresses
* CPU and memory
