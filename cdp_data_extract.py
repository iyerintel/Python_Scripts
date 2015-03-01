#!/usr/bin/env python

'''
opens the 'r1_cdp.txt' file and using regular
expressions extracts the remote hostname, remote IP address, model, vendor, 
and device_type.
'''

import re
from pprint import pprint


def cdp_parse(pattern, cdp_data):
    '''
    Search for pattern in the cdp_data
    Return relevant .group(1) 
    Else return ''
    '''
 
    # Break the CDP data up into its individual lines
    cdp_data = cdp_data.split('\n')

    for data in cdp_data:
        # Search for pattern
        pattern = re.search(pattern, data)

        # Return match if found
        if pattern:
            return_val = pattern.group(1)
            return return_val.strip()

    return ''


# Technique to allow importable and executable code to coexist (will explain in class#8)
if __name__ == '__main__':
    
    cdp_file = 'r1_cdp.txt'
    f = open(cdp_file)
    
    # Read cdp_data into a list
    cdp_data = f.read()
    f.close()

    net_dev = {}

    net_dev['remote_hostname'] = cdp_parse(r'Device ID: (.+)', cdp_data)
    net_dev['ip'] = cdp_parse(r'IP address: (.+)', cdp_data)
    net_dev['vendor'] = cdp_parse(r'^Platform: (.+?) ', cdp_data)
    net_dev['model'] = cdp_parse(r'^Platform: \w+ (.+),', cdp_data)
    net_dev['device_type'] = cdp_parse(r'^Platform: .+Capabilities: (.+?) ', cdp_data)


    print
    pprint(net_dev)
    print


'''
 a program that opens the 'sw1_cdp.txt' file and finds all of the remote
hostnames, remote IP addresses, and remote platforms. output should look 
similar to the following:
 remote_hosts: ['R1', 'R2', 'R3', 'R4', 'R5']
          IPs: ['10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.4', '10.1.1.5']
     platform: ['Cisco 881', 'Cisco 881', 'Cisco 881', 'Cisco 881', 'Cisco 881']
'''


f = open("sw1_cdp.txt")
cdp_data = f.read()
f.close()

dict = {}

dict['remote_hosts'] = re.findall(r"Device ID: (.+)", cdp_data)
dict['IPs'] = re.findall(r"IP address: (.+)", cdp_data)
dict['platform'] = re.findall(r"Platform: (.+?),", cdp_data)


# Print output
print 
ordered_var = ('remote_hosts', 'IPs', 'platform')
for k in ordered_var:
    print "%15s: %-20s" % (k, dict[k])

print 
