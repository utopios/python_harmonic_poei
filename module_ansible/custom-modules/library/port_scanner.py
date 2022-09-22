from socket import socket, AF_INET, SOCK_STREAM

from ansible.module_utils.basic import *

def analyse(port):
    s = socket(AF_INET, SOCK_STREAM)
    result = s.connect_ex(("127.0.0.1", port))
    if result == 0:
        response = "open"
    else:
        response = "close"
    s.close()
    return response

def scanner(module):
    try:
        result = []
        ports = module.params["ports"]
        for p in ports:
            result.append({"port": p, "status": analyse(p)})
        return result
    except:
        return {"error": True}

def main():
    fields = {
        "ports": {
            "required": True,
            "type": "list"
        },
    }
    module = AnsibleModule(argument_spec=fields)

    # response = {"result": "hello world"}
    module.exit_json(changed=False, result=scanner(module))


if __name__ == '__main__':
    main()