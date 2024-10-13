import os

print(os.getcwd())
if os.path.exists('../..'):
    os.chdir('../..')
else:
    os.mkdir('../..')
    os.chdir('../..')
print(os.getcwd())
# os.makedirs(r'second\third')
# for i in os.walk('.'):
#     print(i)
os.chdir(r'/module7')
print(os.getcwd())
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(dirs)
print(file)
print(os.stat(file[0]).st_size)
os.system('cmd')