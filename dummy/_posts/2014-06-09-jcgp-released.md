---
title: "JCGP Released!"
categories: [projects, jcgp]
tags: []
---

After almost six months of intensive work, JCGP is finally released! Not released in the sense that it is finished, oh no; I'm calling it released because I handed it in a few weeks ago. That said, there are many things wrong with it that I intend to fix at some point. I've started tracking issues on Bitbucket, so if anyone is interested in contributing, [have at it](https://bitbucket.org/epedroni/jcgp/issues).

<center><img class="img-responsive" alt="JCGP Interface" src="{{ site.baseurl }}/assets/projects/jcgp/release.png" /></center>

Most of the features I set out to implement are there in some form or another.

* The backend is fully functional and new algorithms can be easily implemented via the modular system.
* Any new parameters registered by algorithms are properly shown in the GUI for user interaction. Monitors are also OK.
* Using the GUI it is possible to look at each gene's connections and entire output paths.
* It is also possible to manipulate the connections by clicking and dragging on them.
* Applying values to the inputs and watching the outputs kind of works, but it's a bit glitchy still.
* It is possible to print things to the GUI console, but it requires a flush for concurrency reasons.

So there we have it! I'm going to take some time off to be as far away from Java as possible, but I know that sooner or later I will end up tinkering with this again. One thing that is particularly bugging me is the GUI chromosome pane. While it does work, the code is not pretty. That's probably what I will tackle next, eventually.

