AUTHOR = 'Jeremy Guillette'
SITENAME = 'Pelican Test'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
PAGINATED_TEMPLATES = {'category': None, 'author': None, 'archives': None}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theming
THEME = '/Users/jguillette/gitstuff/pelican-themes/backdrop'

SITESUBTITLE = "Hello world!"
BACKDROP_IMAGE = "images/nagai_record_store.jpg"