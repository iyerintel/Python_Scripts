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


