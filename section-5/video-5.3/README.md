# Ansible 2 for Configuration Management, Video 5.3

This folder illustrates passing arguments to a module and returning results.

## Prerequisites

Install Ansible per the instructions in `section-1/video-1.3`.

## Module Arguments and Results

When building a custom module, the first thing we need to do is decide what
information needs to be passed to the module (arguments) and what information
it will return (results). Of course, the arguments are going to be determined
by what we want the module to do, and the results should be determined by
what information might be useful for users of the module (as we saw in Video
4.2 where we used information from some AWS modules as variables in the
following modules).

In this case, we have an example module in `library` that takes in a string,
a number, and a boolean. If the boolean is true, the module succeeds, and if
the boolean is false, the module fails. The module always returns its inputs
whether it succeeds or fails.

## Running

Run from this folder:

```
ansible-playbook -i localhost, playbook.yaml
```
