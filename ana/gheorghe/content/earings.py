""" Earings content-type
"""
from zope.interface import implements
from interfaces import IATEarings
from plone.app.blob.content import ATBlob
from ana.gheorghe.content.schema import addATBlob
from ana.gheorghe.content.schema import AnaSchema

def addATEarings(container, id, **kwargs):
    """ Add Content-type
    """
    return addATBlob(container, id, subtype='Image', klass=ATEarings, **kwargs)

class ATEarings(ATBlob):
    """ Earings content-type
    """
    implements(IATEarings)

    meta_type = portal_type = 'ATEarings'
    _at_rename_after_creation = True
    schema = AnaSchema.copy()
