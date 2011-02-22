""" Viewlets
"""
from zope.viewlet.interfaces import IViewletManager

class IPortalHeader(IViewletManager):
    """A viewlet manager that sits in the portal header
    """

class IPortalFooter(IViewletManager):
    """A viewlet manager that sits in the portal footer
    """
