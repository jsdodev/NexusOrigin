# cursos/views.py

from django.shortcuts import render
from django.http import JsonResponse

# Dicionário com todos os dados dos cursos (AGORA GLOBAL)
cursos = {
    "ia": {
        "nome": "Domine IA",
        "descr": "Do básico à criação de modelos inteligentes: sua jornada em IA começa aqui.",
        "imagem": "https://wordpress-cms-gc-prod-assets.quero.space/uploads/2023/04/Inteligencia-Artificial.jpg",
        "youtube_id": "8gHwzJ5q9YQ"
    },
    "javascript": {
        "nome": "JavaScript Completo",
        "descr": "De iniciante à profissional: JavaScript com projetos reais e linguagem simples.",
        "imagem": "https://blog.facialix.com/wp-content/uploads/2022/08/logo-curso-introduccion-programacion-js.jpg",
        "youtube_id": "McKNP3g6VBA"
    },
    "frontend": {
        "nome": "Front-End",
        "descr": "Domine Front-End e crie interfaces modernas e responsivas do zero.",
        "imagem": "https://usemobile.com.br/wp-content/uploads/2024/05/capa-front-end.jpg",
        "youtube_id": "SUA_ID_DO_VIDEO_AQUI_FRONTEND"
    },
    "python": {
        "nome": "Python para Iniciantes",
        "descr": "Aprenda Python do zero ao avançado com aulas práticas e projetos reais.",
        "imagem": "https://dkrn4sk0rn31v.cloudfront.net/uploads/2020/01/07093212/PYTHON.png",
        "youtube_id": "SUA_ID_DO_VIDEO_AQUI_PYTHON"
    },
    "git": {
        "nome": "Git e GitHub",
        "descr": "Aprenda Git e GitHub e eleve seu nível em qualquer projeto de programação.",
        "imagem": "https://assets.dio.me/vcgnme8q1cSGzdYzWL_wURKVR8sP_w-84qtgRf3N8_o/f:webp/q:80/L2FydGljbGVzL2NvdmVyL2QyNDg5Zjk2LWQ1NmYtNGI4Mi1iYzdmLTg0ZmJjOWZiMTM2OC5qcGc",
        "youtube_id": "SUA_ID_DO_VIDEO_AQUI_GIT"
    },
    "htmlcss": {
        "nome": "HTML e CSS",
        "descr": "Aprenda HTML e CSS e crie sites incríveis do zero. 100% online e prático.",
        "imagem": "https://hotmart.s3.amazonaws.com/product_pictures/d2badee3-49a9-4627-9f7d-a5e51ae35384/sitehtmlcss1024x579.jpg",
        "youtube_id": "SUA_ID_DO_VIDEO_AQUI_HTMLCSS"
    }
}

def home(request):
    return render(request, 'home.html', {'cursos': cursos})

def curso_detalhes(request, slug):
    curso = cursos.get(slug)
    if curso:
        return render(request, 'cursos_detalhes.html', {'curso': curso})
    else:
        return JsonResponse({"erro": "curso não encontrado"}, status=404)

def api_curso(request, slug):
    curso = cursos.get(slug)
    if curso:
        return JsonResponse(curso)
    else:
        return JsonResponse({"erro": "curso não encontrado"}, status=404)