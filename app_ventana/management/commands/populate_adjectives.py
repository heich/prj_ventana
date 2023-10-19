# populate_adjectives.py
# correr conpython manage.py populate_adjectives

from django.core.management.base import BaseCommand
from app_ventana.models import Adjective, AntonymPair
import random

class Command(BaseCommand):
    help = 'Populate Adjective table with provided adjectives and set antonym relationships'

    def handle(self, *args, **kwargs):
        # Lista de adjetivos y sus antónimos
        adjetivos  = [
            'Agradecido,Ingrato',
            'Agudo,Obtuso',
            'Alegre,Melancólico',
            'Altruista,Egoísta',
            'Amable,Grosero',
            'Ambicioso,Conformista',
            'Amigable,Hostil',
            'Analítico,Emocional',
            'Apacible,Agresivo',
            'Apasionado,Desapasionado',
            'Asertivo,Sumiso',
            'Atento,Distante',
            'Atrevido,Cauteloso',
            'Audaz,Tímido',
            'Aventurero,Hogareño',
            'Capaz,Incapaz',
            'Cariñoso,Frío',
            'Carismático,Aburrido',
            'Sensato,Temerario',
            'Cautivo,Libre',
            'Colaborador,Excluyente',
            'Comedido,Descomedido',
            'Compasivo,Inhumano',
            'Comprometido,Descomprometido',
            'Comunicativo,Reservado',
            'Concentrado,Distraído',
            'Confiado,Desconfiado',
            'Consciente,Inconsciente',
            'Considerado,Desconsiderado',
            'Convincente,Inconvincente',
            'Cooperativo,Competitivo',
            'Cordial,Rudo',
            'Creativo,Monótono',
            'Crédulo,Incredulo',
            'Curioso,Apático',
            'Decente,Indecente',
            'Decidido,Indeciso',
            'Dedicado,Desinteresado',
            'Deliberado,Aleatorio',
            'Delicado,Tosco',
            'Desafiante,Complaciente',
            'Despiadado,Misericordioso',
            'Despreocupado,Preocupado',
            'Determinado,Vacilante',
            'Digno,Indigno',
            'Diligente,Negligente',
            'Diplomático,Franco',
            'Directo,Indirecto',
            'Disciplinado,Desordenado',
            'Educado,Vulgar',
            'Eficaz,Ineficaz',
            'Eficiente,Ineficiente',
            'Empático,Egocéntrico',
            'Emprendedor,Resistente al cambio',
            'Encantador,Repelente',
            'Entusiasta,Apatético',
            'Espontáneo,Programado',
            'Eufórico,Deprimido',
            'Excéntrico,Convencional',
            'Exigente,Permisivo',
            'Fiel,Infiel',
            'Flexible,Rígido',
            'Frugal,Derrochador',
            'Fuerte,Débil',
            'Generoso,Tacaño',
            'Gracioso,Serio',
            'Honesto,Deshonesto',
            'Honrado,Corrupto',
            'Humilde,Orgulloso',
            'Iluso,Realista',
            'Imaginativo,Ordinario',
            'Irreflexivo,Reflexivo',
            'Independiente,Dependiente',
            'Inquieto,Tranquilo',
            'Inquisitivo,Indiferente',
            'Inspirado,Desmotivado',
            'Intelectual,Ignorante',
            'Introvertido,Extrovertido',
            'Intuitivo,Lógico',
            'Justo,Injusto',
            'Leal,Traicionero',
            'Meticuloso,Descuidado',
            'Metódico,Caótico',
            'Modesto,Vanidoso',
            'Objetivo,Subjetivo',
            'Optimista,Pesimista',
            'Organizado,Desorganizado',
            'Paciente,Impaciente',
            'Pacífico,Conflictivo',
            'Perspicaz,Ingenuo',
            'Persuasivo,Inamovible',
            'Práctico,Idealista',
            'Precavido,Arriesgado',
            'Previsor,Sorpresivo',
            'Prudente,Imprudente',
            'Razonable,Irrazonable',
            'Moderado,Impulsivo',
            'Resiliente,Vulnerable',
            'Respetuoso,Irrespetuoso',
            'Responsable,Irresponsable',
            'Resuelto,Dubitativo',
            'Sabio,Necio',
            'Seguro,Inseguro',
            'Sencillo,Presumido',
            'Sensible,Insensible',
            'Sereno,Nervioso',
            'Formal,Juguetón',
            'Simpático,Antipático',
            'Sincero,Hipócrita',
            'Sociable,Insociable',
            'Sofisticado,Rústico',
            'Solidario,Individualista',
            'Tolerable,Insoportable',
            'Tolerante,Intolerante',
            'Trabajador,Perezoso',
            'Valiente,Cobarde',
            'Vivaz,Lento',
            'Voluntario,Forzado',
        ]


        #Adjective = apps.get_model('app_ventana', 'Adjective')
        #AntonymPair = apps.get_model('app_ventana', 'AntonymPair')

        for adjective_pair in adjetivos:
            adjective1, adjective2 = adjective_pair.split(',')

            # Crea el adjetivo 1
            adj1 = Adjective.objects.create(adjective_text=adjective1)

            # Crea el adjetivo 2
            adj2 = Adjective.objects.create(adjective_text=adjective2)

            # Crea la relación de antónimo
            AntonymPair.objects.create(adjective1_field=adj1, adjective2_field=adj2)

        self.stdout.write(self.style.SUCCESS('Adjectives and antonym relationships added successfully'))
