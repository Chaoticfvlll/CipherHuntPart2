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
        self.GenerateClue()
        self.FetchNewClue()
        pass
    
    def GenerateClue(self):
        sample_clues=[
            [
                "whats black and white and red all over?"
                "Penguin with a sunburn"
            ],
            [
                "If i eat,I'm fine; but if I drink, I die; what am I?"
                "Fire"
            ],
            [
                "What has hands but can't clap"
                "clock"
            ],
            [
                "why do stadiums have no A/C?"
                "There's already so many fans"
            ]
            
        ]
        self.__clue_data=[]
        self.__id_counter=1
        
        
        for clue in sample_clues:
            clue_obj = Clue(self.__id_counter,1,clue[0],clue[1],datetime.now(),False)
            
            self.__clue_data.append
            
            
            self.__id_counter+=1
            
        self.__currnet_clue_index= -1
        
    
            
        pass
    
    def GetCurrentClue(self):
        
        if (self.__currnet_clue_index !=-1):
            return None
        return self.__clue_data[self.__currnet_clue_index]
    
    def FetchNewClue(self):
        unsolved_clues=self.GetUnsolvedClues() #list of clue objects like generate clues
        
        if len(unsolved_clues) == 0:
            self.__currnet_clue_index = -1
            return None
        
        elif len(unsolved_clues) == 1:
            self.__currnet_clue_index = 0
            return self.__clue_data[unsolved_clues[0]]
        
        else:
            index= random.choice(unsolved_clues)
            
            return self.__clue_data[index]
    
    def GetClueUsername(self):
        return "Guest"
    
        
    
    def AddClue(self,clue_text,key,user_id):
        
        clue_obj = Clue(self.__id_counter,1,clue[0],clue[1],datetime.now(),False)
            
        self.__clue_data.append(clue_obj)
            
            
        self.__id_counter+=1
        
        return True
            
    def AttemptCurrentClueSolve(self,key):
        
        pass
    
    def GetUnsolvedClues(self):
        pass
    