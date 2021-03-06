from oficio.models import *

class ReceivedOL(models.Model):
    received_in = models.DateField(verbose_name='Recebido em')
    ol_date = models.DateField(verbose_name='Data do Ofício')
    ol_origin_id = models.CharField(max_length=50, null=True, blank=True, verbose_name='Número ou Identificação do Ofício')
    authority = models.ForeignKey(Authority, null=True, blank=True, related_name='authority', on_delete=models.SET_NULL, verbose_name='Autoridade Emitente')
    lawsuit_number = models.CharField(null=True, blank=True, max_length=100, verbose_name='Processo nº:')
    lawsuit_author = models.CharField(null=True, blank=True, max_length=200, verbose_name='Autor')
    author_type = models.IntegerField(choices=PERSON_TYPE_CHOICE, default=1, verbose_name='Tipo de Pessoa')
    author_doc_number = models.CharField(null=True, blank=True, max_length=14, verbose_name='CPF ou CNPJ')
    lawsuit_accused = models.CharField(null=True, blank=True, max_length=200, verbose_name='Réu')
    accused_type = models.IntegerField(choices=PERSON_TYPE_CHOICE, default=1, verbose_name='Tipo de Pessoa')
    accused_doc_number = models.CharField(null=True, blank=True, max_length=14, verbose_name='CPF ou CNPJ')
    deadline = models.DateField(verbose_name='Prazo para Resposta')
    received_ol_number = models.CharField(null=True, blank=True, max_length=50, verbose_name='Número do Ofício Recebido')
    answer_ol = models.CharField(null=True, blank=True, max_length=50, verbose_name='Número do Ofício Resposta')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ofício Recebido'
        verbose_name_plural = 'Ofícios Recebidos'
    def __str__(self):
        return '{}'.format(self.received_ol_number)
