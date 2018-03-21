import configparser
# argparse is not used, show just to remind myself (it is a similar construct):
# from argparse import ArgumentParser


def write_config():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {
        'Parameter1': 'Value1',
        'Parameter2': 'Value2',
        'Parameter3': 'Value3'
    }
    config['SECTION1'] = {}
    config['SECTION1']['PARAMETER1'] = 'Value1'
    config['SECTION1']['PARAMETER2'] = 'Value2'
    config['SECTION1']['PARAMETER3'] = 'Value3'

    with open('my_created_manually.cnf', 'w') as file:
        config.write(file)


def read_config(file):
    config = configparser.ConfigParser()
    config.read(file)
    print(config.sections())
    # print(config['client'])
    for key in config['client']:
        print(key, ': ', config['client'][key], sep='')
        # print(config['client'][key])


read_config('my.cnf')