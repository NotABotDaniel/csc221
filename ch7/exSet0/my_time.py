class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def myFormat(n):
        return "0" + str(n) if len(str(n)) < 2 else str(n)

    def __str__(self):
        return str(self.hours) + ":" + self.myFormat(self.minutes) + ":" + self.myFormat(self.seconds)
    
