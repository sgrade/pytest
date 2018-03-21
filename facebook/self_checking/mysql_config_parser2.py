import configparser


def parse_config(filename):
    f = configparser.ConfigParser()
    f.read(filename)
    print(f.sections())
    for key in f['client']:
        print(key, ': ', f['client'][key], sep='')


conf = 'my.cnf'
parse_config(conf)
