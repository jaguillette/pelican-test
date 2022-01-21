AUTHOR = 'Jeremy Guillette'
SITENAME = 'Jeremy Guillette'
SITESUBTITLE = "That's me! This is my website."
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'docs'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Github', 'https://github.com/jaguillette'),
         ('Twitter', 'https://twitter.com/jaxguillette'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theming
THEME = 'themes/alchemy/alchemy'

# SITESUBTITLE = "Hello world!"
# BACKDROP_IMAGE = "images/nagai_record_store.jpg"
# PAGINATED_TEMPLATES = {'category': None, 'author': None, 'archives': None}

BOOTSTRAP_CSS = 'theme/css/bootstrap.min.css'

INDEX_SAVE_AS = 'blog.html'
INDEX_RENAME = 'Blog'
