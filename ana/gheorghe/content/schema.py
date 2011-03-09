""" Ana schema
"""
try:
    from Products.CMFCore.CMFCatalogAware import WorkflowAware
    hasCMF22 = True
except ImportError:
    hasCMF22 = False
from zope.event import notify
from zope.lifecycleevent import ObjectCreatedEvent, ObjectModifiedEvent
from plone.app.blob.markings import markAs
from plone.app.blob.content import ATBlob
from Products.ATContentTypes import ATCTMessageFactory as _
from Products.Archetypes import atapi

AnaSchema = ATBlob.schema.copy() + atapi.Schema((
    atapi.StringField('code', schemata='default',
        required=True, languageIndependent=True,
        widget=atapi.StringWidget(
            label=_(u"label_code", default=u"Cod"),
            description=_(u"help_code",
                          default=(u"Cod produs (ex. 01-0014. 01: cercei, "
                                   "02: brosa, 03: bratara)")),
            dollars_and_cents=True,
        )),
    atapi.FloatField('price', schemata='default',
        required=True, languageIndependent=True,
        widget=atapi.DecimalWidget(
            label=_(u"label_price", default=u"Pret"),
            description=_(u"help_price",
                          default=u"Pret produs RON (ex. 13.99)"),
            dollars_and_cents=True,
        )),
    atapi.LinesField('color', schemata='default',
        required=True, languageIndependent=True,
        multiValued=True,
        widget=atapi.KeywordWidget(
            label=_(u"label_color", default=u"Culoare"),
            description=_(u"help_color",
                default=u"Culori produs (ex. verde, rosu). O culoare pe linie"),
        )),
    atapi.LinesField('material', schemata='default',
        required=False, languageIndependent=True,
        multiValued=True,
        widget=atapi.KeywordWidget(
            label=_(u"label_material", default=u"Materie prima"),
            description=_(u"help_material",
                default=u"Material, pietre folosite (ex. argint, aur, emerald, "
                         "portelan). Unul pe linie"),
        )),
))

def addATBlob(container, id, subtype='Blob', klass=None, **kwargs):
    """ extended at-constructor copied from ClassGen.py """
    obj = klass(id)
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
