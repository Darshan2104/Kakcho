from cmath import isnan, nan
from pickle import GET
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import pandas as pd
import csv
from django.conf import settings
import os
from miniProject.settings import BASE_DIR
import math


# @login_required
UPLOAD_FOLDER = 'miniProject/media/'

global l
l = []

def upload_file(request):
    if request.method == 'POST':
        input_file = request.FILES['file']
        # l = input_file
        df = pd.read_csv(input_file)
        # z = df
        l.append(df)
        # print("local : ",l)
        # print("local : ",len(l))
        # print("Done!!!!")
        return render(request,'Select.html')
    else:
        return render(request,'home.html') 

# print(len(l))
# print("Global",z)

def task1(request):
    # print("task1 : ",len(l))
    if len(l) == 0:
        return redirect('upload_file') 
    else:
        df = l[-1]
        paid = df.query('Type == "Paid"')
        free = df.query('Type == "Free"')

        paid.to_csv('./media/paid.csv')
        free.to_csv('./media/free.csv')

        file_path = os.path.join(BASE_DIR, 'media')
        obj = ['paid.csv','free.csv'] #list of csv-->files
        return render(request,'Select.html',{'file_path':file_path, 'obj':obj,'task':1})

def task2(request):
    if len(l) == 0:
        return redirect('upload_file')
    else:
        df = l[-1]
        all_unique_rate = df['Rating'].unique()
        obj = [] #list of csv-->files
        # print(all_unique_rate)
        for a in all_unique_rate:
            name = a
            z = df.loc[df['Rating'] == a]
            z.to_csv('./media/'+str(name)+'.csv')
            obj.append(str(name) + '.csv')

        return render(request,'Select.html',{'obj':obj,'task':2})

def task3(request):
    if len(l) == 0:
        return redirect('upload_file')
    else:
        df = l[-1]
        all_rate = df['Rating']
        new_col = []
        # print(all_rate)
        for i in all_rate:
            # print(i)
            if math.isnan(i):
                new_col.append(round(0))
            else:
                new_col.append(round(i))
        # print(new_col)
    # Rating Roundoff
        df['Rating Roundoff'] = new_col
        df.to_csv('./media/Updated_file.csv')
        obj = ['Updated_file.csv']
        return render(request,'Select.html',{'obj':obj,'task':3})
