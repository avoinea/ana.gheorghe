from zope.interface import Interface

class IContent(Interface):
    """ Ana Gheorghe content
    """

class IATEarings(IContent):
    """ Marker interface for Earings content-type
    """

class IATBracelet(IContent):
    """ Marker interface for Bracelet content-type
    """

class IATBrooch(IContent):
    """ Marker interface for Brooch content-type
    """

class IATHair(IContent):
    """ Marker interface for Hair content-type
    """
