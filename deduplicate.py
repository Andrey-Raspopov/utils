import shutil
import sys

fn = sys.argv[1]
shutil.copyfile(fn,f'{fn}.bak')
ifile = open(f'{fn}.bak')
ofile = open(fn, 'w')


data = ifile.read().split('\n')
ifile.close()
data = list(set(data))
data.sort()
ofile.write('\n'.join(data))
ofile.close()
