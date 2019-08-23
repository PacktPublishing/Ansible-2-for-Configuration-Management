# Ansible 2 for Configuration Management, Video 3.1

This video demonstrates Ansible roles

## Prerequisites

Install Ansible per the instructions in `section-1/video-1.3`.

This example installs a specific version of Java onto a set of hosts. You can
use the `setup` directory to provision one server and two clients as virtual
machines in AWS or use what you learn in these videos to modify this example
to work with existing hosts.

Look at the variables in `group_vars/all.yaml` to make sure they match your
configuration (especially the location of your SSH private key).

## Roles

Roles allows us to group related tasks together with the files and configuration
needed to run those tasks. In this example, we create a role called `java` that
installs a specific version of Java onto an Ubuntu machine. The role goes into
the directory `roles/java` so Ansible will find it. This role contains a file
`tasks/main.yaml` that contains the tasks the role should perform.

Because we placed the role in the directory `java` in the `roles` directory,
we can refer to it in our playbook and Ansible will find it:

```
---
- hosts: all
  become: yes
  roles:
    - java
```

Note that our role can also declare variables in the `default` directory. We
can override these with variables from other places (for example, `group_vars`).
