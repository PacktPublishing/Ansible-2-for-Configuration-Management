# Ansible 2 for Configuration Management, Video 3.6

This video illustrates control flow in templates.

## Prerequisites

Install Ansible per the instructions in `section-1/video-1.3`.

## Template Control Flow

Templates allow us to do more than just substitute variables. We can have
conditional sections and loops. The included `filebeat.yml.j2` demonstrates
the `{% if %}` and `{% for %}` constructs.

## Running

Run from this folder and print the resulting template:

```
ansible-playbook -i inventory playbook.yaml
cat /tmp/filebeat.yml
```
