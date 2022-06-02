import string
import random


class BoggleBoard:
  
  def __init__(self):
    self.letters= string.ascii_uppercase
    self.dice_dict= {
       1 : "AAEEGN",
       2 : "ELRTTY",
       3 : "AOOTTW",
       4 : "ABBJOO",
       5 : "EHRTVW",
       6 : "CIMOTU",
       7 : "DISTTY",
       8 : "EIOSST",
       9 : "DELRVY",
       10: "ACHOPS",
       11: "HIMNQU",
       12: "EEINSU",
       13: "EEGHNW",
       14: "AFFKPS",
       15: "HLNNRZ",
       16: "DEILRX"
    }

    for n in range(4):
      self.first_line=""
      for k in range(4):
        self.first_line += "-"
      print(self.first_line)
    
    

  def shake(self):
    count=0
    for n in range(4):
      line=""
      for k in range(4):
        pot_letter=""
        count+=1
        pot_letter= random.choice(self.dice_dict[count])
        if pot_letter == "Q":
          line+= "Qu "
        else:
          line+=pot_letter
          line+="  "
            
      print(line)

boggle= BoggleBoard()
boggle.shake()