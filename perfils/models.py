from django.db import models
from django.contrib.auth.models import User
# import exceções
from django.forms import ValidationError
# expressão regular
import re
from utils.validacpf import valida_cpf


class PerfilModels(models.Model):
    ESTADOS_CHOICES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),        
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    idade = models.IntegerField(verbose_name='Idade')
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    endereco = models.CharField(max_length=50, verbose_name='Endereço')
    numero = models.CharField(max_length=50, verbose_name='Número')
    complemento = models.CharField(max_length=30, verbose_name='Complemento')
    bairro = models.CharField(max_length=30, verbose_name='Bairro')
    cep = models.CharField(max_length=8, verbose_name='Cep')
    cidade = models.CharField(max_length=30, verbose_name='Cidade')
    estado = models.CharField(max_length=30, default='PR', choices=ESTADOS_CHOICES, verbose_name='Estado')
    
    
    def __str__(self):
        return f'{self.usuario}'
    
    
    # função para validar dados
    def clean(self):
        error_message = {}
        
        if not valida_cpf(self.cpf):
            error_message['cpf'] = 'Digite um CPF válido!'
        
        if re.search(r'[ˆ0,9]', self.cep) or len(self.cep) < 8:
            error_message['cep'] = 'Digite um CEP válido, somente números!'
        
        if error_message:
            raise ValueError(error_message)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"
        indexes = [
            models.Index(fields=["usuario"], name="usuario_perfil_idx"),
        ]
    
"""
PerfilUsuario
    user - FK user (ou OneToOne)
    idade - Int
    data_nascimento - Date
    cpf - char
    endereco - char
    numero - char
    complemento - char
    bairro - char
    cep - Char
    cidade - char
    estado - Choices
"""