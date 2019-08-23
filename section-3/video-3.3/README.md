# Ansible 2 for Configuration Management, Video 3.3

This video demonstrates customizing a role using variables.

## Prerequisites

Install Ansible per the instructions in `section-1/video-1.3`.

This example installs InfluxDB onto a host. You can use the `setup` directory
to provision the server as a virtual machine in AWS or use what you learn in
these videos to modify this example to work with existing hosts.

Look at the variables in `group_vars/all.yaml` to make sure they match your
configuration (especially the location of your SSH private key).

## Customizing Roles

Each role has a set of variables it uses. We need to look at the role
documentation or at the role itself to find the variables.

Variables in `group_vars` will override variables in the role `defaults`,
so it is very easy to customize a role once we know what variables it uses
and how they should be provided.

In this case, look in the file `group_vars/servers.yaml` for an example of how
we can configure the `manala.influxdb` role.
