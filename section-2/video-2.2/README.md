# Ansible 2 for Configuration Management, Video 2.2

Video 2.2 provides an introduction to YAML.

## Prerequisites

None

## YAML

YAML has scalar values (simple data like strings, numbers, or booleans) and
data structures (lists and dictionaries).

Strings don't have to be quoted unless they have special characters:

```
hosts: localhost
ansible_ssh_user: ubuntu
filebeat_version: '7.2.0'
```

The last item is quoted to ensure it doesn't get interpreted as a number even
if it gets changed (e.g. to `7.2`).

Numbers can be of any type:

```
retries: 5       # integer
pi: 3.14         # floating point
version: "1.0"   # explicit string
mode: 0644       # octal
```

A list is like an array:

```
ports:
  - 22
  - 5044
  - 8443
```

A dictionary is multiple key / value pairs:

```
template:
  src: filebeat.yml.j2
  dest: /etc/filebeat/filebeat.yml
  owner: root
  group: root
  mode: 0600
```
