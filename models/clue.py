from dataclasses import dataclass
from datetime import datetime
import random

@dataclass
class Clue:
    id: int
    user_id: int
    clue_text:str 
    key:str
    date_created: datetime
    is_solved: bool 

class ClueModel:
    def __init__(self, db):
        pass
    
    def GenerateClue(self):
        pass
    
    def GetCurrentClue(self):
        pass
    
    def FetchNewClue(self):
        pass
    
    def AddClue(self,clue_text,key,user_id):
        pass
    
    def AttemptCurrentClueSolve(self,key):
        if (clue_text == key):
            is_solved= "true"
        pass
    
    def GetUnsolvedClues(self):
        pass
    