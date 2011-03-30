""" Necklace content-type
"""
from zope.interface import implements
from interfaces import IATNecklace
from plone.app.blob.content import ATBlob
from ana.gheorghe.content.schema import addATBlob
from ana.gheorghe.content.schema import AnaSchema

def addATNecklace(container, id, **kwargs):
    """ Add Content-type
    """
    return addATBlob(container, id, subtype='Image', klass=ATNecklace, **kwargs)

class ATNecklace(ATBlob):
    """ Necklace content-type
    """
    implements(IATNecklace)

    meta_type = portal_type = 'ATNecklace'
    _at_rename_after_creation = True
    schema = AnaSchema.copy()
