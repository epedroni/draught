---
title: "Media Conversion Script"
categories: [projects, linux]
tags: []
---

Ever since I replaced my laptop's ODD with a 1TB HDD, I've been having trouble figuring out what to do with all the space. I have a sizable music collection, but it is pretty much entirely MP3s at around 256kbps on average. Since I have so much space, I've started going through my favourite albums and slowly ripping them in FLAC.

This of course started causing problems. While DeaDBeeF and pretty much all other open-source media players can handle FLAC out-of-the-box, good old Windows Media Player requires external drivers to be installed. This means that when I want to send one of my songs to my girlfriend, I need to somehow convert it to MP3 first. I initially used online converters, but as an obsessive Linux user, I figured I could do better. Enter the media conversion script.

This is actually my first somewhat serious shell script. I've written scripts to automate long evolutionary experiment runs before, but those never used more idiomatic shell features like if statements. The requirement was simple; I wanted a script that would take one or more FLAC files and output transcoded MP3 files with the same names to an MP3 subdirectory. This is what the initial version looked like:

```
#!/usr/bin/zsh
# Converted files are saved under ./mp3
mkdir -p mp3
echo "Saving converted files to ./mp3/"

# Run all arguments through ffmpeg
for arg in $@
do
	output="./mp3/${arg%.*}.mp3"
	echo "Converting $arg to $output"
	ffmpeg -i "$arg" -b:a 320k "$output" -loglevel warning
done

exit 0
```

This works and has the added bonus that it will try to convert anything into MP3, not just FLAC. Passing incompatible arguments is not a terrible problem since ffmpeg will just output an error message. However, being lazy, I wanted to go one step further and have it so, when run with no arguments, the script attempted to convert all FLAC files in the directory to MP3. Understanding zsh arrays and how to deal with them in scripts took some serious experimentation, googling and assistance from my buddy [Hans](http://hans.viessmann.co/), but here's the final result:

```
#!/usr/bin/env zsh
# Convert one or more files into 320kbps mp3 files.
# One or more files may be specified as arguments. If
# no arguments are specified, the script attempts to
# convert all .flac files in the directory into mp3s.


# Converted files are saved under ./mp3
mkdir -p mp3
echo "Saving converted files to ./mp3/"

# Use flac files as arguments if no arguments are provided
if [ $# -gt 0 ]; then
	args=($@)
else
	args=(./*.flac)
fi


# Run all arguments through ffmpeg
for arg in $args
do
	output="./mp3/${arg%.*}.mp3"
	echo "Converting $arg to $output"
	ffmpeg -i "$arg" -b:a 320k "$output" -loglevel warning
done

exit 0
```

To be perfectly honest, I thought this would be one of those things that I spend a whole day on and then never use again, but I'm happy to say that I have used this script multiple times. It really does come in handy when converting media files for my girlfriend, which is something that I'll likely be doing more and more as my music library gradually fills up with FLAC files. Feel free to take this script and do whatever you want to it, and don't forget the ffmpeg dependency.
