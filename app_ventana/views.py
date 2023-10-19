from django.shortcuts import render, redirect, reverse
from .models import Token, Adjective, Feedback, AntonymPair
from django.contrib.auth import authenticate, login, logout
import uuid  # Importa la biblioteca uuid para generar el token ID
import random
from django.contrib.auth.models import User



import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("app_ventana.views")



# Define la función para generar un token único
def crear_token():
    return str(uuid.uuid4())

# Vista para la página de inicio (landing page)
def inicio(request):
    logger.debug('<<Inicio...')
    return render(request, 'ventana/inicio.html')

# Vista para la página de inicio de sesión
def iniciar_sesion(request):

    logger.debug('<<Iniciar sesion....')
    if request.method == 'POST':
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        
        logger.debug('<< Buscando usuario...')

        # Validar al usuario en la base de datos por correo electrónico
        user = authenticate(request, username=user_email)
        if user is not None:
            logger.debug('<<User: {u}\nemail:{m}'.format(u = user_name, m = user_email))
            login(request, user)
            return redirect(reverse('exito'))  # hacia donde va esto??? heich
        else:
            logger.debug('<< No existe usuario...')
            context = {'error_message': 'No existe el usuario.',}
            return render(request, 'ventana/iniciar_sesion.html', context)     

    # si el template incluye una variable, es importante pasarla vacia para no generar un error
    context = {'error_message': '',}
    return render(request, 'ventana/iniciar_sesion.html', context)


# cerrar_sesion
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')

# Vista para la página de registro
def registro(request):
    logger.debug('<<Registro....')
    if request.user.is_authenticated:
        # Usuario autenticado, redirigir a la página de selección de adjetivos
        logger.debug('<<Adjetivos....')
        return redirect('seleccion_adjetivos')
    
    if request.method == 'POST':
        logger.debug('<<POST....')
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']

        # Verificar si el correo electrónico ya existe
        existing_user = Token.objects.filter(user_email=user_email).first()
        if existing_user:
            logger.debug('<<usuario existente....')
            context = {'error_message': 'El correo electrónico ya está registrado.',}
            #return render(request, 'ventana/registro.html', {'error_message': 'El correo electrónico ya está registrado.'})
            return render(request, 'ventana/registro.html', context) 
            #return render(request, 'ventana/registro.html') 
        
        
        # Crear un nuevo token ID y redirigir a la página de selección de adjetivos
        token_id = crear_token()  # Implementa esta función para generar un token único
        
        Token.objects.create(token_id=token_id, user_name=user_name, user_email=user_email)

         # Crear un nuevo usuario de Django
        user = User.objects.create_user(username=user_name, email=user_email)

        login(request, user)
        return redirect('seleccion_adjetivos')
    
    context = {'error_message': '',}
    #return render(request, 'ventana/registro.html')
    return render(request, 'ventana/registro.html', context) 

# Vista para la página de selección de adjetivos
def seleccion_adjetivos(request):
    logger.debug('<<Seleccion adjetivos....{1}',request.user.is_authenticated)
    if not request.user.is_authenticated:
        # Usuario no autenticado, redirigir a la página de inicio
        return redirect('inicio')
    
    if request.method == 'POST':
        selected_adjectives_ids = request.POST.getlist('adjectives')
        
        # Obtener los objetos Adjective correspondientes a los IDs seleccionados
        selected_adjectives = Adjective.objects.filter(pk__in=selected_adjectives_ids)
        
        # Crear un nuevo objeto Feedback y asociarlo con el usuario actual
        feedback = Feedback.objects.create(user=request.user)
        
        # Asignar los adjetivos seleccionados al Feedback
        feedback.adjectives.set(selected_adjectives)
        
        # Generar la URL para que otros usuarios evalúen estos adjetivos
        url = generate_evaluation_url(request.user)
        
        # Guardar la URL en el Feedback
        feedback.evaluation_url = url
        feedback.save()
        
        return redirect('registro')  # Ojo:: cambiar el destino despues de recibir la evaluacion

    # # Obtener 30 pares de adjetivos al azar de la base de datos
    # all_adjectives = list(Adjective.objects.all())
    # random.shuffle(all_adjectives)
    # selected_adjectives = all_adjectives[:30]

    # return render(request, 'ventana/seleccion_adjetivos.html', {'adjectives': selected_adjectives})

    # Obtener todos los adjetivos y sus antónimos de la base de datos
    #all_adjectives = list(AntonymPair.objects.all())
    adjective_pairs = AntonymPair.objects.all()

    # Baraja aleatoriamente los pares para que sean diferentes cada vez
    #random.shuffle(all_adjectives)

    # Obtén solo los primeros 30 pares de adjetivos
    #selected_pairs = all_adjectives[:30]
    #return render(request, 'ventana/seleccion_adjetivos.html', {'adjective_pairs': selected_pairs})
    return render(request, 'ventana/seleccion_adjetivos.html', {'adjective_pairs': adjective_pairs})




# Función para generar la URL de evaluación
def generate_evaluation_url(user):
    logger.debug('<< Generar URL ....')
    # Obtener el token asociado al usuario
    user_token = Token.objects.get(user=user)
    
    # Generar una URL única utilizando el token
    unique_url = reverse('evaluacion', args=[user_token.token_id])
    
    return unique_url



# Vista para mostrar resultados
def resultados_evaluaciones(request):
    logger.debug('<< Resultado evaluaciones....')
    if not request.user.is_authenticated:
        # Usuario no autenticado, redirigir a la página de inicio
        return redirect('inicio')
    
    # Obtener las evaluaciones del usuario autenticado
    feedback_list = Feedback.objects.filter(token=request.user)
    
    return render(request, 'ventana/resultados_evaluaciones.html', {'feedback_list': feedback_list})
