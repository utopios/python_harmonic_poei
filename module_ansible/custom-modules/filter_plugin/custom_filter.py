class FilterModule(object):

    def special_filter(self, element):
        return element + ' added by custom filter'

    def port_filter(self, ports):
        result = ""
        for p in ports:
            result += p.port + " "+ p.status+" | "
        return result