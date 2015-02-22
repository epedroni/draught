---
title: "i3 Customisation"
categories: [projects, linux]
tags: []
---

Earlier this year I took a leap of faith into the world of Archlinux, and since then I have been very pleased. My computer does break down about once a week because I can't seem to stop messing with it, but fixing it is always fun and I'm slowly learning the ins and outs of Linux. Over the past few months I made many changes to my i3 configuration, and I'll be sharing the most relevant ones in this post.

## Workspaces

It took me about 10 minutes to realise that workspaces are wonderful and Windows should have them, and this is partially the reason why I have sticked with i3. Changing workspace is seamless and quick, unlike desktop environments like Unity which have all sorts of fancy animations. I also prefer the number system rather than a workspace grid; I don't care if my workspaces are stacked horizontally or vertically, if I want workspace 3, I just switch to workspace 3. 

After a while, however, I noticed that I had unconsciously developed a habit. I would always start up Chromium in workspace 1, Eclipse in workspace 2, have a terminal handy in workspace 3 and push DeaDBeeF all the way to workspace 10. I found out that i3 supports any number of arbitrarily named workspaces, so I went ahead and created two new ones: Web and Music. I then used an assign rule to make sure Chromium and DeaDBeeF always start in their respective workspaces.

<center><img class="img-responsive" alt="Custom Workspaces" src="{{ site.baseurl }}/assets/projects/linux-transition/i3-custom-workspaces.png" /></center>

## Dropdown Terminal

I came across a few dropdown terminal ideas for i3, but never paid too much attention until recently, when I decided to implement one myself. The idea is to have a Quake-style terminal that can be shown or hidden with a quick command. I was able to do this with a bit of trial and error by using an exec statement to start a named instance of XTerm when i3 starts, and then a for\_window statement to push XTerm to the scratchpad:

```
for_window [class="XTerm" instance="dropdown"] floating enable, move scratchpad, scratchpad show, move absolute position 178 -20, move scratchpad

exec xterm -name dropdown -g 125x32

bindsym $mod+q [class="XTerm" instance="dropdown"] scratchpad show
```

That last bindsym is the dropdown terminal command, which shows/hides the scratchpad XTerm instance. You might have noticed that the for\_window line is a bit messy, lots of moving things around. The reason for that is because, for some reason, moving windows to the scratchpad overrides their position to be centred on the screen. This only happens the first time it is moved to the scratchpad though, so this for\_window shows it, moves it to the right position, and hides it again afterwards. This nasty hack isn't actually noticeable, but it'll have to stay this way until this issue is addressed in future i3 versions. Here's what it looks like:

<center><img class="img-responsive" alt="Dropdown Terminal" src="{{ site.baseurl }}/assets/projects/linux-transition/i3-dropdown.png" /></center>

## More Keyboard Shortcuts

Keyboard shortcuts are fantastic, and with selective scratchpad show commands, a lot can be achieved. First off though, I set a few commands for quickstarting applications that I used often:

```
bindsym $mod+Shift+n exec chromium

bindsym $mod+Shift+m exec deadbeef

bindsym $mod+Shift+comma exec gedit
```

And incidentally, $mod+n and $mod+m are the bindsyms used for switching to the Web and Music workspaces, which works out nicely. $mod+comma brings GEdit out of the scratchpad, though I prefer not to have GEdit start automatically since I don't use it as often as the dropdown terminal.

I also [found](https://faq.i3wm.org/question/125/how-to-change-the-systems-volume/?answer=1582#post-id-1582) a few nifty one-liners to deal with volume controls:

```
bindsym XF86AudioRaiseVolume exec --no-startup-id pactl set-sink-volume 0 -- +3% && killall -SIGUSR1 i3status

bindsym XF86AudioLowerVolume exec --no-startup-id pactl set-sink-volume 0 -- -3% && killall -SIGUSR1 i3status

bindsym XF86AudioMute exec --no-startup-id pactl set-sink-mute 0 toggle && killall -SIGUSR1 i3status
```

These control the volume of Pulseaudio output 0 and also force i3status to refresh, so I don't have to wait 5 seconds to see the volume change on the screen. 

And finally, screenshots and screen locking:

```
bindsym Print exec scrot ~/screenshots/%Y-%m-%d-%T-screenshot.png

bindsym Pause exec i3lock -i ~/img/lock.png -u -p win
```

There are a few more changes I made, such as mapping the menu key on the right side of the spacebar to Super as well, so I can use shortcuts with my right hand as well, but those aren't exclusive to i3. My .i3/config is available [here]({{ site.baseurl }}/assets/projects/linux-transition/i3-config), so feel free to adapt it or steal it altogether!
