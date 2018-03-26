import configparser


def parse_config(filename):
    f = configparser.ConfigParser()
    f.read(filename)
    for i in f['client']:
        print(f['client'][i])


conf = 'my.cnf'
parse_config(conf)
