# Fairdrop

Airdropping coins is nothing new. Proof of work and airdrops are the 2 main ways to - try to - distribute coins from a new project in a "fair" way.  
In practice, Airdroping is a completely broken system. Technical oriented users are able to use bots, farms of accounts, fake social accounts to gather most of the coins, while regular users just can have some dust. 

Idena (https://idena.io/) solves that and gives back a real sense to air drops, with the fairness it was supposed to have. Hence "FairDrop".  
With Idena giving a strong uniqueness guarantee on the identity Fairdrop raises to a new level an effectively makes it sure the coins are sent to various person and groups. 

This is a game changer for a lots of crypto projects.  
Fairdrop aims to become the reference for really fair Airdrops with a high granularity level.

## Current version

Current version is based upon a Python webserver and uses a custom made Idena authentification library.  
The auth library itself is an implementation of the "Sign in with Idena" protocol, and works with the official Idena app.

Code is being cleaned up a little bit and now fully released, with our website launched.

We release all the code under the MIT open source Licence.  

Graphic, design work and textual content are tailor made for the Fairdrop.io website that runs the service and can't be used publicly without prior authorization.

This project was submitted to the "Sign in with Idena" contest: https://gitcoin.co/issue/idena-network/idena-go/431/4364


## Pros for an Idena User
Using the app only requires a login from time to time to keep an "active" status.  
This is done in 2 clicks with no user nor password, thanks to the "sign in with idena" feature.  
Idena users are used to do more work (flips, validation ceremony) to gather coins. This is an easy and no cost involved operation.  
What idena user wouldn't get free coins from teams and sponsors? Not even giving away personal detail nor email...

## Use of Idena state
Eventhough the coin's teams and sponsors don't have personnal details from Idena users, they can target or modulate what the offer depending on the status.  
Humans for instance proved they were able of consistently focus on a task and be good at it. It's likely they will also use a similar focus to dig the coin they are given.  
In that perspective, it's likely teams give more to humans than verified, and more to verified than to newbies or candidates.

The higher in the hierarchy, the less chance this is a temp and throwable account, the more likely the coins will be put to good use and serve as effective promotion for the project.

## Impact on Idena Eco system
First impact is a technological helper. We developed the "Sign in with Idena" backend in python, from scratch by following the official specs.  
Instead of relying on the official Go/Postgresql implementation, we now have - and release as open source - a simple Python module that can be used as part of a server or in an autonomous way, integrated to any python app.  
This will be a nice help for any Python dev willing to use "sign in with idena" feature.  

Second impact is reaching out to other coins and projects.  
Idena is not pow nor pos, it does not compete with other coins that all have a specific target (privacy, nft, smart contracts....).  
What idena does and does well is ensure identities are unique and driven by humans.

In that perspective, many chains would gain by building bridges with Idena.  
Airdropping is a nice way to move toward that goal, since it's an easy move that does not require any specific technical work.  
This allows for other projects to be aware of idena and its strength, and hopefully they will consider using it for more.  

Last impact is on the Idena user base itself.  
Since you need to have an Idena id to be eligible to Fairdrops, and fairdrops should provide greater amounts than unfair ones, freebie seekers will enroll with Idena and try to maintain an account there.  
So this Fairdrop project should foster a continuous user base growth.

## More insights
See companion files `install_notes.md` and `auth_module.md`.

## Support the project
If you want to support the project then please consider donating ETH or DNA to below-mentioned wallet address or create an issue or PR here on GitHub.

ETH/DNA: `0xe2fc55e0c06a036319b28cc9ebd99a0dc75f0785`
