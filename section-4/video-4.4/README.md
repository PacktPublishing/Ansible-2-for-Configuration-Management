# Ansible 2 for Configuration Management, Video 4.4

This folder demonstrates managing Docker from Ansible.

## Prerequisites

Complete the prerequisites in the main `README.md` file prior to running
this example.

This example installs Docker onto a server and then uses it to start InfluxDB
as a service. You can use the `setup` directory to provision the server as a
virtual machine in AWS or use what you learn in these videos to modify this
example to work with existing hosts.

Look at the variables in `group_vars/all.yaml` to make sure they match your
configuration (especially the location of your SSH private key).

## Managing Docker from Ansible

Ansible provides many modules to manage Docker. This folder uses `docker_image`
to make sure the exact desired version is pulled, then `docker_volume` to make
sure a volume is created to store persistent data. For more information, see
the role in `roles/influxdb-docker`.

## Running

Run `ansible-playbook -i inventory playbook.yaml`.
