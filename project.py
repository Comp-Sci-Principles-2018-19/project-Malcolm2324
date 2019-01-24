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
    print("My first agile Iteration is to make a test based game. This game will include dragons, levels, other monsters and trap doors. This is my first step because kids will have fun playing this game. Also, this is my first step because I do not know how to make any other games")
    if choice==None:
        choice=input("knife or hammer")
    if choice=="knife":
            return"knife"
    else:
            return"hammer"

def test_suite():
          
          
    test(startgame()=="knife")
    
startgame()
test_suite()