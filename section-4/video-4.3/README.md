# Ansible 2 for Configuration Management, Video 4.3

This folder demonstrates building an Amazon Machine Image (AMI) using Packer
and Ansible.

**NOTE** The AMI created by this playbook is not terminated automatically.
Remember to go in and clean up the AMI that you create!

## Prerequisites

First, complete the prerequisites in the main `README.md` file.

Next, install Packer by downloading the binary package from:

https://www.packer.io/downloads.html

Unzip into a directory on your PATH, such as `/usr/local/bin`.

Next, install the AWS command line interface:

```
sudo pip install awscli
```

You will also need to configure AWS (e.g. using `aws configure`) per the usual
Amazon Web Services instructions. This configuration is used by Packer.

Finally, edit the `packer-aws.json` file based on an available AWS subnet and
security group. The security group you select must allow SSH from your own
IP address. The security group and the subnet must be on the same network.

## Packer

Packer works by creating and starting a virtual machine, running one or more
provisioners on it (in this case Ansible), then packaging the updated virtual
machine. In this case, we end up with an AMI that can immediately be used to
deploy a server with the ELK stack already installed.

## Running

Run `packer build packer-aws.json`.

Note that this process will take a while as we need to wait for the instance to
finish initializing before we can run Ansible.
