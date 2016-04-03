import csv, json
import numpy as np
from collections import Counter
from sklearn import svm

def readdata (): #calls the csv file into python
    csvfile = open('DrColby_data.csv',"rU")
    dmd = csv.reader(csvfile, delimiter = ",")
    dmd.next()
    header = list(dmd)
    csvfile.close()
    dmd_data = []
    for row in header:
        dmd_data.append(row)
    return dmd_data
mydata = readdata() #the data from the csv file

def readanycolumn(mydata, n): #to read a column
    datacolumn = []
    for row in mydata:
        datacolumn.append(row[n])
    return datacolumn

def countelements(n):
    x = readanycolumn(mydata,n)
    d = Counter(x)
    count=json.dumps(d)
    return count

with open('DrColby_data.csv') as fin, open('out.csv', 'wb') as fout:
    r = csv.reader(fin)
    w = csv.writer(fout)
    for row in r:
        replacements = {'Y':'1', 'N':'0', 'F':'3', 'M':'4', 'W':'1', 'B': '2', 'A':'3', 'H':'4', 'C':'1', 'PE':'2', 'S':'4','M':'1', 'V':'2','SL':'1', 'SG':'2', 'L':'3', 'S':'4', 'G':'5','DS':'1', 'SF':'2', 'F':'3', 'D':'4', 'T':'1', 'B':'2', 'R':'3', 'P' : '1', 'MO':'0', 'MI':'0', '':'0', ' ': '0'}
        for row in r:
            w.writerow([replacements.get(cell,cell)for cell in row])

def new_data (): #calls the csv file into python
    csv_file = open('out.csv',"rU")
    dmd = csv.reader(csv_file, delimiter = ",")
    #header = list(dmd)
   # strip=map(lambda s: s.strip (), strip)
    dmd_data = []
    for row in csv_file:
        dmd_data.append(row)
    csv_file.close()
    return dmd_data
newdata=new_data()
newdata[:]=[line.rstrip("\n") for line in newdata]

the_data= np.array(newdata)
#print dataset
thedata = the_data.T
dataset = thedata.tolist()
#the_data = [float(x) for x in the_data]

def split_class_and_data(dataset): #splits the class values into one list and the remaining data into 2nd list
    y =[]
    d=[]
    for row in dataset:
        row1 = row.split(",");
        y.append(row1[15])
        d.append(row1[1:14]+row1[16:])
    return (y,d) #tuple that returns the 1st elent, the second element)

y,X= split_class_and_data(dataset)


clf=svm.SVC(kernel='linear', C=1) #setting up svm to be trained. use linear as default
clf.fit(X,y) #first arg is data, second arg is the class
print "clf=", clf
print"Now predicting"
t1=X[0]   #the first entry in the data, and without the class info and predict what class it belongs to.
r=clf.predict(t1) #pass in the item or entry that you want to make a prediction about
print "Prediction result=",r
print "\n\n"


print "svmdata.py loaded"
#training is analogous to treatment outcome, location etc etc is learned by the svm and it is trained

