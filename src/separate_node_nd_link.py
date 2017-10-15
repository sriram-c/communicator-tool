#Programme to separate node and link dmrs
#Written by Roja(21-09-16)

import sys

fnode = open('node_f' , 'w')
flink = open('link_f' , 'w')

for line in open(sys.argv[1]):
	if '<node cfrom' in line:
		fnode.write(line)
	elif '<node carg' in line:
		fnode.write(line)
	else:
		flink.write(line)
fnode.close()
flink.close()


#print dmrs info:
fn = open('node_f', 'r')
fl = open('link_f', 'r')

print '<dmrs cfrom="-1" cto="1">'
print fn.read(),
print fl.read()
print '</dmrs>'
