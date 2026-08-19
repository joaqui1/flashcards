"""Practical Level 1 extensions for the backend-junior curriculum.

The base catalog stays in ``cards.py``. This module promotes a few existing
cards and adds a small set of practical exercises that close the gap between
knowing the pieces and being able to build a tiny DRF API.
"""

from .cards import (
    CARDS,
    CURRICULUM_LEVELS,
    FOUNDATION_SEQUENCE,
    MODULES,
    PREREQUISITES,
    VERSION_INFO,
    c,
)


NEW_FOUNDATION_CARDS = [
    c(
        "f01",
        "modelos",
        "Leé este Model completo. ¿Qué representa cada campo y qué termina guardándose en la base?",
        "Post representa una tabla. titulo y contenido son columnas de texto; autor guarda una ForeignKey hacia User; publicado guarda un booleano con False por defecto; creado_en registra automáticamente el momento de creación. Django agrega una primary key si no declaramos otra.",
        context="Antes de construir serializers o endpoints, necesitás poder mirar un Model real y traducirlo mentalmente a tabla, columnas, relaciones y defaults.",
        code="""
            class Post(models.Model):
                titulo = models.CharField(max_length=200)
                contenido = models.TextField()
                autor = models.ForeignKey(
                    settings.AUTH_USER_MODEL,
                    on_delete=models.CASCADE,
                )
                publicado = models.BooleanField(default=False)
                creado_en = models.DateTimeField(auto_now_add=True)
        """,
        explanation="El Model es el contrato persistente del dominio: define qué datos existen, qué tipos tienen y qué relaciones debe respetar la base. Poder leerlo de arriba abajo permite anticipar columnas, claves foráneas, valores por defecto y qué datos necesitará cualquier serializer o endpoint que trabaje con Post.",
        kind="leer código",
        source="models",
    ),
    c(
        "f02",
        "orm_db",
        "Seguí este CRUD con el ORM. ¿Qué operación hace cada línea contra la base de datos?",
        "create inserta una fila; get consulta exactamente una; modificar el atributo y llamar save actualiza la fila; delete la elimina. Para consultar una colección usarías normalmente filter o all en lugar de get.",
        context="Un junior va a hacer CRUD todo el tiempo. La idea es reconocer la escritura o lectura SQL que hay detrás sin memorizar SQL para cada caso.",
        code="""
            post = Post.objects.create(
                titulo="Hola",
                contenido="Mi primer post",
                autor=request.user,
            )

            post = Post.objects.get(pk=post.pk)
            post.titulo = "Título nuevo"
            post.save(update_fields=["titulo"])
            post.delete()
        """,
        explanation="El ORM no elimina las operaciones fundamentales de una base: INSERT, SELECT, UPDATE y DELETE siguen existiendo. Django ofrece objetos y métodos para expresarlas en Python. Entender esa correspondencia evita tratar save, create o get como magia y ayuda a depurar cuándo se consulta o modifica realmente la base.",
        kind="leer código",
        source="queries",
    ),
    c(
        "f03",
        "drf",
        "Explicá de punta a punta qué pasa cuando llega POST /api/posts/ a esta API mínima.",
        "El router dirige la request a PostViewSet.create. IsAuthenticated exige una identidad válida. El ModelSerializer valida titulo y contenido. perform_create toma el usuario del request y llama serializer.save, que crea el Post mediante el ORM. DRF serializa el objeto creado y responde normalmente 201.",
        context="Este ejercicio junta las piezas del Nivel 1. No alcanza con reconocer cada clase por separado: tenés que poder seguir una request real desde la URL hasta la fila creada y la response.",
        code="""
            # models.py
            class Post(models.Model):
                titulo = models.CharField(max_length=200)
                contenido = models.TextField()
                autor = models.ForeignKey(User, on_delete=models.CASCADE)

            # serializers.py
            class PostSerializer(serializers.ModelSerializer):
                class Meta:
                    model = Post
                    fields = ["id", "titulo", "contenido", "autor"]
                    read_only_fields = ["id", "autor"]

            # views.py
            class PostViewSet(ModelViewSet):
                queryset = Post.objects.all()
                serializer_class = PostSerializer
                permission_classes = [IsAuthenticated]

                def perform_create(self, serializer):
                    serializer.save(autor=self.request.user)

            # urls.py
            router.register("posts", PostViewSet)
        """,
        explanation="Una API de DRF funciona por composición: routing elige el ViewSet, autenticación y permissions controlan acceso, el serializer controla el contrato de datos y el ORM persiste. Si podés seguir este recorrido y decir qué responsabilidad pertenece a cada capa, ya tenés una base útil para construir CRUD sin copiar código a ciegas.",
        kind="razonamiento",
        source="views",
    ),
]


