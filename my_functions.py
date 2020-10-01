from napalm import get_network_driver
from pprint import pprint

def create_con(device):
    device_type = device.pop("device_type")
    driver = get_network_driver(device_type)
    new_device = driver(**device)
    print("Connection created")
    return new_device

def create_backup(napalm_con):
    napalm_con.open()
    output = napalm_con.get_config()
    backup = output["running"]
    fname = napalm_con.get_facts()["hostname"]
    f = open(fname, "w")
    f.write(backup)
    f.close() 
    napalm_con.close()
    print("Config saved to a file for "+fname)

def create_checkpoint(napalm_con):
    napalm_con.open()
    output = napalm_con._get_checkpoint_file()
    f = open("nxos1.conf","w")
    f.write(output)
    f.close()
    napalm_con.close()
    print("Checkpoint file created")
