# Ansible 2 for Configuration Management, Video 3.5

This video discusses the use of a Jinja 2 template in the Filebeat role.

## Prerequisites

Complete the prerequisites in the main `README.md` file prior to running
this example.

This example installs Elasticsearch, Kibana, and Logstash onto "servers" and
Filebeat onto "clients". You can use the `setup` directory to provision one
server and two clients as virtual machines in AWS or use what you learn in
these videos to modify this example to work with existing hosts.

Look at the variables in `group_vars/all.yaml` to make sure they match your
configuration (especially the location of your SSH private key).

## Templates

The Ansible `template` module allows us to customize the content of a file
using variables. Ansible uses the Jinja2 template engine to process the file.
Templates can include simple variable substitution as well as more complex
logic.

The `filebeat` role in `roles` contains a template that allows us to configure
the location of Logstash using a variable. This makes it much easier to reuse
the role because we only have to change the variable; we don't have to edit
the configuration file in the role.

## Running

Run from this folder:

```
ansible-playbook -i inventory playbook.yaml
```
