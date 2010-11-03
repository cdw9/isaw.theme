from zope.interface import Interface
from zope.viewlet.interfaces import IViewletManager

from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """

class ILeftCol(IViewletManager):
    """A viewlet manager that sits in the left most column of the page
       (an addition to the main template)
    """

class IUtilsView(Interface):
    """ Marker interface for misc browser view """

    def getUpcomingEvents(limit):
        """Grabbing upcoming events for the home page"""
