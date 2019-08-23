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
module: kibana_index_pattern

short_description: Manage a Kibana index pattern

version_added: "2.8"

description:
    - "Create, update, and delete index patterns in Kibana"

options:
    kibana_url:
        description:
            - URL of the Kibana server.
        required: true
    name:
        description:
            - The name for this index pattern.
        required: true
    pattern:
        description:
            - The pattern to match. Required if state is present.
    time_field_name:
        description:
            - Field to use to filter data by time. Default is none.
    state:
        description:
            - Goal state for the pattern.
        choices: [present, absent]
        default: present
author:
    - Alan Hohn
'''

EXAMPLES = '''
# Create or update an index pattern
- name: filebeat pattern
  kibana_index_pattern:
    kibana_url: http://kibana:5601/
    name: logs-pattern
    time_field_name: "@timestamp"
    pattern: "filebeat-*"

# Remove an index pattern
- name: remove filebeat pattern
  my_test:
    kibana_url: http://kibana:5601/
    name: logs-pattern
    state: absent
'''

RETURN = '''
name:
    description: The name of the pattern
    type: str
    returned: always
pattern:
    description: The pattern used for matching
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
import requests


def compare_current_state(current, desired):
    attributes = current['attributes']
    if desired['time_field_name'] == None:
        return (attributes['title'] == desired['pattern']
            and not 'timeFieldName' in attributes)
    return (attributes['title'] == desired['pattern']
        and attributes['timeFieldName'] == desired['time_field_name'])


def store_new_state(state, result):
    result['name'] = state['id']
    result['pattern'] = state['attributes']['title']


def state_present(module, url, result):
    # Check current state
    pattern_exists = False
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        if compare_current_state(r.json(), module.params):
            # No changes needed
            module.exit_json(**result)
        else:
            # Exists but needs update
            pattern_exists = True
    elif r.status_code != requests.codes.not_found:
        msg = 'Failed to query Kibana (status {code}): {output}'.format(
            code=r.status_code, output=r.text
        )
        module.fail_json(msg=msg, **result)

    # If we got here, we need to change state
    result['changed'] = True

    attributes = dict(
        title=module.params['pattern']
    )
    if module.params['time_field_name'] is not None:
        attributes['timeFieldName'] = module.params['time_field_name']
    payload = {"attributes": attributes}
    headers = {'kbn-xsrf': 'true'}

    if pattern_exists:
        r = requests.put(url, json=payload, headers=headers)
    else:
        r = requests.post(url, json=payload, headers=headers)

    if r.status_code != requests.codes.ok:
        msg = 'Failed to update Kibana (status {code}): {output}'.format(
            code=r.status_code, output=r.text
        )
        module.fail_json(msg=msg, **result)

    store_new_state(r.json(), result)
    module.exit_json(**result)


def state_absent(module, url, result):
    # Check current state
    r = requests.get(url)
    if r.status_code == requests.codes.not_found:
        # Nothing to delete
        module.exit_json(**result)
    elif r.status_code != requests.codes.ok:
        msg = 'Failed to query Kibana (status {code}): {output}'.format(
            code=r.status_code, output=r.text
        )
        module.fail_json(msg=msg, **result)

    result['changed'] = True

    headers = {'kbn-xsrf': 'true'}
    r = requests.delete(url, headers=headers)
    if r.status_code != requests.codes.ok:
        msg = 'Failed to update Kibana (status {code}): {output}'.format(
            code=r.status_code, output=r.text
        )
        module.fail_json(msg=msg, **result)

    module.exit_json(**result)


def run_module():
    module_args = dict(
        kibana_url=dict(type='str', required=True),
        name=dict(type='str', required=True),
        time_field_name=dict(type='str', required=False),
        pattern=dict(type='str', required=False),
        state=dict(default='present', choices=['present', 'absent'])
    )

    result = dict(
        changed=False,
        name='',
        pattern=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    url = '{url}/api/saved_objects/index-pattern/{name}'.format(
        url=module.params['kibana_url'],
        name=module.params['name']
    )

    if module.params['state'] == 'present':
        state_present(module, url, result)
    elif module.params['state'] == 'absent':
        state_absent(module, url, result)
    else:
        module.fail_json(msg='Unrecognized state', **result)


def main():
    run_module()


if __name__ == '__main__':
    main()
