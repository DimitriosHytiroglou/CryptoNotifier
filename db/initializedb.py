import person
import shelve

db = shelve.open('../db/persondb')

DivergenceServiceList, SpikeServiceList = person.initializeServices()

db['DivergenceServiceList'] = DivergenceServiceList
db['SpikeServiceList'] = SpikeServiceList

db.close()