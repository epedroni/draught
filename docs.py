# Show help for a particular topic
# if the topic is unknown, show general help
def showHelp(topic):
	if topic == "new":
		print("usage: draught new <type> <title>\n")
		print("Available types:")
		print("\tpost\tcreate a new post in _posts, ready for publishing")
		print("\tdraft\tcreate a new draft in _drafts\n")
		print("<title> is the literal title of the content, not the name of the file")
		
	elif topic == "publish":
		print("usage: draught publish\n")
		print("Displays an indexed list of drafts, type in the index of desired draft and press return to publish it.")
		print("This moves it to the _posts directory and adds today's date as the prefix.")
		
	else:
		print("usage: draught <command> [<args>]\n")
		print("Available commands:")
		print("\tnew\tcreate new content")
		print("\tpublish\tmake drafts available\n")
		print("See 'draught help <command>' for information about commands.")

