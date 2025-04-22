from django.shortcuts import render
# Create your views here.

def index(request):

    dados={
        1:{"nome": "Nebulosa Carina",
           "legenda":"webtelescope.org/ NASA / James Webb"},
        2:{"nome": "Galáxia Centauri",
           "legenda":"webtelescope.org/ NASA / James Webb"},
        3:{"nome": "Planeta Mustafar",
           "legenda":"webtelescope.org/ NASA / James Webb"},
        4:{"nome": "Planeta Naboo",
           "legenda":"webtelescope.org/ NASA / James Webb"},
        5:{"nome": "Planeta Mandalore",
           "legenda":"webtelescope.org/ NASA / James Webb"},
         6:{"nome": "Estrela Cardinali",
           "legenda":"webtelescope.org/ NASA / James Webb"}
    }
    return render(request, 'galeria/index.html', {"cards":dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')