from django.shortcuts import render
from django.http import HttpResponse
from .models import Autor

def index(request):
    # lista = [1, 2, 3, 4, 5, 6] - Mutável
    # tupla = (1, 2, 3, 4, 5, 6) Imutável
    combo_mac = ('big mac', 'coca cola', 'batatinha')
    PI_MAT = 3.14
    # chave e valor DICIONARIO

    autores = {
        1:{"nome":"Luiz Fernando", "biografia":"Desenvolvedor Django", "email":"lui@gmail.com"
        },
        2:{"nome":"Maria", "biografia":"Desenvolvedora Django", "email":"maria@gmail.com"
        },
        3:{"nome":"Zezin", "biografia":"Desenvolvedor Django", "email":"zezin@gmail.com"
        }
    }

    autores = Autor.objects.all()

    return render(request,'motorartigos/index.html', {"autores":autores})

def artigo(request):
    return render(request,'motorartigos/artigo.html')
