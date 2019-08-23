# Ansible 2 for Configuration Management, Video 1.4

This folder contains information for configuring Ansible to control remote
machines.

Ansible typically connects to remote machines via Secure Shell (SSH). It
typically requires administrative (root) access to install and configure
software and configure and manage system services.

By default, Ansible expects:

1. To use key-based (passwordless) login for SSH
2. After logging in via SSH, to use `sudo` without a password to gain root
   access.

Ansible can prompt for a password if necessary, but passwordless access makes
Ansible much simpler to use.

## Prerequisites

Install Ansible per the instructions in `section-1/video-1.3`.

## Configuring SSH

1. Make sure the remote user has your SSH public key in
   `$HOME/.ssh/authorized_keys`. You can use `ssh-copy-id` to do this
   manually. Cloud providers such as Amazon Web Services do this automatically.
2. Make sure you have the server's public key in your local
   `$HOME/.ssh/known_hosts` file. This tells your local SSH client what key
   to expect from the remote server so it does not need to prompt you. This
   is done the first time you SSH in. You can see an example of using Ansible
   to automate this in the `setup` directory.

## Configuring sudo

1. Make sure `/etc/sudoers` is configured for an admin group (e.g. `admin`,
   `wheel`, or `sudo`) and is set for `NOPASSWD`.
2. Make sure the remote user Ansible will use is in the admin group.

## Testing SSH and sudo

Look at the variables in `group_vars/all.yaml` to make sure they match your
configuration (especially the location of your SSH private key).

Run from this folder:

```
ansible-playbook -i inventory playbook.yaml
```
