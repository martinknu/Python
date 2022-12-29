
import os

#Environment variables
#print(os.environ)

#OS name
print(os.uname())

#List directories in cwd
print(os.listdir("."))


#Make directory
os.mkdir("mynewdir2", mode=0o777, dir_fd=None)

# os.makedirs(name, mode=0o777, exist_ok=False)

print(os.times())



print(os.cpu_count())
print(os.sysconf_names)
print(os.curdir)
print(os.getrandom(1, flags=0))
print()
print()
print()
print()