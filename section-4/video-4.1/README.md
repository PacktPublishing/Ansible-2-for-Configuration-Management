# Ansible 2 for Configuration Management, Video 4.1

This video demonstrates securing variables with Ansible Vault.

## Prerequisites

Install Ansible per the instructions in `section-1/video-1.3`.

Install the InfluxDB role from Ansible Galaxy by running:

```
ansible-galaxy install -r requirements.yaml
```

This example installs InfluxDB onto a host. You can use the `setup` directory
to provision the server as a virtual machine in AWS or use what you learn in
these videos to modify this example to work with existing hosts.

Look at the variables in `group_vars/all.yaml` to make sure they match your
configuration (especially the location of your SSH private key).

## Ansible Vault

Ansible Vault provides for encrypted storage of secret information so we can
check files into version control while keeping passwords, tokens, etc. secure.

When Ansible runs, it seamlessly decryptes files encrypted with Ansible Vault
using a password we provide. Task and template files can be encrypted but we
usually just encrypt variable files.

In this case, the file `group_vars/servers/vault.yaml` has an encrypted password
while `group_vars/servers/main.yaml` has the unencrypted content.

To see the encrypted content:

```
ansible-vault view group_vars/servers/vault.yaml
```

To run this example:

```
ansible-playbook -i inventory playbook.yaml --ask-vault-pass
```

When prompted for a password, enter `password`.
