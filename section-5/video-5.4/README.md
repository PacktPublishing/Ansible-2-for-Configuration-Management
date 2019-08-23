# Ansible 2 for Configuration Management, Video 5.4

This folder illustrates using an Ansible custom module.

## Prerequisites

Complete the prerequisites in the main `README.md` file prior to running
this example.

This example installs Elasticsearch, Kibana, and Logstash onto "servers" and
Filebeat onto "clients". You can use the `setup` directory to provision one
server and two clients as virtual machines in AWS or use what you learn in
these videos to modify this example to work with existing hosts.

Look at the variables in `group_vars/all.yaml` to make sure they match your
configuration (especially the location of your SSH private key).

## Ansible Custom Modules

To complete our Kibana setup, we need to create an index pattern for Filebeat
data so we can easily visualize it. We can do this in the Kibana dashboard
using a browser, but it would be better to automate it. To do this, because
there isn't an existing Ansible module for Kibana index patterns, we use a
custom one.

The `kibana_setup` role contains our custom module in the file
`library/kibana_index_pattern.py`. This allows us to include a task definition
like this:

```
- name: filebeat pattern
  kibana_index_pattern:
    kibana_url: http://localhost:5601/
    name: logs-pattern
    time_field_name: "@timestamp"
    pattern: "filebeat-*"
```

As we look at the module code, note how we first check the current state
before we decide to change anything. This allows us to ensure we are
idempotent. To illustrate this, we separate the `kibana_setup` role into a
different playbook.

## Running

First run from this folder:

```
ansible-playbook -i inventory first.yaml
```

Next, run the separate playbook for `kibana_setup`:

```
ansible-playbook -i inventory second.yaml
```

Finally, run the same playbook again to show that our module notices that the
index pattern already exists:

```
ansible-playbook -i inventory second.yaml
```
