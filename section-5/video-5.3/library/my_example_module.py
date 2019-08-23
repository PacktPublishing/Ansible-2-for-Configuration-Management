#!/usr/bin/python

# Copyright: (c) 2019, Alan Hohn
# MIT (see LICENSE)

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: my_example_module

author:
    - Alan Hohn
'''

EXAMPLES = '''
# Returns OK
- name: example good result
  my_example_module:
    a_string: "things are all good"
    a_number: 123
    things_are_good: True

# Returns an error
- name: example bad result
  my_example_module:
    a_string: "things are not so good"
    a_number: 789
    things_are_good: False
'''

RETURN = '''
    Returns the inputs
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        a_string=dict(type='str', required=True),
        a_number=dict(type='int', required=True),
        things_are_good=dict(type='bool', required=False),
    )

    result = dict(
        changed=False,
        output_string='',
        output_number=0,
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    result['output_string'] = module.params['a_string']
    result['output_number'] = module.params['a_number']

    if module.params['things_are_good']:
        result['changed'] = True
        module.exit_json(**result)
    else:
        module.fail_json(msg='You said things are not good', **result)


def main():
    run_module()


if __name__ == '__main__':
    main()
