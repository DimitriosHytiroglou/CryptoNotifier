import shelve
db = shelve.open('../db/persondb')               # Reopen shelve with same filename

for key in sorted(db):                     # Iterate to display database objects
    print(key, '\t=>', db[key])            # Prints with custom format

#sue = db['Sue']                      # Index by key to fetch
#sue.updateFirstName("Josey")                         # Update in memory using class's method
#db['Sue'] = sue                      # Assign to key to update in shelve
#print(db['Sue'])
db.close()                                 # Close after making changes