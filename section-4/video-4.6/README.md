# Ansible 2 for Configuration Management, Video 4.6

This folder demonstrates automating using Ansible to deploy to a Kubernetes
cluster.

## Prerequisites

Install Ansible per the instructions in `section-1/video-1.3`.

Next, install the necessary Python modules. For example, on Ubuntu 18.04:

```
sudo pip install openshift
```

Finally, make sure your Kubernetes cluster is configured.

## Ansible and Kubernetes

Kubernetes is a container orchestration environment. Kubernetes works with
resources created through an API server, such as deployments and services.
The Kubernetes control plane then makes cluster changes as needed to reach
the state specified in the resources. This makes it a very good fit for Ansible,
as Ansible can perform idempotent operations to ensure the resources are
configured correctly, and Kubernetes will then perform the necessary cluster
changes to reach the desired state.

## Running

Run `ansible-playbook -i localhost, playbook.yaml`.
