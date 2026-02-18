# list views but simple

Were gonna do it in just a couple lines.

## Basic thing
View:

- get all the objects from the model
- context = dictionary with objects (name is name of list)
- return render

## new better thing
View:

- model = {which model}
- model_name = title of model
- context = dictionary with objects (name is model_name+"_list")
- return render

can now be customised for whatever model

## generic list view
Way better than that thing we wrote but with the same idea

## Now how to make a list view
views.py

class _____listView(generic.ListView):
  model = _____

that's it. Done.

for detail, ______detail.html

<h1> _____ {_____.name} <h1>

whatever you want

# Yay Done!



