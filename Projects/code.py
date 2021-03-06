# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path, delimiter=',',skip_header=1)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
new_record = np.asarray(new_record)
census = np.concatenate((data,new_record),axis=0)
print(census)
#Code starts here



# --------------
#Code starts here
import numpy as np
age = census[:,0]
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)
print(max_age,min_age,age_mean,age_std)


# --------------
#Code starts here
import numpy as np
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]
len_0,len_1,len_2,len_3,len_4 = len(race_0),len(race_1),len(race_2),len(race_3),len(race_4)
print(len_0,len_1,len_2,len_3,len_4)
x = min(len_0,len_1,len_2,len_3,len_4)
if len_0 == x:
    minority_race = 0
if len_1 == x:
    minority_race = 1
if len_2 == x:
    minority_race = 2
if len_3 == x:
    minority_race = 3
if len_4 == x:
    minority_race = 4
print(minority_race)   




# --------------
#Code starts here
import numpy as np
senior_citizens = census[census[:,0]>60]
working_hours_sum = senior_citizens[:,6].sum()
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
import numpy as np
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])
print(avg_pay_high)
print(avg_pay_low)


