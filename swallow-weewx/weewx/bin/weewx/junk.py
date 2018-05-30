'''
Created on Feb 14, 2016

@author: tkeffer
'''
from __future__ import with_statement

import weewx.manager
import weedb

from weewx.engine import StdService

# Inherit from the base class StdService:
class GetSolar(StdService):
    """Custom service that reads the solar database"""
    
    def __init__(self, engine, config_dict):
        # Pass the initialization information on to my superclass:
        super(GetSolar, self).__init__(engine, config_dict)
        
        self.solar_dict = weewx.manager.get_database_dict_from_config(config_dict, 'SBFspot_mysql')
        
        self.bind(weewx.NEW_ARCHIVE_RECORD, self.newArchiveRecord)
        
    def newArchiveRecord(self, event):
        
        connect = weedb.connect(self.solar_dict)
        try:
            cursor = connect.cursor()
            cursor.execute("SELECT PacTot FROM vwSpotData WHERE TimeStamp = (SELECT MAX(TimeStamp) FROM vwSpotData)")
            result = cursor.fetchone()
            print "result=", result
            event.record['radiation'] = result[0] if result is not None else None
            cursor.close()
        finally:
            connect.close()
        