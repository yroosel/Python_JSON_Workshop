### 2 #### FUNCTIONS TO CREATE (A) list of devices and (B) list of device interfaces
### Using an excel file as input for a Python script
### This script creates a JSON structure based on information an excel spreadsheet
### You have to understand Python dict and Python lists
### Contact yvan.rooseleer@biasc.be if you have questions
### It's up to you to ### WRITE YOUR OWN CODE ### where this is indicated
### Validate your JSON structure
### Use print statements to understand return values and return types
### There is a simplified solution (main2) and a more difficult solution (main)
###
import xlrd
import json
###
### RULES
inventory_dict         = {}  #### {"interface": "gi0/1", "ip_address": "1.2.2.1", "subnet_mask": "255.255.255.0", "device": "dv"
inventory_list         = []  #### [inventory_dict]  
interface_dict         = {}  #### {"interface": "gi0/1", "ip_address": "1.2.2.1", "subnet_mask": "255.255.255.0"}
interface_list         = []  #### [interface_dict]    
dev_dict               = {}  #### {"device": {dev_name": "n", "role": "r", interfaces": interface_list}}
dev_list               = []  #### [dev_dict]  
rack_struc             = {}  #### {dev_dict_list}
rack_struc["rack"]     = []
####

def find_all_device_interfaces(xlf):
    ### READ EXCEL FILE AND RETURN NUMBER OF ROWS
    wb = xlrd.open_workbook(xlf)
    sheet = wb.sheet_by_index(0)
    number_rows = sheet.nrows
    dev_interfaces = []
    for r in range(number_rows):
        if r > 0: ### first row contains columns names
            COL_A =  sheet.cell_value(r, 0)  #### column A
            COL_B =  sheet.cell_value(r, 1)  #### column B
            COL_C =  sheet.cell_value(r, 2)  #### column C
            COL_D =  sheet.cell_value(r, 3)  #### column D
            COL_E =  sheet.cell_value(r, 4)  #### column E
            inventory_dict["device"]      = COL_A
            inventory_dict["role"]        = COL_B
            inventory_dict["interface"]   = COL_C 
            inventory_dict["ipaddress"]   = COL_D
            inventory_dict["subnetmask"]  = COL_E
            dev_interfaces.append(inventory_dict.copy()) # need to use copy()
    return dev_interfaces

def make_list_of_devices_and_roles(inventory):  
    dev_list  = []
    dev_dict  = {}
    mem       = {}
    for rec in inventory:
        dev_dict["dev_name"] = rec["device"]
        dev_dict["role"]     = rec["role"]
        if mem != dev_dict["dev_name"]:
            dev_list.append(dev_dict.copy())  # need to use copy()
        mem = dev_dict["dev_name"]
    #for rec in loc_g:    
        #print(rec)
    #del loc_g[0] ### if last item copied as first item
    return dev_list

def make_list_of_devices(inv_list): 
    dev_list = []
    mem = None
    for rec in inv_list:
        dev_name = rec["device"]
        if mem != dev:
            dev_list.append(dev_name)
        mem = dev_name
    return dev_list

def attach_interfaces_to_devices(dev_name, inventory):    
    intf_dict = {}
    intf_list = [intf_dict]
    for item in inventory:
        if item["device"] == dev_name:
            if item["device"] != None:
                intf_dict["interface"]   = item["interface"]
                intf_dict["ipaddress"]   = item["ipaddress"]
                intf_dict["subnetmask"]  = item["subnetmask"]
                intf_list.append(intf_dict.copy()) # need to use copy()
    del intf_list[0] ### if last item copied as first item
    return intf_list
        
#### MAIN ####   
def main2(): ### no role for devices, only device name
    inventory_list = find_all_device_interfaces("devices_ip.xlsx")
    dev_list       = make_list_of_devices(inventory_list)  
    for device_rec in dev_list:
        intf_list  = attach_interfaces_to_devices(device_rec, inventory_list)
        dev_dict["device"] = { "device": {"dev_name": device_rec , "interfaces": intf_list }} 
        rack_struc["rack"].append(dev_dict["device"])
    js_rack = json.dumps(rack_struc)

def main(): ### role added 
    inventory_list = find_all_device_interfaces("devices_ip.xlsx")
    device_list    = make_list_of_devices_and_roles(inventory_list)      
    for device_rec in device_list:  
        intf_list  = attach_interfaces_to_devices(device_rec["dev_name"], inventory_list)
        dev_dict["device"] = { "device": device_rec , "interfaces": intf_list }
        rack_struc["rack"].append(dev_dict["device"])
    js_rack = json.dumps(rack_struc)

#### execute main() when called directly        
if __name__ == '__main__':
    main()  ### alternative: main2()
