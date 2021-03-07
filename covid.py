import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

#Data Correction ---------------------------------------
# missing_values = ['NA','NAN','na','nan','']
# data = pd.read_csv('country_vaccinations.csv',na_values=missing_values) Reading CSV file
# data.dropna()
# data = data.fillna(0)
# data.to_csv('file2.csv') #converting DataFrame to csv file

data = pd.read_csv('file2.csv') #Reading data from file
data = pd.DataFrame(data)
ind = data.loc[data['iso_code']=='IND'] #Extracting India covid vaccination data
usa = data.loc[(data['iso_code']=='USA')] #Extracting USA covid vaccination data

#Total Vaccinations Comparision----------------------------------------------------
x = ['India','USA']
y = [ind['daily_vaccinations'].sum(0),usa['daily_vaccinations'].sum(0)]
print("daily Vaccination",y[0],y[1])
fig1 = plt.figure(1)
ax = fig1.add_subplot(1,1,1)
ax.bar(x,y)
plt.xlabel('Countries')
plt.ylabel('People in Crores')
plt.title('Comparision of people vacinated')
plt.show()


#Vaccination Stage-------------------------------------------------------------
def fullyVacinated(country): #Calculating the number of people who are fully vaccinated
    country = list(country['people_fully_vaccinated'])
    ppl = country[0]
    for i in range(1,len(country)):
        ppl = country[i] - ppl
    return ppl
fig2 = plt.figure(2)
ax1 = fig2.add_subplot(1,2,1)
ax1.set_title("Percentages of People in different stages in India")
ax2 = fig2.add_subplot(1,2,2)
ax2.set_title("Percentages of People in different stages in USA")
x1 = ['Stage 1','Stage 2']
y1 = []
full_ind = fullyVacinated(ind) 
y1.append(y[0]-full_ind)
y1.append(full_ind)
print(y1)
y2 = []
full_usa = fullyVacinated(usa)
y2.append(y[1]-full_usa)
y2.append(full_usa)
print(y2)
ax1.pie(y1,labels=x1,autopct='%1.0f%%')
ax2.pie(y2,labels=x1,autopct='%1.0f%%')
plt.show()

#People vaccinated Per Million--------------------------------------------------
x3 = ind['date']
y3 = ind['daily_vaccinations_per_million']
fig3 = plt.figure(3)
ax3 = fig3.add_subplot(1,2,1)
ax3.set_title("Daily Vaccinations per Million in India")
ax3.bar(x3,y3)
ax3.set_xticklabels(x3,rotation=90,horizontalalignment='right',fontsize=5)
x4 = usa['date']
y4 = usa['daily_vaccinations_per_million']
ax4 =fig3.add_subplot(1,2,2)
ax4.set_title("Daily Vaccinations per Million in USA")
ax4.bar(x4,y4)
ax4.set_xticklabels(x4,rotation=90,horizontalalignment='right',fontsize=5)
plt.show()

#Daily Vacination India and USA-------------------------------------------------
x6 = ind['date']
y6 = ind['daily_vaccinations']
fig4 = plt.figure(4)
ax6 = fig4.add_subplot(1,2,1)
ax6.set_title("Daily Vaccinations in India")
ax6.bar(x6,y6)
ax6.set_xticklabels(x6,rotation=90,horizontalalignment='right',fontsize=5)
x5 = usa['date']
y5 = usa['daily_vaccinations']
ax5 = fig4.add_subplot(1,2,2)
ax5.set_title("Daily Vaccinations in USA")
ax5.bar(x5,y5)
ax5.set_xticklabels(x5,rotation=90,horizontalalignment='right',fontsize=5)
plt.show()




















