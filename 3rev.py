from pprint import pprint
from napalm import get_network_driver
from my_devices import cisco3,arista1
from my_functions import create_con,create_backup


arista = create_con(arista1)
cisco =  create_con(cisco3)

arista.open()
print("Load the change")
arista.load_merge_candidate(filename="arista1.lasthop.io-loopbacks-remove")
print("Show config diff:")
print(arista.compare_config())
print("Apply the change")
arista.commit_config()
print("Config saved")
arista.close()

cisco.open()
print("Load the change")
cisco.load_merge_candidate(filename="cisco3.lasthop.io-loopbacks-remove")
print("Show config diff:")
print(cisco.compare_config())
print("Apply the change")
cisco.commit_config()
print("Config saved")
cisco.close()

