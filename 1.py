from pprint import pprint
from napalm import get_network_driver
from my_devices import cisco3,arista1
from my_functions import create_con

con_list = []

arista = create_con(arista1)
con_list.append(arista)

cisco =  create_con(cisco3)
con_list.append(cisco)

for elem in con_list:
    elem.open()
    print("Platform:")
    print(elem.platform)
    print("Driver:")
    print(elem)
    print("Device facts:")
    pprint(elem.get_facts())
    print("----------------")
    elem.close()

