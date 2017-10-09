import person
import shelve

DivergenceDB = shelve.open('../db/personDivergenceDB')
SpikeDB = shelve.open('../db/personSpikeDB')


DivergenceServiceList, SpikeServiceList = person.initializeServices()

DivergenceDB['DivergenceServiceList'] = DivergenceServiceList
SpikeDB['SpikeServiceList'] = SpikeServiceList

DivergenceDB.close()
SpikeDB.close()