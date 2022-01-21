---
layout: post
title: Working with Timelines
---

Earlier today, I was catching up on some of my RSS feeds, and I read [an article from Not Even Past](http://notevenpast.org/digital-teaching-a-mid-semester-timeline/) on using timelines in college classrooms. The article (by [Chris Babits](https://liberalarts.utexas.edu/history/graduate/gradstudents/profile.php?id=cmb5532)) presents a strong case for the pedagogical goals served by creating a digital timeline assignment.

The case is similar to some that I've heard and made at work, where I do my best to make digital assignments easier. Since it uses open source or freely accessible technologies, I can share some of the things that have made assignments with [Timeline JS](https://drive.google.com/drive/folders/0BzL83QaGF5vHbkZzVGNVVUVpUjQ?usp=sharing) easier.

I've helped with a couple of courses that have had students each contribute a single entry in a timeline, pulling the results together in a timeline as a point of discussion  or study aid. If you want to take that route, Google Forms make things easier.

In this kind of assignment, it's tempting to have all of the students in a course edit the same Google Sheet, which powers the timeline. If students are editing the spreadsheet themselves, however, the opportunities for error increase exponentially the larger the course.

To get around that, I've recommended hooking up the spreadsheet to a Google Form. I have a template in [this Google Drive Folder](https://drive.google.com/drive/folders/0BzL83QaGF5vHbkZzVGNVVUVpUjQ?usp=sharing), which you're free to copy and use if you like. Just copy the form into your Google Drive (from the folder, Forms don't have a view only access setting).

Once you're editing your own copy, make the response spreadsheet by clicking the green spreadsheet-y button (under Responses). As long as you do that to create the responses spreadsheet first, you can change the titles of the form fields, or even take some out, without breaking your setup.

One downside to using a Google Form is that it's a bit harder to go back and edit a timeline entry. However, it is possible. Just make sure that in the form's settings, respondents can edit their responses. Then, once a student submits their timeline entry, they can click a link to edit their response and bookmark that page, which will preserve their ability to edit that entry.

Another potential pitfall lies in attributing work to students. I'm as guilty as anyone of assuming that any slick looking system is keeping track of who I am and what I'm doing, but there's no such mechanism built in to the form I've set up. Instead, students have to either add names to their timeline entries themselves, or you can set up an extra form field for them (Timeline JS will just ignore it).

These are some tricks that I've learned after helping out with a couple of timeline assignments using Timeline JS. Hopefully they help some folks avoid some of the troubles that I've run into, so that they can focus on the real benefits of student collaboration on interactive digital timelines.

And if you're feeling particularly adventurous, you can check out this [timeline tool](https://github.com/jaguillette/fabulousTime) that I frankenstein-ed together from Timeline JS and [visjs](http://visjs.org/) to make a timeline monster capable of displaying way more timeline entries in a slightly more comfortable space. It [requires only minimal configuration and tweaking](https://www.xkcd.com/1742/).
