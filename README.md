# DjangoCBV
Crud usando Class Based View
- A ideia é de fazer ela ser um crud sem conecção com outras apps para depois eu reutilizar no meu [ProjetoFinal](https://github.com/Pancitopenico/ProjetoFinal/).

# Página inicial
##### Página simples só com um hello world e alguns links

# Crud Links

- Listar todos os clientes -> localhost:8000/cliente/
- Criar novo cliente -> localhost:8000/cliente/create/
- Detalhes do cliente -> localhost:8000/cliente/detail/<int:pk>/
- Deletar o cliente -> localhost:8000/cliente/delete/<int:pk>/

# Clientes Models

- nome = models.CharField(max_length=50, null=True, blank=False)
- email = models.CharField(max_length=50, null=True, blank=True)
- endereco = models.CharField(max_length=50, null=True, blank=True)
- telefone = models.IntegerField(null=True, blank=False)
- observacoes = models.TextField(null=True, blank=True)


# Instalação
- Comando para criar um ambiente virtual: 
- python3 -m venv **nomeDoAmbiente**
- . **nomeDoAmbiente**/bin/activate
- pip install -r requirements-dev.txt
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py runserver


# Class Based View (CBV)

##### CBV list 
Crio a minha classe depois expecifico o model.
Para eu utilizar esta view dentro da minha pasta templates deve haver um arquivo que começa com o nome do meu **MODEL** e termina com **_list**
Ou eu posso pegar está variavel e dar Override nela e especificar o meu template.

- **template_name_suffix = '_list'**

- Dentro do meu template, devo criar um loop, para listar todos os objetos da minha lista

- FOTO DO MEU CLIENTE_LIST.HTML

** ***========================*** **

# CBV create
Crio a minha classe depois expecifico o model.
Para eu utilizar esta view dentro da minha pasta templates deve haver um arquivo que começa com o nome do meu **MODEL** e termina com **_form**
Ou eu posso pegar está variavel e dar Override nela e especificar o meu template.

- **template_name_suffix = '_form'**

- Além disto eu devo especificar os campos do meu model, para a criação do novo item.
- fields = ['nome', 'email', 'endereco', 'telefone', 'observacoes']

- Não posso esquecer de importar o **reverse_lazy**, pelo simples motivo que após salvar o objeto ele deve ser redirecionado para outra página, geralmente a página de listagem.

- **from django.urls import reverse, reverse_lazy**

- **success_url = reverse_lazy('cliente_list')**

- Dentro do meu template não posso esquecer do meu **csrf_token**

FOTO DO MEU CLIENTE_FORM.HTML

** ***========================*** **

#CBV update
OBS: A update view é muito similar com a create view.
Crio a minha classe depois expecifico o model.
Para eu utilizar esta view dentro da minha pasta templates deve haver um arquivo que começa com o nome do meu **MODEL** e termina com **_form**
Ou eu posso pegar está variavel e dar Override nela e especificar o meu template.

- **template_name_suffix = '_form'**

- Não posso esquecer de importar o **reverse_lazy**, pelo simples motivo que após salvar o objeto ele deve ser redirecionado para outra página, geralmente a página de listagem.

- **from django.urls import reverse, reverse_lazy**

- **success_url = reverse_lazy('cliente_list')**

- Dentro do meu template não posso esquecer do meu **csrf_token**

** ***========================*** **

# CBV delete
Crio a minha classe depois expecifico o model.
Para eu utilizar esta view dentro da minha pasta templates deve haver um arquivo que começa com o nome do meu **MODEL** e termina com **_confirm_delete**
Ou eu posso pegar está variavel e dar Override nela e especificar o meu template.
- **template_name_suffix = '_confirm_delete'**

- Não posso esquecer de importar o **reverse_lazy**, pelo simples motivo que após apagar o objeto ele deve ser redirecionado para outra página, geralmente a página de listagem.

- **from django.urls import reverse, reverse_lazy**

- **success_url = reverse_lazy('cliente_list')**

- Dentro do meu template não posso esquecer do meu csrf_token e para acessar as minhas variaveis posso utilizar {{object.**CampoDoMeuModel**}}

FOTO DO MEU CLIENTE_CONFIRM_DELETE.HTML

** ***========================*** **

# CBV detail

Crio a minha classe depois expecifico o model.
Para eu utilizar esta view dentro da minha pasta templates deve haver um arquivo que começa com o nome do meu **MODEL** e termina com **_detail**
Ou eu posso pegar está variavel e dar Override nela e especificar o meu template.

FOTO DO MEU CLIENTE_DETAIL.HTML

** ***========================*** **
<<<<<<< HEAD

=======
>>>>>>> 86737cedbcba3459970691b8394afe1a0c5d9a73
