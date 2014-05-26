import os
import json
import tempfile
import unittest

from jsonlinedb import storage
from jsonlinedb.exceptions import JsonlineDBException

TEST_DATA_DIR='tests/data/'

def mktfile(prefix='tmp-'):
    ''' creates temp file
    
    returns filepath
    '''
    os_handle, filename = tempfile.mkstemp(dir=TEST_DATA_DIR, prefix=prefix, suffix='.json')
    print filename
    return filename

def mktestjson(prefix='tmp-'):
    ''' create test JSONline file
    '''
    filepath = mktfile(prefix=prefix)
    with open(filepath, 'w') as db:
        for i in range(100):
            db.write('%s\n' % json.dumps({'key': i, 'value': i}))           
    return filepath


class StorageTest(unittest.TestCase):

    def test_storage(self):
        ''' test_storage
        '''
        tmpfile = mktfile(prefix='test-storage-')
        db = storage.JsonStorage(jsondb_path=tmpfile)
        self.assertEqual(type(db), storage.JsonStorage)


    def test_storage_does_not_exist(self):
        ''' test_storage_does_not_exist
        '''
        self.assertRaises(RuntimeError, storage.JsonStorage, jsondb_path='/tmp/jsonlinedb.not-exists')

        
    def test_make_unqie_index(self):
        ''' test_make_unqie_index
        '''
        filepath = mktestjson(prefix='test-make-unique-index-')
        db = storage.JsonStorage(jsondb_path=filepath)
        db.make_unique_index(['key',])
        self.assertEqual(db.stats(), {'records': [('key', 100)]})

                
    def test_failed_make_unqie_index(self):
        ''' test_make_unqie_index
        '''
        filepath = mktestjson(prefix='test-failed-unique-index-')
        db = storage.JsonStorage(jsondb_path=filepath)
        # failed: fields for indexing are not passed
        self.assertRaises(RuntimeError, db.make_unique_index)
                

    def test_get_put_data(self):
        ''' test_get_put_data
        '''
        tmpfile = mktestjson(prefix='test-get-put-data-')
        db = storage.JsonStorage(jsondb_path=tmpfile)
        db.make_unique_index(['key'])
        self.assertEqual(db.get(key=10), [{u'key': 10, u'value': 10}])      
        self.assertEqual(db.get(key=20), [{u'key': 20, u'value': 20}])      
        self.assertEqual(db.get(key=30), [{u'key': 30, u'value': 30}])      
        self.assertEqual(db.get(key=100), [])      
        db.put({'key': 100, 'value': 100})
        db.make_unique_index(['key'])
        self.assertEqual(db.get(key=100), [{u'key': 100, u'value': 100}])      
        self.assertEqual(db.stats(), {'records': [('key', 101)]})

    
    def test_json_decode_error(self):
        ''' test_json_decode_error
        '''
        def f1():
            pass
        tmpfile = mktfile(prefix='test-json-decode-error-')
        db = storage.JsonStorage(jsondb_path=tmpfile)
        self.assertRaises(JsonlineDBException, db.put, f1)

        
    def test_index_not_found(self):
        ''' test_index_not_found
        '''
        tmpfile = mktfile(prefix='test-index-not-found-')
        db = storage.JsonStorage(jsondb_path=tmpfile)
        self.assertRaises(RuntimeError, db.get, unknown_key=10)

    
    def test_items(self):
        ''' test_items
        '''        
        tmpfile = mktestjson(prefix='test-items-')
        db = storage.JsonStorage(jsondb_path=tmpfile)
        items = [item for item in db.items()]
        self.assertEqual(len(items), 100)
        


        
