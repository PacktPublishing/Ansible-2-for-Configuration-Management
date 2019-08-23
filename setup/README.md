# Ansible 2 for Configuration Management, AWS Setup

This folder uses Ansible to create virtual machines in Amazon Web Services.

**NOTE** The virtual machine instances created by this playbook are not
terminated automatically. Remember to terminate the instances using the
`destroy.sh` script to avoid being charged for instances you are not using!

## Prerequisites

To use this Ansible configuration, you must first install Ansible. See the
instructions in Section 1.

Next, install the necessary Python modules:

```
sudo pip install boto boto3 botocore jmespath awscli
```

Note that on some systems, if you are using Python 3, you need to run `pip3`
instead of `pip`. Match the command you used to install Ansible itself.

The AWS command line interface is needed as it is used from within the Ansible
playbook to get SSH host key information.

You will also need to configure AWS (e.g. using `aws configure`) per the usual
Amazon Web Services instructions. This configuration is used within Ansible
itself as well as by the `aws` command.

## Variables

Review the variables in `group_vars/all.yaml` to see if any changes are
required. In particular, the default is to use a key called `aws` so you will
either need to have a key by that name or change the variable to an existing
key.

## Running

Run `create.sh` to set up AWS. Run `destroy.sh` to terminate the instances.

Note that creation will take a while as we need to wait for the instance to
finish initializing before we can collect the SSH host key.

**NOTE** Ansible will warn that the instance did not start before timeout.
This is expected and the task to fetch host keys has a retry in it to wait
for instance startup. Also note that if AWS is a little slow in assigning 
a public IP to an instance, Ansible may fail the first time. This is not an
issue; just run it again and it should succeed.

