# This module initializes the databases for the services
# It MUST be run before the first time the user interface is run, or the database will have an error later on.

import person
import shelve

DivergenceDB = shelve.open('../db/personDivergenceDB')
SpikeDB = shelve.open('../db/personSpikeDB')

DivergenceServiceList, SpikeServiceList = person.initializeServices()

DivergenceDB['DivergenceServiceList'] = DivergenceServiceList
SpikeDB['SpikeServiceList'] = SpikeServiceList

DivergenceDB.close()
SpikeDB.close()


