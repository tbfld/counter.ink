---
title: 2017-12-28-whence-and-whither-btc
description:
extract:
created: 2024-11-17 17:08
updated: 2025-02-14 22:04
author:
images:
order:
enableToc:
permalink:
aliases:
draft:
publish:
date: 2017-12-28
tags:
- cryptography
- history
- language
- right
- technology
- theory
---

To: nettime-l
Subject: Re: <nettime> Ten years in, nobody has come up with a use for blockchain
From: byfield
Date: [Thu, 28 Dec 2017 14:11:51 -0500](https://nettime.org/Lists-Archives/nettime-l-1712/msg00061.html)

On 28 Dec 2017, at 4:46, nettime’s avid reader wrote:

> Ten years in, nobody has come up with a use for blockchain
> 
> 	https://hackernoon.com/ten-years-in-nobody-has-come-up-with-a-use-case-for-blockchain-ee98c180100
> 
> Dec 22, 2017
> Kai Stinchcombe
> 
> Everyone says the blockchain, the technology underpinning cryptocurrencies such as bitcoin, is going to change EVERYTHING. And yet, after years of tireless effort and billions of dollars invested, nobody has actually come up with a use for the blockchain—besides currency speculation and illegal transactions.
> 
> Each purported use case — from payments to legal documents, from escrow to voting systems—amounts to a set of contortions to add a distributed, encrypted, anonymous ledger where none was needed. What if there isn’t actually any use for a distributed ledger at all? What if, ten years after it was invented, the reason nobody has adopted a distributed ledger at scale is because nobody wants it?
> 
>  <...>

I lost interest in Bitcoin a while ago beyond occasionally ruing the alt.fact that, after spending years and years paying attention to cypherpunks+ lists, I guess I could have been one of the first few hundred people to screw around with it. So what I say here is based largely on happy ignorance about most of what’s being claimed now — or, if you like, based on a clearer understanding where it came from rather than ***topian noise about where it’s supposedly headed. Having admitted that...

This avid-reader article seems like a flurry of angry complaints, many based on unexamined assumptions.

Bitcoin began as a sort of thought experiment, more than anything else: a proof of concept, driven more or less by the dictum that ‘cypherpunks write code.’ That phrase itself was a reaction: the significant distinction was that most people *don’t* write code, or that they write something other than code (laws, for example — hence Lessig’s book *Code*). The phrase first appeared in Eric Hughes’s *Cypherpunks Manifesto* (1993), but that short essay had lots of other phrases in it that didn’t become world-changing slogans shouted by the same crowd who brought you things like PGP, Wikileaks, BitTorrent, TOR, OpenSSL, Signal, warrant canaries, etc. ‘Cypherpunks write code’ became the go-to mantra on the cypherpunks mailing list as that list descended into endless Hayekio-Vingean ranting and worse — it was basically the list’s in-joke way of saying ‘STFU.’ When the meta-meta-meta-ranting on cypherpunks became too much, Perry Metzger started another mailing list, ‘cryptography,’ whose seemingly neutral name masked the implied polemic: no ‘punk’ political noise. It was there some time later that Bitcoin was first announced.

	https://www.activism.net/cypherpunk/manifesto.html
	https://web.archive.org/web/20150331182052/http://www.mail-archive.com/cryptography@metzdowd.com/msg13215.html

(Most nettimers know a bit about Hayek, but Vernor Vinge maybe not. His sci-fi-fi writings were constantly invoked by the cypherpunks crowd — mostly his novella *True Names*, but I think his space opera *A Deepness in the Sky* is more relevant in this context: the dialectic of localizers.)

	https://en.wikipedia.org/wiki/A*Deepness*in*the*Sky

Bitcoin’s success has led to a sort of Whig Interpretation of History 
that hoovers up all kinds of anti/idealistic nonsense and obscures its 
proof-of-concept origins. Those origins are important in this context, 
now, because they can help us to cut through a lot of the current 
Bitcoin ravings. This avid-reader essay is a pure expression of that 
whiggish view: the author complains about pretty much everything 
including the kitchen sink. In contrast, here’s the abstract from 
Satoshi’s original paper proposing Bitcoin:

> Abstract. A purely peer-to-peer version of electronic cash would allow online payments to be sent directly from one party to another without going through a financial institution. Digital signatures provide part of the solution, but the main benefits are lost if a trusted third party is still required to prevent double-spending. We propose a solution to the double-spending problem using a peer-to-peer network. The network timestamps transactions by hashing them into an ongoing chain of hash-based proof-of-work, forming a record that cannot be changed without redoing the proof-of-work. The longest chain not only serves as proof of the sequence of events witnessed, but proof that it came from the largest pool of CPU power. As long as a majority of CPU power is controlled by nodes that are not cooperating to attack the network, they’ll generate the longest chain and outpace attackers. The network itself requires minimal structure. Messages are broadcast on a best effort basis, and nodes can leave and rejoin the network at will, accepting the longest proof-of-work chain as proof of what happened while they were gone.

	https://bitcoin.org/bitcoin.pdf

But, as they say, read the whole thing — it’s just a few pages, and in its bare-bones clarity its reads more like an IETF RFC than a revolutionary manifesto. That suggests one useful way to understand Bitcoin mania: it bears the same relation to the basic insight of Bitcoin that pop debates about the alt.right relate to, say, RFC 1866, ‘Hypertext Markup Language - 2.0.’

	https://www.rfc-editor.org/rfc/rfc1866.txt

The *goal* of the Bitcoin proof of concept was ‘an electronic payment system based on cryptographic proof instead of trust, allowing any two willing parties to transact directly with each other without the need for a trusted third party.’ So when the author of this avid-reader essay complains ‘but Visa... but FDIC... but NASDAQ,’ one reasonable response is: ¯\*(ツ)*/¯. The point of Bitcoin wasn’t to succeed to the degree that it has, or in the way that it has. Instead, it was a rough prototype for a networked ‘cash system’ that wouldn’t *necessarily depend on* third parties to provide a bullet list of services that, together, sketch out ‘trust’ as it’s mostly experienced in consumer society: processing transactions, mediating disputes, verifying identities, defining and enforcing jurisdictions, and so on.

Now, obviously, the avid-reader author hopes to intervene in in the popular madness of Bitcoin, so it makes sense for him (I assume him) to spell out how and why it’s less efficient / scalable than VISA, riskier than FDIC-backed deposits, and all the rest. At the same time, though, the project he announces is a bit different: showing that the blockchain is rubbish.

Like everyone else, I don’t know what’ll happen with Bitcoin. Perry Metzger recently did a very back-of-the-envelope calculation that for Bitcoin to reach the million-dollar mark would require something like the current global output of electricity — which seems like a hard limit. But within that all I can say is that it seems to be the first globally distributed ponzi-ish scheme. If that’s roughly right, the good news is that it’ll turn out to be something like the AOL of digital currencies. The bad news is that there are ~150 suckers born every minute, and probably about as many new exotic financial products that depend in some arbitrary, opaque, derivative way on Bitcoin’s value increasing. So a correction may take a while yet.

But none of that really has to do with the rough idea of a blockchain. Indeed, if anything of enduring value comes from Bitcoin (aside from massive ‘creative destruction,’ with all the human misery that’ll likely entail), I think it will be that very unsexy idea — which boils down to little more than making it cheaper to make certain kinds of history now than to forge it later on. Again, if Bitcoin didn’t quite get that right, ¯\*(ツ)*/¯. It’s an RFC, a request for comments, and the failures the avid-reader author lists off are comments. If it crashes, that too will be a comment.

In itself, this isn’t really a new idea, or at least it can be seen as an incremental variation on the ancient idea of provenance: how do we know where something comes from? The aim in Bitcoin is to make it easier to verify the answer and harder to fake it. That’s it. But history isn’t linear, and some ‘increments’ are more important than others. The key difference in this case is the effort to make that real/fake distinction easier to automate. I think that step toward automating that distinction will turn out to be very significant. But not as a fetishized or even noticeable thing in itself. Think of bar codes or PLU stickers on agricultural products: we don’t need to archive for all of eternity where that avocado came from, we just need to know for limited purposes in specific contexts to facilitate certain kinds of transactions at particular points — which, as it happens, are cogs in a much deeper, detailed, distributed negotiation between administrative structures and, for lack of a better term, actual stuff.

But this is where the Hayekio-Vingean origins of Bitcoin matter: whatever Satoshi’s ‘intent’ was, Bitcoin was deeply informed by the ideas of a milieu that was implacably hostile to ‘trusted third parties’ — which mostly meant government and some of the peculiar commercial creatures it enables (VISA, FDIC, NASDAQ, for example). Bitcoin was a demo of an attack on a dominant global model of *trust*: a working-code prototype of a system in which the end user — i.e., whoever would accept BTC — is responsible for validating it. Blockchain-inspired techniques will be widely implemented, I think, but in the social and political context of systemic changes that shift more and more of that function — assessing risk — away from ‘government’ and onto the end user.

That’s why, again, it’s worth reading Satoshi’s paper — it’s clear about one systemic weakness: ‘The system is secure as long as honest nodes collectively control more CPU power than any cooperating group of attacker nodes.... If a majority of CPU power is controlled by honest nodes, the honest chain will grow the fastest and outpace any competing chains.... The incentive may help encourage nodes to stay honest.... As such, the verification is reliable as long as honest nodes control the network, but is more vulnerable if the network is overpowered by an attacker.’ And so on, again and again. It’s remarkable — hilarious, even — how often the word ‘honest’ appears in the paper, and how deeply Bitcoin relies on ‘honesty’ without any serious effort to define what it means. Normally, I wouldn’t expect a writer to define such a seemingly self-evident idea, but in the context of an effort to dismantle trust we should probably make an exception.

It may well be that Bitcoin is based on sufficiently sound cryptographic theory and practice that it’ll remain secure against ‘dishonest’ attacks *within* the system. In that case, Bitcoins may prove to have durable value — maybe in the way that certain postage stamps have drifted from everyday use to historical fetishists for hobbyists to collect. That’s not a prediction — again, I don’t know. But as blockchain-inspire techniques are integrated into general-purpose systems — again, with limited purposes in specific contexts to facilitate certain kinds of transactions at particular points — they won’t have anything to do with Bitcoin. And every one of them will be vulnerable to attacks from ‘without’ — outside of — their narrowly oriented focus. Some of them will be quick-and-dirty thefts, others will be bogglingly long and deep cons, and all of them will be vulnerable to ‘dishonest’ attackers operating at every level from every perspective.

The standard responses to that kind of concern is ‘the market will sort it out,’ but which market? The store where you buy an avocado is just an immediate, tangible manifestation: as with PLU codes, behind them there are markets upon markets upon markets that make that sticker useful: meta-markets, meta-meta-markets, derivative markets, etc. These meta- and derivative markets will define the values built into blockchain-inspire techniques, and their main criteria will be how effectively they shift risk-assessment functions onto the end user.

The author of the avid-reader essay asked ‘What if, ten years after it was invented, the reason nobody has adopted a distributed ledger at scale is because nobody wants it?’ One answer: who cares what you want? The answer is *a lot of people* — but not for the same reasons you do. Here’s another way to think about what this might mean: a world of honesty but without trust.

Cheers,
Ted

