# Python 3 support for pjproject/pjsip with audio buffers

I have simply combined the following two libraries because I needed both in one.

This version works with pjproject-2.9.


## Install and compile PJSUA(XT) for Python 3
```
sudo apt install python3 python3-dev build-essential libasound2-dev
wget https://www.pjsip.org/release/2.9/pjproject-2.9.zip
unzip pjproject-2.9.zip
cd pjproject-2.9
chmod +x configure aconfigure
./configure CXXFLAGS=-fPIC CFLAGS=-fPIC LDFLAGS=-fPIC CPPFLAGS=-fPIC
make dep
make
sudo make install

cd pjsip-apps/src/
git clone https://github.com/nicolaipre/python3-pjsip-buffer.git
cd python3-pjsip-buffer

python3 setup-pjsuaxt.py build
python3 setup-pjsuaxt.py install
```

## Test installation
```
Python 3.6.4 (default, Jul  1 2019, 21:52:48)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pjsuaxt
>>>
```

## Usage
See https://github.com/UFAL-DSG/alex/blob/master/alex/components/hub/vio.py

### Credits to:
https://github.com/UFAL-DSG/pjsip - For implementing buffered streaming
https://github.com/mgwilliams/python3-pjsip - For porting to Python 3

