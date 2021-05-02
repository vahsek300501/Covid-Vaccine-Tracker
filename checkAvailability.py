import urllib.request
import datetime
from datetime import date
import re

def getDateArray():
  dateArr = []
  
  for i in range(0,10):
    today = date.today()
    tmpDate = today + datetime.timedelta(days = i)
    print(tmpDate)
    dateStr = str(tmpDate.day) + "-" +str(tmpDate.month) + "-" +str(tmpDate.year)
    dateArr.append(dateStr)

  return dateArr

