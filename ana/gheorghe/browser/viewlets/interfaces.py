""" Viewlets
"""
from zope.viewlet.interfaces import IViewletManager

class IPortalHeader(IViewletManager):
    """A viewlet manager that sits in the portal header
    """

class IPortalSections(IViewletManager):
    """A viewlet manager that sits in left side of the content
    """

class IPortalFooter(IViewletManager):
    """A viewlet manager that sits in the portal footer
    """
