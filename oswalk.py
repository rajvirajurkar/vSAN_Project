import os

'''os.walk(dir_name) ==> walk through filesystem files, directory 
os.system(command) ==> running os command through python'''

dir_name = '/Users/rrajurkar/documents/vSAN'
for root_dir, base_dir, files in os.walk(dir_name):
	print ("Root dir: ", root_dir)
	print("base dir : ", base_dir)
	print ("Files :", files)
	print ("==========\n")