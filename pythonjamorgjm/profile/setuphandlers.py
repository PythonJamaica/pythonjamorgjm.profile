# -*- coding: utf-8 -*-
#from CMFCore.utils import getToolByName
from plone import api
#from Products.CMFPlone.interfaces import constrains
import logging
from zExceptions import BadRequest
import Globals


logger = logging.getLogger(__name__)

PROFILE_ID='profile-pythonjamorgjm.profile:default'
PRODUCT = 'pythonjamorgjm.profile'

def setupVarious(context):
    if context.readDataFile('pythonjamorgjm.profile.marker.txt') is None:
        print "skipped"
        return
    setup = api.portal.get_tool(name='portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'typeinfo')
    
    """if api.content.get('/news'):
        api.content.delete(api.content.get('/news'))
        logger.info('removed the news folder')
    if api.content.get('/Members'):
        api.content.delete(api.content.get('/Members'))
        logger.info('removed the Members folder')
    if api.content.get('/events'):   
        api.content.delete(api.content.get('/events'))
        logger.info('removed the events folder')

    portal = api.portal.get()

    # configure default site view to be 'site_index'
    print "setting default page"
    portal.manage_changeProperties(default_page='site_index')
    portal.setLayout("site_index")
    logger.info('replaced the default front page of the site')
    # we will be organizing folders by year
    # starting by hardcoding for 2014
    # no longer using the reports folder 
    """
