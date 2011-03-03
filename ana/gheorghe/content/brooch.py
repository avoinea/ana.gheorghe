""" Brooch content-type
"""
from zope.interface import implements
from interfaces import IATBrooch
from plone.app.blob.content import ATBlob
from ana.gheorghe.content.schema import addATBlob
from ana.gheorghe.content.schema import AnaSchema

def addATBrooch(container, id, **kwargs):
    """ Add Content-type
    """
    return addATBlob(container, id, subtype='Image', klass=ATBrooch, **kwargs)

class ATBrooch(ATBlob):
    """ Brooch content-type
    """
    implements(IATBrooch)

    meta_type = portal_type = 'ATBrooch'
    _at_rename_after_creation = True
    schema = AnaSchema.copy()
