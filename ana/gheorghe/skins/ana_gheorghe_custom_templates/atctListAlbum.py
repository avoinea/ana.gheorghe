## Script (Python) "atctListAlbum"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=images=0, folders=0, subimages=0, others=0
##title=Helper method for photo album view
##
result = {}


result['images'] = context.getFolderContents({
    'sort_on': 'effective',
    'sort_order': 'reverse',
    'object_provides': 'ana.gheorghe.content.interfaces.IContent'
    }, full_objects=True)

result['folders'] = ()
result['subimages'] = ()
result['others'] = ()

return result
