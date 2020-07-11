import re
import math

def getHours(time):
  hours = re.findall("^\d+", time)
  return int(hours[0])

def getMinutes(time):
  minutes = re.findall("\d+$", time)
  return int(minutes[0])

def add_time(start, duration, dayName=False):
  startTime = start.split()
  startHours = getHours(startTime[0])
  startMinutes = getMinutes(startTime[0])
  durationHours = getHours(duration)
  durationMinutes = getMinutes(duration)

  start_PM = re.search("PM$", start)
  if start_PM:
    startHours += 12 #converts to mil time
  else:
    if startHours == 12:
      startHours = 0 #sets 12 am to 0

  #adds minutes, converts to hours, zero fills
  newMinutes = startMinutes + durationMinutes
  if newMinutes >= 60:
    durationHours += 1
    newMinutes = newMinutes % 60
  newMinutes = str(newMinutes)
  newMinutes = newMinutes.zfill(2)

  #calc num of new days (new day is counted after passing 12pm each night, not a literal 24 hour period)
  newHours = startHours + durationHours
  days = math.floor(newHours / 24)

  #if the day of week provided as arg, format and calculate the new day to display correctly
  if dayName != False:
    dayName = dayName.title()
    week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
    dayIndex = week.index(dayName)
    #adds new days to current day index and % 7
    newDayIndex = (dayIndex + days) % 7
    dayName = week[newDayIndex]
    dayName = ', ' + dayName
  else:
    dayName = ''

  #format day string according to directions
  if days == 0:
    days = ''
  elif days == 1:
    days = ' (next day)' 
  else:
    days = ' ({} days later)'.format(days) 

  #extract new hours for times over 24
  newHours = newHours % 24
  #convert new hours to standard time
  if newHours >= 12:
    newMeridian = 'PM'
    if newHours > 12: #don't sub 12 from 12 PM
      newHours -= 12
  else:
    newMeridian = 'AM'
    if newHours <= 0: #change 0 to 12 AM
      newHours = 12
  newHours = str(newHours)    

  new_time = newHours + ':' + newMinutes + ' ' + newMeridian + dayName + days
  
  #print(new_time)
  return new_time

add_time("3:30 PM", "2:12")
add_time("11:55 AM", "3:12")
add_time("9:15 PM", "5:30")
add_time("11:40 AM", "0:25")
add_time("2:59 AM", "24:00")
add_time("11:59 PM", "24:05")
add_time("8:16 PM", "466:02")
add_time("5:01 AM", "0:00")
add_time("3:30 PM", "2:12", "Monday")
add_time("2:59 AM", "24:00", "saturDay")
add_time("11:59 PM", "24:05", "Wednesday")
add_time("8:16 PM", "466:02", "tuesday")
