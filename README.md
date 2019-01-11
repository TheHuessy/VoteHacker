# VoteHacker
My first interactive web crawler used to cheat at an office poll.

## Background

One of my co-workers was getting married and the office collected money to spend on a gift from their wedding registry. I overheard that the co-worker's spouse had expressed interest in an Xbox, but had been discouraged from putting it on the registry, and I figured it would be funny to get hte co-worker the Xbox that their to-be spouse wanted. 

Not everyone in the office saw the humor in getting someone a gift for someone else and so a poll was made and sent out for everyone to vote on. This was my opportunity to strike!

## Method

The crawler is relatively simple. In order to reproduce this, you will need to install not just the selenium package in python, but also the gecko web driver. Once gecko is installed, you will be good to go. Furthermore, this crawler works because the poll site being used, poll-maker.com, is not a very complex site and the poll wasn't set up to keep people from voting more than once. Again, with all of these condtions, it was my moment to "persuade" democracy in the direction I thought it should go in.

The crawler goes out to the poll URL, finds two buttons: the choice for Xbox and the "vote" button, clicks them in the correct order, and then reloads the page and keeps doing it. It is set up, via a while loop connected to the variable `voting` to iterate, subtracting 1 from `voting` each iteration, until the value of `voting` is zero.

The crawler also opens and immediatly minimizes the the window so that the crawl can go on without anyone who happens to be passing by seeing that I'm cheating.

**NOTE** It turned out that everyone cheated on the poll manually, sitting at their desks clicking and reloading to skew the results away from Xbox. I was the only one to build a bot to my cheating for me, so I feel rather superior especially since we're in an IT department.

## Future Applications

This sort of crawler is useful because it shows one how to go to a relatively unprotected page and interact with different aspects of the site. The crawler uses Xpath locations to find the various elements it wants to interact with and then executes built in commands (`.click()`) to carry out the actual interaction. 

This could be done to any site where a user needs to repeat repetitive tasks. It is also a decent way to scrape a website without triggering an IP ban as it takes more time to interact with the site as opposed to simply calling specific, procedurally build URLs over and over again from the same IP.
