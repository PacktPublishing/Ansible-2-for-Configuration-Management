# Ansible 2 for Configuration Management, Video 5.1

This folder demonstrates custom Ansible facts.

## Prerequisites

Install Ansible per the instructions in `section-1/video-1.3`.

This example installs a custom fact on a remote host. You can use the `setup`
directory to provision the host as a virtual machine in AWS or use what you
learn in these videos to modify this example to work with existing hosts.

Look at the variables in `group_vars/all.yaml` to make sure they match your
configuration (especially the location of your SSH private key).

## Custom Facts

When the `setup` module runs, it looks in `/etc/ansible/facts.d` on the remote
system. Any executable it finds with the extension `.fact` will be run and the
output treated as JSON. This output will be added to the available facts in the
`ansible_local` dictionary.

To illustrate this, we add a custom fact that collects and prints out load
averages for a host.

## Running

Run `ansible-playbook -i inventory playbook.yaml`.
