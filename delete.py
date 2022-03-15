import os
import shutil
import time



deleted_folders_count = 0
deleted_files_count = 0
path = input("Enter the folder path:-")
days = 30
sec=time.time()-(24*60*60*30)
if os.path.exists(path):
	for file in os.listdir(path):
		path1=path+"/"+file
		ctime = os.stat(path1).st_ctime
		if sec >= ctime:
			if not os.remove(path1):

				print(f"{path} is removed successfully")

			else:

				print("Unable to delete the "+path1)
else:
	print("wrong")				

		
	
  

	
	