# -*- coding: utf-8 -*-
import sphinx_bootstrap_theme
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

html_theme_options = {
    'navbar_site_name': "Contents",
    'navbar_links': [
        ('<i class="fab fa-github fa-lg"></i>', "https://github.com/TaiSakuma/urbanoctowaddle", True),
    ],
    'navbar_sidebarrel': False,
    'navbar_pagenav': False,
    'source_link_position': "footer",
    'bootswatch_theme': "yeti",
    'bootstrap_version': "3",
}

templates_path_theme = ['conf_theme/sphinx_bootstrap_theme/templates']
html_static_path_theme = ['conf_theme/sphinx_bootstrap_theme/static']

##__________________________________________________________________||
