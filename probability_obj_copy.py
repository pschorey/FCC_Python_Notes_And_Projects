import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    #self.balls = kwargs #ie: {'blue': 4, 'red': 2, 'green': 6}
    self.contents = []
    for k,v in kwargs.items():
      i = 0
      while i < v:
        self.contents.append(k)
        i += 1

  def draw (self, num):
    removed = []
    count = len(self.contents)
    if num >= count:
      return self.contents
    else:
      i = 0
      while i < num:
        #random inclusive
        index = random.randint(0,count - 1)
        removed.append(self.contents[index])
        del self.contents[index]        
        count -= 1
        i += 1 
      return removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  matchedExpectation = 0
  allResults = []
  i = 0
  while i < num_experiments:
    testObj = copy.deepcopy(hat)
    allResults.append(testObj.draw(num_balls_drawn))
    i += 1
  #loop through results one at a time
  for item in allResults:
    #convert row into a dictionary with key:count format
    countedTest = Counter(item)
    #print(countedTest)
    matches = True
    #loop through expected answer to see if matches all key: val pairs
    for k,v in expected_balls.items():
      #checks for non-matches, breaks loop if so
      if (countedTest[k] < v):
        #print('no', countedTest, 'expected', expected_balls, k, ':', v)
        
        #no matches, stop looping
        matches = False
        break
      #for debugging, print results
      '''
      else:
        print('yes.', countedTest, 'expected', expected_balls, k, ':', v)
      '''        
    #loop has finished, now increment if true
    if matches == True:
      matchedExpectation += 1

  return matchedExpectation / num_experiments
