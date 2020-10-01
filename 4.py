from pprint import pprint
from napalm import get_network_driver
from my_devices import nxos1
from my_functions import create_con,create_checkpoint
 
nxos1_con = create_con(nxos1)

create_checkpoint(nxos1_con)

print("Open connection")
nxos1_con.open()
print("Load the change:")
nxos1_con.load_replace_candidate(filename="nxos1.conf.new")
print("Config diff:")
print(nxos1_con.compare_config())
print("Discard the change")
nxos1_con.discard_config()
print("Config diff:")
print(nxos1_con.compare_config())
print("Close connection")
nxos1_con.close()
