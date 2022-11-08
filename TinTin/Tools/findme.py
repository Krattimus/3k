import sys
import re

target_string = open('3k/TinTin/Data/3k.map', 'r').read()
pattern = re.compile( r"R\s+{\s+([0123456789]+)}.*" + str(sys.argv[1]) + ".*")
result = re.findall(pattern, target_string);

for (vnum) in result:
	print ("displayroom " + vnum)

