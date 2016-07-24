#!/usr/bin/python

import re, os, sys, commands

if len(sys.argv) != 2:
	print "Error"
	sys.exit(1)

cwd = os.getcwd()
cpp = os.path.join(os.getcwd(), sys.argv[1].lower() + ".cpp")
cpp_file = open(cpp, "w")

cpp_file.write("#include \"" + sys.argv[1].lower() + ".h\"\n")
cpp_file.write("\n")
for x in range(4,0,-1):
	cpp_file.write("static void TestCase" + str(x) + "()\n")
	cpp_file.write("{\n\n")
	cpp_file.write("}\n\n")

cpp_file.write("void " + sys.argv[1] + "::Run()\n")
cpp_file.write("{\n")
for x in range(1,5):
	cpp_file.write("    TestCase" + str(x) + "();\n")
cpp_file.write("}")
cpp_file.close()

h = os.path.join(os.getcwd(), sys.argv[1].lower() + ".h")
h_file = open(h, "w")
h_file.write("#ifndef " + sys.argv[1].upper() + "_H\n")
h_file.write("#define " + sys.argv[1].upper() + "_H\n")
h_file.write("\n")
h_file.write("#include \"question.h\"\n")
for x in range(0,3):
	h_file.write("\n")
h_file.write("class " + sys.argv[1] + " : public Question\n")
h_file.write("{\n")
h_file.write("public:\n")
h_file.write("    virtual void Run();\n")
h_file.write("};\n")
h_file.write("\n")
h_file.write("#endif")
h_file.close()
