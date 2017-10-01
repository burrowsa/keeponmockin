class Printer(object):
    @property
    def online(self):
        # makes calls to physical printer
        raise RuntimeError("This code would fail in test")
        
    def submit_job(self, job):
        if not self.online:
            raise RuntimeError("Printer is offline")
        
        # makes calls to physical printer
        raise RuntimeError("This code would fail in test")
