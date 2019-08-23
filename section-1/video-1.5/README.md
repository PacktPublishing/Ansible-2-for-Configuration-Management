# Ansible 2 for Configuration Management, Video 1.5

This folder contains sample ad-hoc Ansible commands.

Ansible ad-hoc commands are used to automate a task on one or more servers
without storing that task in a playbook. It is useful for checking and testing
state or for commands that only need to be run once.

## Prerequisites

Install Ansible per the instructions in `section-1/video-1.3`. To use connections
to remote machines, you may need to configure SSH and sudo as described in Video 1.4.

## Ad-hoc Commands

An ad-hoc Ansible command uses the `ansible` command rather than
`ansible-playbook`. Here are some examples:

```
# Loopback test of the local machine
ansible all -i localhost, -c local -m ping

# Test connectivity to hosts in the inventory
ansible all -i inventory -e @vars.yaml -m ping

# Ensure a service is running on the "server" machine
ansible server -i inventory -e @vars.yaml -b -m service -a "name=elasticsearch state=started"
```

The last two examples use the file `vars.yaml`, which tells Ansible how to
connect to and control the remote systems. Look at the variables in `vars.yaml`
to make sure they match your configuration (especially the location of your
SSH private key).

The last two examples use inventory, which is described in upcoming videos.
