""" Custom content
"""
try:
    from Products.LinguaPlone.public import registerType
except ImportError:
    from Products.Archetypes.atapi import registerType

from ana.gheorghe.config import packageName
from ana.gheorghe.content import earings

registerType(earings.ATEarings, packageName)
