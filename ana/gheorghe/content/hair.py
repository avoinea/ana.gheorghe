""" Hair content-type
"""
from zope.interface import implements
from interfaces import IATHair
from plone.app.blob.content import ATBlob
from ana.gheorghe.content.schema import addATBlob
from ana.gheorghe.content.schema import AnaSchema

def addATHair(container, id, **kwargs):
    """ Add Content-type
    """
    return addATBlob(container, id, subtype='Image', klass=ATHair, **kwargs)

class ATHair(ATBlob):
    """ Hair content-type
    """
    implements(IATHair)

    meta_type = portal_type = 'ATHair'
    _at_rename_after_creation = True
    schema = AnaSchema.copy()