PROMOTION_ENRICHMENTS = {
    "dj12": {
        "context": "Creaste la app foro y sus archivos existen, pero Django todavía necesita saber que esa app forma parte del proyecto para integrar modelos, migraciones y otras piezas.",
        "explanation": "Un proyecto Django carga aplicaciones registradas como parte de su configuración. INSTALLED_APPS no es un índice decorativo: participa en el registro de modelos, migraciones, templates, static files y AppConfig. Entenderlo evita perder tiempo buscando bugs en archivos correctos que Django nunca llegó a registrar.",
    },
    "m15": {
        "context": "Un Post puede gustarle a muchos usuarios y un usuario puede dar like a muchos posts. Queremos manipular esa relación desde objetos Django sin crear duplicados del mismo par.",
        "explanation": "ManyToManyField representa una relación de muchos a muchos mediante una tabla intermedia. El manager de la relación ofrece add, remove y consultas como all. Pensar en la tabla intermedia explica por qué agregar el mismo par de objetos no debería crear relaciones duplicadas y cuándo conviene usar un modelo intermedio explícito.",
    },
    "s03": {
        "context": "La API necesita exponer un Post sin permitir que el cliente decida campos administrados por el servidor, como id, autor o fecha de creación.",
        "explanation": "ModelSerializer reutiliza información del Model, pero el contrato HTTP sigue siendo una decisión explícita. fields define qué datos cruzan la frontera y read_only_fields separa lo que el cliente puede ver de lo que puede controlar. Esa distinción es básica para evitar asignaciones inseguras y APIs que cambian accidentalmente al crecer el modelo.",
    },
    "d02": {
        "context": "El ViewSet ya sabe listar y crear posts, pero el endpoint no debería aceptar escrituras de usuarios anónimos.",
        "explanation": "permission_classes declara una regla de acceso antes de ejecutar la operación del endpoint. IsAuthenticated no decide quién es dueño de cada objeto; solo exige una identidad autenticada. Separar autenticación básica de ownership ayuda a combinar permisos sin creer que estar logueado habilita cualquier acción.",
    },
    "d03": {
        "context": "El cliente envía el contenido del Post, pero el autor debe salir de la identidad autenticada por el servidor y no de un id incluido en el JSON.",
        "explanation": "perform_create es un punto de extensión del flujo de creación de ModelViewSet. El serializer ya validó el input y el servidor agrega datos confiables antes de guardar. Derivar autor desde request.user evita suplantación y muestra una regla general: los datos de seguridad no se aceptan como verdad solo porque llegaron en el body.",
    },
}


PREREQUISITES.update(
    {
        "dj12": ["dj07"],
        "f01": ["b07"],
        "m15": ["f01"],
        "f02": ["f01", "b08"],
        "s03": ["s01"],
        "d02": ["p04"],
        "d03": ["d02", "s03", "p04"],
        "f03": ["f01", "f02", "s03", "d01", "d02", "d03", "d04"],
    }
)


_existing_ids = {card["id"] for card in CARDS}
for _card in NEW_FOUNDATION_CARDS:
    if _card["id"] not in _existing_ids:
        CARDS.append(_card)
        _existing_ids.add(_card["id"])

_card_by_id = {card["id"]: card for card in CARDS}
for _card_id, _notes in PROMOTION_ENRICHMENTS.items():
    _card_by_id[_card_id].update(_notes)


def _move_after(anchor, *card_ids):
    for card_id in card_ids:
        if card_id in FOUNDATION_SEQUENCE:
            FOUNDATION_SEQUENCE.remove(card_id)
    position = FOUNDATION_SEQUENCE.index(anchor) + 1
    FOUNDATION_SEQUENCE[position:position] = list(card_ids)


_move_after("dj07", "dj12")
_move_after("dj10", "f01")
_move_after("m04", "m15")
_move_after("m24", "f02")
_move_after("s01", "s03")
_move_after("p06", "d02", "d03")
_move_after("d08", "f03")


_foundation_order = {
    card_id: index for index, card_id in enumerate(FOUNDATION_SEQUENCE)
}
_level_positions = {level["id"]: 0 for level in CURRICULUM_LEVELS}

for _catalog_index, _card in enumerate(CARDS):
    if _card["id"] in _foundation_order:
        _level = 1
        _sequence = _foundation_order[_card["id"]]
    elif _card["module"] == "entrevista":
        _level = 4
        _sequence = _catalog_index
    elif _card["difficulty"] == "base" and _card["kind"] != "veredicto":
        _level = 2
        _sequence = _catalog_index
    else:
        _level = 3
        _sequence = _catalog_index

    _card["level"] = _level
    _card["sequence"] = _sequence
    _card["prerequisites"] = PREREQUISITES.get(_card["id"], [])
    _level_positions[_level] += 1

for _level_info in CURRICULUM_LEVELS:
    _level_info["card_count"] = _level_positions[_level_info["id"]]

VERSION_INFO["verified"] = "19 de agosto de 2026"

__all__ = [
    "CARDS",
    "CURRICULUM_LEVELS",
    "FOUNDATION_SEQUENCE",
    "MODULES",
    "VERSION_INFO",
]
