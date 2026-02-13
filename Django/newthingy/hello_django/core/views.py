from django.shortcuts import render

count = 0
def view_count(request):
  global count
  count += 1
  context = {'view_count': count}
  return render(request, 'core/viewCount.html', context)