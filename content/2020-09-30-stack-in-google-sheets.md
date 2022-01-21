---
layout: post
title: Stacking Data in Google Sheets
---

Have you ever been working with a spreadsheet that had a bunch of values
separated by commas, semicolons, pipes, or new lines in a single column?
Something like this?

| Recipient | Goods |
| --------- | ----- |
| Michaelangelo | pizza, nunchucks, skateboard |
| Donatello | displayport cables, Redbull |
| Leonardo | kale, seitan, courage |
| Raphael | knives, punching bag, beef, roller skates, pizza |

It makes it pretty hard to do any kind of analysis on the data, but it can be
hard to undo. A better way to represent the same data is like this:

| Recipient | Good |
| --------- | ---- |
| Michaelangelo | pizza |
| Michaelangelo | nunchucks |
| Michaelangelo | skateboard |
| Donatello | displayport cables |
| Donatello | Redbull |
| Leonardo | kale |
| Leonardo | seitan |
| Leonardo | courage |
| Raphael | knives |
| Raphael | punching bag |
| Raphael | beef |
| Raphael | roller skates |
| Raphael | pizza |

That can get fed more easily to visualization and analysis software, but it can
be difficult to get from the first dataset to the second without using code,
and when I tell some people to use Python scripts for things, they run away
from me. (This isn't true, they just get "Zoom connectivity problems" these
days).

Today I found a [really useful post on Stack Exchange](https://webapps.stackexchange.com/questions/60861/google-sheets-split-multi-line-cell-into-new-rows-duplicate-surrounding-row-e)
and generalized it a bit to make it way easier to get from data that's all
smushed together to data that's nicely stacked for analysis. I'm very excited
about it so I'm writing up this how-to.

The first step is to get your data into Google sheets, whether through
uploading, importing, copying and pasting, however you like. Just get it there.

Step two is to open up the script editor. You can find this under the "Tools"
menu in Google Sheets. We're going to be making a custom formula!

Now, copy this code block and paste it in to the script editor:

    function stackrows(range, index, on) {
      var output2 = [];

      // Iterating through spreadsheet rows with iterator i
      for(var i=0, iLen=range.length; i<iLen; i++) {
        var split_cell = range[i][index].split(on);

        // Iterating through each value that's been split with j
        for(var j=0, jLen=split_cell.length; j<jLen; j++) {
          var output1 = [];
          var split_value_j = split_cell[j].trim()

          // Iterating through values in spreadsheet rows with k
          for(var k=0, kLen=range[0].length; k<kLen; k++) {
            if(k == index) {
              output1.push(split_value_j);
            } else {
              output1.push(range[i][k]);
            }
          }
          output2.push(output1);
        }
      }
      return output2;
    }

This is a modified version of the excellent script from that
[Stack Exchange post](https://webapps.stackexchange.com/questions/60861/google-sheets-split-multi-line-cell-into-new-rows-duplicate-surrounding-row-e).
Mine is different because it's a bit more flexible, I've added some comments to
help myself remember what's happening, and I've renamed a couple of variables.
Once you've pasted in the text, save this function in your script editor.

Now there's a new function available in Google sheets. We defined "stackrows",
so now we can use it in this spreadsheet. You'll have to copy this formula into
the script editor of every spreadsheet you do this to, unless there's a better
way I don't know about (very possible).

I prefer to make a new sheet and reference the old sheet with my new formula,
but you can opt not to do that if you're okay with messier data that you'll
have to selectively copy and paste into something else eventually. Pick out the
top left corner of where you want your new data to appear, and start
typing the formula `=stackrows(`. It isn't a built-in function, so it won't
auto-complete, but it will work anyways.

I didn't rename any sheets in my [sample spreadsheet](https://docs.google.com/spreadsheets/d/1ZsGbv_tTXZxixj-GbeTxBZkQF1mgnYadRYjbV9yvSP8/edit?usp=sharing),
so my formula looks like this: `=stackrows(Sheet1!A1:B5,1,",")`. What that's
doing is running our new "stackrows" function on the range `Sheet1!A1:B5`. If
you aren't familiar with Google Sheets range syntax, after you type the opening
parenthesis in the formula, you can use your mouse to navigate to and select
the range you want. Then it's saying to split up data in the second column
(column indices start from zero, so a=0, b=1, c=2, etc.). The last thing
specified is the separator, in this case a comma. Don't forget to put quotes
around it!

That's it! You should see a bit of loading and then get your data in the new
sheet. You can even use the new sheet as the input for an even newer sheet if
you have a couple of columns with smushed together data.

Rather than fill this with screenshots, I'll just link to a
[sample spreadsheet](https://docs.google.com/spreadsheets/d/1ZsGbv_tTXZxixj-GbeTxBZkQF1mgnYadRYjbV9yvSP8/edit?usp=sharing)
that I made that demonstrates how this works. You can make your own copy to
poke at it, figure out how it works, and hopefully make use of this process
yourself.
