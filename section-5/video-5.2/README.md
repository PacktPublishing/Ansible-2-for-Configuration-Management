# Ansible 2 for Configuration Management, Video 5.2

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
    kibana_url: http://kibana:5601/
    name: logs-pattern
    time_field_name: "@timestamp"
    pattern: "filebeat-*"
```

We will look at the Python code for the custom module in the next videos.

## Looping

Rather than hard-coding the index pattern, to make our role even more useful,
we include this slightly more complex task:

```
- name: kibana index patterns
  kibana_index_pattern:
    kibana_url: "{{ kibana_url }}"
    name: "{{ item.key }}"
    pattern: "{{ item.value.pattern }}"
    time_field_name: "{{ item.value.time_field_name | default(omit) }}"
  with_dict: "{{ kibana_indexes }}"
```

This allows us to include a dictionary `kibana_indexes` in `group_vars` that
specifies all of the index patterns we want created. The task will loop
through the dictionary and use each item with the `kibana_index_pattern`
module.

## Running

Run from this folder:

```
ansible-playbook -i inventory playbook.yaml
```
