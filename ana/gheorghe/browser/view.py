""" View controllers
"""
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

class Cooliris(BrowserView):
    """ Cooliris view controller
    """
    def children(self):
        """ Items to display
        """
        ctool = getToolByName(self.context, 'portal_catalog')
        brains = ctool(portal_type='ATBracelet')

        for brain in brains:
            yield brain

        brains = ctool(portal_type='ATEarings')
        for brain in brains:
            yield brain

        brains = ctool(portal_type='ATBrooch')
        for brain in brains:
            yield brain
