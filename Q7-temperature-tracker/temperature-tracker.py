class TempTracker():

    def __init__(self):
        self.temps = []
        self.mean = -1
        self.modes = []
        self.occurences = {}
        self.vals = {}
        self.max_occurences = 1

    def get_mode(self):
        return self.modes

    def get_max(self):
        return max(self.temps)
    
    def get_min(self):
        return min(self.temps)
    
    def get_mean(self):
        return self.mean

    def insert(self, new_temp):
        # update mean
        if len(self.temps) == 0:
            self.mean = new_temp
        else:
            self.mean = 1.0 * self.mean * len(self.temps) + new_temp
            self.mean = 1.0 * self.mean / (len(self.temps) + 1)
        
        # update modes
        if new_temp not in self.occurences:
            self.occurences[new_temp] = 1
        else:
            self.occurences[new_temp] += 1
            if self.occurences[new_temp] > self.max_occurences:
                self.max_occurences = self.occurences[new_temp]

        if self.occurences[new_temp] not in self.vals:
            self.vals[self.occurences[new_temp]] = [new_temp]
        else:
            self.vals[self.occurences[new_temp]] = list(set(self.vals[self.occurences[new_temp]] + [new_temp]))

        self.modes = self.vals[self.max_occurences]

        self.temps.append(new_temp)
        print(self.temps)


Temp = TempTracker()

Temp.insert(42)
Temp.insert(23)
Temp.insert(23)
Temp.insert(1337)
Temp.insert(42)

print(Temp.get_min())
print(Temp.get_max())
print(Temp.get_mean())
print(Temp.get_mode())