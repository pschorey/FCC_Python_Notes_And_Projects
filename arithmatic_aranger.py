import re

#Problem object constructor
class Problem:
  def __init__(self, num, operator, denom):
    self.num = num
    self.operator = operator
    self.denom = denom
    self.maxLength = 2; #operator plus space
    if (len(self.num) > len(self.denom)):
      self.maxLength += len(self.num)
    else:
      self.maxLength += len(self.denom)
    self.whitespaceNum = self.maxLength - len(self.num)
    self.whitespaceDenom = self.maxLength - 2 - len(self.denom)
    try:
      self.solution = eval(self.num + self.operator + self.denom) 
    except:
      self.solution = ''  
    self.solutionOffset = self.maxLength - len(str(self.solution))

#Error Checking Global / Functions
err = False #changes to err string if err found
def checkNumOfProblems (problems):
  if len(problems) > 5:
    global err
    err = "Error: Too many problems."
def checkDigits (num):
  digitCheck = re.search("\D", num)
  if digitCheck:
    global err
    err = "Error: Numbers must only contain digits."
def checkLen (num):
  if len(num) > 4:
    global err
    err = "Error: Numbers cannot be more than four digits."
def checkPlusOrMinus (operator):  
  plusOrMinus = re.search("\+|\-", operator)
  if not plusOrMinus:
    global err
    err = "Error: Operator must be '+' or '-'."

def addWhiteSpace(num):
  str = ''
  i = 0
  while i < num:
    str = str + ' '
    i += 1  
  return str  

def createEquals(num):
  str = ''
  i = 0
  while i < num:
    str = str + '-'
    i += 1  
  return str 

#Main function, args sent from test
def arithmetic_arranger(*args):

  problems = args[0]
  problemList = []
  global err #digit check doesn't get global var, if not set globally....
  err = False
  arranged_problems = ''
  numStr = ''
  denomStr = ''
  equalStr = ''
  solutionStr = ''

  checkNumOfProblems(problems)

  solve = False #param to solve when passed
  if len(args) > 1:
    solve = args[1] #sets to true

  for idx, problem in enumerate(problems):
    args = re.split("\s", problem)
    problemList.append(Problem(args[0],args[1],args[2]))

  for idx, obj in enumerate(problemList):
    #Error checking
    checkPlusOrMinus(obj.operator)
    checkDigits(obj.num)
    checkDigits(obj.denom)
    checkLen(obj.num)
    checkLen(obj.denom)

    if not err:
      numStr = numStr + addWhiteSpace(obj.whitespaceNum) + str(obj.num)
      denomStr = denomStr + obj.operator + ' ' + addWhiteSpace(obj.whitespaceDenom) + str(obj.denom)
      equalStr = equalStr + createEquals(obj.maxLength)
      solutionStr =  solutionStr + addWhiteSpace(obj.solutionOffset) + str(obj.solution)

      if idx < len(problemList) - 1:
        numStr = numStr + addWhiteSpace(4)
        denomStr = denomStr + addWhiteSpace(4)
        equalStr = equalStr + addWhiteSpace(4)
        solutionStr = solutionStr + addWhiteSpace(4)
      else:
        arranged_problems = numStr + '\n' + denomStr + '\n' + equalStr
        if solve == True:
          arranged_problems = arranged_problems + '\n' + solutionStr

  if err:
    #print(err)
    return err
  else:
    #print(arranged_problems)
    return arranged_problems


arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)