class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # doesn't work, idk why
    # def format(n):
    #     return "0" + str(n) if len(str(n)) < 2 else str(n)

    # def __str__(self):
    #     return str(self.hours) + ":" + str(self.minutes) + ":" + format(self.seconds)
    
    def __str__(self):
        return str(self.hours) + ":" + str(self.minutes) + ":" + ("0" + str(self.seconds) if len(str(self.seconds)) < 2 else str(self.seconds))
