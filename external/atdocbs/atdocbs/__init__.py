# Tai Sakuma <tai.sakuma@gmail.com>
import os

version = 0.1

def path():
    return [os.path.abspath(os.path.dirname(os.path.dirname(__file__)))]

def update_context(app, pagename, templatename, context, doctree):
    context['atdocbs_version'] = version.__version__

def setup(app):
    # add_html_theme is new in Sphinx 1.6+
    if hasattr(app, 'add_html_theme'):
        theme_path = os.path.abspath(os.path.dirname(__file__))
        app.add_html_theme('atdocbs', theme_path)
    app.connect('html-page-context', update_context)
    return {'version': version }
