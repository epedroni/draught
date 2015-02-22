---
title: "Draught"
proj_id: "draught"
proj_page: "https://github.com/epedroni/draught"
permalink: /projects/draught/
date: "December 2014"
---

## Description

Draught is an idea for a project that I had recently and hope to execute in the near future. Simply put, it would be a [Jekyll](http://jekyllrb.com/) website manager. Before moving on to Jekyll I tried using [Hugo](http://gohugo.io/), and one of the things I liked about it (that is missing in Jekyll) was the ability to create new content by typing `hugo new <filename>` directly into the terminal. This command would not only create the file in the right directory, but also optionally add some user-defined front matter to it (called an archetype) automatically.

I recently wrote a simple shell script to do something like that:

```
#!/usr/bin/env zsh
# Create a new post for my jekyll blog.
# This script takes one or two arguments:
#   - given a single argument, it creates a suitable .md file
#     in _posts with a basic front matter, including the title.
#   - given two arguments, it uses the second argument as a
#     a project name and attempts to create a post with the
#     correct categories for that project.

if [ -d _posts ]; then
	if [ $# -gt 0 ]; then
		validtitle=${1:gs/ /-/}
		filename="_posts/`date +%Y-%m-%d`-$validtitle.md"
		if [ $# -gt 1 ]; then
			proj_id=${2:gs/ /-/}
			cats="projects, $proj_id"
		fi 
		echo "---\ntitle: \"$1\"\ncategories: [$cats]\ntags: []\n---\n" >> $filename
		nano +6 $filename
	else
		echo "Please specify a title and optionally a project name."
	fi
else
	echo "Directory _posts not found, is this a jekyll website?"
fi
```

Needless to say this is a rather simple script, but it gave me the idea to a write a full-fledged CLI website management tool. Shell scripting would naturally not be appropriate for a more sophisticated project, so I hope to develop Draught in Python.


## Specifications

My intention is to implement functionality such as:

* Creating new posts including user-defined front matter;
* Showing a list of posts, optionally sorted by category, year, etc;
* Managing existing posts, i.e. deleting, editing;
* Support for drafting, i.e. create a draft and make it public later with a single command;
* Ideally proper integration with Jekyll's collections feature.

This isn't a formal list of specifications as I've only just started the project, but I will update it as it develops. It is hosted on Bitbucket and will be free and open-source from the get-go, and I hope to have it somewhat stable and functional soon as it will help me with this website as well.
