import os

log = r""

flog = open(log,'w')
path = r''
file_map = {}
for folder,subfolder,files in os.walk(path):
	for f in files:
		fp = os.path.join(folder,f)
		# print fp
		# flog.write(fp+'\n')
		if os.path.isfile(fp) and os.path.getsize(fp)>2097152:
			file_map[fp] = {'fname':f, 'size':os.path.getsize(fp)}
similar_files = {}
fp = file_map
for f in fp:
	if not similar_files.get(fp[f]['fname']+str(fp[f]['size']), None):
		similar_files[fp[f]['fname']+str(fp[f]['size'])] = []
	similar_files[fp[f]['fname']+str(fp[f]['size'])].append(f)
for f in similar_files:
	if len(similar_files[f])>1:
		flog.write(f+'\n')
		print f
		flog.write('-'*len(f)+'\n')
		print '-'*len(f)
		for fi in similar_files[f]:
			flog.write(fi+'\n')
			print fi
		flog.write('\n')
	# print
flog.close()

