---
yaml_begin: true
title: 1998-03-07 reply to keith sanborn
description: 
extract: 
created: 2024-11-17 17:08
updated: 2026-01-20 12:25
author: "tb"
images: false
order: 
enableToc: 
permalink: 
aliases: 

publish: 
date: 1998-03-07
tags:
  - art
  - culture
  - information/data
  - design/interface
yaml_end: true
---

*(Note: This message dates from a period when, for various reasons, I practiced writing fully justified texts. I’ve set this email in a monospaced font to make that clear. For extra OG-typography fun, I “hung” the punctuation on the right margin. )*

To: nettime-l
Subject: <nettime> an entirely new subject
From: t byfield
Date: [Sat, 7 Mar 1998 03:31:31 -0500](https://nettime.org/Lists-Archives/nettime-l-9803/msg00039.html)

`I spent a little time this afternoon composing a response to Mr.`
`Sanborn’s eruption, but it proved to be too much of a chore; he`
`doesn’t really seem to have a point, other than branding his in-`
`terlocutors as neoconservatives, neo-manicheans, Machiavellians,`
`and social darwinists. (Fascists can’t be very far off now, can`
`it?) In any event, I thought to myself, Self, how about writing`
`something Constructive for a change? So here’s something that I`
`have been thinking about a bit: databases [turgid spoiler here;`
`if you hate turgid blocks of text, don’t say I didn’t warn you]`
`\<And, whether they like it or not, extra-special thanks to Pit,`
`Diana, and D. S. Bennahum for getting me thinking again, FWIW.>`
`(And if you got this as a BCC, then it’s dedicated to you... :)`

Cheers,
Ted

`Until quite recently, most programming languages worth consider-`
`ing would fail unless every element they encountered was explic-`
`itly classified in advance. Put simply, if a program would need`
`to process a datum, the programmer would need to announce in ad-`
`vance how the program should parse it. While this is still true`
`for the most part, the accumulation of human effort that’s gone`
`into software development has pushed most interactions (even of`
`“developers”) to “higher” levels--that is, forms of interaction`
`that don’t require such intimate interaction with data. I’m not`
`talking about pointing-and-clicking in a GUI, or optical charac-`
`ter recognition programs; however sophisticated, processes like`
`this are ways of facilitating input and output--in short, human`
`interaction interfaces. Rather, what interests me are databases`
`that don’t need to know the “type” of the data they store prior`
`to incorporating it. That means: a database that can store--and`
`process, within limits--streams of data (for example, raw ether-`
`net traffic over N period), memory core (the momentary state of`
`a system *in the process of operating*), media states (an image`
`of a hard drive), simple matrices (a subdatabase) or complex ma-`
`trices (arrays of “time-series” data)...and, of course, formats`
`we all know, such as ASCII, numbers, hex or binary data, images`
`(TIFs, PICTs, BMPs, faxes), word-processing documents, video or`
`sound streams or analog streams (such as encoded radio signals).`
`It’s hard to grok just how important this is until one realizes`
`that a database is, by definition, more than a way to put files`
`somewhere, anywhere, wherever, and tagging them with serial num-`
`bers; there’s no doubt that actually making a database that can`
`store these various formats without mangling them was a supreme`
`achievement for its programmers, but it’d be useless for anyone`
`else. Instead, certain kinds of databases can, more than merely`
`storing data of undeclared “types,” *analyze* data according to`
`the peculiar structure of that data. Since almost all available`
`data is structured according to standardized methods, it’s fair-`
`ly simple to declare the range of likely structures a given dat-`
`um may correspond to and discover which one it is, even when it`
`wasn’t “declared” when it was incorporated. But declaring every`
`single type, and then developing numerous ways to analyze every`
`possible format, and then developing metaformal structures that`
`will allow users to construct their own tools for analyzing any`
`given datum or array of data... In principle, it’s much more ef-`
`ficient to develop formal methods for analyzing data in general,`
`because the “native” structure of any given element will reveal`
`its own peculiar logic and greater or lesser resemblance to any`
`other datum. What you’re reading right now, for instance, ASCII`
`text, has certain peculiar traits--the logical patterns in meth-`
`ods of encoding characters, the patterns of justified text, the`
`patterns imposed by the English language (the incidence of this`
`or that letter, word length, grammatical and syntactic patterns,`
`and so on)--all of which are encoded in overlapping frequencies`
`in the binary data this essay consists of. Had I encrypted this`
`message, someone who didn’t have the key but wanted to crack it`
`would search the data for ways to find patterns that correspond`
`to known linguistic characteristics; knowing that I write in En-`
`glish would help, but wouldn’t be necessary; and knowing that I`
`write in a Latin alphabet would help, but wouldn’t be necessary`
`--in both cases because the data structures in which these meta-`
`languages (English, ASCII) are encoded reveal their own particu-`
`lar patterns. Once the basic encodings are found the high-level`
`encodings are relatively trivial to find. And so it is with new`
`databases: it’s often more efficient to examine a datum or data`
`stream for “behavioral” patterns than it is to pay attention to`
`what it (or someone) says it is. I’ve explained one reason this`
`is so, but there’s another equally if not more important reason,`
`a fundamental principle of database construction: the potential`
`value of data isn’t limited to the interrelationships we antici-`
`pate. By limiting the elements one incorporates into a database`
`to what you (*think* you) know--for example by declaring “types”`
`--you limit what you might discover. In other words, by telling`
`a database “this element is ASCII” and “that element is a video`
`stream,” you’ll lose more (by categorizing) than you might gain`
`(by examining). Now, I should say, this is a gross oversimplifi-`
`cation of the specific techniques that modern databases can use`
`to function efficiently in everyday practice: there’d be little`
`point in searching through an hour-long video file just because`
`someone wanted to find this or that string of text in a memo he`
`or she sent last week. But the fact remains that some databases`
`will allow you to find every use of, for example, a picture--in`
`video files, in image files, in images embedded in word-process-`
`ing documents, and in elements whose type was never declared to`
`the database. But I wouldn’t write this much just to extoll the`
`wonders of modern database technologies, that’s not my point at`
`all. Rather, what’s remarkable about this, I think, is where it`
`will lead in terms of the way we communicate. To declare a data`
`type is, at root, to declare the GENRE of an utterance: this is`
`fiction, this is nonfiction, this is a book, this is a love let-`
`ter, this is an art film, this is a laundry list... And what we`
`are now seeing is the rise of a technique for folding every pos-`
`sible genre we might think up into a metastructure that regards`
`genres--categories that have served to structure the communicat-`
`ive basis of our knowledge--as *obstructions* to possible forms`
`of, not “knowledge” as we now understand it, but meaningful cor-`
`relation. The problem is, of course, that the “agent” that will`
`perceive this correlation and thereby construct the meanings is`
`no longer an individual or even a group of people; and so we’ll`
`have no way, at least according to our current ways of thinking,`
`to verify the validity, worth, or use of these correlations. We`
`won’t believe it because we won’t--can’t--know *how* to believe`
`it; and so we shall argue in various ways that the correlations`
`are *meaningless*. According to the constitutions of knowledges`
`we know, we will be right; but according to the ways of constit-`
`uting knowledge we do not and cannot know, we’ll be quite wrong.`
`The question I would like to leave you with is this: Are you an`
`Ancient, or are you a Modern? Do you firmly believe that the ca-`
`pacities of an individual mind (or group of individuals) is the`
`basis of all valid knowledge, or are you willing to accept what`
`a machine says is so? One can, of course, dismiss this question`
`by pointing out that machines ask only those questions they are`
`told to ask, so the choice that I’ve presented is a false dicho-`
`tomy. To be sure--for a few years. And then what? Much as expli-`
`cit data-type declarations have, through cumulative labor, been`
`obviated by modern databases, I am very sure that explicit quer-`
`ies will be obviated soon enough: their structures, values, and`
`terminologies will be built--by human beings--into basic system`
`functions. So the question I posed can be put off, but it won’t`
`go away--not forever, and in fact, not even for the foreseeable`
`future. Not that I could answer this question myself. No one, I`
`think, would relish the prospect of a fundamental shift in epis-`
`temology--which, if you haven’t noticed, is in no way a “theore-`
`tical” problem.  On the contrary, it’s a palpable, painful prob-`
`lem that’s ever-present in everyday life: the lingering culture`
`wars over the validity of psychoanalysis (wherein data does not`
`correspond to its declared type), whether individual experience` 
`should take priority over sociological statistics, the relative`
`merits of legal theories of individual privacy and group securi-`
`ty--these all prefigure and contribute to the ways in which the`
`shift toward disembodied or supraindividual “knowledge” will af-`
`fect us all. But more important, for me, than the affect it has`
`on individuals is the prospect of a meta-genre: a database, may-`
`be many, that can produce from what it stores whichever genre a`
`user requests. Or, more important, what it might produce when a`
`user no longer needs a genre to construct any form of knowledge.`

— t. byfield
