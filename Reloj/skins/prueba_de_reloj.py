import turtle
import time
import math

# Función para dibujar un círculo como el reloj
def draw_clock(radius):
    turtle.hideturtle()
    turtle.pensize(7)
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.dot(15)

    # Configuración para un círculo transparente
    turtle.fillcolor('')  # Color de relleno transparente
    turtle.pensize(2.5)     # Grosor de la pluma = 0 (sin bordes)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Función para dibujar las manecillas del reloj
def draw_hand(angle, length):
    turtle.pendown()
    turtle.goto(0, 0)
    turtle.setheading(angle)
    turtle.penup()
    turtle.backward(length)
    turtle.pendown()
    turtle.goto(0, 0)

# Función para calcular el ángulo de las manecillas
def get_angle(value, total):
    return (value / total) * -360 - 90

## Configuración inicial de la pantalla
screen = turtle.Screen()
screen.title("Reloj")
screen.bgcolor("white")
screen.tracer(0)
screen.setup(width=400, height=400)

# Dibujar el reloj inicial
radius = 140  # Define el radio aquí
draw_clock(radius)

# Función para ajustar el tamaño del reloj según el tamaño de la ventana
def resize_window(width, height):
    min_size = min(width, height)
    clock_size = min_size * 0.8  # El reloj ocupará el 80% del tamaño mínimo

    turtle.clear()


# Actualizar el tamaño del reloj al cambiar el tamaño de la ventana
screen.update()
screen.listen()
screen.onclick(resize_window)


# Bucle para actualizar las manecillas del reloj
while True:
    # Obtener el tiempo actual
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Calcular los ángulos para las manecillas
    hour_angle = get_angle(hours, 12)
    minute_angle = get_angle(minutes, 60)
    second_angle = get_angle(seconds, 60)

    # Borrar las manecillas anteriores
    turtle.clear()

    # Dibujar el reloj
    resize_window(screen.window_width(), screen.window_height())
   
    # Dibujar las manecillas del reloj
    draw_hand(hour_angle, radius * 0.5)
    draw_hand(minute_angle, radius * 0.8)
    draw_hand(second_angle, radius * 0.8)

    # Actualizar la pantalla de Turtle
    turtle.update()

    # Esperar un segundo antes de la próxima actualización
    time.sleep(1)
