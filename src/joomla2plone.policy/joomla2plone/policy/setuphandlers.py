# -*- coding: utf-8 -*-

from joomla2plone.policy.utils import createFolder

def remove_default_content(site):
    """Borra el contenido creado en la instalación de Plone"""

#    removable = ['Members','news','events','front-page']
    removable = ['Members','events','front-page']

    for item in removable:
        if hasattr(site, item):
            site.manage_delObjects([item])

def create_site_structure(site) :
    """Crea la estructura del sitio migrado"""

    createFolder(site, u'Artículos',
                 allowed_types=['News Item','collective.nitf.content'],
                 exclude_from_nav=True)

    createFolder(site, u'Encuestas',
                 allowed_types=['collective.polls.poll'],
                 exclude_from_nav=True)

    createFolder(site, u'Contenidos',
                 allowed_types=['Document','Link','Image','File'],
                 exclude_from_nav=True)

    createFolder(site, u'Multimedia',
                 allowed_types=['Image','File'],
                 exclude_from_nav=True)

def setupVarious(context):
    """
    Método que ejecuta los pasos de personalización
    """

    if context.readDataFile('joomla2plone.policy-default.txt') is None:
        return

    portal = context.getSite()
    remove_default_content(portal)
    create_site_structure(portal)
