---
title: "Config File Backup Script"
categories: [projects, linux]
tags: []
---

As I've mentioned before, I have been quite interested in scripting recently. I played around with [shell scripts](/projects/linux/2014/11/media-conversion-script) a little, but I find that they are a bit clumsy, at least for inexperienced users like me. I have wanted to learn Python for a while now, but I find tutorials a bit boring. I prefer to pick up languages by applying them to actual problems, and a few days ago I thought of a good one to tackle.

As a Linux user I am constantly messing with plain-text config files, which are scattered throughout my home directory. I realised that if something were to happen to my computer forcing me to reinstall, I would lose all of my hard-tweaked settings. Not a happy prospect, and since I have backups of all my projects and media, why not config files as well? Since config files are usually quite small, I thought it appropriate to create a git repository and push any changes upstream. If I ever reinstall, all I need to do is clone the repository and move the files back to their respective locations. The idea of manually gathering so many files into the same directory and then manually restoring them did not please me, however. If a script can do it for me, then a script *will* do it for me.

## Making Backups

Faced with a problem and armed with the tools to solve it, I set about designing the solution. What I wanted was a simple Python script that would create the backups with little intervention from my part. The way to accomplish that was to create a list of files to back up, and let the script work through those. The list is stored in plain-text format and simply contains the path to each file separated by line breaks. I wrote a Python function that reads the list and treats each line as a new file to copy to the backup location:

```
import os
import shutil

backupDir = os.path.join(os.path.expanduser('~'), '.cfgbk')
fileList = os.path.join(backupDir, 'files')

def makeBackups():
    
	files = open(fileList, 'r')

	for index, file in enumerate(files):
		source = os.path.expanduser(file.rstrip())
	
		if os.path.isfile(source) and not os.path.islink(source):
			name = str(index) + '-' + os.path.basename(source)
			print('[cfgbk] Copying ' + source + ' as ' + name)
			shutil.copy2(source, os.path.join(backupDir, name))
	
		elif os.path.isdir(source) and not os.path.islink(source):
			if source[-1] == '/':
				source = source.rstrip('/')
			name = str(index) + '-' +source.split('/')[-1]
			print('[cfgbk] Copying ' + source + ' as ' + name)
			shutil.copytree(source, os.path.join(backupDir, name), symlinks=False, ignore_dangling_symlinks=True)
	
	files.close()
```

Some config files are called "config" and contained in a separated directory, such as "~/.i3/config", meaning I had to devise a system to allow identically-named files to be copied. I decided to simply add the index of the file to the backup's name. In the interest of flexibility, I also added support for backing up entire directories. The standard modules `os` and `shutil` came in handy at this stage, allowing me to easily manipulate paths and copy files.

## Deleting Backups

I then thought of a problem with this script. If I ever remove an entry from the list, the backed up file will no longer be overwritten by this function, but it won't be removed either. In order to make sure that the files in "~/.cfgbk" are only ever the ones I want to have backed up, I implemented a function which removes all currently backed up files:

```
def clearBackups():
	for root, dirs, files in os.walk(backupDir):
		for f in files:
			if re.match('^[0-9]+-', f):
				os.unlink(os.path.join(root, f))
				print('[cfgbk] Removing ' + os.path.join(root, f))
		for d in dirs:
			if re.match('^[0-9]+-', d):
				shutil.rmtree(os.path.join(root, d))
				print('[cfgbk] Removing ' + os.path.join(root, d))
	return
```

Using regular expressions I can make sure to only remove files numbered in the specific way I number them when backing up. This is a rather crude solution that I hope to improve in the future, but it is one safe as long as nothing that matches "^[0-9]+-" is placed in the backup directory.

## Adding Files

The script is ready to be used, but as a lazy Linux user, I don't want to open the file list and manually add a file path every time I want to have a new file backed up. Instead, I added to the script a function which does it for me:

```
def addFiles(newfiles):
	files = open(fileList, 'a')
	
	for file in newfiles:
		path = os.path.abspath(str(file))
		print('[cfgbk] Adding file: ' + path)
		files.write(path + '\n')
	
	files.close()
	return
```

It works with any number of arguments, which allows me to add many files at once. The only thing that is missing is a way to select the desired function. I did this using the `argparse` module. Figuring out how to use it was a bit confusing, and I'm not sure I've done it right, but it seems to work:

```
if __name__ == "__main__":

	# Define and parse arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('mode', choices=['clear', 'c', 'backup', 'b', 'add', 'a'], help='define what mode to execute in')
	parser.add_argument('files', nargs='*', help='when using cfgbk add, one or more files should be provided')

	args = parser.parse_args()

	# Act depending on mode selected	
	if args.mode == 'backup' or args.mode == 'b':
		makeBackups()
	elif args.mode == 'clear' or args.mode == 'c':
		clearBackups()
	elif args.mode == 'add' or args.mode == 'a':
		addFiles(args.files)
```

The script works, though it is a bit unstable. I hope to add some error-checking and other defensive measures in the future, though for now it takes care of my immediate backup needs. I've created a repository for it on Github: <https://github.com/epedroni/cfgbk>.
