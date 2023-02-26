class BarkBuddy: #name can be changed once we figure it out, I just like the name Bark Buddy
    stages = {0:"Default"}
    def __init__(self, id, username):
        self.oxygen = 0
        self.level = 1 #starts at level 1
        self.water = 48
        self.ID = id #I'm not sure what we should use to ID the trees
        self.owner = username #username of account holder
        self.age = 0 #days
        self.endurance = 5 #number of days the tree can go on 0 water, once this value reaches 0 the tree fucking dies. should not go higher than the initial value
        self.alive = True
        self.current_stage = 0
        self.sprite = self.stages[self.current_stage]
    
    def murder_tree(self): #nick will like this one
        self.alive = False
        #other stuff to sort goes here
    
    def is_watered(self): #check if tree is watered
        if self.water > 16 and self.water < 80: return True #if tree isn't overwatered 
        else: return False
    
    async def apply_item(self,item): #applies item buffs
        async for f in item.funcs: f()
        
    async def increment_level(self): #increase level and check if tree will evolve
        self.level += 1
        evo_check = await self.can_evolve()
        if evo_check: self.evolve()
    
    async def check_level_increase(self): #check if level can increase
        lu_check = await (self.oxygen // (5**self.level))+1
        if lu_check > self.level: return True
        else: return False
    
    async def can_evolve(self): #check if tree can evolve
        evo_check = await (self.level in self.stages.keys())
        if evo_check: return True
        else: return False
    
    async def water_tree(self): #numbers can be changed later
        check = await 80 - self.water
        if check < 24: self.water += check
        else: self.water += 24
    
    async def evolve(self): #evolve the tree!
        self.current_stage = self.stages[self.level]
        self.sprite = self.stages[self.current_stage]
        #other evolution stuff goes here
        
    async def update_oxygen(self):
        spam = await self.is_watered()
        if spam: self.oxygen += 10 #numbers can be changed later
        else: self.oxygen += 5
        if self.check_level_increase(): await self.increment_level()
    
    async def bihourly(self): #run oxygen and water decrease bihourly
        fl = (self.update_oxygen, self.decrement_water)
        for f in fl: await f()
    
    async def daily(self): #daily tasks
        if self.water == 0 and self.endurance == 0: #kill tree if neglected for too long
            await self.murder_tree()
        elif self.water == 0 and self.endurance > 0: #tree weakens if neglected
            await self.weaken()
        elif self.water > 0: #if tree is not neglected then increase endurance
            await self.strengthen()
    
    async def on_load(self): #when the tree is loaded by the website this is all that the user should know
        return self.oxygen, self.level, self.water, self.owner, self.age, self.alive, self.stages[self.current_stage]
            
            
class BarkBuddyDemo(BarkBuddy): #barkbuddy class to be used in the demo, very fudgeable
    stages = {0:"Default",2:"Steven"}
    def __init__(self, id, username):
        self.oxygen = 24
        self.level = 1 #starts at level 1
        self.water = 48
        self.id = id #I'm not sure what we should use to ID the trees
        self.owner = username #username of account holder
        self.age = 0 #days
        self.endurance = 5 #number of days the tree can go on 0 water, once this value reaches 0 the tree fucking dies. should not go higher than the initial value
        self.alive = True
    
    async def force_oxygen_increase(self):
        await self.demoFuncs()
    
    async def demoFuncs(self):
        self.oxygen += 5
        if self.check_level_increase(): await self.increment_level()
        
