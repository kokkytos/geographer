AUTHOR = 'Leonidas Liakos'
SITENAME = 'Λεωνίδας Λιάκος - Γεωγράφος. Leonidas Liakos - Geographer'
SITEURL = 'https://geographer.gr'
#SITEURL = ''
BANNER = '../extra/header_left_bg.png'
BANNER_SUBTITLE = 'This is my subtitle'
BANNER_ALL_PAGES = True
DISQUS_SITENAME = 'geographer'
GOOGLE_ANALYTICS = "UA-116514702-1"


PATH = 'content'

TIMEZONE = 'Europe/Athens'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
SHOW_ARTICLE_CATEGORY = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
BOOTSTRAP_NAVBAR_INVERSE =True
#DISPLAY_ARTICLE_INFO_ON_INDEX =True
DISPLAY_TAGS_ON_SIDEBAR =True
DISPLAY_TAGS_INLINE=True
TAGS_URL="tags.html"
DISPLAY_CATEGORIES_ON_SIDEBAR = True
SIDEBAR_ON_LEFT = False
DISABLE_SIDEBAR_TITLE_ICONS = False


# Blogroll
LINKS = (('GISlab', 'https://gislab.gr/'),
        ('European Soil Data Centre', 'https://esdac.jrc.ec.europa.eu/'),
        ('Ε.ΓΕΩ', 'https://geographers.gr/'),
         
        )

# Social widget
SOCIAL = (('Linkedin', 'https://www.linkedin.com/in/leonidasliakos'),
          ('Twitter', 'https://twitter.com/leonidasliakos'),
          ('Github', 'https://github.com/kokkytos'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


STATIC_PATHS = ['images',
                'extra',
                'html',
                'extra/CNAME',]



# https://stackoverflow.com/a/61572517
# https://docs.getpelican.com/en/stable/tips.html#copy-static-files-to-the-root-of-your-site
EXTRA_PATH_METADATA = {
'extra/CNAME': {'path': 'CNAME'},
'html/map.html': {'path': 'html/map.html'},
'html/m.html': {'path': 'html/m.html'},
'html/m_files/leaflet-1.3.1/leaflet.js': {'path': 'html/m_files/leaflet-1.3.1/leaflet.js'},
'html/m_files/leaflet-1.3.1/leaflet.css': {'path': 'html/m_files/leaflet-1.3.1/leaflet.css'},
'html/m_files/leaflet-1.3.1/images/marker-icon.png': {'path': 'html/m_files/leaflet-1.3.1/images/marker-icon.png'},
'html/m_files/leaflet-1.3.1/images/layers.png': {'path': 'html/m_files/leaflet-1.3.1/images/layers.png'},
'html/m_files/leaflet-1.3.1/images/marker-shadow.png': {'path': 'html/m_files/leaflet-1.3.1/images/marker-shadow.png'},
'html/m_files/leaflet-1.3.1/images/layers-2x.png': {'path': 'html/m_files/leaflet-1.3.1/images/layers-2x.png'},
'html/m_files/leaflet-1.3.1/images/marker-icon-2x.png': {'path':'html/m_files/leaflet-1.3.1/images/marker-icon-2x.png'},
'html/m_files/leafletfix-1.0.0/leafletfix.css': {'path': 'html/m_files/leafletfix-1.0.0/leafletfix.css'},
'html/m_files/Proj4Leaflet-1.0.1/proj4leaflet.js': {'path': 'html/m_files/Proj4Leaflet-1.0.1/proj4leaflet.js'},
'html/m_files/leaflet-binding-2.0.4.1/leaflet.js': {'path': 'html/m_files/leaflet-binding-2.0.4.1/leaflet.js'},
'html/m_files/proj4-2.6.2/proj4.min.js': {'path': 'html/m_files/proj4-2.6.2/proj4.min.js'},
'html/m_files/rstudio_leaflet-1.3.1/rstudio_leaflet.css': {'path': 'html/m_files/rstudio_leaflet-1.3.1/rstudio_leaflet.css'},
'html/m_files/rstudio_leaflet-1.3.1/images/1px.png': {'path': 'html/m_files/rstudio_leaflet-1.3.1/images/1px.png'},
'html/m_files/jquery-1.12.4/jquery.min.js': {'path': 'html/m_files/jquery-1.12.4/jquery.min.js'},
'html/m_files/htmlwidgets-1.5.4/htmlwidgets.js': {'path':'html/m_files/htmlwidgets-1.5.4/htmlwidgets.js'},
}


# Arguments passed into pandoc
PANDOC_ARGS = [
    "--mathjax",
]




# Non-Pandoc Extensions that are not enabled by default in pandoc
#   https://pandoc.org/MANUAL.html#non-pandoc-extensions
PANDOC_EXTENSIONS = [
    "+abbreviations",
    "+backtick_code_blocks",
    "+emoji",
    "+strikeout",
    "+superscript",
    ]


THEME = "/home/leonidas/Documents/Documents/Diafora/pelican-themes/pelican-bootstrap3/"


PLUGIN_PATHS = ['/home/leonidas/Documents/Documents/Diafora/pelican-plugins', ]
PLUGINS = ['i18n_subsites','tag_cloud', 'share_post',]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}



ARTICLE_EXCLUDES = ['html']

# PHOTO_LIBRARY = "/home/leonidas/Pictures/images"
# PHOTO_GALLERY = (1024, 768, 80)
# PHOTO_ARTICLE = (760, 506, 80)
# PHOTO_THUMB = (192, 144, 60)
# PHOTO_SQUARE_THUMB = False
# PHOTO_PROFILING_ENABLED = True


#SHARIFF = True
#SHARIFF_LANG = 'en'
#SHARIFF_ORIENTATION = "horizontal"
#SHARIFF_THEME = "gray"

#https://stackoverflow.com/questions/67141040/pelican-how-to-remove-html-extension-on-local-host
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'



