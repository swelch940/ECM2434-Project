import asyncio

class BarkBuddy:
    def __init__(self, id, username, oxygen=0,water=40,level=1,stages={0:"Default"},endurance=5,alive=True):
        self.ID = id
        self.USERNAME = username
        self.STAGES = stages
        self.current_stage = 0
        self.oxygen = oxygen
        self.water = water
        self.level = level
        self.endurance = endurance
        self.alive = alive
        
        self.run_loop()
        #add and sub functions, we can await these uwu
        self.add = lambda a,b: a+b
        self.sub = lambda a,b: a-b if a-b >= 0 else 0
    
    #BIHOURLY TASKS: increase oxygen, reduce water
    async def bihourly(self):
        self.oxygen = self.add(self.oxygen, 5**(self.level-1))
        self.water = self.sub(self.water, 2)
        spam = await self.level_handling()
        if spam == (True, True):
            return "yes level up, yes evo"
        elif spam == (False, False):
            return "no level up, no evo"
        elif spam == (True, False):
            return "yes level up, no evo"
    
    #DAILY TASKS: check endurance
    async def daily(self):
        spam = self.sub(self.endurance,1)
        if self.water == 0 and spam == 0: #if the tree is too weak it dies
            await self.murder_tree()
        elif self.water == 0 and spam > 0:
            self.endurance = spam
        elif self.water > 0 and self.endurance < 5:#if it has been watered strengthen tree
            self.endurance = await self.add(self.endurance, 1)
    
    #INCREASE LEVEL
    async def level_handling(self):
        if (self.oxygen // (5**(self.level - 1))) == self.level: #this scaling is jank
            self.level = self.add(self.level, 1)
            spam = await self.evo_handling()
            if spam: return (True, True) #yes level up, yes evo
            else: return (True, False) #yes level up, no evo
        else: return (False, False) #no level up, no evo
    #EVOLVE
    async def evo_handling(self):
        for key in self.STAGES.keys():
            if key == self.level: #if the level and the key match it's a valid evo, so it evolves, otherwise it does nothing
                self.current_stage = key
                return True
        return False
        
    
    #WATER THE TREE
    async def water_tree(self):
        self.water = await self.add(self.water,20)
    
    #THE CODE THAT THE EVENT LOOP RUNS
    async def event_loop(self):
        for i in range(12):#loop for bihourly stuff
            await asyncio.sleep(7200)
            await self.bihourly()
        await self.daily()
    
    #MURDER THE TREE
    def murder_tree(self):
        self.alive = False
        #other stuff goes here
    
    #THE LOOP ITSELF
    def run_loop(self):
        while self.alive:
            asyncio.run(self.event_loop())