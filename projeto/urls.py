from django.conf.urls import include, url
from . import views


tarefa_patterns = [
    url(r"^$", views.tarefas, name="tarefas"),
    url(r"^(?P<id_tarefa>\d+)$", views.tarefa, name="tarefa"),
    url(
        r"^(?P<id_tarefa>\d+)/iniciar$",
        views.iniciar_tarefa,
        name="iniciar_tarefa"
    ),
    url(
        r"^(?P<id_tarefa>\d+)/pausar$",
        views.pausar_tarefa,
        name="pausar_tarefa"
    ),
    url(
        r"^(?P<id_tarefa>\d+)/concluir$",
        views.concluir_tarefa,
        name="concluir_tarefa"
    ),
    url(
        r"^(?P<id_tarefa>\d+)/deletar$",
        views.deletar_tarefa,
        name="deletar_tarefa"
    ),
    url(
        r"^(?P<id_tarefa>\d+)/comentar/$",
        views.comentar,
        name="comentar"
    ),
    url(
        r"^(?P<id_tarefa>\d+)/permitido_iniciar/$",
        views.permissao_iniciar,
        name="permissao_iniciar"
    ),
]

urlpatterns = [
    url(r"^$", views.index, name="projetos"),
    url(r"^login$", views.LoginView.as_view(), name="login"),
    url(r"^funcionarios$", views.funcionarios, name="funcionarios"),
    url(r"^novo_projeto$", views.novo_projeto, name="novo_projeto"),
    url(r"^novo_funcionario$", views.novo_funcionario, name="novo_funcionario"),
    url(r"^nova_tarefa$", views.nova_tarefa, name="nova_tarefa"),
    url(r'^tarefa/', include(tarefa_patterns)),
]
