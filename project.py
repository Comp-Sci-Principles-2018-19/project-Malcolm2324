import sys

def turn_clockwise(dir):
    return None
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
def startgame(choice=None):
    print("You are at two doors. Which door will you choose?")
    if choice==None:
        choice=input("1 or 2")
    if choice=="1":
        print("If 1 you will go through the door and  you will find a knife and monsters")
    else:
        print("you will fall into a trap")
    return choice
 
 
def door1(choice=None):
    if choice==None:
        choice=input("fight or flee")
    if choice=="fight":
        print("you die")
        return "dead"
    else:
        print("you run away and go back to the two doors")
        return"start"
def door2(stuff=None):
    print(" you fall into a trap and find yourself on to a ice floor")
    if stuff=="knife":
        print("lucky you have a knife to climb out of the slide")
        return "survive"
    else:
        print("without a knife you slide to your death")
        return "dead"
    
   
def test_suite():
          
          
    test(startgame("1")=="1")
    test(startgame("2")=="2")
    test(door1("fight")=="dead")
    test(door1("flee")=="start")
    test(door2()=="dead")
    test(door2("knife")=="survive")
"""
if startgame()=="knife":
    escape_bridge()
else:
    print("you lose")
"""
#test_suite()
def main():
    stuff=None
    while True:
        
        if startgame()=="1":
            if door1()=="dead":
               continue
            else:
                stuff="knife"
                continue
                
        else:
            if door2(stuff)=="dead":
                stuff=None
                continue
        
main()