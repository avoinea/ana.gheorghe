""" Bracelet content-type
"""
from zope.interface import implements
from interfaces import IATBracelet
from plone.app.blob.content import ATBlob
from ana.gheorghe.content.schema import addATBlob
from ana.gheorghe.content.schema import AnaSchema

def addATBracelet(container, id, **kwargs):
    """ Add Content-type
    """
    return addATBlob(container, id, subtype='Image', klass=ATBracelet, **kwargs)

class ATBracelet(ATBlob):
    """ Bracelet content-type
    """
    implements(IATBracelet)

    meta_type = portal_type = 'ATBracelet'
    _at_rename_after_creation = True
    schema = AnaSchema.copy()
