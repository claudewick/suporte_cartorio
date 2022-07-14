from oficio.models import *

class SentOL(models.Model):
    creation_date = models.DateField(verbose_name='Data de Elaboração')
    answer_to_ol = models.ForeignKey(ReceivedOL, null=True, on_delete=models.SET_NULL, verbose_name='Resposta ao Ofício nº')
    authority = models.ForeignKey(Authority, null=True, on_delete=models.SET_NULL, verbose_name='Destinatário')
    lawsuit_number = models.CharField(null=True, blank=True, max_length=50, verbose_name='Processo nº')
    lawsuit_author = models.CharField(null=True, blank= True, max_length=200, verbose_name='Autor')
    author_type = models.IntegerField(choices=PERSON_TYPE_CHOICE, default=1, verbose_name='Tipo de Pessoa')
    author_doc_number = models.CharField(null=True, blank=True, max_length=14, verbose_name='CPF ou CNPJ')
    lawsuit_accused = models.CharField(null=True, blank=True, max_length=200, verbose_name='Réu')
    accused_type = models.IntegerField(choices=PERSON_TYPE_CHOICE, default=1, verbose_name='Tipo de Pessoa')
    accused_doc_number = models.CharField(null=True, blank=True, max_length=14, verbose_name='CPF ou CNPJ')
    answer = models.TextField(verbose_name='Texto do Ofício')
    sent_ol_number = models.CharField(null=True, blank=True, max_length=50, verbose_name='Número de Ofício Expedido')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ofício Enviado'
        verbose_name_plural = 'Ofícios Enviados'
        
    def __str__(self):
        return '{}'.format(self.sent_ol_number)
