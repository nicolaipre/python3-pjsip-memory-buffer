
class BufferIO:
    """ Simple input-output buffer
    """
    def __init__(self, duration_ms=20, sample_rate=48000.0):

        self.audio_data        = bytearray()
        self.sample_rate       = sample_rate
        self.sample_period_sec = 1.0/self.sample_rate
        self.samples_per_frame = int((duration_ms/1000.0) / self.sample_period_sec)

    def _read_and_slice(self, n):
        byte_chunk      = self.audio_data[:n] 
        self.audio_data = self.audio_data[n:]
        return bytes(byte_chunk)

    def read(self):
        if len(self.audio_data) <= self.samples_per_frame:
            return False

        samples = self._read_and_slice(self.samples_per_frame)
        print("READ:", len(samples), "bytes | Buffer size: ", len(self.audio_data))
        return samples

    def write(self, data):
        self.audio_data += bytes(data)
        print("WRITE:", len(data), " bytes | Buffer size:", len(self.audio_data))