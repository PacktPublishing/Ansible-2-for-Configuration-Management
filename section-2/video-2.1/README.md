# Ansible 2 for Configuration Management, Video 2.1

This folder demonstrates Ansible tasks and idempotence.

## Prerequisites

Install Ansible per the instructions in `section-1/video-1.3`.

## Tasks

Each play in an Ansible playbook contains a list of tasks (or a list of roles,
described in later videos).

Each task is one single piece of automation for Ansible to do. But Ansible is
smart, and only performs the task if necessary. This smart behavior makes
Ansible much safer and makes it possible to run Ansible multiple times without
worrying about the current state of the system. (This is called "idempotence".)

Here is a sample Ansible task to install a package.

```
- name: install elasticsearch
  package:
    name: elasticsearch
    state: present
```

Each task runs some Ansible "module", in this case the `package` module.
The `package` module checks the state of the `elasticsearch` package. If it
is already installed ("present") then Ansible does nothing. If it is not
installed, Ansible will install it.

Ansible typically uses underlying operating system functionality where possible.
In this case the package module uses the underlying package manager (e.g. Apt
or Yum) to actually install the package.

See `playbook.yaml` for example tasks that demonstrate idempotence.

## Running

To run:

```
ansible-playbook -i localhost, playbook.yaml
```
