# -*- coding: utf-8 -*-
from application import  app
import  os
class UrlManager(object):
    @staticmethod
    def buildUrl( path ):
        config_domain = app.config['DOMAIN']
        return "%s%s"%( config_domain['www'],path )

