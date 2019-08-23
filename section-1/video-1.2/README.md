# Ansible 2 for Configuration Management, Video 1.2

This folder contains an Ansible demo.

## Prerequisites

Complete the prerequisites in the main `README.md` file prior to running
this example.

This example installs Elasticsearch, Kibana, and Logstash onto "servers" and
Filebeat onto "clients". You can use the `setup` directory to provision one
server and two clients as virtual machines in AWS or use what you learn in
these videos to modify this example to work with existing hosts.

Look at the variables in `group_vars/all.yaml` to make sure they match your
configuration (especially the location of your SSH private key).

## Running

Run from this folder:

```
ansible-playbook -i inventory playbook.yaml
```
