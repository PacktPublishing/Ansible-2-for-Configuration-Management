# Ansible 2 for Configuration Management, Video 1.7

This folder demonstrates Ansible playbooks.

## Prerequisites

Install Ansible per the instructions in `section-1/video-1.3`.

To run this playbook you need to set up an inventory file with machines that
match the playbook groups. You can do this in AWS using the instructions in the
`setup` folder.

## Playbooks and Plays

Ansible playbooks are files in the YAML format that contain plays. Each play
specifies the host or hosts it applies to. Each play contains a list of tasks
(or a list of roles, described in later videos).

See `playbook.yaml` for an example Ansible playbook.

## Running

To run:

```
ansible-playbook -i inventory playbook.yaml
```
