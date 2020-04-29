all:
	python3.7 setup.py build

clean distclean realclean:
	python3.7 setup.py clean
	rm -rf ./build

install:
	python3.7 setup.py $@

remove:
	rm /usr/local/lib/python3.7/dist-packages/pjsuaxt.py
	rm /usr/local/lib/python3.7/dist-packages/pjsuaxt-2.1.0.egg-info
	rm /usr/local/lib/python3.7/dist-packages/_pjsuaxt.cpython-37m-x86_64-linux-gnu.so

dep doc:

