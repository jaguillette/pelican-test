Title: First steps
Date: 2022-01-04
Category: update

Since this is a blog generator, might as well test it with documenting the process of setting it up. I'm set up in a fresh python virtual environment, and so far I've installed the following packages as they've come up:

    pelican
    markdown
    ghp-import

I set up this repository with `pelican-quickstart`, and since I knew I wanted to use github pages, I set up my repository as well, so I could set the base url to `https://jaguillette.github.io/pelican-test` from the jump. I also configured the automation to be set up for deploying to github pages, just following the prompts.

The first time I ran `pelican content` to generate the site, it failed and said it couldn't find any files it recognized, but didn't list markdown as something it was looking for, so I ran `pip install markdown`. After that `pelican content` and `pelican --listen` were both happy to run.

I took a look at the `Makefile` to see what kinds of options I have. I saw `make publish`, but that looks like it'll just generate with production settings. `make github` looked like the ticket, but at first it complained because I didn't have `ghp-import` (GitHub pages import). Then it complained because I forgot to initialize the repo. I did that and added the remote origin, then ran `make github` again. That pushed a `gh-pages` branch to the repo, which happened to be the first branch. That just has the site content. I set up my `.gitignore`, then pushed the main code to `main`, which I had to make the default branch since `gh-pages` was there first. The repo was already set up to deploy though, and looks to work.