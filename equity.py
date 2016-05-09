import datetime
import dateutil.parser as dp
import csv
interest=0.03625 # Our interest rate
R=1+interest/365 # Interest multiplier

def equity(ledger='ledger.csv',today=datetime.date.today()):
  # today is assumed to be future to all deposits in ledger
  f=open(ledger,'r')
  r=csv.reader(f,delimiter=',')
  aSum=0 # Alexis's equity
  mSum=0 # Marcus's equity
  for row in r:
    date=dp.parse(row[0]).date()
    days=(today-date).days
    aDeposit=float(row[1])
    mDeposit=float(row[2])
    aContribution=aDeposit*R**days
    mContribution=mDeposit*R**days
    aSum+=aContribution
    mSum+=mContribution
  return aSum,mSum,aSum+mSum
