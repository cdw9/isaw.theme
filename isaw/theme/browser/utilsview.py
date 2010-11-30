from DateTime import DateTime

from zope.interface import implements

from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView

from isaw.theme.browser.interfaces import IUtilsView


class UtilsView(BrowserView):
    """See `IUtilsView` for documentation
    """
    implements(IUtilsView)

    def __init__(self, context, request=None):
        self.context = context
        self.request = request
        self.portal_catalog = getToolByName(context, 'portal_catalog')

    def getUpcomingEvents(self, limit=2):
        """Grabbing latests news stuff for the news landing page"""
        return self.portal_catalog(portal_type=['Conference',
                                                'Exhibition',
                                                'Event',
                                                'events',
                                                'Lecture',
                                                'Performance',
                                                'Seminar',
                                                'Sponsored'],
                                   end={'query': DateTime(), 'range': 'min'},
                                   sort_on='start',
                                   review_state='published')[:limit]

    def getMonthName(self, month, full=None):
        """ Translates a month int into a short name """
        month_list = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
                      'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
        full_month_list = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL',
                           'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER',
                           'OCTOBER', 'NOVEMBER', 'DECEMBER']
        if type(month) is int and 0 < month < 13:
            return full and full_month_list[month-1] or month_list[month-1]
        return ''
