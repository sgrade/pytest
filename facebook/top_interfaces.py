

class TopTwo:
    """
    Processes file with Juniper CLI output showing input/output packets,
    returns top X utilization report

    Sample CLI output:
    www.juniper.net/documentation/en_US/junos/topics/task/operational/security-real-time-interface-information-displaying.html
    """

    def __init__(self, file, number_of_interfaces_in_top):
        self.file = file
        self.number = number_of_interfaces_in_top
        self.top_utilization = dict()

    def compare_utilization(self, port, utilization):
        """Fills an intermediate dictionary with port/utilization;
        Takes care of future report size
        """

        if len(self.top_utilization) < self.number:
            self.top_utilization[utilization] = port
        else:
            for util, prt in self.top_utilization.items():
                if utilization > util:
                    self.top_utilization.pop(util)
                    # utilization is the key to ease sorting later
                    self.top_utilization[utilization] = port
                    return self.top_utilization

    def process_file(self):
        """Processes the file"""
        with open(self.file, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                else:
                    line_splitted = line.split()
                    # processes only lines with data, ignores other lines
                    if len(line_splitted) == 6 and line_splitted[2].isdigit() and line_splitted[4].isdigit():
                        utilization = int(line_splitted[2]) + int(line_splitted[4])
                        if utilization > 0:
                            port_number = line_splitted[0]
                            self.compare_utilization(port_number, utilization)

    def get_report(self):
        """Generates console report form 'top_utilization' dictionary"""
        self.process_file()
        srtd = sorted(self.top_utilization.items())
        srtd.reverse()
        print('Top', self.number, 'interfaces')
        for tpl in srtd:
            print('Interface:', tpl[1], '  utilization:', tpl[0])


x = TopTwo('monitor_interface_traffic.txt', 6)
x.get_report()
