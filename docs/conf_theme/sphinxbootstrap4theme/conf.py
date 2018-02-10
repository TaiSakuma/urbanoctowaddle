# -*- coding: utf-8 -*-
import sphinxbootstrap4theme
html_theme = 'sphinxbootstrap4theme'
html_theme_path = [sphinxbootstrap4theme.get_path()]

# https://github.com/myyasuda/sphinxbootstrap4theme
# http://myyasuda.github.io/sphinxbootstrap4theme/setup.html#instllation

html_theme_options = {
    # Navbar style.
    # Values: 'fixed-top', 'full' (Default: 'fixed-top')
    'navbar_style' : 'fixed-top',

    # Navbar link color modifier class.
    # Values: 'dark', 'light' (Default: 'dark')
    'navbar_color_class' : 'dark',

    # Navbar background color class.
    # Values: 'inverse', 'primary', 'faded', 'success',
    #         'info', 'warning', 'danger' (Default: 'inverse')
    'navbar_bg_class' : 'inverse',

    # Show global TOC in navbar.
    # To display up to 4 tier in the drop-down menu.
    # Values: True, False (Default: True)
    'navbar_show_pages' : True,

    # Link name for global TOC in navbar.
    # (Default: 'Pages')
    'navbar_pages_title' : 'Pages',

    # Specify a list of menu in navbar.
    # Tuples forms:
    #  ('Name', 'external url or path of pages in the document', boolean)
    # Third argument:
    # True indicates an external link.
    # False indicates path of pages in the document.
    'navbar_links' : [
         ('Home', 'index', False),
         ("Link", "http://example.com", True)
    ],

    # Total width(%) of the document and the sidebar.
    # (Default: 80%)
    'main_width' : '80%',

    # Render sidebar.
    # Values: True, False (Default: True)
    'show_sidebar' : True,

    # Render sidebar in the right of the document.
    # Values：True, False (Default: False)
    'sidebar_right': False,

    # Fix sidebar.
    # Values: True, False (Default: True)
    'sidebar_fixed': True,

    # Html table header class.
    # Values: 'inverse', 'light' (Deafult: 'inverse')
    'table_thead_class' : 'inverse'
}

templates_path_theme = ['conf_theme/sphinxbootstrap4theme/templates']

##__________________________________________________________________||
