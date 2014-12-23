---
title: "GUI Refactorings"
categories: [projects, jcgp]
tags: []
---

Like I said a few months ago, my intention is to slowly refactor and improve JCGP over the coming years. I've been relaxing for a while now, so I feel the time has finally come to fix that GUI once and for all. 

## The Problem

The release GUI is messy to say the least. Miraculously, it is largely bug-free as far as I could test it, but I am not proud to say that the way it was implemented was very sloppy. I had the detailed specifications regarding what it should do, but since I was running out of time, I ended up implementing it before I properly designed it, which is *always* a mistake. So this time around, I'm taking the time to sit down and design the whole thing on paper first, to make sure the new implementation is cleaner and more maintainable than the current one.

One thing that bothered me about the old design was the sheer number of event handlers used. In order to implement the chromosome pane mechanics (highlighting connections, click-and-drag to make new connections), it is understandable that many mouse events have to be handled. What annoyed me, however, was that I tried cramming as much of the code as possible into the lower classes in the hierarchy (`GUIInput`, `GUINode` and `GUIOutput`) in an attempt to clean up the `ChromosomePane` class which was also getting out of hand. What that meant, however, was that each instance of `GUIInput`, `GUINode` and `GUIOutput` had their own set of 10-odd mouse event handlers. In CGP, large genomes are often employed, and in the current architecture the memory footprint increases dramatically with genome size. 

<center><img class="img-responsive" alt="Class hierarchy UML" src="{{ site.baseurl }}/assets/projects/jcgp/gui-pop-hierarchy.png" />Oh, UML.</center>

Another problem with the handlers was the location of the logic, so to speak. I decided to implement an FSM-like system, where each gene had a state and the appearance of the gene was a function of its state. As I added more and more functionality to the interface, however, I was forced to put state transition logic into the state outputs themselves; while it works, it makes the code terribly disorganised and hard to understand, let alone maintain. Furthermore, shifting so much of the code into the gene classes meant that references to upper-level components had to be passed down and held by the genes; while the memory overhead is acceptable, it still makes for a disorganised class hierarchy.

## The New Design

I spent some time thinking about the handler issue, and I realised that instance-specific handlers are entirely unnecessary in this case. Since the behaviour of each type of gene should be the same, a single instance of each handler should suffice. I created a container class in which the gene handlers are stored statically. When instantiating its genes, the `ChromosomePane` now simply adds the event handlers to the new instance, via a static method in the container class. The method argument type ensures that those handlers can never be added to the wrong objects, and no more than a single instance of each handler is necessary. Problem solved! This also takes care of the inversion-of-control problem I was having, as the gene classes no longer require references to upper-level components. 

Regarding the FSM model, I decided to keep it, as it is a very neat way to do things, but I am currently re-designing it to be much more strict with regard to where the logic is set. I am trying to keep state transition logic exclusively in the event handlers and reserve the state output logic for the appearance of the gene exclusively. It gets harder and harder as I reintroduce features, but the code does look more friendly and maintainable this way.

I've created a new branch, `refactor`, to refactor the code without touching the development branch. If you're interested to see the state of the refactorings, feel free to [clone it](https://bitbucket.org/epedroni/jcgp/branch/refactor).
