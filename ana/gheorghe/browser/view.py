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
        brains = ctool(
            object_provides='ana.gheorghe.content.interfaces.IContent',
            sort_on='effective', sort_order='reverse')

        for brain in brains:
            yield brain
