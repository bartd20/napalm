from pprint import pprint
from napalm import get_network_driver
from my_devices import cisco3,arista1
from my_functions import create_con,create_backup

con_list = []

arista = create_con(arista1)
con_list.append(arista)

cisco =  create_con(cisco3)
con_list.append(cisco)

for elem in con_list:
    elem.open()
    print("Platform: "+elem.platform)
    print("Arp table:")
    pprint(elem.get_arp_table())
    print("----------")
    elem.close()

for elem in con_list:
    elem.open()
    print("Platform: "+elem.platform)
    print("NTP peers:")
    try:
        print(elem.get_ntp_peers())
    except Exception:
        print("Error")
    print("-----------")
    elem.close()

create_backup(cisco)
create_backup(arista)
