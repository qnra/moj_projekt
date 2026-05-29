from django.http import HttpResponse
from .models import Pomiar
import random
import json

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def sensor_view(request):

    distance = random.randint(5, 100)

    Pomiar.objects.create(distance=distance)

    pomiary = Pomiar.objects.order_by('-created_at')[:20]

    labels = []
    values = []

    for p in reversed(pomiary):
        labels.append(p.created_at.strftime("%H:%M:%S"))
        values.append(p.distance)

    html = f"""
    <html>

    <head>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    </head>

    <body>

    <h1>Czujnik odległości</h1>

    <h2>Aktualny pomiar: {distance} cm</h2>

    <canvas id="myChart"></canvas>

    <script>

    const ctx = document.getElementById('myChart');

    new Chart(ctx, {{
        type: 'line',
        data: {{
            labels: {json.dumps(labels)},
            datasets: [{{
                label: 'Odległość (cm)',
                data: {json.dumps(values)}
            }}]
        }}
    }});

    </script>

    </body>

    </html>
    """

    return HttpResponse(html)

def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')

    else:

        form = UserCreationForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )