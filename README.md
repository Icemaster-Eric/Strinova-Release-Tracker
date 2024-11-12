# Strinova Release Tracker

[Strinova](https://www.strinova.com/?lang=en-US) is an anime-style third-person tactical competitive shooter. I was able to play in the last closed beta they held during Oct 10 - Oct 21, and thoroughly enjoyed it. It's set to release this year, but so far there hasn't been any news about the release date yet.

That's why I created this website: **to predict the release date of Strinova through their preregistration numbers**. This is possible because many games will only release after they hit their preregistration milestones, in order to seem like the game is well-received. It's an extremely common practice for developers to simply nudge their preregistration numbers all the way to their milestones.

![image](https://github.com/user-attachments/assets/107ce964-5b2d-42dc-9fb2-b8372e1ba8b2)

We're currently at 4.4m preregistrations, so quite a ways from the 6m goal. I decided to try and predict when we'll pass the 6m mark, so I cooked up a [selenium script](https://github.com/Icemaster-Eric/Strinova-Release-Tracker/blob/main/prereg_counter.py) that scrapes the website's preregistration data once every 10 minutes, and then made a website to visualize and analyze the data.

To my surprise, the preregistrations are going up at a nearly linear pace (check it out in the website)! This is an obvious sign that the developers are artificially manipulating the preregistration numbers, but it also allows me to accurately predict when the preregistrations will hit their set milestones.
