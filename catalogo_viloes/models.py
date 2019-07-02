from django.db import models

# Create your models here.
class Vilao(models.Model):

    armas_opcoes = [
        ('machado','Machado'),
        ('escada','Escada'),
        ('espada','Espada'),
        ('tesoura','Tesoura'),
        ('veneno','Veneno'),
        ('pexera','Pexera'),
        ('serra elétrica','Serra Elétrica'),
        ('punhos','Punhos'),
        ('ak4','AK47'),
        ('almofada','Almofada'),
        ('outros','Outros'),
        ('desarmado','Desarmado'),
    ]

    nivel_valor = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),

    ]

    nome = models.CharField(max_length=30)
    categoria = models.CharField(max_length=10)
    habilidade = models.TextField()
    mortes = models.PositiveIntegerField()
    armas = models.CharField(max_length=20, choices=armas_opcoes)
    nivel_maldade = models.PositiveIntegerField(choices=nivel_valor)
    vivo = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='')

    def __str__(self):
        return self.nome