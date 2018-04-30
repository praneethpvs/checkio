import time


def slow_write(self, output, size, duration):
    bytes_written = 0
    start_time = time.time()
    while bytes_written < size:
        now = time.time()
        if duration != 0:
            desired_bytes = ((now - start_time) / duration) * size
        else:
            desired_bytes = size
        desired_bytes = min(size, desired_bytes)
        if desired_bytes < bytes_written:
            time.sleep(0.2)
        else:
            while (bytes_written < desired_bytes):
                output.write('A')
                bytes_written = bytes_written + 1
            output.flush()
    now = time.time()
    self.log_message("Request took %f seconds", now - start_time)
