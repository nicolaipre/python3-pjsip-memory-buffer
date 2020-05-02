
from Audio import BufferIO
from threading import Thread

class PjsipStream:
    def __init__(self, sample_rate=48000.0, samples_per_frame=960, channel_count=2, bits_per_sample=16)
        self.sample_rate = sample_rate
        self.samples_per_frame = samples_per_frame
        self.channel_count = channel_count
        self.bits_per_sample = bits_per_sample


    def _listen_loop(self, sink):
        """ Listener thread
        """
        self.lib.thread_register("ListenThread") # Register thread with pj lib

        mem_capture = pj.MemCapture(self.lib,
            clock_rate      =self.sample_rate,
            sample_per_frame=self.samples_per_frame,
            channel_count   =self.channel_count,
            bits_per_sample =self.bits_per_sample
        )

        # Create and connect audio capture
        mem_capture.create()
        self.lib.conf_connect(self.current_call.info().conf_slot, mem_capture.port_slot)

        while True:
            if (mem_capture.get_read_available() > self.samples_per_frame * self.channel_count): # May be incorrect
                data = mem_capture.get_frame() # Grab audio frame
                sink.write(data) # Write audio frame to sink



    def listen(self, sink):
        """ Listen to the current call.
            Receive a stream of PCM audio from call (memory).
            Sink must be an object with a write().

            Write a frame of audio data to the specified sink.
        """
        self.listen_thread = Thread(
            target=self._listen_loop,
            args  =(sink,)
        )
        self.listen_thread.start()


    def stop_listening(self):
        self.listen_thread.join()







    def _play_loop(self, source):
        """ Player thread
        """
        self.lib.thread_register("PlayThread")

        mem_player = pj.MemPlayer(self.lib,
            clock_rate      =self.sample_rate,
            sample_per_frame=self.samples_per_frame,
            channel_count   =self.channel_count,
            bits_per_sample =self.bits_per_sample
        )

        # Create and connect audio player
        mem_player.create()
        self.lib.conf_connect(mem_player.port_slot, self.current_call.info().conf_slot)

        while True:
            if (mem_player.get_write_available() > self.samples_per_frame * self.channel_count):
                data = source.read()
                
                if data == False: # If buffer does not hold enough data, dont put_frame
                    continue
                
                total_bytes_played = mem_player.put_frame(data)



    def play(self, source):
        """ Play audio from source into call.
            Transmit a stream of PCM audio to call (memory).
            Stream must be an object with a read().

            Play a frame of audio data from the specified source.
        """
        self.play_thread = Thread(
            target=self._play_loop,
            args  =(source,)
        )
        self.play_thread.start()


    def stop_playing(self):
        self.play_thread.join()
