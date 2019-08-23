# Ansible 2 for Configuration Management, Video 2.5

This video demonstrates more advanced use of Ansible inventory groups.

## Prerequisites

Install Ansible per the instructions in `section-1/video-1.3`.

If you want to try out AWS dynamic inventory, you need to set up instances in
AWS using the instructions in the `setup` folder.

## Inventory Groups

In addition to the basic inventory groups we saw before, we can create groups
of groups. This is useful for applying different, overlapping configuration
to hosts. For example, we might want to apply some configuration to all of
our servers, but some configuration only to web servers. We can get ready for
that by using groups of groups, for example:

```
[servers:children]
app_servers
web_servers

[app_servers]
app01
app02
app03

[web_servers]
web01
web02
web03
```

## Using Groups with Dynamic Inventory

Dynamic inventory scripts such as the `ec2.py` script used for Amazon Web
Services produce groups based on information about the hosts, such as the
"tags" applied to hosts. However, these group names are automatically generated
and hard to work with. We can use groups of groups to create friendly names
without losing the flexibility of dynamic inventory.

For an example, see the file `inventory/inventory`. This file is used
alongside the `ec2.py` dynamic inventory script, so it does not declare any
hosts directly. Instead, it places the automatically generated group names
from the dynamic inventory script into a parent group with a name that is
easier to use:

```
[servers:children]
tag_type_server
```

This allows us to use the group name `servers` in our `playbook.yaml` file
rather than having to use the group name `tag_type_server`.
