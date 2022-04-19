from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pandas as pd
from pandas.io import json
import csv
import random

from .models import Data




# def make_csv(data):
#     fieldnames = data[0].keys()
#     rows = data
#     with open("property.csv", 'w', newline='') as csv_file:
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(rows)


# def table_view(request):
#     property_data = []
#     for index, item in enumerate(range(5)):
#         data = {}
#         property_list = ["orchid", "esplanade", "supreeme", "magante", "belair"]
#         data["property_name"] = property_list[index]
#         data["property_price"] = random.randint(3, 10) * 100000
#         data["property_rent"] = random.randint(3, 10) * 1000
#         data["emi"] = random.randint(3, 10) * 100
#         data["tax"] = random.randint(150, 455)
#         data["other_exp"] = random.randint(110, 550)  
#         property_data.append(data) 
        
#     # make_csv(property_data)
    
#     return render(request, "myapp/table.html", {
#         "property_data":property_data,
#         "table_headers": property_data[0].keys() 
#     })


def delete_previous_data():
    data = Data.objects.all()
    data.delete()
    return data

def read_file(all_data, filename):
    df = pd.read_csv(all_data)
    converted_to_json = df.reset_index().to_json(orient='records')
    
    data = []
    
    data = json.loads(converted_to_json)
    for d in data:
        name = d["property_name"]
        price = d["property_price"]
        rent = d["property_rent"]
        emi = d["emi"]
        tax = d["tax"]
        exp = d["other_exp"]
        monthly_expenses = emi + tax + exp
        monthly_income = rent - monthly_expenses
        
        dt = Data(name=name, price=price, rent=rent, emi=emi, tax=tax, exp=exp,
                monthly_expenses=monthly_expenses, monthly_income=monthly_income)
        dt.save()
        
    file_name = filename[0]
    
    data_objects = Data.objects.all()
    context = {"data_objects": data_objects,
            "file_name":file_name}
    return context
    

def csv_file_accept(request):
    if (request.method == "POST"):
        if request.FILES and request.FILES["file"]:
            uploaded_file = request.FILES["file"]
            
            # To know the filename
            name_of_file = []
            for filename, file in request.FILES.items():
                name_of_file.append(file)
                
            # delete the previous data.    
            delete_previous_data()
            
            context = read_file(uploaded_file, name_of_file)
            return render(request, "myapp/index.html", context)
        return render(request, "myapp/index.html")             
    else:
        print("This is GET request.")        
        
    return render(request, "myapp/index.html")


