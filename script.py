import glob
import json
import os

v = "var char_data = "

list_json = glob.glob('hanzi-writer-data/./*.json')

for l in list_json:
	name = os.path.basename(l)
	new_name = name.replace("on", "")
	print(new_name)
	with open(l) as f:
		d = json.load(f)
		k = json.dumps(d)
		c = v + k
		print(c)
		file_write = "char_data_js/"
		f_path = os.path.join(file_write, new_name)
		f1 = open(f_path, "w")
		f1.write(c)
		f1.close()