import sys
import re
import os

filename = os.path.expanduser('~') + '/3k/TinTin/Data/3k.map'
target_string = open(filename, 'r').read()
pattern = re.compile( r"R\s+{\s?([0123456789]+)}.*" + str(sys.argv[1]) + ".*")
result = re.findall(pattern, target_string);

for (vnum) in result:
	print ("displayroom " + vnum)

