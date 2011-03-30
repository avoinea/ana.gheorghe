  # -*- extra stuff goes here -*-
from ana.gheorghe import config

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    import content

    from Products.CMFCore import utils
    from Products.Archetypes import atapi
    from Products.ATContentTypes import permission as atct

    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(config.packageName), config.packageName)

    for atype, constructor in zip(content_types, constructors):
        if atype.portal_type == 'ATEarings':
            constructor = content.earings.addATEarings
        elif atype.portal_type == 'ATBrooch':
            constructor = content.brooch.addATBrooch
        elif atype.portal_type == 'ATBracelet':
            constructor = content.bracelet.addATBracelet
        elif atype.portal_type == 'ATHair':
            constructor = content.hair.addATHair
        elif atype.portal_type == 'ATNecklace':
            constructor = content.necklace.addATNecklace

        utils.ContentInit("%s: %s" % (config.packageName, atype.portal_type),
            content_types = (atype,),
            permission = config.permissions[atype.portal_type],
            extra_constructors = (constructor,),
            ).initialize(context)
