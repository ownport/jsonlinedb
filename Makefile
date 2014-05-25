update-packages:
	@ echo 'update nose'
	@ pip install nose
	@ echo 'update coverage'
	@ pip install coverage

test-all:
	@ nosetests --cover-package=jsonlinedb --verbosity=1

test-all-with-coverage:
	@ nosetests --cover-package=jsonlinedb --verbosity=1	--cover-erase --with-coverage

	
