#!/usr/bin/python

import re, os, commands, re

def ExecuteCmd(str):
	status, result = commands.getstatusoutput(str)
	if status != 0:
		print "Error executing: " + str
		sys.exit(1)
	else:
		return result

tokens = os.getcwd().split("/")
project_name = tokens[-1]
print "project_name: " + project_name

base_nbproject = "/home/johnnyj/nbproject"

#Change the project name in all the other files to the new project name.
ExecuteCmd("cp -r " + base_nbproject + " . ")
ExecuteCmd("find ./nbproject/ -type f -exec sed -i \"s/move-semantics/" + project_name + "/g\" {} +")
ExecuteCmd("find ./nbproject/ -name \"project.xml\" -exec sed -i \"s/Move-Semantics/" + project_name + "/g\" {} +")

cpp_files = ExecuteCmd("ls *.cpp").split()
header_files = ExecuteCmd("ls *.h").split()

new_nbproject = os.path.join(os.getcwd(), "nbproject")
config_file = open(os.path.join(new_nbproject, "configurations.xml"), "r")
new_config = []
s = ""
for line in config_file:
	new_config.append(line)
	m = re.match(".*logicalFolder.*HeaderFiles.*", line)
	if m:
		for h in header_files:
			new_config.append("        <itemPath>"+ h + "</itemPath>\n")
	m = re.match(".*logicalFolder.*SourceFiles.*",line)
	if m:
		for c in cpp_files:
			new_config.append("        <itemPath>"+ c + "</itemPath>\n")
	m = re.match(".*</compileType>.*", line)
	if m:
		for c in cpp_files:
			new_config.append("        <item path=\"" + c + "\" ex=\"false\" tool=\"1\" flavor2=\"0\">        </item>\n")
		for h in header_files:
			new_config.append("        <item path=\"" + h + "\" ex=\"false\" tool=\"3\" flavor2=\"0\">        </item>\n")

config_file.close()
f = open(os.path.join(new_nbproject, "configurations.xml"), "w")
for e in new_config:
	f.write(e)
			



