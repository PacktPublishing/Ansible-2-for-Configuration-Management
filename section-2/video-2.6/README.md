# Ansible 2 for Configuration Management, Video 2.6

This video demonstrates applying variables to inventory groups.

## Prerequisites

Install Ansible per the instructions in `section-1/video-1.3`.

This example installs a specific version of Java onto a set of hosts. You can
use the `setup` directory to provision one server and two clients as virtual
machines in AWS or use what you learn in these videos to modify this example
to work with existing hosts.

Look at the variables in `group_vars/all.yaml` to make sure they match your
configuration (especially the location of your SSH private key).

## Group Variables

If we place files with variables in the `group_vars` directory, Ansible will
automatically apply them to inventory groups. We can either create a file
in `group_vars` with the group name, or we can create a directory with the
group name and place in it as many files as we need.

This example illustrates installing a different version of Java on different
hosts. The playbook and tasks are the same for all hosts, but the variables
are different for different groups, so that Ansible's behavior is different
for different groups.
