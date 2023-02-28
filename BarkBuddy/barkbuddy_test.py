import asyncio
from barkbuddy import TestBuddy

class BarkBuddyTest:
    
    def __init__(self):
        self.testbuddy = TestBuddy(12345, "YarnYoshi69")
    
    def assert_murder(self):
        self.testbuddy.murder_tree()
        try:
            assert self.testbuddy.alive == False
        except(AssertionError):
            return False
        else: return True
    
    def assert_water_check(self):
        try:
            assert self.testbuddy.is_watered()
        except (AssertionError):
            return False
        else: return True
    
    async def assert_level_increase(self):
        before = await self.testbuddy.level
        after = await self.testbuddy.increment_level()
        spam = None
        try:
            assert before == after - 1
        except(AssertionError):
            spam = False
        else:
            spam = True
        finally:
            self.testbuddy.level = before
            return spam
    
    async def assert_level_increase_check(self):
        await self.testbuddy.increment_level()
        try:
            assert self.testbuddy.check_level_increase()
        except AssertionError:
            spam = False
        else:
            spam = True
        finally:
            self.testbuddy.level = await self.testbuddy.level - 1
            return spam
    
    async def assert_strengthen_works_correctly(self):
        self.testbuddy.water = await self.testbuddy.water + 5
        before = self.testbuddy.endurance
        try:
            await self.testbuddy.daily()
            assert self.endurance == before + 1
        except AssertionError:
            spam = False
        else:
            spam = True
        finally:
            self.endurance = await self.endurance - 1
            self.testbuddy.water = await self.testbuddy.water - 5
            return spam
    
    async def assert_weaken_works_correctly(self):
        self.testbuddy.water = 0
        before = self.testbuddy.endurance
        try:
            await self.testbuddy.daily()
            assert self.endurance == before - 1
        except AssertionError: spam = False
        else: spam = True
        finally:
            self.endurance = await self.endurance + 1
            self.testbuddy.water = 20
            return spam
    
    async def on_load_works(self):
        x = await self.testbuddy.on_load()
        y = (self.testbuddy.oxygen, self.testbuddy.level,self.testbuddy.water,self.testbuddy.owner,self.testbuddy.age,self.testbuddy.alive,self.testbuddy.stages[self.testbuddy.current_stage])
        try:
            assert x == y
        except AssertionError: spam = False
        else: spam = True
        finally: return spam
    
    async def tree_functions_in_event_loop(self):
        ham = self.testbuddy
        await self.testbuddy.run_events()
        try:
            assert ham.oxygen == self.testbuddy.oxygen - 120
            assert ham.water == self.testbuddy.water - 12
        except AssertionError:
            spam = False
        else: spam = True
        finally:
            self.testbuddy = ham
            return spam