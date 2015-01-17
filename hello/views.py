from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    return HttpResponse('''
<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <title>Vertigo -- Lean Mean Green Machine</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
        <link href='http://fonts.googleapis.com/css?family=Josefin+Sans:400,600|Shadows+Into+Light|Play|Cuprum:400,700|Courgette' rel='stylesheet' type='text/css'>
    </head>
    <body>
        <header>
            <h1>Vertigo </h1>
            <h2>Green Encryption</h2>
            
        </header>
        <div>
            
        </div>
        <footer>
             
       </footer>
    </body>
</html>
''')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

