class Radio:

    def __init__(self):
        self.mode = "FM"
        self.f = [87.5,"MHz"]

    def __str__(self):
        return f"{self.mode} Radio: {self.f[0]:.1f} {self.f[1]}"

    def set_mode(self,mode):
        if mode == "FM":
            self.mode = "FM"
            self.f = [87.5,"MHz"]
        else:
            self.mode = "AM"
            self.f = [150,"kHz"]
    
    def set_frequency(self,frequency):
        # frequency = float(frequency)
        if self.mode == "FM":
            if frequency < 87.5 or frequency > 108:
                pass
            else:
                self.f = [frequency,"MHz"]

        elif self.mode == "AM":
            if frequency < 150 or frequency > 280:
                pass
            else:
                self.f = [frequency,"kHz"]
            
    def adjust_frequency(self,frequency):

        # frequency = float(frequency)
        temp = self.f[0] + frequency

        if self.mode == "FM":
            if temp < 87.5 or temp > 108:
                return False
            else:
                self.f = [temp,"MHz"]
                return True

        elif self.mode == "AM":
            if temp < 150 or temp > 280:
                return False
            else:
                self.f = [temp,"kHz"]
                return True
            
    def get_mode(self):
        return self.mode
    
    def get_frequency(self):
        return f"{self.f[0]}"