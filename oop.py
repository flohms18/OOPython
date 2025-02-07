class GridF1 :
    def __init__(self):
        self.TeamName = "HP Scuderia Ferrari"
        self.Driver1 = "Charles Leclerc"
        self.Driver2 = "Carlos Sainz"
        self.LastPosition = 2
        self.CurrentWC = False
    
    def GetDriver1(self):
        return self.Driver1
    
    def SetDriver2(self, Driver2):
        self.Driver2 = Driver2
    
    def GetDriver2(self):
        return self.Driver2



MyTeam = GridF1()
MyTeam.SetDriver2("Lewis Hamilton")
print(MyTeam.GetDriver1())
print(MyTeam.GetDriver2())
print(MyTeam.__dict__)


class GridF2(GridF1):
    
    def __init__(self):
        self.TeamName = "Mercedes AMG Petronas"
        self.Driver1 = "Valtteri Bottas"
        self.Driver2 = "George Russell"
        self.LastPosition = 2
        self.CurrentWC = False
    
    def GetDriver1(self):
        return self.Driver1
    def SetDriver2(self , Driver2):
        self.Driver2 = Driver2
    def GetDriver2(self):
        return self.Driver2 

MyTeamF2 = GridF2()
MyTeamF2.SetDriver2("Max Verstappen")
print(MyTeamF2.GetDriver2())        