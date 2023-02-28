import asyncio

        

class BarkBuddy: #name can be changed once we figure it out, I just like the name Bark Buddy
    def __init__(self, id, username, level=1,water=20,age=0,endurance=5,alive=True,current_stage=0, stages={0:"Default"}):
        self.oxygen = 0
        self.level = level #starts at level 1
        self.water = water #current water level
        self.ID = id #I'm not sure what we should use to ID the trees
        self.owner = username #username of account holder
        self.age = age #days
        self.endurance = endurance #number of days the tree can go on 0 water, once this value reaches 0 the tree fucking dies. should not go higher than the initial value
        self.alive = alive
        self.current_stage = current_stage
        self.sprite = self.stages[self.current_stage]
        self.stages = stages
        self.run_events() #RUN THE TREEEEEEEEEE
        
    def murder_tree(self): #nick will like this one
        self.alive = False
        #other stuff to sort goes here
    
    def is_watered(self): #check if tree is watered
        if self.water > 16 and self.water < 80: return True #if tree isn't overwatered 
        else: return False

    async def get_image_file(self): #returns an iterator which goes over the file object
        with open(self.stages[self.current_stage]+".png","rb") as f: l = await f.read()
        for line in l:
            yield line
    
    async def apply_item(self,item): #applies item buffs
        async for f in item.funcs: f()
        
    async def increment_level(self): #increase level and check if tree will evolve
        self.level = await self.level + 1
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
        else: self.water += 12
    
    async def evolve(self): #evolve the tree!
        self.current_stage = self.stages[self.level]
        self.sprite = self.stages[self.current_stage]
        #other evolution stuff goes here
        
    async def update_oxygen(self):
        spam = await self.is_watered()
        if spam: self.oxygen += 10 #numbers can be changed later
        else: self.oxygen += 5
        if self.check_level_increase(): await self.increment_level()
    
    async def decrement_water(self):
        if self.water < 2: self.water = 0
        else: self.water = await self.water - 2 #this number can be retooled for later
        
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
    
    async def living_event_loop(self):
        while self.alive:
            async for i in range(12):
                asyncio.sleep(7200)
                await self.bihourly()
            await self.daily()
    
    async def run_events(self):
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(self.living_event_loop())
        except:
            loop.close()
            
class BarkBuddyDemo(BarkBuddy): #barkbuddy class to be used in the demo, very fudgeable
    def __init__(self): #call init of barkbuddy with edited oxygen count
        super(BarkBuddyDemo,self).__init__(oxygen=24, stages = {0:"Default",2:"Steven"})
        
    async def demoFuncs(self):
        self.oxygen = await self.oxygen + 5
        if self.check_level_increase(): await self.increment_level()


class TestBuddy(BarkBuddy):
    stages = {0:"some_file",2:"some_other_file"}
    def __init__(self, id, username):
        self.oxygen = 24
        self.level = 1
        self.water = 20
        self.id = id
        self.owner = username
        self.age = 0
        self.endurance = 3
        self.alive = True
    
    def set_endurance(self, n):
        self.endurance = n
    
    async def living_event_loop(self):
        async for i in range(6):
            asyncio.sleep(1)
            await self.bihourly()
        await self.daily()
            
    async def increment_level(self):
        self.level = await self.level + 1
    
    async def on_load(self):
        return await super().on_load()
    
        
