from os.path import dirname, join, realpath

def app_root():
    return dirname(dirname(dirname(realpath(__file__))))
