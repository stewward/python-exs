from sys import argv 
from os.path import exists #operating system = os.path

script, from_file, to_file = argv 

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Does the outpout file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata) #indata is whatever we had in our infile. 

print("Alright, all done!")
out_file.close()
in_file.close()