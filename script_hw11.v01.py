import glob
#import os.path
import os
import shutil
import subprocess

def get_files(dir_name): #получить список файлов
	jpg_files = glob.glob(os.path.join(dir_name, "*.jpg"))
	return jpg_files

def copy_files(files, dir_name): #создать директорию назначения, скопировать туда файлы
	destination = os.path.join(dir_name)
	os.mkdir(destination)
	for current_file in files:
		shutil.copy(current_file, destination)

def convert_files(files): #конвертировать файлы внешней командой
	for current_file in files:
		arg = [ "convert", current_file, "-resize", "200", current_file ]
		subprocess.Popen(arg)

copy_files(get_files("Source"), "Destination")
convert_files(get_files("Destination"))