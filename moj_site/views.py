from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

try:
    from gpiozero import LED
    led = LED(17)

except Exception:

    class FakeLED:

        def __init__(self):
            self.is_lit = False

        def on(self):
            self.is_lit = True
            print("LED ON")

        def off(self):
            self.is_lit = False
            print("LED OFF")

        def toggle(self):
            self.is_lit = not self.is_lit
            print("LED TOGGLE")

    led = FakeLED()


@login_required
def led_on(request):
    led.on()
    return HttpResponse("<h1>Dioda została WŁĄCZONA!</h1><br><a href='../'>Powrót</a>")


@login_required
def led_off(request):
    led.off()
    return HttpResponse("<h1>Dioda została WYŁĄCZONA!</h1><br><a href='../'>Powrót</a>")


@login_required
def led_index(request):

    html = """
    <html>
    <head>
    <title>Sterowanie LED</title>
    </head>

    <body>

    <h1>Sterowanie diodą z Raspberry Pi</h1>

    <p>Stan diody: {}</p>

    <button onclick="location.href='/led/on/'">
        Włącz diodę
    </button>

    <button onclick="location.href='/led/off/'">
        Wyłącz diodę
    </button>

    </body>
    </html>
    """.format(
        "WŁĄCZONA" if led.is_lit else "WYŁĄCZONA"
    )

    return HttpResponse(html)