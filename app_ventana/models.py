from django.db import models

class Token(models.Model):
    token_id = models.CharField(max_length=100, unique=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()

    class Meta:
        app_label = 'app_ventana'  # Agrega esta línea



class Adjective(models.Model):
    adjective_id = models.AutoField(primary_key=True)
    adjective_text = models.CharField(max_length=50)
    
    # Agrega un campo de relación para los antónimos
    antonyms = models.ManyToManyField('self', symmetrical=True, through='AntonymPair', related_name='related_antonyms')

    def __str__(self):
        return self.adjective_text

    class Meta:
        app_label = 'app_ventana'

class AntonymPair(models.Model):
    adjective1_field = models.ForeignKey(Adjective, on_delete=models.CASCADE, related_name='antonym_pairs_1')
    adjective2_field = models.ForeignKey(Adjective, on_delete=models.CASCADE, related_name='antonym_pairs_2')

    def __str__(self):
        return f'{self.adjective1_field.adjective_text} - {self.adjective2_field.adjective_text}'

    class Meta:
        app_label = 'app_ventana'


class Feedback(models.Model):
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    selected_adjectives = models.ManyToManyField(Adjective)

    class Meta:
        app_label = 'app_ventana'
