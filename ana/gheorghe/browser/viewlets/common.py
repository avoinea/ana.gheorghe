from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class FooterViewlet(ViewletBase):
    index = ViewPageTemplateFile('footer.pt')
