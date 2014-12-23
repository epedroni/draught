---
title: "Window Manager: i3-wm"
categories: [projects, linux]
tags: []
---

One of the first things I did after I installed Arch about a month ago was install X.org and look into user interfaces. I had never used a system with only a window manager and no desktop environment, but seeing as window managers are much more lightweight, I decided to give it a try. I looked through the supported window managers on the ArchWiki and came across i3, which struck me as a good option:

> i3 — Tiling window manager, completely written from scratch. i3 was created because wmii, our favorite window manager at the time, did not provide some features we wanted (multi-monitor done right, for example) had some bugs, did not progress since quite some time and was not easy to hack at all (source code comments/documentation completely lacking). Notable differences are in the areas of multi-monitor support and the tree metaphor. For speed the Plan 9 interface of wmii is not implemented.

So I did a sudo pacman -S i3, set up my .xinitrc, and this is what I got:

<center><img class="img-responsive" alt="Vanilla i3" src="{{ site.baseurl }}/assets/projects/linux-transition/i3-wm-1.png" /></center>

Not bad, but not quite good either. I wasn't too pleased with the status bar, I felt it showed some things I wasn't interested in and omitted things I wanted to see. So I made some changes:

<center><img class="img-responsive" alt="Improved Status" src="{{ site.baseurl }}/assets/projects/linux-transition/i3-wm-2.png" /></center>

In short: rearranged the date, added a CST timezone clock and processor temperature, removed RAM usage and some network information, compacted the battery display slightly, and added disk usage for my two data partitions. Next, the colour scheme. The status bar is pretty much fixed, unless I write a custom script to output the information, so I decided to leave that as it is for now. I did play around with the window colours, however:

<center><img class="img-responsive" alt="Colour Scheme" src="{{ site.baseurl }}/assets/projects/linux-transition/i3-wm-3.png" /></center>

I also chose a different system font, DejaVu Sans, and made the status bar text a little smaller. 

In general, I am quite pleased with i3. I used the Aero Snap feature on Windows quite a bit, and having a window manager which does it seamlessly with quick keyboard shortcuts is very nice. Performance-wise i3 is very snappy, which makes a big difference for me when it comes to productivity. It's nice having a window manager that doesn't get in the way and lets me have things the way I want them. I have some more tweaks in mind, taking advantage of the keybinding and scratchpad functionalities provided. I'll post those here when they're all set up.
