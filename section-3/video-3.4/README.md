# Ansible 2 for Configuration Management, Video 3.4

This folder demonstrates a custom Filebeat role.

## Prerequisites

Complete the prerequisites in the main `README.md` file prior to running
this example.

This example installs Elasticsearch, Kibana, and Logstash onto "servers" and
Filebeat onto "clients". You can use the `setup` directory to provision one
server and two clients as virtual machines in AWS or use what you learn in
these videos to modify this example to work with existing hosts.

Look at the variables in `group_vars/all.yaml` to make sure they match your
configuration (especially the location of your SSH private key).

## Custom Role

The `filebeat` role in `roles` is a custom role that installs Filebeat. With
this custom role, we can control exactly how Filebeat is installed, including
the exact version.

## Running

Run from this folder:

```
ansible-playbook -i inventory playbook.yaml
```
