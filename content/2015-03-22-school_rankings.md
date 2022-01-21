---
Title: High School Rankings in the US
---

Where are the best high schools in the US?
==========================================

That's a question that occurred to me when I saw [this ranking data from Niche](https://k12.niche.com/rankings/public-high-schools/best-overall/) on Facebook.

Niche uses [a number of factors](https://k12.niche.com/rankings/methodology/) for its rankings, but one thing that I really wanted to see was if there were any concentrations of great schools anywhere in the US.

So, a bit of scraping, a bit of geocoding, and with some help from CartoDB, I whipped up a couple of maps. Here's the whole US:

<iframe width='100%' height='520' frameborder='0' src='https://jaguillette.cartodb.com/viz/0806c1ba-d0fa-11e4-b148-0e9d821ea90d/embed_map' allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

You might notice that Chicago, New York City, San Francisco, and Los Angeles all have a lot of top-ranking high schools in their metro areas. I also noticed that there aren't that many top-ranking high schools that aren't near fairly large cities. My guess is that this is just a population effect, but I haven't done the math to confirm this idea.

I also looked at Massachusetts and Pennsylvania:

<iframe width='100%' height='520' frameborder='0' src='https://jaguillette.cartodb.com/viz/a57a15f4-d0f6-11e4-b1a0-0e0c41326911/embed_map' allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

<iframe width='100%' height='520' frameborder='0' src='https://jaguillette.cartodb.com/viz/8b1285fc-d0f6-11e4-b1a0-0e0c41326911/embed_map' allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

In both, there's a definite bias towards major cities in the area, with Philly having a few more top-ranked high schools than Pittsburgh in Pennsylvania, and the Boston area (inside 495) eclipsing Worcester and Springfield in Massachusetts.

This data is definitely more suggestive than it is definite, but I think it's valuable to look at data from different angles to have more of a conversation about it, particularly with school rankings.

If you're interested, I put the code I used for this up [on GitHub](https://github.com/jaguillette/top100schools). You should be able to run it on an Anaconda Python installation, and it's not super difficult to generate new CSVs from different states to put into your own maps.
