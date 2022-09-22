class FilterModule(object):

    def filters(self):
        return {
            "port_filter": self.port_filter
        }

    def special_filter(self, element):
        return element + ' added by custom filter'

    def port_filter(self, ports):
        result = ""
        for p in ports:
            result += "port :{port}, status:{state} | ".format(port=p["port"], state=p["status"])

        return result
