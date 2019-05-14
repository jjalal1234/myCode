#!/usr/bin/env python3

switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

print(switch['hostname'])
print(switch['ip'])
#print(switch['lynx'])
print("Frist test - .get()")
print(switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!")

