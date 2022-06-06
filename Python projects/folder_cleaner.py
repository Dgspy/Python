import os

def createfolder(folder):
	if not os.path.exists(folder):
		os.makedirs(folder)

def move(foldername, files):
	for file in files:
		os.replace(file, f"(foldername)/(file)")

files = os.listdir()
files.remove('folder_cleaner.py')
print(files)

createfolder('Images')
createfolder('Docs')
createfolder('Media')

imgExts = ['png','jpg','jpeg','img']
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

docsExts = ['docs','pdf','exe','txt']
docs = [file for file in files if os.path.splitext(file)[1].lower() in docsExts]

mediaExts = ['mp3','mp4','ogg','fiv']
media = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

others = []
for file in files:
	exts = os.path.splitext(file)[1].lower()
	if (exts not in mediaExts) and (exts not in docsExts) and (exts not in imgExts) and os.path.isfile(file):
		others.append(file)	
print(others)	
move('Images',images)
move('Docs',docs)
move('Media',media)
move('others',others)