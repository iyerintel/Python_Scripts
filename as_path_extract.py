#!/usr/bin/env python
'''
Using the below "show ip bgp" data, the split function is used to output the IP prefix associated with the neighbor and 
the respective AS path.
'''

entry_1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry_2 = "*  1.1.1.0/24      157.130.10.233         0 701 1299 15169 i"
entry_3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry_4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

for entry in (entry_1, entry_2, entry_3, entry_4):
    entry_split = entry.split()
    ip_prefix = entry_split[1]
    as_path = entry_split[4:-1]
    print "%s %s" % (ip_prefix, as_path)

print "\n"
