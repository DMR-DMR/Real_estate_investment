#formatting variables

linebreak=" "
conclusion= "     ------Investment Conclusion------"
title="     ------Real Estate investments calculator--------"
greeting ="     Hi!, wecome to my leveraged Real Estate investment calculator"
program_version = "     RE investment calculator v.02 - Berlin 08/12/2017"
author="     Diego Maldonado Rosas - diego.maldonado@whu.edu"
keytocontinue="     Press any Key to continue"
line="        --------------------------------------"
# Welcome message

print linebreak
print title
print program_version
print author
print linebreak
print line
print greeting
print linebreak

# import decimal

import numpy as np

#user input section.

ob_price = 70000000 #input("     How much is the purchase price of the object?:  ")
ob_price = float(ob_price)

print linebreak

upfront_pmt = 40000000 #input("     how much money are you paying upfront?:  ")
upfront_pmt = float (upfront_pmt)

print linebreak

y_irate = 5.76 #input ("     What is the interest rate you can get from the bank? (i.e: 3.5% = '3.5'):  ")
y_irate = float (y_irate)
y_irate_percent = ( y_irate / 100.0)
m_irate= float ( y_irate_percent / 12 )

print linebreak

y_duration = 25 #input ("     How many years duration is the loan? (i.e. 30 years = '30'):  ")
y_duration = float (y_duration)
periods = y_duration * 12
periods = float (periods)

print linebreak

m_rent = 460000 #input ("     What is the possible rent per month you can get?:  ")
m_rent = float (m_rent)
y_rent = m_rent*12
y_rent = float (y_rent)

print linebreak

y_rentgrowth = 3 #input ("     What is the avg long term yearly land price increase? (i.e. average 5%/year = '5'):  ")
y_rentgrowth = float (y_rentgrowth)
y_rentgrowth = (y_rentgrowth/100)/12
y_rentgrowth = float (y_rentgrowth)

print linebreak

op_cost = input("     What is your opportunity cost? (i.e. 6% = '6'):  ")
op_costpercent =  (float(op_cost))/100
m_op_cost = op_costpercent/12

#calculate loan principal
principal = ob_price - upfront_pmt
principal = float (principal)

#here comes the formula that calculates the payment of a defined mortgage loan.
m_pmt = np.pmt(m_irate, periods, principal)
m_pmt = round (m_pmt,2)

#here is the formula that calculates the price to rent ratio
price_rent_ratio= ob_price / y_rent
price_rent_ratio = int(price_rent_ratio)

#formula for calculating net yield per month
m_net_yield = m_rent + m_pmt

#PV of cash flow (20 year annuity factor)
apv_m_CF = ((m_net_yield/(m_op_cost - y_rentgrowth)) * ( 1 -((1 + y_rentgrowth) / ( 1 + m_op_cost)) ** periods))
apv = round (apv_m_CF,2)
anpv = (- upfront_pmt + apv) + ((ob_price * ((1+(y_rentgrowth * 12))** y_duration))/((1+op_costpercent) ** y_duration))
resale_price = ob_price * ((1+(y_rentgrowth * 12))** y_duration)

# Calculating IRR
cf = np.repeat(m_net_yield,periods)
cf = np.append(-upfront_pmt,cf)
cf = np.append(cf,(upfront_pmt+m_net_yield))
cf_n = anpv
cf_irr = np.irr(np.r_[-cf_n,cf])
cf_irr = cf_irr*1200
cf_irr = round(cf_irr,4)
#project_irr = round(np.irr(cf_discounted_array),5)


#formatting section for display

S_price = ('${:,.2f}'.format(ob_price))
S_upfrontnt = ('${:,.2f}'.format(upfront_pmt))
S_principal = ('${:,.2f}'.format(principal))
percent_y_irate = ('{:,.2f}%'.format(y_irate))
S_m_rent = ('${:,.2f}'.format(m_rent))
S_m_pmt = ('${:,.2f}'.format(m_pmt))
S_y_rent = ('${:,.2f}'.format(m_rent))
S_y_rent = ('${:,.2f}'.format(y_rent))
S_anpv = ('${:,.2f}'.format(anpv))
cf_irr = ('{:,.2f}%'.format(cf_irr))

#messages
S_price_message =     "     Price of object:...........%s" % S_price
S_principal_message = "     Mortgage loan:.............%s" % S_principal
per_y_rate_message =  "     Interest rate:.............%s" % percent_y_irate
duration_message =    "     Mortgage duration:.........%s years" % y_duration
S_m_rent_message =    "     Expected monthly rent:.....%s " % S_m_rent
S_m_pmt_message =     "     Monthly Mtgage Pmt:........%s " % S_m_pmt
S_anpv_message =      "     Project NPV................%s " % S_anpv
price_rent_ratio_message = "     Price to Rent Ratio........%s " % price_rent_ratio
irr_message =         "     Project IRR................%s " % cf_irr

#import module Table
from prettytable import PrettyTable
table1 = PrettyTable()
table1.field_names = ["obj price", "Upfront PMT", "Loan", "Y I Rate", "Duration" ]
table1.add_row( [S_price, S_upfrontnt, S_principal, percent_y_irate, y_duration] )
print table1

#print all conclusion messages
print linebreak
print linebreak
print conclusion
print linebreak
print S_price_message
print S_principal_message
print per_y_rate_message
print duration_message
print S_m_pmt_message
print S_m_rent_message
print linebreak
print S_anpv_message
print price_rent_ratio_message
print irr_message
print linebreak
print linebreak
print linebreak
print program_version
print author
print linebreak
print resale_price

input(" press any key to exit ")
