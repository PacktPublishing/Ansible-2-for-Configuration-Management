# Ansible 2 for Configuration Management, Video 2.3

Variables allow configuration of Ansible tasks so they can be applied
differently to different hosts or changed more easily. This folder
demonstrates applying variables to tasks.

## Prerequisites

Install Ansible per the instructions in `section-1/video-1.3`.

This example installs a specific version of Java onto a set of hosts. You can
use the `setup` directory to provision one server and two clients as virtual
machines in AWS or use what you learn in these videos to modify this example
to work with existing hosts.

Look at the variables in `group_vars/all.yaml` to make sure they match your
configuration (especially the location of your SSH private key).

## Variables

Variables are a way to provide Ansible with configuration that can be reused
in multiple places or changed more easily. Variables can be substituted into
tasks using `{{ variable_name }}` syntax provided by the Jinja 2 library.

For example, this playbook installs a specific version of Java:

```
- hosts: all
  vars:
    java_version: 8u162-b12-1
  tasks:
- name: install java
  apt:
    name: java={{ java_version }}
    update_cache: yes
```

We can easily change the version of Java by updating the variable or by
overriding it from the command line or another variable file. This could
allow us to install different Java versions on different hosts or more easily
control updating to a new version.
