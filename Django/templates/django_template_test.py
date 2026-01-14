import django
import os.path
from django.template import Template, Context

#setup Django. Don't mess with these lines
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
django.conf.settings.configure(
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        os.path.join(PROJECT_PATH),
        ],
    }])
django.setup()

#define your template. 
#these get long, so it's helpful to create it as a separate file
template = django.template.loader.get_template('template.html')

#define your context and render. I'm looping through a list
# so that I can render a bunch of times.
Context = {"name":"some shit", "adj":"gud", "comment": "Might do again.", "numStars": 4}
book = template.render(Context)

with open('newReview.html', 'w') as f:
  f.write(book)

# for g in ['Alice', 'Bob', 'Cathy', 'Dave']:
#     context = {'name':g}
#     personalized_email = template.render(context)

#     with open('invite_'+g+'.txt', 'w') as f:
#         f.write(personalized_email)

# {extends template.html}

# {% block content %}
#     <h2>Reviewed {name}</h2>
#     <p>It was {adj}. {comment}</p>
#     <p>Rating: {numStars} / 5 Stars/</p>

# {% endblock %}