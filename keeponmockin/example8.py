

class Printer(object):
    @property
    def online(self):
        # makes calls to physical printer
        raise RuntimeError("This code would fail in test")

    @online.setter
    def set_online(self):
        # makes calls to physical printer
        raise RuntimeError("This code would fail in test")
        

def prepare_printer():
    printer = Printer()
    printer.online = True
    return printer
