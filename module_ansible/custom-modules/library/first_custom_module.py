from ansible.module_utils.basic import *


def logic_module(module):
    return {
        "response": module.params["name"] + " "+module.params["description"]
    }


def main():
    fields = {
        "name": {
            "default": "default value",
            "type": "str"
        },
        "description": {
            "required": True,
            "type": "str"
        }
    }

    module = AnsibleModule(argument_spec=fields)

    # response = {"result": "hello world"}
    module.exit_json(changed=False, result=logic_module(module))


if __name__ == '__main__':
    main()
