""" Earings content-type
"""
from zope.event import notify
from zope.lifecycleevent import ObjectCreatedEvent, ObjectModifiedEvent
from plone.app.blob.markings import markAs
from plone.app.blob.content import ATBlob
from zope.interface import implements
from interfaces import IATEarings
try:
    from Products.CMFCore.CMFCatalogAware import WorkflowAware
    hasCMF22 = True
except ImportError:
    hasCMF22 = False

def addATBlob(container, id, subtype='Blob', **kwargs):
    """ extended at-constructor copied from ClassGen.py """
    obj = ATEarings(id)
    if subtype is not None:
        markAs(obj, subtype)    # mark with interfaces needed for subtype
    if not hasCMF22:
        notify(ObjectCreatedEvent(obj))
    container._setObject(id, obj, suppress_events=hasCMF22)
    obj = container._getOb(id)
    if hasCMF22:
        obj.manage_afterAdd(obj, container)
    obj.initializeArchetype(**kwargs)
    if not hasCMF22:
        notify(ObjectModifiedEvent(obj))
    return obj.getId()

def addATEarings(container, id, **kwargs):
    """ Add Content-type
    """
    return addATBlob(container, id, subtype='Image', **kwargs)

class ATEarings(ATBlob):
    """ Earings content-type
    """
    implements(IATEarings)

    meta_type = portal_type = 'ATEarings'
    _at_rename_after_creation = True
    schema = ATBlob.schema.copy()
