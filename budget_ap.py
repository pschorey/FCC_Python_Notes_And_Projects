import math

class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, amount, description=''):
    self.ledger.append({'amount':amount, 'description':description})

  def withdraw(self, amount, description=''):
    if self.check_funds(amount) == True:
      self.ledger.append({'amount':amount*-1, 'description':description})
      return True
    else:
      return False

  def transfer(self, amount, category):
    if self.check_funds(amount) == True:
      #transfer out of category
      withdrawDescription = "Transfer to " + category.category
      self.ledger.append({'amount':amount*-1, 'description':withdrawDescription})
      #transfer into category
      depositDescription = "Transfer from " + self.category
      category.deposit(amount, depositDescription)
      return True
    else:
      return False  

  def get_balance(self):
    total = 0
    for row in self.ledger:
      total += row['amount']
    return total

  def check_funds(self, amount):
    balance = 0
    for row in self.ledger:
      balance += row['amount']  
    if amount <= balance:
      return True
    else:
      return False

  #called from str(self.food) etc.
  def __repr__(self):
    result = ''
    title = self.category.center(30, '*')
    result += title + '\n'
    total = 0
    for row in self.ledger:
      #for key in row:
      description = row['description'][:23]
      result += description
      amount = row['amount']
      total += row['amount']
      amount = format(amount, '.2f')
      offset = 30 - len(description)
      offsetStr = '{:>' + str(offset) + '}'
      amount = offsetStr.format(amount)
      result += amount + '\n'
    result += 'Total: ' + format(total)
    return result


def create_spend_chart(categories):
  columns = []
  total = 0
  for category in categories:
    categorySpend = 0
    for row in category.ledger:
      if row['amount'] < 0:
        categorySpend += (row['amount'] * -1)
        total += (row['amount'] * -1)
    columns.append({'name':category.category, 'spent':categorySpend})  
    
  i = 0
  while i < len(columns):
    columns[i]['percentage'] = math.floor((columns[i]['spent'] / total)*10)*10
    print(columns[i]['percentage'])
    i += 1

  res = "Percentage spent by category\n"
  y = 100
  while y >= 0:
    part = str(y) + "| "
    part = part.rjust(5)
    res += part
    z = 0
    yData = ''
    while z < len(columns):
      if columns[z]['percentage'] >= y:
        yData = 'o  '
      else:
        yData = '   '
      res += yData
      z += 1
    res += '\n' 
    if y == 0:
      res += '    -'
      for x in columns:
        res += '---'
      res += '\n'
    y -= 10
  
  longestName = 0
  for x in columns:
    if len(x['name']) > longestName:
      longestName = len(x['name'])

  
  ln = 0
  while ln < longestName:
    xLabel = '     '
    for x in columns:
      if ln < len(x['name']):
        part = x['name'][ln] + '  '
      else:
        part = '   '  
      xLabel += part
    res += xLabel + '\n'  
    ln += 1   
  print (res)
  print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
  return res
  #print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")  
