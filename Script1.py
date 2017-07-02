import os

log = r"C:\Users\Admin\Desktop\Flog.txt"

flog = open(log,'w')
path = r'c:\\'
file_map = {}
for folder,subfolder,files in os.walk(path):
	for f in files:
		fp = os.path.join(folder,f)
		# print fp
		# flog.write(fp+'\n')
		if os.path.isfile(fp):
			file_map[fp] = {'fname':f, 'size':os.path.getsize(fp)}
similar_files = {}
fp = file_map
for f in fp:
	if not similar_files.get(fp[f]['fname']+str(fp[f]['size']), None):
		similar_files[fp[f]['fname']+str(fp[f]['size'])] = []
	similar_files[fp[f]['fname']+str(fp[f]['size'])].append(f)
for f in similar_files:
	flog.write(f+'\n')
	print f
	flog.write('-'*len(f)+'\n')
	print '-'*len(f)
	if len(similar_files[f])>1:
		for fi in similar_files[f]:
			flog.write(fi+'\n')
			print fi
	# print
	flog.write('\n')
flog.close()

