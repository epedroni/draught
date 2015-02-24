#!/usr/bin/env python3

'''
TODO:
        - manage (groundwork is laid out)
        - sitemap generator
        - archetypes
'''
import os, sys, shutil, re, manager, yaml
from datetime import date

class DraughtException(Exception):
        def __init__(self, reason, showHelp=False):
                self.reason = reason
                self.showHelp = showHelp

# Load help file and print help for the given command, if available
def showHelp(command):
        help = yaml.load(open(os.path.join(sys.path[0], "docs.yml"), 'r'))
        try:
                print(help[command])
        except:
                print(help["default"])

# Recursively cd up until either _config.yml is found or we reach /
def getWebsiteRoot():
        path = str(os.getcwd())
        while path != "/":
                if os.path.isfile("./_config.yml") and not os.path.islink("./_config.yml"):
                        return path
                else:
                        os.chdir("..")
                        path = str(os.getcwd())
        raise DraughtException("this is not a Jekyll website")

# Asks a y/n question, returns true if y, false if n
def askYN(question):
        print("[draught] " + question, end=" (Y/n) ")
        answer = input().lower()
        
        if answer == "" or answer == "y" or answer == "yes":
                return True
        else:
                return False

# Ensure that a directory exists, return false if it does not
def ensureDir(path):
        fullPath = os.path.join(siteRoot, path)
        if not os.path.exists(fullPath):
                if askYN("Directory " + path + " has not been found, would you like to create it?"):
                        try:
                                os.mkdir(fullPath)
                                return True
                        except:
                                return False
                else:
                        return False
        else:
                return True

# Add the Jekyll date prefix in proper slugified format
def addDatePrefix(string):
        return date.isoformat(date.today()) + "-" + string

# Condition strings for URLs
def slugify(string, addDate=False):
        slug = string.lower()
        slug = re.sub("[^(a-z0-9)]+", "-", slug).strip("-")
        if addDate:
                slug = addDatePrefix(slug)
        return slug

# Determine content type and create it
def createNewContent(collection, title, extension="md"):
        # first check if the given collection is explicitly defined in _config.yml
        config = yaml.load(open(os.path.join(siteRoot, "_config.yml")))
        
        if collection in config["collections"]:
                makeNewFile("_" + collection, slugify(title) + "." + extension)
        elif collection == "post" or collection == "posts":
                makeNewFile("_posts", slugify(title, addDate=True) + "." + extension)
                
        elif collection == "draft" or collection == "drafts":
                makeNewFile("_drafts", slugify(title) + "." + extension)
        else:
                raise DraughtException(collection + " is not a valid collection, declared collections are: " + ', '.join([k for k in config["collections"].keys()]))
        
# Create a new file, path is relative to website root
def makeNewFile(relativePath, name):
        if ensureDir(relativePath):
                filePath = os.path.join(siteRoot, relativePath, name)
                if not os.path.exists(filePath):
                        open(filePath, 'a').close()
                else:
                        raise DraughtException(os.path.join(relativePath, name) + " already exists")
        else:
                raise DraughtException(relativePath + " does not exist, or requires higher permissions")

def publishContent():
        drafts = manager.Manager(os.path.join(siteRoot, "_drafts")).getContents()
        if len(drafts) > 0:
                print("[draught] These are your drafts:")
                for index, item in enumerate(drafts):
                        print("\t", index, ":", item[0])
                print("[draught] What would you like to publish? ", end="")
                publish = input()
                if re.search("[^0-9]", publish) == None:
                        publish = int(publish)
                        if publish < len(drafts):
                                oldName = drafts[publish][0]
                                oldPath = os.path.join(drafts[publish][1], oldName)
                                
                                newName = addDatePrefix(oldName)
                                newPath = os.path.join(siteRoot, "_posts", newName)
                                
                                if (os.path.exists(newPath)):
                                        raise DraughtException("_posts/" + newName + " already exists")
                                else:
                                        shutil.move(oldPath, newPath)
                                        print("[draught] Published _drafts/" + oldName + " to _posts/" + newName)
                        else:
                                raise DraughtException(str(publish) + " does not correspond to a draft")
                else:
                        raise DraughtException("please input a number relative to a draft")
        else:
                print("[draught] You have no drafts to publish")

# The entry point
if __name__ == "__main__":
        # first off, check if cwd is in a jekyll directory
        try:
                siteRoot = getWebsiteRoot()
        
                # now parse arguments
                command = ""
                command = sys.argv[1]
                if command == "new":
                        createNewContent(sys.argv[2], sys.argv[3])
                elif command == "publish":
                        publishContent()
                elif command == "help":
                        if len(sys.argv) > 2:
                                showHelp(sys.argv[2]);
                        else:
                                showHelp("help")
                else:
                        raise DraughtException("unknown command \'" + sys.argv[1] + "\'", showHelp=True)
        except IndexError:
                print("[draught] Error: arguments missing")
                showHelp(command)
        except DraughtException as e:
                print("[draught] Error:", e.reason)
                if e.showHelp:
                        showHelp(command)
                        

