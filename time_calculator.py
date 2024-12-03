def add_time(start, duration, startday=None):
  weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  new_time = start
  stthrs, sttmin = hhhmmints(hhmm12to24(start))
  durhrs, durmin = hhhmmints(duration)
  newhrs, newmin = stthrs + durhrs, sttmin + durmin 
  nbhrs = newmin // 60
  newmin = newmin % 60
  newhrs = newhrs + nbhrs
  nbdays = newhrs // 24
  newhrs = newhrs % 24
  new_time = hhmm24to12(f'{newhrs:0>2}' + ":" + f'{newmin:0>2}')
  if startday!=None:
    startday = startday.lower()
    startday = startday.title()
    try:
      sttdate=weekdays.index(startday)
    except:
      print("Warning: invalid weekday input.")
    enddate = sttdate + nbdays
    enddate = enddate % 7
    endday = weekdays[enddate]
    new_time = new_time + ", " + endday
  if nbdays > 0:
    if nbdays > 1:
      new_time = new_time + " (" + str(nbdays) + " days later)"
    else:
      new_time = new_time + " (next day)"
  return new_time
  
def hhmm12to24(timestring):
# Convert from 12 hour to 24 hour format
  hrsint, minint = hhhmmints(timestring)
  prdstr = timestring[-2:].upper()
  if not prdstr in ["AM", "PM"]: return 'Error: not a valid AM/PM period.'
# Algorithm below from https://www.freecodecamp.org/news/mathematics-converting-am-pm-to-24-hour-clock/
  if prdstr=="AM" and (hrsint, minint) > (12, 00) and (hrsint, minint) <= (12, 59):
    hrsoff = -12
  elif prdstr=="PM" and (hrsint, minint) > (1, 00) and (hrsint, minint) <= (11, 59):
    hrsoff = 12
  else:
    hrsoff = 0
  return f'{hrsint+hrsoff:0>2}' + ":" + f'{minint:0>2}'
#  return str(hrsint+hrsoff) + ":" + str(minint) + " "

# Convert from 24 hour to 12 hour format
def hhmm24to12(timestring):
  hrsint, minint = hhhmmints(timestring)
# Algorithm below _adapted_ from https://www.freecodecamp.org/news/mathematics-converting-am-pm-to-24-hour-clock/
  hrsoff=0
  if (hrsint, minint) > (0, 0) and (hrsint, minint) <= (0, 59):
    hrsoff=12
    prdstr="AM"
  elif (hrsint, minint) > (1, 0) and (hrsint, minint) <= (11, 59): prdstr="AM"
  elif (hrsint, minint) > (12, 0) and (hrsint, minint) <= (12, 59): prdstr="PM"
  elif (hrsint, minint) > (13, 0) and (hrsint, minint) <= (23, 59):
    hrsoff=-12
    prdstr="PM"

  return str(hrsint+hrsoff) + ":" + f'{minint:0>2}' + " " + prdstr
#  return f'{hrsint+hrsoff:0>2}' + ":" + f'{minint:0>2}' + " " + prdstr

# Take in string with digits, colon as separator, 
# and return integers for hours, mins
def hhhmmints(timestring):
  hrsint, minint = 0, 0
  if not timestring.find(':'): return 'Error: not a valid time string.'
  colpos = timestring.find(':')
  try:
    hrsint = int(timestring[:colpos])
    minint = int(timestring[colpos+1:colpos+3])
  except:
    'Error: not a valid time string.'
  return hrsint, minint