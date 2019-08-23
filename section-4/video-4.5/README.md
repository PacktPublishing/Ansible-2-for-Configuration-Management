# Ansible 2 for Configuration Management, Video 4.5

This folder demonstrates automating using Ansible inside Docker containers
via the Ansible Docker connector.

The example starts a Docker container and then controls it using Ansible.

## Prerequisites

Install Ansible per the instructions in `section-1/video-1.3`.

Next, install Docker and the necessary Python module. For example, on Ubuntu
18.04:

```
sudo apt install -y docker.io 
sudo pip install docker
```

Finally, make sure you have Docker working for the user running Ansible.

## Ansible Docker connector

Ansible uses connectors to control how to create its control connection. Until
now, we've used the default connector, SSH, and the `local` connector. The
`docker` connector allows Ansible to run commands inside a running Docker
container, allowing us to use Ansible to act inside a Docker container while
it is running.

## Running

Run `ansible-playbook -i localhost, playbook.yaml`.
