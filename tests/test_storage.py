import os
import tempfile
import unittest

from jsonlinedb import storage

TEST_DATA_DIR='tests/data/'

def mktfile():
    return tempfile.mkstemp(dir=TEST_DATA_DIR, prefix='tmp-', suffix='.json')

class StorageTest(unittest.TestCase):

    def test_storage(self):
        
        tmpfile = mktfile()
        print type(tmpfile), tmpfile
        db = storage.JsonStorage(jsondb_path=tmpfile)
        
