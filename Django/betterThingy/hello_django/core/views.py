from urllib import request
from django.shortcuts import render, redirect
from django.views import View
from .models import Task

# Create your views here.
count = 1
def page_count(request):
  global count 
  count += 1 
  context = {'count':count}
  return render(request, 'core/count.html', context)


class Bmi(View):
  def get(self, request):
    #for a GET request, our response should be  a form
    # if there are results in the session, also show them
    bmi_data = request.session.pop('bmi_data', None)

    return render(request, 'core/bmi.html',bmi_data)

  def post(self, request):
    #for a POST request, we should handle the form and then redirect
    height = int(request.POST.get('height'))
    weight = int(request.POST.get('weight'))
    bmi = weight / height * height
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    request.session['bmi_data'] = {
        'height':height,
        'weight':weight,
        'bmi': round(bmi,1),
        'category': category,
    }
    print(bmi)
    return redirect(request.path)


class Bread(View):
  def get(self, request):
    #for a GET request, our response should be  a form
    # if there are results in the session, also show them
    form_data = request.session.pop('form_data', None)

    return render(request, 'core/bread.html',form_data)

  def post(self, request):
    #for a POST request, we should handle the form and then redirect
    flour = int(request.POST.get('flour'))
    target_hydration = float(request.POST.get('target_hydration'))
    starter = int(request.POST.get('starter'))

    #hydration = total water / total flour
    # so if 100% hydration starter:
    # hydration = (water + 0.5 * starter) / (flour + 0.5 * starter)
    # so solve that for water:
    water = (target_hydration * (flour + 0.5 * starter)) - (0.5 * starter)
    
    request.session['form_data'] = {
      'flour':flour,
      'target_hydration':target_hydration,
      'starter': starter,
      'water': round(water),
    }
    
    return redirect(request.path)

class SolveTime(View):   
  def get(self, request):
    solvetime_data = request.session.pop('solvetime_data', None)
    return render(request, 'core/solveTime.html', solvetime_data)
  
  def post(self, request):
    coefs = int(request.POST.get('coefs'))
    degree = int(request.POST.get('degree'))

    # solve time = (coefs * degree^2) / 12
    solve_time = (coefs * degree ** 2) / 12

    request.session['solvetime_data'] = {
      'coefs': coefs,
      'degree': degree,
      'solve_time': round(solve_time),
    }

    return redirect(request.path)
  

class TodoIndex(View):
  def get(self, request):
    tasks = Task.objects.all()
    todo_data = {
      'tasks': tasks
    }
    return render(request, 'core/todo.html', todo_data)
  
  def post(self, request):
    name = request.POST.get('name')
    description = request.POST.get('description')

    Task.objects.create(name=name, description=description)

    return redirect(request.path)

class EconIndex(View):
  def get(self, request):
    title_data = {'title': "Country name"}
    return render(request, 'core/econProject/index.html', title_data)

class EconMap(View):
  def get(self, request):
    title_data = {'title': "Country Map"}
    return render(request, 'core/econProject/map.html', title_data)

class EconImports(View):
  def get(self, request):
    title_data = {'title': "Country Imports and Exports"}
    return render(request, 'core/econProject/impexp.html', title_data)
  
class EconEcon(View):
  def get(self, request):
    title_data = {'title': "Country Economy"}
    return render(request, 'core/econProject/econ.html', title_data)