#!/bin/bash
MY_DIR="$(cd "${0%/*}" 2>/dev/null; echo "$PWD")"
PLAYBOOK=${MY_DIR}/teardown.yaml

ansible-playbook -i localhost, ${PLAYBOOK} $*
