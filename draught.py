#!/usr/bin/env python3

'''
TODO:
    - manage (groundwork is laid out)
    - archetypes
    - rss
'''
import io
import os
import sys
import shutil
import re
import pkg_resources
import yaml
import manager
from datetime import date

# Recursively cd up until either _config.yml is found or we reach /
def getWebsiteRoot():
    path = str(os.getcwd())
    while path != "/":
        if os.path.isfile("./_config.yml") and not os.path.islink("./_config.yml"):
            return path
        else:
            os.chdir("..")
            path = str(os.getcwd())
    error("this is not a Jekyll website")

# Show a formatted information message
def info(message):
    print("[draught]", message)

# Show a formatted error message and optionally exit
def error(message, exit=True):
    print("[draught] Error:", message)
    if exit:
        sys.exit(1)

# Load help file and print help for the given command, if available
def showHelp(command):
    help = yaml.load(pkg_resources.resource_string(__name__, 'resources/docs.yml'))
    try:
        print(help[command])
    except:
        print(help["default"])

# Asks a y/n question, returns true if y, false if n
def askYN(question):
    print("[draught] " + question, end=" (Y/n) ")
    answer = input().lower()
    
    if answer == "" or answer == "y" or answer == "yes":
        return True
    else:
        return False

# Ensure that a directory exists, return false if it does not
def ensureDir(relativePath):
    fullPath = os.path.join(siteRoot, relativePath)
    if os.path.exists(fullPath):
        return True
    else:
        if askYN("Directory " + relativePath + " has not been found, would you like to create it?"):
            try:
                os.mkdir(fullPath)
                return True
            except:
                return False
        else:
            return False

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
    collections = yaml.load(open(os.path.join(siteRoot, "_config.yml")))["collections"]
    
    if collection in collections:
        makeNewFile("_" + collection, slugify(title) + "." + extension)
    elif collection == "post" or collection == "posts":
        makeNewFile("_posts", slugify(title, addDate=True) + "." + extension)
    elif collection == "draft" or collection == "drafts":
        makeNewFile("_drafts", slugify(title) + "." + extension)
    else:
        error(collection + " is not a valid collection, declared collections are: " + ', '.join([k for k in collections.keys()]))
    
# Create a new file, path is relative to website root
def makeNewFile(relativePath, name):
    if ensureDir(relativePath):
        filePath = os.path.join(siteRoot, relativePath, name)
        if not os.path.exists(filePath):
            open(filePath, 'a').close()
        else:
            error(os.path.join(relativePath, name) + " already exists")
    else:
        error(relativePath + " does not exist, or requires higher permissions")

# Print an indexed list of drafts and prompt user for draft(s) to publish
def publishContent():
    info("These are your drafts:")
    
    for draft in manager.prompt(os.path.join(siteRoot, "_drafts")):
        publishDraft(draft)

# Publish specified draft in the form returned by the manager
def publishDraft(draft):
    oldName = draft[1]
    oldPath = os.path.join(draft[0], oldName)

    newName = addDatePrefix(oldName)
    newPath = os.path.join(siteRoot, "_posts", newName)

    if (os.path.exists(newPath)):
        error("_posts/" + newName + " already exists", exit=False)
    else:
        shutil.move(oldPath, newPath)
        info("Published _drafts/" + oldName + " to _posts/" + newName)

# Sort through sys.argv, print error messages if anything bad happens
def parseArguments():
    command = ""
    try:
        # now parse arguments
        command = sys.argv[1]
        if command == "new" or command == "n":
            createNewContent(sys.argv[2], sys.argv[3])
        elif command == "publish" or command == "p":
            publishContent()
        elif command == "help" or command == "h":
            if len(sys.argv) > 2:
                showHelp(sys.argv[2]);
            else:
                showHelp("help")
        else:
            info("unknown command: \'" + sys.argv[1] + "\'")
            showHelp("default")
    except IndexError:
        error("arguments missing", exit=False)
        showHelp(command)

# The entry point
if __name__ == "__main__":
    # first off, check if cwd is a jekyll (sub-)directory
    siteRoot = getWebsiteRoot()
    parseArguments()
        
