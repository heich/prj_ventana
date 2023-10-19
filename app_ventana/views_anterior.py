from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Token, Adjective, Feedback
import uuid  # Importa la biblioteca uuid
import random # seleccionar 30 adjetivos aleatoriamente

# Create your views here.

# Define la función para generar un token único
def generate_unique_token():
    return str(uuid.uuid4())


def registro(request):
    if 'token_id' in request.session:
        # Usuario con token ya existente
        token_id = request.session['token_id']
        if request.method == 'POST':
            selected_adjectives = request.POST.getlist('adjectives')
            token = Token.objects.get(token_id=token_id)
            feedback = Feedback.objects.create(token=token)
            feedback.selected_adjectives.set(selected_adjectives)
            return redirect('registro')
    else:
        # Nuevo usuario
        if request.method == 'POST':
            user_name = request.POST['user_name']
            user_email = request.POST['user_email']
            token_id = generate_unique_token()
            Token.objects.create(token_id=token_id, user_name=user_name, user_email=user_email)

            # Selecciona 30 adjetivos al azar de los disponibles
            all_adjectives = list(Adjective.objects.all())
            random.shuffle(all_adjectives)

            selected_adjectives = all_adjectives[:30]

            #request.session['token_id'] = token_id

            feedback = Feedback.objects.create(token=Token.objects.get(token_id=token_id))
            #feedback = Feedback.objects.create(token=token_id)
            feedback.selected_adjectives.set(selected_adjectives)
            return redirect('registro')

            #return redirect('registro')

    adjectives = Adjective.objects.all()
    context = {'adjectives': adjectives}
    return render(request, 'ventana/registro.html', context)
