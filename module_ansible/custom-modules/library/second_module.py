from ansible.module_utils.basic import *


def write_module(module):
    try:
        with open(module.params["file_name"], "w") as f:
            f.write(module.params["file_content"])
            return {"message": "file ok"}
    except:
        return {"error": "error writing file"}

def main():
    fields = {
        "file_name": {
            "required": True,
            "type": "str"
        },
        "file_content": {
            "required": True,
            "type": "str"
        }
    }
    module = AnsibleModule(argument_spec=fields)

    # response = {"result": "hello world"}
    module.exit_json(changed=False, result=write_module(module))


if __name__ == '__main__':
    main()