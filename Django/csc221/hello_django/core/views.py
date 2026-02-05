from django.shortcuts import render, redirect
from django.views import View

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
