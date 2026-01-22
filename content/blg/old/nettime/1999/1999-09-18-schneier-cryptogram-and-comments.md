---
yaml_begin: true
title: 1999-09-18 schneier cryptogram and comments
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
date: 1999-09-18
tags:
  - cryptography
  - data
  - device
  - email
  - internet
  - security
  - technology
yaml_end: true
---

To: nettime-l
Subject: <nettime> remarks + fwd: CRYPTO-GRAM, September 15, 1999
From: t byfield
Date: [Sat, 18 Sep 1999 15:07:01 +0100](https://nettime.org/Lists-Archives/nettime-l-9909/msg00116.html)

[it’s always an open question among the nettime moderators whether it’s good or bad to forward items from other lists — whether the ‘extra’ traffic puts people off, whether it discourages ‘original’ contributions, whether it makes the list seem like an ‘impersonal text machine’ instead of a forum that’s open to discussion, etc. i’m sure most subscribers think about it too; but the moderators talk about it every so often, and that’s the feedback i know best.

in general, when i forward things i have two thoughts in mind: the specific items are somehow relevant to nettime, and it’s an effective way to point out resources that are useful or interesting — (alphabetically) the Cook Report <www.cookreport.com> [newsletter; annual subscription fee], LBO-talk [Left Business Observer] <www.panix.com/~dhenwood/> [forwards, discussion], NTKnow <www.ntk.net> [weekly newsletter], PRIVACY Forum <www.vortex.com> [occasional digest], RISKS <catless.ncl.ac.uk/Risks/> [regular digest], TBTF <www.tbtf.com> [semiregular newsletter], TELECOM Digest <hyperarchive.lcs.mit.edu/telecom-archives/archives> [discussion; annual subscription fee], for example.

the erstwhile motto of nettime, ‘collaborative text filtering,’ is a good goal, though it’s also just a clever name for processes that seem to be native to ‘net discourse’ anyway — forwarding, bouncing, redistributing, aggregating, sharing, etc. to do it with specific items is good (or bad: viruses, good-luck junk, etc.); but to do it with general resources — lists, publications, archives, sites — is better, i think. specific items reinforces an economy of exceptionalism in which nettime tends to become (among other things) inward-looking, an archive of the ‘best,’ the ‘most interesting,’ the ‘most unique’; but to do it with general resources tends to make nettime a bit more open and outward-looking. there are lots of tired old maxims to describe this, about ‘teaching people to fish,’ ‘giving people tools,’ and so on — and, though cliched, they’re true. anyway...

bruce schneier’s CRYPTO-GRAM <www.counterpane.com>, below, is an excellent resource for clear, succinct info about cryptography, security, policy, etc. this issue seemed particularly interesting because schneier says he’s ‘never understood the current fuss about the open source software movement’: it’s what cryptographers and security experts have been doing for decades.’ fine and dandy, no problem, it’s not open source he doesn’t understand, it’s the ‘current fuss’ he doesn’t understand.

schneier is pretty infatuated with the idea that he’s an expert. he *is* an expert, no question — he wrote _Applied Cryptography_, the standard intro reference work on cryptography — but, beyond that, he never tires of banging his can about the fact that he’s an expert. what he calls the ‘current fuss’ is, in part, the means by which people who *aren’t* experts are learning about open source theories and practices and the many ways in which they’re important. ‘hype’ in another way to say ‘current fuss’: for a while, it was quite trendy to wank about ‘net hype,’ but the result of that hype is the fact that huge numbers of people learned about the net and began to use it — and some of them began to learn about it in a deeper sense through using it. hype has its upside.

aside from the fact that this issue of CRYPTO-GRAM is full of good notices, it illustrates something that’s been bugging me for a while — the widespread tendency to reduce net-related questions to security issues, as if ‘security’ were the basis of networking, the main point, the infrastructure, and the rest were just fluffy side-effects, optional, superstructural.

the recent hotmail exploit is a good example: media coverage immediately treated the immediate problem — the fact that X might be able to read Y’s mail or send mail in Y’s name without X knowing or approving of it — as a security issue. but security is only one facet of that problem; another facet, much vaguer but no less real, might be called ‘trust.’ put another way, even though it might be technically possible for Y to do this, but X might *trust* him or her not to do so. this kind of trust is the stuff of everyday life off the net; but on the net, this kind of trust tends to evaporate — in large part because there’s a big ‘current fuss’ about security. and security boils down to little more than ways of enforcing in advance the vague ‘protocols’ of trust, along the lines of the statement ‘you can’t quit — you’re fired’: security eliminates possibilities by forcing people to do ‘what they should do anyway.’ taken to its logical extreme, a secured world is a world without ethics, because none is needed — except, of course, on the part of those who defined what was being secured, how it was being secured, what it’s being secured against, and so on.

security and trust are a chicken-and-egg problem: security requires certain kinds of trust, and trust requires certain kinds of securities. but it’s significant that the phrase ‘trust expert’ sounds silly, that ‘threat model’ is a more common idea than ‘trust model,’ that people concerned with privacy don’t trust that surveillance agencies probably aren’t interested in them, that many if not most ‘hackers’ have a basic sense of ethics, that moderators are more likely to make mistakes or bad choices than to ‘censor’ contributors, that the media never cover events like the hotmail discovery in terms of trust. how many hotmail accounts could be read by anyone? 40 million! how many *were* read? probably a few thousand. how much damage was done? probably very, very little... so where is are the headlines blaring ‘HOTMAIL SECURITY BREACH SHOWN TO BE NEGLIGIBLE — 0.000625% OF USERS AFFECTED’?

cryptography and security are important issues, definitely, but — by definition — neither more nor less important than ‘plainness’ and trust. the current fuss about security has been running for much longer and has cut much more deeply than the current fuss about the open source movement. and since many people learn about security in the larger context of learning about networks, they’re tacitly, generally encouraged to assume that security is fundamental to networking. but ‘security’ is a complex field, built on all kinds of assumptions about basic social relations — who can or can’t be trusted to do what, when, how, why, where, etc. specific security models and methods *impose* those assumptions on social fields and *enforce* them, in much the same way that architecture defines (or tries to define) where people can go, how they can get where they’re going, what they can and can’t do in various areas, and so on. and security is, as schneier forever points out, implemented by experts. the upshot: the realm of possible social relations on the networks is being decided by experts. and in much the same way that the current fuss about the open source movement is the means by which more and more people are learning about its theories and practices, the current fuss about security is the means by which more and more people are learning that security — rather than trust — is a fundamental aspect of networking. but if networking had been built on a foundation of security rather than trust, then no one would have been interested to begin with; or, if they were, they’d never have been given access to resources whose potential power far outstripped their technical understanding. in short, ‘insecurity’ — trust expressed in negative terms — is a very fruitful thing.

to a certain extent, it’s necessary to delegate power to experts: very few people know how to design a microchip, define a reliable operating system, write a good program, or develop a useful communications protocol. but it doesn’t therefore follow that the substance of what transpires within those formal frameworks should be defined by ‘experts,’ because there’s no such thing as an expert on the realm of social possibility. emile durkheim put it best: the science of the future has no subject.

 — cheers, tb]

***

`         CRYPTO-GRAM`

`       September 15, 1999`

`       by Bruce Schneier`
`        Founder and CTO`
`   Counterpane Internet Security, Inc.`
`      schneier@counterpane.com`
`     http://www.counterpane.com`
`A free monthly newsletter providing summaries, analyses, insights, and`
`commentaries on computer security and cryptography.`

`Back issues are available at http://www.counterpane.com. To subscribe or`
`unsubscribe, see below.`
`Copyright (c) 1999 by Bruce Schneier`
`** *** ***** ******* *********** *************`

`In this issue:`
`   Open Source and Security`
`   NSA Key in Microsoft Crypto API?`
`   Counterpane Systems -- Featured Research`
`   News`
`   Extra Scary News`
`   Counterpane News`
`   The Doghouse: E*Trade`
`   Factoring a 512-bit Number`
`   Comments from Readers`
`** *** ***** ******* *********** *************`

`     Open Source and Security`

`As a cryptography and computer security expert, I have never understood the`
`current fuss about the open source software movement. In the cryptography`
`world, we consider open source necessary for good security; we have for`
`decades. Public security is always more secure than proprietary security.`
`It’s true for cryptographic algorithms, security protocols, and security`
`source code. For us, open source isn’t just a business model; it’s smart`
`engineering practice.`

`Open Source Cryptography`

`Cryptography has been espousing open source ideals for decades, although we`
`call it “using public algorithms and protocols.” The idea is simple:`
`cryptography is hard to do right, and the only way to know if something was`
`done right is to be able to examine it.`

`This is vital in cryptography, because security has nothing to do with`
`functionality. You can have two algorithms, one secure and the other`
`insecure, and they both can work perfectly. They can encrypt and decrypt,`
`they can be efficient and have a pretty user interface, they can never`
`crash. The only way to tell good cryptography from bad cryptography is to`
`have it examined.`

`Even worse, it doesn’t do any good to have a bunch of random people examine`
`the code; the only way to tell good cryptography from bad cryptography is`
`to have it examined by experts. Analyzing cryptography is hard, and there`
`are very few people in the world who can do it competently. Before an`
`algorithm can really be considered secure, it needs to be examined by many`
`experts over the course of years.`

`This argues very strongly for open source cryptographic algorithms. Since`
`the only way to have any confidence in an algorithm’s security is to have`
`experts examine it, and the only way they will spend the time necessary to`
`adequately examine it is to allow them to publish research papers about it,`
`the algorithm has to be public. A proprietary algorithm, no matter who`
`designed it and who was paid under NDA to evaluate it, is much riskier than`
`a public algorithm.`

`The counter-argument you sometimes hear is that secret cryptography is`
`stronger because it is secret, and public algorithms are riskier because`
`they are public. This sounds plausible, until you think about it for a`
`minute. Public algorithms are designed to be secure even though they are`
`public; that’s how they’re made. So there’s no risk in making them public.`
` If an algorithm is only secure if it remains secret, then it will only be`
`secure until someone reverse-engineers and publishes the algorithms. A`
`variety of secret digital cellular telephone algorithms have been “outed”`
`and promptly broken, illustrating the futility of that argument.`

`Instead of using public algorithms, the U.S. digital cellular companies`
`decided to create their own proprietary cryptography. Over the past few`
`years, different algorithms have been made public. (No, the cell phone`
`industry didn’t want them made public. What generally happens is that a`
`cryptographer receives a confidential specification in a plain brown`
`wrapper.) And once they have been made public, they have been broken. Now`
`the U.S. cellular industry is considering public algorithms to replace`
`their broken proprietary ones.`

`On the other hand, the popular e-mail encryption program PGP has always`
`used public algorithms. And none of those algorithms has ever been broken.`
` The same is true for the various Internet cryptographic protocols: SSL,`
`S/MIME, IPSec, SSH, and so on.`

`The Best Evaluation Money Can’t Buy`

`Right now the U.S. government is choosing an encryption algorithm to`
`replace DES, called AES (the Advanced Encryption Standard). There are five`
`contenders for the standard, and before the final one is chosen the world’s`
`best cryptographers will spend thousands of hours evaluating them. No`
`company, no matter how rich, can afford that kind of evaluation. And since`
`AES is free for all uses, there’s no reason for a company to even bother`
`creating its own standard. Open cryptography is not only better -- it’s`
`cheaper, too.`

`The same reasoning that leads smart companies to use published cryptography`
`also leads them to use published security protocols: anyone who creates his`
`own security protocol is either a genius or a fool. Since there are more`
`of the latter than the former, using published protocols is just smarter.`

`Consider IPSec, the Internet IP security protocol. Beginning in 1992, it`
`was designed in the open by committee and was the subject of considerable`
`public scrutiny from the start. Everyone knew it was an important protocol`
`and people spent a lot of effort trying to get it right. Security`
`technologies were proposed, broken, and then modified. Versions were`
`codified and analyzed. The first draft of the standard was published in`
`1995. Different aspects of IPSec were debated on security merits and on`
`performance, ease of implementation, upgradability, and use.`

`In November 1998, the committee published a slew of RFCs -- one in a series`
`of steps to make IPSec an Internet standard. And it is still being`
`studied. Cryptographers at the Naval Research Laboratory recently`
`discovered a minor implementation flaw. The work continues, in public, by`
`anyone and everyone who is interested. The result, based on years of`
`public analysis, is a strong protocol that is trusted by many.`

`On the other hand, Microsoft developed its own Point-to-Point Tunneling`
`Protocol (PPTP) to do much the same thing. They invented their own`
`authentication protocol, their own hash functions, and their own`
`key-generation algorithm. Every one of these items was badly flawed. They`
`used a known encryption algorithm, but they used it in such a way as to`
`negate its security. They made implementation mistakes that weakened the`
`system even further. But since they did all this work internally, no one`
`knew that PPTP was weak.`

`Microsoft fielded PPTP in Windows NT and 95, and used it in their virtual`
`private network (VPN) products. Eventually they published their protocols,`
`and in the summer of 1998, the company I work for, Counterpane Systems,`
`published a paper describing the flaws we found. Once again, public`
`scrutiny paid off. Microsoft quickly posted a series of fixes, which we`
`evaluated this summer and found improved, but still flawed.`

`Like algorithms, the only way to tell a good security protocol from a`
`broken one is to have experts evaluate it. So if you need to use a`
`security protocol, you’d be much smarter taking one that has already been`
`evaluated. You can create your own, but what are the odds of it being as`
`secure as one that has been evaluated over the past several years by experts?`

`Securing Your Code`

`The exact same reasoning leads any smart security engineer to demand open`
`source code for anything related to security. Let’s review: Security has`
`nothing to do with functionality. Therefore, no amount of beta testing can`
`ever uncover a security flaw. The only way to find security flaws in a`
`piece of code -- such as in a cryptographic algorithm or security protocol`
`-- is to evaluate it. This is true for all code, whether it is open source`
`or proprietary. And you can’t just have anyone evaluate the code, you need`
`experts in security software evaluating the code. You need them evaluating`
`it multiple times and from different angles, over the course of years.`
`It’s possible to hire this kind of expertise, but it is much cheaper and`
`more effective to let the community at large do this. And the best way to`
`make that happen is to publish the source code.`

`But then if you want your code to truly be secure, you’ll need to do more`
`than just publish it under an open source license. There are two obvious`
`caveats you should keep in mind.`

`First, simply publishing the code does not automatically mean that people`
`will examine it for security flaws. Security researchers are fickle and`
`busy people. They do not have the time to examine every piece of source`
`code that is published. So while opening up source code is a good thing,`
`it is not a guarantee of security. I could name a dozen open source`
`security libraries that no one has ever heard of, and no one has ever`
`evaluated. On the other hand, the security code in Linux has been looked`
`at by a lot of very good security engineers.`

`Second, you need to be sure that security problems are fixed promptly when`
`found. People will find security flaws in open source security code. This`
`is a good thing. There’s no reason to believe that open source code is, at`
`the time of its writing, more secure than proprietary code. The point of`
`making it open source is so that many, many people look at the code for`
`security flaws and find them. Quickly. These then have to be fixed. So a`
`two year-old piece of open source code is likely to have far fewer security`
`flaws than proprietary code, simply because so many of them have been found`
`and fixed over that time. Security flaws will also be discovered in`
`proprietary code, but at a much slower rate.`

`Comparing the security of Linux with that of Microsoft Windows is not very`
`instructive. Microsoft has done such a terrible job with security that it`
`is not really a fair comparison. But comparing Linux with Solaris, for`
`example, is more instructive. People are finding security problems with`
`Linux faster and they are being fixed more quickly. The result is an`
`operating system that, even though it has only been out a few years, is`
`much more robust than Solaris was at the same age.`

`Secure PR`

`One of the great benefits of the open source movement is the`
`positive-feedback effect of publicity. Walk into any computer superstore`
`these days, and you’ll see an entire shelf of Linux-based products. People`
`buy them because Linux’s appeal is no longer limited to geeks; it’s a`
`useful tool for certain applications. The same feedback loop works in`
`security: public algorithms and protocols gain credibility because people`
`know them and use them, and then they become the current buzzword.`
`Marketing people call this mindshare. It’s not a perfect model, but hey,`
`it’s better than the alternative.`
`** *** ***** ******* *********** *************`

`    NSA Key in Microsoft Crypto API?`

`A few months ago, I talked about Microsoft’s system for digitally signing`
`cryptography suites that go into its operating system. The point is that`
`only approved crypto suites can be used, which makes thing like export`
`control easier. Annoying as it is, this is the current marketplace.`

`Microsoft has two keys, a primary and a spare. The Crypto-Gram article`
`talked about attacks based on the fact that a crypto suite is considered`
`signed if it is signed by EITHER key, and that there is no mechanism for`
`transitioning from the primary key to the backup. It’s stupid`
`cryptography, but the sort of thing you’d expect out of Microsoft.`

`Suddenly there’s a flurry of press activity because someone notices that`
`the second key in Microsoft’s Crypto API in Windows NT Service Pack 5 is`
`called “NSAKEY” in the code. Ah ha! The NSA can sign crypto suites. They`
`can use this ability to drop a Trojaned crypto suite into your computers.`
`Or so the conspiracy theory goes.`

`I don’t buy it.`

`First, if the NSA wanted to compromise Microsoft’s Crypto API, it would be`
`much easier to either 1) convince MS to tell them the secret key for MS’s`
`signature key, 2) get MS to sign an NSA-compromised module, or 3) install a`
`module other than Crypto API to break the encryption (no other modules need`
`signatures). It’s always easier to break good encryption by attacking the`
`random number generator than it is to brute-force the key.`

`Second, NSA doesn’t need a key to compromise security in Windows. Programs`
`like Back Orifice can do it without any keys. Attacking the Crypto API`
`still requires that the victim run an executable (even a Word macro) on his`
`computer. If you can convince a victim to run an untrusted macro, there`
`are a zillion smarter ways to compromise security.`

`Third, why in the world would anyone call a secret NSA key “NSAKEY”? Lots`
`of people have access to source code within Microsoft; a conspiracy like`
`this would only be known by a few people. Anyone with a debugger could`
`have found this “NSAKEY.” If this is a covert mechanism, it’s not very covert.`

`I see two possibilities. One, that the backup key is just as Microsoft`
`says, a backup key. It’s called “NSAKEY” for some dumb reason, and that’s`
`that.`

`Two, that it is actually an NSA key. If the NSA is going to use Microsoft`
`products for classified traffic, they’re going to install their own`
`cryptography. They’re not going to want to show it to anyone, not even`
`Microsoft. They are going to want to sign their own modules. So the`
`backup key could also be an NSA internal key, so that they could install`
`strong cryptography on Microsoft products for their own internal use.`

`But it’s not an NSA key so they can secretly inflict weak cryptography on`
`the unsuspecting masses. There are just too many smarter things they can`
`do to the unsuspecting masses.`

`My original article:`
`http://www.counterpane.com/crypto-gram-9904.html#certificates`

`Announcement:`
`http://www.cryptonym.com/hottopics/msft-nsa.html`

`Nice analysis:`
`http://ntbugtraq.ntadvice.com/default.asp?sid=1&pid=47&aid=52`

`Useful news article:`
`http://www.wired.com/news/news/technology/story/21577.html`
`** *** ***** ******* *********** *************`

`  Counterpane Systems -- Featured Research`

`”Cryptanalysis of Microsoft’s PPTP Authentication Extensions (MS-CHAPv2)”`

`Bruce Schneier and Mudge, CQRE, Duesseldorf, Oct 1999, to appear.`

`The Point-to-Point Tunneling Protocol (PPTP) is used to secure PPP`
`connections over TCP/IP link. In response to [SM98], Microsoft released`
`extensions to the PPTP authentication mechanism (MS-CHAP), called`
`MS-CHAPv2. We present an overview of the changes in the authentication and`
`encryption-key generation portions of MS-CHAPv2, and assess the`
`improvements and remaining weaknesses in Microsoft’s PPTP implementation.`
`While fixing some of the more egregious errors in MS-CHAPv1, the new`
`protocol still suffers from some of the same weaknesses.`

`http://www.counterpane.com/pptpv2-paper.html`
`** *** ***** ******* *********** *************`

`          News`

`The Internet Auditing Project. This is REAL interesting. A group did a`
`low-level security audit of 36 million hosts on the Internet. Just how`
`secure is the Internet really?`
`http://www.securityfocus.com/templates/forum_message.html?forum=2&head=32&id=32`
`http://www.internetnews.com/intl-news/print/0,1089,6_184381,00.html`

`And if that isn’t scary enough, here’s a more detailed audit of 2200`
`Internet sites.`
`http://www.fish.com/survey/`

`My all-time favorite Y2K compliance statement:`
`http://www.hartscientific.com/y2k.htm`

`If you need more evidence that proprietary security just doesn’t work,`
`Microsoft’s digital music security format is cracked within days of being`
`released:`
`http://www.wired.com/news/news/technology/story/21325.html`
`http://www.news.com/News/Item/0,4,0-40672,00.html?st.ne.lh..ni`
`http://www.msnbc.com/news/302195.asp`

`Patent blackmail: Lawyers for someone named Leon Stambler have been`
`sending threatening letters to security companies, claiming that SSL, PCK,`
`FIPS 196, SET, Microsoft PPTP, Authenticode, etc. infringe on his patent.`
`See for yourself; the U.S. patent numbers are 5,793,302 and 5,646,998. See`
`for yourself; the U.S. patent numbers are 5,793,302 and 5,646,998.`
`http://164.195.100.11/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&`
`u=/netahtml/srchnum.htm&r=1&f=G&l=50&s1=’5,793,302’.WKU.&OS=PN/5,793,302&RS=`
`PN/5,793,302`
`http://164.195.100.11/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&`
`u=/netahtml/srchnum.htm&r=1&f=G&l=50&s1=’5,646,998’.WKU.&OS=PN/5,646,998&RS=`
`PN/5,646,998`

`With all the talk about electronic voting, it’s nice that someone`
`recognizes that there are some serious security problems. The most severe,`
`at least to me, is voter coercion. When you step into a private voting`
`booth, you can vote as you please. No one can do anything about it. If`
`you can vote from your computer, in your own home, with some kind of`
`electronic security measure, then it is possible for someone to buy your`
`vote and to ensure that you deliver on the goods.`
`http://www.nytimes.com/library/tech/99/08/cyber/articles/14vote.html`

`Many people asked me about my comment last issue about Windows NT needing`
`over 300 security changes to make it secure. I queried the Usenet`
`newsgroup comp.os.ms-windows.nt.admin.security asking if it was folklore or`
`truth, and got several answers.  The consensus seemed to be that the`
`number was somewhere between 50 and 3000, and 300 wasn’t an unreasonable`
`estimate.  A good checklist is available here:`
`http://people.hp.se/stnor/`
`And see also:`
`http://www.trustedsystems.com/NSAGuide.htm`

`The U.S. crypto export regulations has led to the development of some`
`excellent products from non-U.S. companies. Judging from this article,`
`though, this isn’t one of them:`
`http://www.rediff.com/computer/1999/jul/09suri.htm`

`Two Microsoft security white papers. They’re not great, but they do`
`explain the Microsoft party line.`
`Security basics:`
`http://www.microsoft.com/security/resources/security101wp.asp`
`Office 2000 Macro Security:`
`http://officeupdate.microsoft.com/2000/downloadDetails/o2ksec.htm`

`A flaw in Hotmail allows anyone to read anyone else’s email, without a`
`password. To me, the real interesting story is not that the flaw was`
`discovered, but that it might have been known by the underground community`
`long before it became public. Some of the news stories imply this.`
`http://www.wired.com/news/news/technology/story/21503.html`
`http://www.msnbc.com:80/news/306093.asp`
`http://www.zdnet.com.au:80/zdnn/stories/zdnn_display/0,3440,2324361,00.html`
`http://news.excite.com/news/zd/990901/10/the-bug-syndrome`
`http://news.excite.com/news/zd/990901/06/how-hotmail-blew`
`http://www.salon.com/tech/log/1999/09/02/hotmail_hack/print.html`

`Encrypted sculpture at the CIA’s headquarters in Langley, VA.`
`http://www.npr.org/programs/atc/990826.kryptos.html`

`Join the military and see the basements of Ft. Meade. The National`
`Security Agency is offering free college tuition and room and board to`
`hackers willing to work for them for five years after graduation.`
`http://www.currents.net/newstoday/99/08/27/news3.html`
`http://www.cnn.com/TECH/computing/9908/26/t_t/teen.hacker/index.html`

`Nice BBC article on U.S. encryption debate:`
`http://news.bbc.co.uk/hi/english/world/americas/newsid_430000/430384.stm`

`Funny stuff: the real story of Alice and Bob:`
`http://www.conceptlabs.co.uk/alicebob.html`

`There was a really good article -- clear, complete, understandable -- in`
`_The Sciences_ recently about quantum computing. Cryptome has put the`
`article online, with the permission of the author.`
`http://cryptome.org/qc-grover.htm`
`** *** ***** ******* *********** *************`

`       Extra Scary News`

`The Justice Department is planning to ask Congress for new authority`
`allowing federal agents armed with search warrants to secretly break into`
`homes and offices to obtain decryption keys or passwords or to implant`
`”recovery devices” or otherwise modify computers to ensure that any`
`encrypted messages or files can be read by the government.`

`With this dramatic proposal, the Clinton Administration is basically`
`saying: “If you don’t give your key in advance to a third party, we will`
`secretly enter your house to take it if we suspect criminal conduct.”`

`The full text of the Justice Department proposal, a section-by-section`
`analysis prepared by DOJ lawyers, and related materials are available at:`

`http://www.epic.org/crypto/legislation/cesa_release.html`
`http://www.cdt.org/crypto/CESA`

`http://www.washingtonpost.com/wp-srv/business/daily/aug99/encryption20.htm`
`http://www.zdnet.com/zdnn/stories/news/0,4586,2317907,00.html`
`http://www.techweb.com/wire/story/TWB19990820S0012`
`** *** ***** ******* *********** *************`

`       Counterpane News`
`Bruce Schneier will be speaking at SANS Network Security 99, October 3-10,`
`in New Orleans. See http://www.sans.org/ns99/ns99.htm for more conference`
`details.`

`    Attack Trees: Wed, 6 Oct, 10:30-12:30`
`    Internet Cryptography: Tue, 5 Oct, 9:00-5:00`

`Bruce Schneier authored the “Inside Risks” column for the Aug, Sep, and Oct`
`99 issues of _Communications of the ACM_.`
`Biometrics: Uses and Abuses:`
`http://www.counterpane.com/insiderisks1.html`
`The Trojan Horse Race:`
`http://www.counterpane.com/insiderisks2.html`
`Risks of Relying on Cryptography:`
`http://www.counterpane.com/insiderisks3.html`
`** *** ***** ******* *********** *************`

`    The Doghouse: E*Trade`

`E*Trade’s password security isn’t. They limit the logon password to a`
`maximum of 6 characters, and the only choices are letters (upper and lower`
`case are distinguished), numbers, $, and _. Whose portfolio do you want to`
`trade today?`
`** *** ***** ******* *********** *************`

`     Factoring a 512-bit Number`

`A factoring record was broken last month, on 22 August. A group led by`
`Herman te Riele of CWI in Amsterdam factored a 512-bit (155-digit) hard`
`number. By “hard,” I mean that it was the product of two 78-digit`
`primes...the kind of numbers used by the RSA algorithm.`

`About 300 fast SGI workstations and Pentium PCs did the work, mostly on`
`nights and weekends, over the course of seven months. The algorithm used`
`was the General Number Field Sieve. The algorithm has two parts: a sieving`
`step and a matrix reduction step. The sieving step was the part that the`
`300 computers worked on: about 8000 MIPS-years over 3.7 months. (This is`
`the step that Shamir’s TWINKLE device can speed up.) The matrix reduction`
`step took 224 CPU hours (and about 3.2 Gig of memory) on the Cray C916 at`
`the SARA Amsterdam Academic Computer Center. If this were done over the`
`general Internet, using resources comparable to what was used in the recent`
`DES cracking efforts, it would take about a week calendar time.`

`The entire effort was 50 times easier than breaking DES. Factoring`
`e-commerce keys is definitely very practical, and will be becoming even`
`more so in future years. It is certainly reasonable to expect 768-bit`
`numbers to be factored within a few years, so comments from RSA`
`Laboratories that RSA keys should be a minimum of 768 bits are much too`
`optimistic.`

`Certicom used the event to tout the benefits of elliptic curve public-key`
`cryptography. Elliptic-curve algorithms, unlike algorithms like RSA,`
`ElGamal, and DSA, are not vulnerable to the mathematical techniques that`
`can factor these large numbers. Hence, they reason, elliptic curve`
`algorithms are more secure than RSA and etc. There is some truth here, but`
`only if you accept the premise that elliptic curve algorithms have`
`fundamentally different mathematics. I wrote about this earlier; the short`
`summary is that you should use elliptic curve cryptography if memory`
`considerations demand it, but RSA with long keys is probably safer.`

`This event is significant for two reasons. One, most of the Internet`
`security protocols use 512-bit RSA. This means that non-cryptographers`
`will take notice of this, and probably panic a bit. And two, unlike other`
`factoring efforts, this was done by one organization in secret. Most`
`cryptographers didn’t even know this effort was going on. This shows that`
`other organizations could already be breaking e-commerce keys regularly,`
`and just not telling anyone.`

`As usual, the press is getting this story wrong. They say things like:`
`”512-bit keys are no longer safe.” This completely misses the point. Like`
`many of these cryptanalysis stories, the real news is that there is no`
`news. The complexity of the factoring effort was no surprise; there were`
`no mathematical advances in the work. Factoring a 512-bit number took`
`about as much computing power as people predicted. If 512-bit keys are`
`insecure today, they were just as insecure last month. Anyone implementing`
`RSA should have moved to 1028-bit keys years ago, and should be thinking`
`about 2048-bit keys today. It’s tiring when people don’t listen to`
`cryptographers when they say that something is insecure, waiting instead`
`for someone to actually demonstrate the insecurity.`

`http://www.cwi.nl/~kik/persb-UK.html`
`http://www.msnbc.com/news/305553.asp`

`RSA’s analysis:`
`http://www.rsa.com/rsalabs/html/rsa155.html`

`Certicom’s rebuttal:`
`http://www.certicom.com/press/RSA-155.htm`

`Prominent Web sites that still use 512-bit RSA:`

`    Travelocity`
`    Microsoft’s online store`
`    Compaq’s online store`
`    Godiva’s online store`
`    Dr. Koop.com`
`    Flowers N More`

`There are lots more. You can check yourself by connecting to a site with a`
`secure domestic version of Microsoft Internet Explorer 4.0.`
`** *** ***** ******* *********** *************`

`      Comments from Readers`

`From: Gene Spafford <spaf@cs.purdue.edu>`
`Subject: Re: Comments on the “NSA” key in Windows NT`

`Well, it is always easier to believe a conspiracy theory or dark designs.`
`However, there may be alternative explanations.`

`For instance, I happen to know that various 3-letter agencies use a lot of`
`Windows machines (in a sense, that should be scary all by itself). Suppose`
`they want to load their own highly-classified, very closely-guarded version`
`of their own crypto routines. Do you think they will send copies of their`
`code out to Redmond to get it signed so it can be loaded? Or are they`
`going to sign it themselves, with their own key, doing it in-house where it`
`is “safe”? If they are going the in-house route, then either Microsoft`
`needs to share the private key with them (bad idea), or the code needs to`
`accommodate a second key schedule generated inside the TLA. Hmmm, that`
`sounds familiar, doesn’t it?`

`Another explanation, that I may have read here (this issue has been`
`discussed on many lists) is that to get the approval for export, the folks`
`at MS needed to include a “back-up” key in case the first was compromised`
`in some way. They would need to switch over to using the alternate key for`
`all the systems already out there. But how would they do that unless the`
`second key was already installed, so they could do the switch using that`
`second key? So, if you were MS, and the NSA required you to install a`
`backup key like this, what would you call it?`

`Of course, it could be that MS wanted the backup key themselves, and the`
`programmer involved in the coding decided to name it something silly.`

`Or, there is a history of MS code being shipped with undocumented code`
`elements, and things that MS management don’t know are present. Suppose the`
`code (involving only a few lines of code) was placed there by an agent of`
`the intelligence services of some other country (it wouldn’t be that hard`
`to subvert an existing employee or place one at MS with good coding skills`
`who could eventually gain access to the appropriate code). He/she names`
`the variables with “NSA” in place in case anyone doing a code review would`
`question it -- and includes a comment block that says “The NSA required`
`this to be here -- do not change or ask questions.” The “sinister purpose”`
`might be correct, but you are blaming the wrong entity.`

`Heck, maybe this is a grand design of Mr. Gates himself: after all, he’s`
`certainly having some aggravation from the U.S. Justice Department!`

`There are other possible explanations for the name, too.`

`These alternate explanations do not mean that the extra key does not have`
`side-effects (such as clandestine installation and circumvention of the`
`export controls). And of course, we will probably never know what the`
`primary reason for this key is, nor will we know what role these`
`side-effects may have had in the decision, despite what people eventually`
`claim.`

`The key thought is that there are possible scenarios for the naming of the`
`key that do not involve nefarious activity, or do not involve such activity`
`by the NSA. That should not be the immediate conclusion people reach.`

`And, at the risk of starting some tirades, let me ask a (rhetorical)`
`question: even if it was put there for purposes of clandestine monitoring,`
`what is wrong with that? If this gets used to monitor terrorists with NBC`
`weapons, drug cartels, or weapons labs in Iraq, isn’t that what we want`
`done? In that light, there should be some concern that this has now been`
`exposed and possibly nullified!  The history of cryptography shows --`
`repeatedly -- that having crypto assets makes a huge difference in times of`
`conflict, and that getting such assets in place and working takes time. It`
`would be naive to believe that there are no such threats looming, or that`
`there is no such likelihood in the future.`

`We should be clear in our discussions as to whether our concern is the`
`presence of the code, or over who may have control of it. Is the issue`
`really one of what controls are in place that ensure that the code isn’t`
`used against inappropriate targets (e.g., law-abiding, friendly businesses`
`and citizens)?  Unfortunately, we don’t have strong assurances in this`
`realm, and there have been some past abuses (or alleged abuses). But that`
`may be moot if we the code was actually placed for some other group’s dark`
`design.`

`From: “Lucky Green” <shamrock@cypherpunks.to>`
`Subject: More NSAKEY musings`

`I’d like to comment on some of your public comments regarding the NSAKEY.`
`The goal of this email is to provide you with a few data points about the`
`mindset intelligence agencies employ when compromising systems.`

`First, I agree with your assessment that the NSA does not /need/ to`
`compromise CAPI to compromise the computers of those running Windows. Which`
`is not analogous to the claim that the NSA would not seek to compromise`
`CAPI by causing Microsoft to install the NSA’s key.`

`For the academic cryptographer, once one catastrophic flaw in a cipher has`
`been found, the work is over. “We have a 2^16th attack. The job is done.`
`Let’s go home”. Intelligence agencies don’t operate this way.`

`My work with GSM has revealed that intelligence agencies, which as we all`
`know ultimately stand behind the GSM ciphers, take a very different`
`approach. Intelligence agencies will compromise every single component of a`
`crypto system they can compromise. Intelligence agencies will, given the`
`opportunity, compromise a component just because they can, not because they`
`need to. This appears to be a somewhat perverted manifestation of`
`implementing multiple redundancy into a system. Which, as I am sure we all`
`agree, is generally a good idea.`

`In the case of GSM, we have discovered the following compromises:`

`o Compromised key generation.`

`The 64-bit keys have the last 10 bits of key zeroed out. (I heard rumors`
`that some implementations only zero out the last 8 bits, but either way,`
`this is undeniably a deliberate compromise of the entropy of the key).`

`o Compromise of the authentication system and keygen algorithm.`

`The GSM MoU was formally notified in 1989 (or 1990 at the latest) about the`
`flaws in COMP128 we discovered last year. Long before GSM was widely`
`fielded. The MoU’s Security Algorithm Group of Experts (SAGE), staffed by`
`individuals who’s identities are unknown to this day, kept this discovery`
`secret and failed to inform even the MoU’s own members. As a result,`
`intelligence agencies can clone phones and calculate the voice privacy keys`
`used during a call.`

`o Compromise of the stronger voice privacy algorithm A5/1.`

`This 64 bit cipher has numerous design “flaws”, resulting in a strength of`
`at most 40 bits. It is inconceivable to me and virtually everybody I`
`talked with that these rather obvious flaws were overlooked by A5/1’s`
`French military designers.`

`o Compromise of the weaker voice privacy algorithm A5/2.`

`The MoU admits that breakability was a design goal of A5/2, even thought`
`SAGE stated in their official analysis of A5/2 that they were unaware of`
`any cryptographic flaws in A5/2.`

`To allow for interception and decryption of GSM traffic, it would have`
`sufficed to compromise the effective key length. It would have sufficed to`
`compromise the keygen. It would have sufficed to compromise the ciphers.`
`The NSA/GCHQ did all three.`

`Given these facts, it would not be at all unusual for the NSA to install`
`backdoors in the Windows OS itself *and* have obtained a copy of`
`Microsoft’s signing key *and* have Microsoft install the NSA’s own key.`

`Think of it as well-designed failover redundant compromise.`
`From: “Kevin F. Quinn” <kevq@banana.demon.co.uk>`
`Subject: Crypto-Gram April 15 1999, and the recent “NSA” spare-key debate.`

`In Crypto-Gram April 15 1999, you mentioned the two-key approach of`
`Microsoft with regard its root keys for Authenticode, and that they`
`included the two keys “presumably for if one ever gets compromised”. We`
`now know the same approach was taken for CSP. Microsoft’s own announcement`
`on the subject is interesting; the two keys are present “in case the root`
`key is destroyed” (paraphrase). I think in your Crypto-Gram you meant`
`”destroyed” rather than “compromised” -- Microsoft seem to be trying to`
`guard against the possibility that the secret root key is burnt in a fire`
`or somesuch; they’re not guarding against unauthorised copies of the key`
`being made with the two-key approach. I think it’s an important`
`distinction to make.`

`The only good reason I can see to have two keys, is to provide security`
`against compromise -- in which case you need to validate signatures against`
`both keys (i.e., AND rather than OR). That way if one key is compromised,`
`the validation will still fail as the second signature won’t be valid. If`
`both keys are stored in separate secured locations, the attacker has to`
`break the security of both locations in order to acquire both keys, and you`
`hope that you might notice one break-in before the second occurs. The`
`sensible way to guard against the possibility of destruction (fire,`
`catastrophe etc) is to have several copies, each securely stored and`
`monitored (the same way classified documents are controlled).`

`Microsoft claim that the two-key approach was suggested by the NSA -- I`
`find it difficult to believe the NSA would suggest including two root keys,`
`to guard against destruction of a root key. My pet theory is that there`
`was a communication problem; the NSA advice went something along the lines`
`of, “having two root keys guards against loss”, meaning compromise, and`
`Microsoft took this to mean destruction.`
`From: Greg Guerin <glguerin@amug.org>`
`Subject: A new spin on the NSA-key/NT issue?`

`In your article at`
`<http://www.counterpane.com/crypto-gram-9904.html#certificates>, you end by`
`saying: “This virus doesn’t exist yet, but it could be written.” [This is`
`a virus that would replace the backup key in NT with a rogue key, and could`
`trick the user into accepting malicious code as signed.]`

`After I wrote <http://amug.org/~glguerin/opinion/win-nsa-key.html>, it`
`occurred to me that the virus now exists, or at least all the parts of it`
`do. It only needs to be “turned to the Dark Side” and assembled. The`
`”construction kit” for this virus is none other than the “repair program” at:`

`    <http://www.cryptonym.com/hottopics/msft-nsa/ReplaceNsaKey.zip>`

`All the parts are there. The “AddDelCsp.exe” program (no source provided)`
`is the active infecting agent. The “nsarplce.dll” and other DLL’s are the`
`”toxins”. The kit even includes “TestReplacement.exe” (with source) to`
`test whether an enterprising young kit-builder has made his changes`
`successfully or not.`

`I’m sorta guessing, but someone with Wintel programming skills could`
`probably construct a virus or Trojan horse with this kit in a matter of`
`hours. Probably the only skill they would have to sharpen is the crypto,`
`but there’s some nice starter info in the Fernandes report itself. A`
`little reading, a little key-generating time, maybe a little patching, and`
`presto. Try it on a local NT system, then release it to the world by`
`mirroring the Fernandes report. Or just send it to some “friends” via`
`Hotmail. It would certainly look authentic, and because even the original`
`”repair” program was unsigned, and the original report says nothing about`
`authenticating the download before running it, it could be a very`
`well-traveled Trojan horse indeed.`

`If this virulent “repair program” is written with a little restraint, it`
`can spread VERY far before anyone even notices. It could even camouflage`
`itself and name its toxic key “NSAKEY”, just like Microsoft’s original.`
`That is, after “removing” itself, it’s still present. How often do people`
`even think of checking that key?`

`If you know someone with NT programming experience, it might be interesting`
`to have them read the Fernandes report, download the virus construction`
`kit, er, I mean “repair” program, then give this a try. I’d guess that not`
`even prior virus-writing skills would be needed, just above-average NT`
`programming skills. I bet you’d have a virulent version in less than an`
`afternoon. A fine project for a lazy Labor Day holiday, eh?`
`From: Sam Kissetner`
`Subject: Meganet`

`I thought this might amuse you. The February issue of Crypto-Gram makes`
`fun of Meganet’s home page for saying:`

`    1 million bit symmetric keys -- The market offer’s [sic] 40-160`
`    bit only!!`

`I visited that page today. (The URL changed; it’s at`
`<http://www.meganet.com/index.htm>.) Maybe they read Crypto-Gram, because`
`they tried to fix the grammatical error. But it was part of a graphic, so`
`they just pasted a little white box over the apostrophe and s, leaving:`

`    1 million bit symmetric keys -- The market offer  40-160 bit only!!!`

`Gee, that’s *much* better.`
`From: Marcus Leech <mleech@nortelnetworks.com>`
`Subject: HP’s crypt(1) description`

`To be fair to HP, and crypt(1) -- HP has merely faithfully reproduced the`
`original crypt(1) MAN page. Crypt(1) first appeared in Unix V7, back`
`around 1978 or so -- at a time when DES was just starting to be used in`
`certain limited areas. That an operating system had any kind of file`
`encryption facility at all was some kind of miracle at the time. Sun has`
`obviously lightly hacked-over the documentation to reflect current reality,`
`while HP has taken the approach of staying faithful to the original`
`documentation.`
`** *** ***** ******* *********** *************`

`CRYPTO-GRAM is a free monthly newsletter providing summaries, analyses,`
`insights, and commentaries on computer security and cryptography.`

`To subscribe, visit http://www.counterpane.com/crypto-gram.html or send a`
`blank message to crypto-gram-subscribe@chaparraltree.com. To unsubscribe,`
`visit http://www.counterpane.com/unsubform.html. Back issues are available`
`on http://www.counterpane.com.`

`Please feel free to forward CRYPTO-GRAM to colleagues and friends who will`
`find it valuable. Permission is granted to reprint CRYPTO-GRAM, as long as`
`it is reprinted in its entirety.`

`CRYPTO-GRAM is written by Bruce Schneier. Schneier is founder and CTO of`
`Counterpane Internet Security Inc., the author of “Applied Cryptography,”`
`and an inventor of the Blowfish, Twofish, and Yarrow algorithms. He served`
`on the board of the International Association for Cryptologic Research,`
`EPIC, and VTW. He is a frequent writer and lecturer on computer security`
`and cryptography.`

`Counterpane Internet Security, Inc. is a venture-funded company bringing`
`innovative managed security solutions to the enterprise.`

`http://www.counterpane.com/`

`Copyright (c) 1999 by Bruce Schneier`
