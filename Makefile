all:
	python3 setup.py build

clean distclean realclean:
	python3 setup.py clean
	rm -rf ./build

install:
	python3 setup.py $@

dep doc:

