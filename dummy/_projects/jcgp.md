---
title: "JCGP"
proj_id: "jcgp"
proj_page: "https://bitbucket.org/epedroni/jcgp/"
permalink: /projects/jcgp/
date: "October 2013"
---

## Cartesian Genetic Programming

Cartesian Genetic Programming, or CGP for short, is a particular modality of GP developed by Julian Miller in the late '90s. In traditional GP, such as Koza's tree-based GP, a computer program is encoded as a genotype, which allows it to *evolve* in exactly the same way as we believe creatures evolve in nature. Individuals from a population are selected based on fitness and their chromosomes are mutated and mixed, creating new and potentially fitter individuals. In the case of GP, the individuals are computer programs (or anything else, as long as it can be encoded), and their fitness is a measure of how close they come to the functionality desired by the user. The iterative process of selection, mutation and crossover repeats until a solution is ideally found.

In my last year of university I had the chance to play around with CGP, which I quite enjoyed. I had to go through the source code to create a new mutation operator, however, and I experienced firsthand the difficulty of maintaining someone else's code. I spoke with Julian about it and he agreed that his performance-oriented implementation was not the easiest for inexperienced users to understand and modify. Given my passion for software development and my interest in GP, I decided to combine the two for my master's project.

## JCGP

In *The Mythical Man-Month*, Frederick Brooks discusses the difference between a program and a programming product. A program is software that is “complete in itself, ready to be run by the author on the system on which it was developed.” A programming product, on the other hand, is said to be “a program that can be run, tested, repaired, and extended by anybody. It is usable in many operating environments, for many sets of data”. 

The above paragraph is taken directly from my master's thesis, because it perfectly captures what I set out to do. The goal of my project was, to the greatest possible extent, to turn CGP from a program into a programming product. I attempted to do this largely by following what Brooks proposes: generalisation, testing, documentation and maintenance. I produced a new implementation of CGP, dubbed JCGP, in Java instead of C. I applied object-oriented design patterns to make it as flexible and accessible to new users as possible, sometimes at the expense of performance. I implemented the algorithms in a generic way, allowing new algorithms to be written and added to the program in a simple plug-and-play fashion. I also created a GUI which aims to illustrate exactly what happens as a population undergoes selection and mutation. In addition to these software features, I wrote a user manual and extensive comments on all of the classes, and produced the associated Javadoc pages, in an attempt to lower the entry requirements for prospective CGP users.

JCGP is a project that I hope to keep maintaining and expanding for a while, so I will post any interesting developments here. The project is licensed under a GPLv3 license, meaning you are free to use it, change it and share it and any changes you make to it, though I would appreciate being attributed for the original version.
