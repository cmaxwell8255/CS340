from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser3'
        PASS = 'apple'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31477
        DB = 'aac'
        COL = 'animals'

        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
    
    def create(self, data):
        print("in create method......")

        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary            
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    def read(self, searchData):
        print("in read method...")
        
        if searchData is not None:
            result = self.database.animals.find(searchData)
                         
        else:
            raise Exception('Nothing to read')
        return result
        
    def update(self, searchData, updateData):
        print("update record...")
        
        if searchData and updateData is not None:
            result = self.database.animals.find(searchData)
            for animal in result:
                self.database.animals.update(searchData, updateData)
                print(animal)
            
        else:
            raise Exception("nothing to update")
        return result
 

    def delete(self, searchData):
        print("record deleted...")
        
        if searchData is not None:
            result = self.database.animals.find(searchData)
            for animal in result:
                self.database.animals.delete_one(searchData)
                print(animal)
        else:
            raise Exception("nothing to update")
        return False

        
