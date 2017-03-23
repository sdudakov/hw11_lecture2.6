import os
import shutil
import subprocess

def get_files(dir_name): #получить список файлов
	jpg_files = os.listdir(os.path.join(dir_name))
	return jpg_files

def convert_files(files, source_dir_name, destination_dir_name): #конвертировать файлы внешней командой
    source_path = os.path.join(source_dir_name)
    destination_path = os.path.join(destination_dir_name)
    os.mkdir(destination_path)
    for current_file in files:
    	source_file = source_path + "/" + current_file
    	destination_file = destination_path + "/" + current_file
    	arg = [ "convert", source_file, "-resize", "200", destination_file ]
    	subprocess.Popen(arg)

convert_files(get_files("Source"), "Source", "Destination")
