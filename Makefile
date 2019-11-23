all:
	python3 setup-pjsuaxt.py build

clean distclean realclean:
	python3 setup-pjsuaxt.py clean
	rm -rf ./build

install:
	python3 setup-pjsuaxt.py $@

dep doc:

