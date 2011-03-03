""" Custom content
"""
try:
    from Products.LinguaPlone.public import registerType
except ImportError:
    from Products.Archetypes.atapi import registerType

from ana.gheorghe.config import packageName
from ana.gheorghe.content import earings
from ana.gheorghe.content import bracelet
from ana.gheorghe.content import brooch

registerType(bracelet.ATBracelet, packageName)
registerType(brooch.ATBrooch, packageName)
registerType(earings.ATEarings, packageName)
