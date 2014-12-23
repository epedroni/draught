---
title: "Sonification Interface"
proj_id: "sonification"
ongoing: false
permalink: /projects/sonification/
date: "October to December 2012"
---
## Background

Sonification is the process of displaying information in sound form rather than visually. Displaying might be the wrong word; there is, in fact, no correct word. If there *was*, it would be "to sonify". However:

<center><figure class="copyright-caption"><img class="img-responsive" alt="Nope." src="{{ site.baseurl }}/assets/projects/sonification/sonify_dict.png" />&copy; dictionary.com</figure></center>

It doesn't seem to be a word just yet. The reason for this, arguably, is that people just prefer seeing their data rather than hearing it. I was certainly taught to read charts and graphs in school. Well, as it turns out, there are those out there who have wondered if hearing data might present advantages over seeing it, and they are trying to find out by doing just that: sonifying their data.

Sonification can be done in many ways. Consider graphing a large dataset; in order to display the entire set in graph form one must sacrifice resolution, so smaller "bumps" would no longer be visible. An alternative solution involving sound would be to treat each data point, given appropriate scaling, as a sample. It would then be possible to *hear* the data, and since high quality sound files are usually sampled at 44.1kHz, that would mean going through 44,100 data points in one second.

But is it actually useful? Is hearing data an eye (ear?) opening experience? In second year, I had the opportunity to implement my very own sonification interface to find out! 

## Tweet Applifier

We were free to choose a dataset and sonify it, so I managed to get some Twitter data using an analytics API (<http://otter.topsy.com>). More specifically, the data I got was the number of daily tweets containing **#apple** between January 1st 2010 and September 26th 2012 (1000 days). I mapped that data onto the frequency setting of a synthesiser, a process called parameter mapping. I also implemented an auditory icon cue; in other words, every data point above a specific threshold caused a sound to be played (a bird tweet, in this case). 

I then produced two more data sets through internet research: a list of dates when Apple made public announcements and product releases, for the same time period. These two sets, being binary (either something happened on a given day, or nothing happened) were also sonified using auditory icons.

The interface itself was developed using [Pure Data](http://puredata.info). This is what it looks like:

<center><img class="img-responsive" alt="Tweet Applifier" src="{{ site.baseurl }}/assets/projects/sonification/tweet_applifier.png" /></center>

The interface performed its function quite well, meaning it sonified the data in the way I intended it to. However, I'm sad to say that hearing the data did not help me interpret it. Personally, I find that it is easier to simply look at the coincident peaks than to hear coincident sounds. Nevertheless, I did notice one advantage: if I slow down the scrolling speed and really pay attention to the around the product launch dates, it is clear that the tweet peaks actually happen shortly after the product launch. I suppose this is to be expected, since word of the product launch takes some time to spread, but it was something I failed to notice by looking at the data alone. 

If you'd like to have a go at it or adapt it for something else, the patch is reasonably well-commented and is available [here]({{ site.baseurl }}/assets/projects/sonification/tweet_applifier.zip). You need Pd-extended to use it, and in my experience it works best on Windows.

