# Python 3 PJSIP with memory buffers for audio streaming

I have simply combined the following two libraries because I needed both in one.

This version works with pjproject-2.9.


## Install and compile PJSUA(XT) for Python 3
```sh
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
git clone https://github.com/nicolaipre/python3-pjsip-memory-buffer.git
cd python3-pjsip-memory-buffer

python3 setup.py build
sudo python3 setup.py install
```

## Test installation
```python
Python 3.6.4 (default, Jul  1 2019, 21:52:48)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pjsuaxt
>>>
```

## Usage
```python
# Create two audio IO buffers
call_audio    = BufferIO(sample_rate=48000.0)
discord_audio = BufferIO(sample_rate=48000.0)

# Create the audio connections
pj_stream  =  PjsipStream(sample_rate=48000.0)
disc_vc    = DiscordVoice(sample_rate=48000.0)

pj_stream.listen(call_audio)  # Capture phone audio to buffer
disc_vc.play(call_audio)      # Play phone audio to discord voice connector

disc_vc.listen(discord_audio) # Capture discord audio to buffer
pj_stream.play(discord_audio) # Play discord audio to phone
```

See file `main.py` in `example-usage` for full example.

- For the original source, see: https://github.com/UFAL-DSG/alex/blob/master/alex/components/hub/vio.py

### Credits to:
- https://github.com/UFAL-DSG/pjsip - For implementing buffered streaming
- https://github.com/mgwilliams/python3-pjsip - For porting to Python 3

