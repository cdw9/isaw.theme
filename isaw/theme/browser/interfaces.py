from plone.theme.interfaces import IDefaultPloneLayer
from zope.viewlet.interfaces import IViewletManager

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """
    
class ILeftCol(IViewletManager):
    """A viewlet manager that sits in the left most column of the page
       (an addition to the main template)
    """
