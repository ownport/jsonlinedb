import os
import sys
import json
import linecache


class JsonStorage(object):

    db_index = dict()
    
    def __init__(self, jsondb_path):
        ''' __init__
        '''
        if not os.path.exists(jsondb_path):
            raise RuntimeError('File does not exist: %s' % jsondb_path)
        self.jsondb_path = jsondb_path
    
    def make_unique_index(self, fields=[]):
        ''' make uniqie index
        '''
        if not fields:
            raise RuntimeError('Index fields are not defined')
        
        with open(self.jsondb_path) as db:
            for pos_id, data in enumerate(db):
                
                data = json.loads(data)

                for field in fields:
                    if not self.db_index.get(field, None):
                        self.db_index[field] = dict()
                    
                    self.db_index[field][data[field]] = pos_id + 1

    def get(self, **kwargs):
        ''' returns JSONline by key
        '''
        result = list()
        for k,v in kwargs.items():
            if k not in self.db_index:
                raise RuntimeError('Index %s not found' % k)
            pos_id = self.db_index[k].get(v, None)
            if pos_id:
                result.append(json.loads(linecache.getline(self.jsondb_path, pos_id)))
        return result

    def put(self, jsondata):
        ''' append data into jsondb
        '''
        with open(self.jsondb_path, 'a') as db:
            db.write("%s\n" % json.dumps(jsondata))

    def items(self):
        with open(self.jsondb_path) as db:
            for i,data in enumerate(db):
                yield json.loads(data)
                    
    def stats(self):
        ''' returns stats
        '''
        return {
            'records': [(field, len(self.db_index[field])) for field in self.db_index],
            'indexes_size': [(field, sys.getsizeof(self.db_index[field])) for field in self.db_index],
        }
         
