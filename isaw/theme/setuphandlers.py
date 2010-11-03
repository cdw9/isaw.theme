from Products.CMFCore.utils import getToolByName

from sixfeetup.utils import helpers as sfutils

def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('isaw.theme_default.txt') is None:
        return

    # Add additional setup code here
    # automagically run a plone migration if needed
    sfutils.runPortalMigration()
    # automagically run the upgrade steps for this package
    sfutils.runUpgradeSteps(u'isaw.theme:default')

def set_property(context, prop_name, value):
   if context.hasProperty(prop_name):
       context.manage_changeProperties(prop_name=value)
   else:
       context.manage_addProperty(prop_name, value, 'string')

def set_layout(context, layout_name):
    if context.hasProperty('default_page'):
        context.manage_delProperties(['default_page'])
    set_property(context, 'layout', layout_name)

def set_default_page(context, page_id):
    if context.hasProperty('layout'):
        context.manage_delProperties(['layout'])
    set_property(context, 'default_page', page_id)

def publish(context):
    portal_workflow = getToolByName(context, 'portal_workflow')
    portal_workflow.doActionFor(
        context,
        'publish',
        comment='Content published automatically'
    )

def createHomePage(context):
    site = context.getParentNode()
    page_id = 'isaw'
    if page_id not in site.objectIds():
        site.invokeFactory('Document', page_id)
        home_page = site[page_id]
        title = 'Institute for the Study of the Ancient World'
        home_page.processForm(values={'title': title})
        set_layout(home_page, 'home_page_view')
        publish(home_page)
        set_default_page(site, page_id)
