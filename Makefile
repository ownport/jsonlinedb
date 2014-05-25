update-packages:
	@ echo 'update nose'
	@ pip install nose
	@ echo 'update coverage'
	@ pip install coverage

test-all:
	@ rm -f tests/data/*
	@ nosetests --cover-package=jsonlinedb --verbosity=1

test-all-with-coverage:
	@ rm -f tests/data/*
	@ nosetests --cover-package=jsonlinedb --verbosity=1	--cover-erase --with-coverage

	
