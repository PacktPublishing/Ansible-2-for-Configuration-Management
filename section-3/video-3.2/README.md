# Ansible 2 for Configuration Management, Video 3.2

This video demonstrates installing and using a role from Ansible Galaxy.

## Prerequisites

Install Ansible per the instructions in `section-1/video-1.3`.

This example installs InfluxDB onto a host. You can use the `setup` directory
to provision the server as a virtual machine in AWS or use what you learn in
these videos to modify this example to work with existing hosts.

Look at the variables in `group_vars/all.yaml` to make sure they match your
configuration (especially the location of your SSH private key).

## Ansible Galaxy

Ansible Galaxy is an online repository of roles. We can install roles from
Ansible Galaxy using the `ansible-galaxy` command:

```
ansible-galaxy install manala.influxdb,1.0.9
```

The version number is optional.

You can also install roles using a requirements file:

```
ansible-galaxy install -r requirements.yaml
```

Roles are installed to `$HOME/.ansible/roles`. We can then use them from
a playbook:

```
---
- hosts: servers
  become: yes
  roles:
    - manala.influxdb
```
