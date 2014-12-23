---
title: "Synergy Uni Map"
proj_id: "unimap"
ongoing: false
permalink: /projects/unimap/
date: "January to May 2013"
---
## Description

All MEng students were required to do a big software engineering group project in third year. The task was very open: to produce a slideshow application in Java. It had to be able to handle five types of content (text, image, video, sound and shapes), and the slideshows had to be read from an XML format common to all groups. We were divided into four groups of 10 structured like companies where each group member took a managerial role, such as financial, marketing or software manager. This makes for a very different and, in many ways, challenging assignment. As a company, we were expected to market a commercially viable product that incorporated the slideshow requirement in some way. We were given five months to complete the assignment, and received very little guidance or supervision throughout. 

It was up to each company to schedule meetings, assign roles, design and implement the product, write up a business plan and get "funding". Every company employee had to be paid hypothetical money, meaning budget shortages had to be factored into the risk analysis and dealt with carefully. We had three deadlines: a meeting with hypothetical shareholders early on, to pitch the product concept and receive funding to produce it; another meeting halfway through the project to present a progress report; and a formal meeting at the end to show the shareholders the product they "paid for" in all its glory.

Needless to say, this is quite an unusual format for a university assignment. Rather than carrying out a small task in a short time, we had a huge task to complete in a long time, requiring extraordinary discipline and planning, not to mention collective organisation within the group. 

## Synergy Software Solutions

<center><img class="img-responsive" alt="Synergy Software Solutions" src="{{ site.baseurl }}/assets/projects/unimap/synergy_logo_white_dragon.png" /></center>

I was fortunate enough to be placed in a group with engaged and hard-working individuals, and this made the project very enjoyable indeed. We were able to achieve a good balance between work and play without compromising productivity. We elected to divide the company into the following hierarchy:

<center><img class="img-responsive" alt="The Managers" src="{{ site.baseurl }}/assets/projects/unimap/synergy_hierarchy.png" /></center>

In addition, we adopted an agile development cycle consisting of week-long sprints. Every Friday we meet for an hour to discuss the current progress: which users stories had already been implemented, whether anyone was struggling with theirs and needed more time, and so on. Despite our management roles, we all took on programming hours, though some more than others. My job as integration manager was to coordinate the merge of the feature branches into the development branch, in preparation for the release.  More about that in a bit though, when we talk about...

## The Product

Our product, Uni Map, was a campus map application designed to lead new students around campus as well as provide information about the current events in each building. We decided to develop a generic slideshow extension to the JavaFX API, and then use it as a library for Uni Map. My duties as integration manager were seasonal in the sense that during the integration phase I had a lot of work, but comparatively little otherwise. For that reason, I was heavily involved in the class-level design of the slideshow library. Having had some experience with Java and object-oriented programming previously, I saw it as an opportunity to learn more practically rather than theoretically. 

<center><img class="img-responsive" alt="Design Concept" src="{{ site.baseurl }}/assets/projects/unimap/uni_map_design.png" />One of the early design concepts for Uni Map.</center>

## Inter-group Interactions

As I mentioned previously, the slideshows themselves were to be stored in an XML format common to all groups. This presents yet another challenge, as we had to arrange a meeting with representatives from all groups in which to discuss the specifications of the common format. A lot of drama naturally ensued, since each group had a very different idea regarding what the format should actually contain; some groups were developing for Android and wanted content dimensions to be specified as a percentage, for instance. We were ultimately able to agree on a final specification, though it was definitely a setback as we had rather hoped to start development without so much ado. 

In addition to settling on a common format, we were also required to commission certain components of our product from another group. This was done much as actual companies would do it; technical advisors from each company carefully drew up very detailed specifications of the required component, at the same time without revealing too much about the product's internal implementation details. Each company then drew up a contract including the specifications but also how much money it was willing to pay for the work commissioned and a deadline for delivery. Meetings were held with technical and legal representatives from each company in order to finalise the deals.

## The Outcome

Our group was quite successful. We were able to carry out three iterations of our agile development cycle and ultimately produce a working protoype of our product. We then pitched it to the members of staff running the assignment as potential customers in a formal, business-like setting. Unfortunately the executable .jar we originally used for deployment is no longer hosted. The source code, however, is still available on bitbucket:

[Synergy Slideshow Library](https://bitbucket.org/epedroni/synergy_slideshow)  
[Synergy Uni Map](https://bitbucket.org/epedroni/uni_map)

This was a very rewarding project, though also very stressful. Looking back on it now, I would have done many things differently; having spent the following year working with Java again for my [final project]({{ site.baseurl }}/projects/jcgp), for instance, made me realise how many mistakes we made in the design of our product. The truth is that there is no royal road to learning, and I certainly learnt a lot from the Synergy days.
