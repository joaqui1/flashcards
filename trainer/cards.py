from textwrap import dedent


VERSION_INFO = {
    "django": "6.0.8",
    "edition": "Backend junior · Python + Django + DRF",
    "verified": "18 de agosto de 2026",
    "focus": "Leer código, detectar errores y tomar decisiones",
}

MODULES = [
    {"id": "django", "name": "Django esencial", "description": "Request/response, URLs, views, settings y ciclo de una petición."},
    {"id": "modelos", "name": "Models y migraciones", "description": "Campos, relaciones, constraints y evolución segura del esquema."},
    {"id": "orm_db", "name": "ORM, SQL y PostgreSQL", "description": "QuerySets, N+1, índices, transacciones y SQL que conviene entender."},
    {"id": "serializers", "name": "DRF · Serializers", "description": "Validación, escritura, representación y SerializerMethodField."},
    {"id": "drf", "name": "DRF · Views y routers", "description": "ModelViewSet, routers, actions, filtros, paginación y respuestas."},
    {"id": "http_api", "name": "APIs y HTTP", "description": "Métodos, status codes, idempotencia, headers y diseño REST."},
    {"id": "auth_security", "name": "Auth, permissions y seguridad", "description": "Autenticación, autorización, ownership y defensas de producción."},
    {"id": "testing", "name": "Testing y debugging", "description": "APITestCase, factories, regresiones y diagnóstico de fallos reales."},
    {"id": "git_deploy", "name": "Git y deploy básico", "description": "Commits, ramas, conflictos, variables de entorno y checklist de deploy."},
    {"id": "python", "name": "Python para backend", "description": "Un repaso corto de mutabilidad, excepciones, iteradores y typing."},
    {"id": "entrevista", "name": "Entrevista Junior", "description": "Preguntas frecuentes y ejercicios integradores sobre un foro real."},
]

DOCS = {
    "django": "https://docs.djangoproject.com/en/6.0/topics/http/",
    "urls": "https://docs.djangoproject.com/en/6.0/topics/http/urls/",
    "models": "https://docs.djangoproject.com/en/6.0/topics/db/models/",
    "migrations": "https://docs.djangoproject.com/en/6.0/topics/migrations/",
    "queries": "https://docs.djangoproject.com/en/6.0/topics/db/queries/",
    "optimization": "https://docs.djangoproject.com/en/6.0/topics/db/optimization/",
    "transactions": "https://docs.djangoproject.com/en/6.0/topics/db/transactions/",
    "postgres": "https://www.postgresql.org/docs/current/tutorial.html",
    "serializers": "https://www.django-rest-framework.org/api-guide/serializers/",
    "fields": "https://www.django-rest-framework.org/api-guide/fields/",
    "views": "https://www.django-rest-framework.org/api-guide/viewsets/",
    "routers": "https://www.django-rest-framework.org/api-guide/routers/",
    "filtering": "https://www.django-rest-framework.org/api-guide/filtering/",
    "pagination": "https://www.django-rest-framework.org/api-guide/pagination/",
    "requests": "https://www.django-rest-framework.org/api-guide/requests/",
    "responses": "https://www.django-rest-framework.org/api-guide/responses/",
    "status": "https://www.django-rest-framework.org/api-guide/status-codes/",
    "authentication": "https://www.django-rest-framework.org/api-guide/authentication/",
    "permissions": "https://www.django-rest-framework.org/api-guide/permissions/",
    "security": "https://docs.djangoproject.com/en/6.0/topics/security/",
    "testing": "https://www.django-rest-framework.org/api-guide/testing/",
    "django_testing": "https://docs.djangoproject.com/en/6.0/topics/testing/overview/",
    "deploy": "https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/",
    "git": "https://git-scm.com/docs/gittutorial",
    "python": "https://docs.python.org/3/tutorial/",
}


def block(value):
    return dedent(value).strip()


def c(card_id, module, question, answer, *, code="", answer_code="", explanation="", kind="razonamiento", difficulty="base", source="django", verdict=None):
    return {
        "id": card_id, "module": module, "question": question, "answer": answer,
        "code": block(code) if code else "", "answer_code": block(answer_code) if answer_code else "",
        "explanation": explanation, "kind": kind, "difficulty": difficulty,
        "source": DOCS[source], "verdict": verdict,
    }


CARDS = [
    # DJANGO ESENCIAL
    c("dj01", "django", "Seguí el recorrido de esta petición. ¿Qué decide qué función se ejecuta y qué debe devolver?", "El URLconf busca el primer patrón compatible y llama a la view. La view debe devolver una HttpResponse o subclase.", code="""
        GET /posts/42/

        # urls.py
        path("posts/<int:pk>/", views.post_detail)
    """, kind="leer código", source="urls"),
    c("dj02", "django", "¿Dónde están los query params? ¿Qué valor obtiene page si falta?", "En request.GET. get('page', 1) devuelve el string recibido o el entero 1 si la clave no existe.", code="""
        def post_list(request):
            page = request.GET.get("page", 1)
    """, kind="leer código"),
    c("dj03", "django", "¿Qué respuesta produce esta view y qué hace render?", "Renderiza el template con el contexto y devuelve una HttpResponse. posts queda disponible en el template.", code="""
        def home(request):
            posts = Post.objects.filter(publicado=True)
            return render(request, "foro/home.html", {"posts": posts})
    """, kind="leer código"),
    c("dj04", "django", "La URL devuelve 404 aunque la view existe. Nombrá tres puntos concretos que revisarías.", "El path de la app, que sus URLs estén incluidas desde el URLconf raíz, que el prefijo final coincida y el orden de patrones.", code="""
        # foro/urls.py
        path("posts/", views.posts)

        # config/urls.py
        path("api/", include("foro.urls"))
    """, kind="debugging", source="urls"),
    c("dj05", "django", "Completá la conversión para que pk llegue como entero.", "Se usa <int:pk>.", code='path("posts/<________>/", views.post_detail)', answer_code='path("posts/<int:pk>/", views.post_detail)', kind="completar", source="urls"),
    c("dj06", "django", "¿Qué problemas tiene esta configuración en producción?", "DEBUG expone información sensible y SECRET_KEY no debe estar en el repo. Ambos settings deben configurarse por entorno.", code="""
        DEBUG = True
        SECRET_KEY = "django-insecure-123"
    """, kind="debugging", difficulty="media", source="deploy"),
    c("dj07", "django", "¿Qué diferencia práctica hay entre proyecto y app?", "config agrupa settings, URLs y entrypoints. foro encapsula una funcionalidad y sus models, views, serializers y tests.", code="""
        config/
          settings.py
          urls.py
        foro/
          models.py
          views.py
    """, kind="leer código"),
    c("dj08", "django", "¿Por qué include() mejora este URLconf?", "Delega el routing del prefijo /api/ a la app y evita concentrar todas las rutas en el archivo raíz.", code='path("api/", include("foro.urls"))', kind="decisión", source="urls"),
    c("dj09", "django", "¿Qué contiene request? Mencioná al menos cinco datos útiles.", "Método, path, headers, query params, body/POST, cookies, archivos y, con auth configurada, user.", code="""
        print(request.method)
        print(request.headers.get("Accept"))
        print(request.user)
    """, kind="explicar"),
    c("dj10", "django", "¿Qué puede salir mal y qué helper expresa mejor un 404?", "get() lanza DoesNotExist si no hay fila. get_object_or_404 transforma ese caso en una respuesta 404.", code='post = Post.objects.get(pk=pk)', answer_code='post = get_object_or_404(Post, pk=pk)', kind="debugging"),
    c("dj11", "django", "¿Por qué usar el nombre de URL en vez de escribir /posts/ a mano?", "reverse resuelve la ruta por su nombre. Si el path cambia, las referencias por nombre siguen válidas.", code="""
        path("posts/", views.post_list, name="post-list")
        reverse("post-list")
    """, kind="decisión", source="urls"),
    c("dj12", "django", "La app foro no está en INSTALLED_APPS. ¿Qué síntomas pueden aparecer?", "Sus modelos y varias integraciones —migraciones, templates, static files o AppConfig— pueden no registrarse como se espera.", code="""
        INSTALLED_APPS = [
            "django.contrib.auth",
            # falta "foro"
        ]
    """, kind="debugging"),

    # MODELS Y MIGRACIONES
    c("m04", "modelos", "¿Qué relación representa autor y dónde queda la clave foránea?", "Muchos Post pueden pertenecer a un User. La columna autor_id queda normalmente en la tabla de Post.", code="""
        autor = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
        )
    """, kind="leer código", source="models"),
    c("m15", "modelos", "¿Qué relación debe existir para que add() funcione? ¿Qué pasa si el usuario ya estaba agregado?", "Post.likes debe ser ManyToManyField hacia User. add crea la relación intermedia; repetir el mismo par no lo duplica.", code="""
        post = Post.objects.get(id=5)
        post.likes.add(request.user)
    """, kind="leer código", source="models"),
    c("m16", "modelos", "Completá la relación para soportar add y user.posts_likeados.all().", "ManyToManyField con related_name='posts_likeados'.", code="""
        likes = models.________(
            settings.AUTH_USER_MODEL,
            related_name="________",
            blank=True,
        )
    """, answer_code="""
        likes = models.ManyToManyField(
            settings.AUTH_USER_MODEL,
            related_name="posts_likeados",
            blank=True,
        )
    """, kind="completar", source="models"),
    c("m17", "modelos", "¿Qué efecto tiene CASCADE? ¿Cuándo sería más seguro PROTECT?", "Al borrar el usuario, CASCADE elimina sus posts. PROTECT sirve si el dominio debe impedir borrar un autor con contenido.", code='autor = models.ForeignKey(User, on_delete=models.CASCADE)', kind="decisión", source="models"),
    c("m18", "modelos", "¿Qué problema evita esta constraint incluso con dos requests simultáneas?", "Evita más de un like del mismo usuario al mismo post. La regla en base protege todos los puntos de entrada y la concurrencia.", code="""
        models.UniqueConstraint(
            fields=["usuario", "post"],
            name="like_unico_por_usuario_post",
        )
    """, kind="razonamiento", difficulty="media", source="models"),
    c("m19", "modelos", "¿Por qué usar un modelo Like explícito en vez de un ManyToManyField simple?", "Permite atributos de la relación, como fecha, y consultar o auditar cada like como entidad propia.", code="""
        class Like(models.Model):
            usuario = models.ForeignKey(User, on_delete=models.CASCADE)
            post = models.ForeignKey(Post, on_delete=models.CASCADE)
            creado_en = models.DateTimeField(auto_now_add=True)
    """, kind="decisión", difficulty="media", source="models"),
    c("m20", "modelos", "¿Qué diferencia hay entre null=True y blank=True?", "null controla SQL NULL. blank controla validación. En texto suele preferirse blank=True y almacenar cadena vacía.", code='resumen = models.CharField(max_length=200, null=True, blank=True)', kind="explicar", source="models"),
    c("m21", "modelos", "Agregaste publicado. ¿Qué comandos faltan y qué hace cada uno?", "makemigrations crea el archivo de cambio; migrate lo aplica a la base.", code='publicado = models.BooleanField(default=False)', answer_code="""
        python manage.py makemigrations
        python manage.py migrate
    """, kind="completar", source="migrations"),
    c("m22", "modelos", "Este campo nuevo se agrega a una tabla con filas. ¿Qué decisión de datos exige?", "Las filas existentes necesitan valor: default, null temporal o una migración por etapas que complete datos antes de endurecer la restricción.", code='estado = models.CharField(max_length=20)', kind="migraciones", difficulty="media", source="migrations"),
    c("m23", "modelos", "¿Por qué las migraciones deben subirse a Git?", "Son la historia versionada del esquema y permiten aplicar los mismos cambios, en orden, en otros entornos.", code="""
        foro/migrations/0001_initial.py
        foro/migrations/0002_post_publicado.py
    """, kind="explicar", source="migrations"),
    c("m24", "modelos", "¿Qué aporta related_name y qué consulta inversa habilita?", "Define el nombre desde User hacia Comentario: user.comentarios.all().", code="""
        autor = models.ForeignKey(
            User, on_delete=models.CASCADE,
            related_name="comentarios",
        )
    """, kind="leer código", source="models"),
    c("m25", "modelos", "¿Qué error de diseño hay si representa dinero?", "FloatField puede introducir errores binarios. Para importes suele usarse DecimalField.", code='precio = models.FloatField()', answer_code='precio = models.DecimalField(max_digits=10, decimal_places=2)', kind="debugging", source="models"),
    c("m26", "modelos", "¿Qué diferencia hay entre auto_now_add y default=timezone.now?", "auto_now_add fija el valor al crear y no permite proporcionarlo normalmente. default también lo asigna, pero acepta un valor explícito.", code="""
        creado_en = models.DateTimeField(auto_now_add=True)
        programado_para = models.DateTimeField(default=timezone.now)
    """, kind="comparar", source="models"),
    c("m27", "modelos", "¿Qué garantiza este índice y qué NO garantiza?", "Puede acelerar consultas sobre slug según el plan. No garantiza unicidad; para eso se usa unique o una constraint.", code='slug = models.SlugField(db_index=True)', kind="razonamiento", difficulty="media", source="models"),

    # ORM, SQL Y POSTGRESQL
    c("o01", "orm_db", "¿Qué devuelve? ¿Consulta inmediatamente? ¿Qué diferencia hay con get()?", "Devuelve un QuerySet con muchos o cero posts. Es lazy. get espera exactamente uno y puede lanzar DoesNotExist o MultipleObjectsReturned.", code="Post.objects.filter(publicado=True)", kind="leer código", source="queries"),
    c("o15", "orm_db", "¿Qué puede salir mal si hay varios posts publicados?", "get espera exactamente una fila. Si hay varias lanza MultipleObjectsReturned; si no hay ninguna, DoesNotExist.", code="Post.objects.get(publicado=True)", kind="debugging", source="queries"),
    c("o16", "orm_db", "¿Qué problema de performance aparece y cómo lo resolverías?", "N+1: una query para posts y potencialmente una por autor. Usaría select_related('autor') porque es ForeignKey.", code="""
        for post in Post.objects.all():
            print(post.autor.username)
    """, answer_code="""
        for post in Post.objects.select_related("autor"):
            print(post.autor.username)
    """, kind="performance", difficulty="media", source="optimization"),
    c("o17", "orm_db", "La relación es ManyToMany. ¿Por qué select_related no alcanza y qué usarías?", "Usaría prefetch_related('likes'), que hace consultas separadas y combina resultados en Python.", code="""
        for post in Post.objects.all():
            print([u.username for u in post.likes.all()])
    """, answer_code='Post.objects.prefetch_related("likes")', kind="performance", difficulty="media", source="optimization"),
    c("o18", "orm_db", "¿Cuándo se evalúa este QuerySet? Nombrá tres disparadores.", "Al iterarlo, convertirlo en list, pedir len, evaluarlo como bool o acceder a resultados que exijan datos.", code="""
        posts = Post.objects.filter(publicado=True)
        # todavía puede no haber SQL
    """, kind="explicar", source="queries"),
    c("o19", "orm_db", "¿Qué devuelve filter si no encuentra nada? ¿Por qué este if funciona?", "Un QuerySet vacío, no una excepción. Su bool detecta resultados, aunque exists expresa mejor una comprobación de existencia.", code="""
        posts = Post.objects.filter(titulo="inexistente")
        if posts:
            print("hay resultados")
    """, kind="leer código", source="queries"),
    c("o20", "orm_db", "Solo querés saber si existe un like. Refactorizá para no materializar objetos.", "exists genera una consulta de existencia apropiada.", code="""
        if len(Like.objects.filter(post=post, usuario=user)) > 0:
            ...
    """, answer_code="""
        if Like.objects.filter(post=post, usuario=user).exists():
            ...
    """, kind="refactor", source="optimization"),
    c("o21", "orm_db", "¿Qué hace F('visitas') y qué carrera evita?", "Incrementa con el valor actual en SQL, sin leer y reescribir desde Python. Evita perder incrementos concurrentes.", code="""
        Post.objects.filter(pk=post.pk).update(
            visitas=F("visitas") + 1
        )
    """, kind="concurrencia", difficulty="media", source="queries"),
    c("o22", "orm_db", "¿Qué agrega Count y qué detalle revisarías con varios JOINs?", "Agrega num_likes a cada Post. Podría necesitar distinct=True si otros joins inflan el conteo.", code='Post.objects.annotate(num_likes=Count("likes"))', kind="leer código", difficulty="media", source="queries"),
    c("o23", "orm_db", "¿Qué diferencia hay entre values y obtener instancias completas?", "values devuelve diccionarios con campos pedidos y evita construir modelos. Se pierde comportamiento del modelo y acceso normal a relaciones.", code='Post.objects.values("id", "titulo")', kind="comparar", source="optimization"),
    c("o24", "orm_db", "¿Por qué order_by es importante al paginar?", "Sin orden estable las filas pueden cambiar de página. Conviene incluir un desempate determinista como pk.", code='Post.objects.filter(publicado=True).order_by("-creado_en", "-pk")', kind="razonamiento", source="queries"),
    c("o25", "orm_db", "¿Qué SQL aproximado representa este lookup?", "Un JOIN entre post y usuario con WHERE sobre username. Django parametriza el valor.", code='Post.objects.filter(autor__username="ana")', answer_code="""
        SELECT post.*
        FROM post
        JOIN auth_user ON post.autor_id = auth_user.id
        WHERE auth_user.username = %s;
    """, kind="traducir a SQL", difficulty="media", source="postgres"),
    c("o26", "orm_db", "¿Qué filas devuelve el LEFT JOIN que un INNER JOIN excluiría?", "Incluye todos los posts, también los que no tienen comentarios; esas columnas aparecen como NULL.", code="""
        SELECT p.id, p.titulo, c.id
        FROM post p
        LEFT JOIN comentario c ON c.post_id = p.id;
    """, kind="leer SQL", source="postgres"),
    c("o27", "orm_db", "¿Qué está mal desde seguridad? ¿Cómo lo corrige el ORM?", "Concatenar input permite SQL injection. El ORM separa consulta y parámetros.", code="""
        sql = "SELECT * FROM post WHERE titulo = '" + request.GET["q"] + "'"
    """, answer_code='Post.objects.filter(titulo=request.GET["q"])', kind="debugging", difficulty="media", source="security"),
    c("o28", "orm_db", "Dos requests ven disponible=True y reservan. ¿Qué combinarías?", "transaction.atomic, select_for_update para bloquear y una constraint/regla en base como última defensa.", code="""
        if turno.disponible:
            turno.disponible = False
            turno.save()
    """, answer_code="""
        with transaction.atomic():
            turno = Turno.objects.select_for_update().get(pk=pk)
            if not turno.disponible:
                raise ValidationError("Turno ocupado")
            turno.disponible = False
            turno.save(update_fields=["disponible"])
    """, kind="concurrencia", difficulty="alta", source="transactions"),
    c("o29", "orm_db", "¿Qué garantiza atomic en este bloque?", "Las escrituras se confirman juntas; si una excepción sale del bloque, se revierten. No resuelve por sí solo toda carrera.", code="""
        with transaction.atomic():
            Pedido.objects.create(usuario=user)
            Stock.objects.filter(pk=item.pk).update(cantidad=F("cantidad") - 1)
    """, kind="transacciones", difficulty="media", source="transactions"),
    c("o30", "orm_db", "¿Cuándo ayuda este índice compuesto y por qué importa el orden?", "Ayuda a consultas que empiezan por publicado y siguen por creado_en. El orden condiciona qué patrones aprovechan el índice.", code="""
        class Meta:
            indexes = [
                models.Index(fields=["publicado", "-creado_en"])
            ]
    """, kind="decisión", difficulty="alta", source="optimization"),

    # DRF SERIALIZERS
    c("s01", "serializers", "¿Qué hace is_valid y dónde quedan los datos confiables?", "Deserializa y valida. Si pasa, los valores normalizados quedan en validated_data; initial_data sigue siendo entrada cruda.", code="""
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
    """, kind="leer código", source="serializers"),
    c("s02", "serializers", "¿Qué riesgo tiene fields='__all__' en escritura?", "Un campo nuevo podría exponerse o volverse escribible accidentalmente. Una lista explícita actúa como allowlist.", code="""
        class Meta:
            model = Post
            fields = "__all__"
    """, kind="seguridad", difficulty="media", source="serializers"),
    c("s03", "serializers", "Completá fields y hacé autor solo de lectura.", "Se declaran fields y read_only_fields en Meta.", code="""
        class Meta:
            model = Post
            fields = [________]
            read_only_fields = [________]
    """, answer_code="""
        fields = ["id", "titulo", "contenido", "autor", "creado_en"]
        read_only_fields = ["id", "autor", "creado_en"]
    """, kind="completar", source="serializers"),
    c("s04", "serializers", "¿Cuándo se ejecuta validate_titulo y qué debe devolver?", "Durante is_valid tras validaciones básicas. Debe devolver el valor o lanzar serializers.ValidationError.", code="""
        def validate_titulo(self, value):
            if "spam" in value.lower():
                raise serializers.ValidationError("Título no permitido")
            return value
    """, kind="explicar", source="serializers"),
    c("s05", "serializers", "¿Por qué esta regla pertenece a validate(self, attrs)?", "Compara dos campos, por lo que necesita validación a nivel de objeto. Debe devolver attrs si es válida.", code="""
        def validate(self, attrs):
            if attrs["inicio"] >= attrs["fin"]:
                raise serializers.ValidationError("Rango inválido")
            return attrs
    """, kind="razonamiento", source="serializers"),
    c("s06", "serializers", "¿Qué problema tiene attrs['titulo'] durante PATCH?", "El campo puede faltar y causar KeyError. Hay que usar attrs.get o combinar con el valor actual de instance.", code='titulo = attrs["titulo"]', answer_code='titulo = attrs.get("titulo", getattr(self.instance, "titulo", ""))', kind="debugging", difficulty="media", source="serializers"),
    c("s07", "serializers", "¿Qué devuelve SerializerMethodField y cómo se llama el método?", "Es calculado y de solo lectura. get_num_likes(self, obj) produce la representación.", code="""
        num_likes = serializers.SerializerMethodField()

        def get_num_likes(self, obj):
            return obj.likes.count()
    """, kind="leer código", source="fields"),
    c("s08", "serializers", "¿Qué problema de performance esconde en una lista?", "Puede ejecutar count por post: N+1. Conviene anotar num_likes en el queryset y leerlo como IntegerField.", code='def get_num_likes(self, obj): return obj.likes.count()', answer_code="""
        # viewset
        queryset = Post.objects.annotate(num_likes=Count("likes"))
        # serializer
        num_likes = serializers.IntegerField(read_only=True)
    """, kind="performance", difficulty="media", source="optimization"),
    c("s09", "serializers", "¿Para qué sirve context['request'] y qué caso contemplás?", "Permite un valor relativo al usuario. Hay que contemplar AnonymousUser o ausencia de request.", code="""
        def get_me_gusta(self, obj):
            request = self.context.get("request")
            return bool(request and request.user.is_authenticated
                        and obj.likes.filter(pk=request.user.pk).exists())
    """, kind="razonamiento", difficulty="media", source="serializers"),
    c("s10", "serializers", "¿Qué diferencia hay entre data y validated_data?", "data es representación de salida. validated_data es el input validado después de is_valid.", code="""
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    """, kind="comparar", source="serializers"),
    c("s11", "serializers", "¿Qué hace partial=True y con qué método suele asociarse?", "Permite omitir campos requeridos. Se usa normalmente con PATCH; PUT representa reemplazo completo.", code='PostSerializer(post, data=request.data, partial=True)', kind="leer código", source="serializers"),
    c("s12", "serializers", "¿Qué método llama save sin instance y cuál con instance?", "Sin instance llama create(validated_data). Con instance llama update(instance, validated_data).", code="""
        PostSerializer(data=data).save()        # create
        PostSerializer(post, data=data).save()  # update
    """, kind="explicar", source="serializers"),
    c("s13", "serializers", "¿Por qué password necesita write_only y create_user?", "write_only evita devolverlo. create_user aplica hashing; create(password=...) podría guardar el texto incorrectamente.", code="""
        password = serializers.CharField(write_only=True)

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)
    """, kind="seguridad", difficulty="media", source="serializers"),
    c("s14", "serializers", "¿Qué respuesta produce raise_exception=True ante input inválido?", "DRF transforma ValidationError en 400 con detalles, usando su manejador de excepciones.", code='serializer.is_valid(raise_exception=True)', kind="explicar", source="serializers"),

    # DRF VIEWS, ROUTERS, FILTROS Y PAGINACIÓN
    c("d01", "drf", "¿Qué acciones aporta ModelViewSet y qué métodos las invocan?", "list/retrieve con GET, create con POST, update con PUT, partial_update con PATCH y destroy con DELETE.", code="""
        class PostViewSet(ModelViewSet):
            queryset = Post.objects.all()
            serializer_class = PostSerializer
    """, kind="mapear", source="views"),
    c("d02", "drf", "Completá: solo usuarios autenticados pueden usar el endpoint.", "Se usa IsAuthenticated.", code="""
        class PostViewSet(ModelViewSet):
            permission_classes = [________]
    """, answer_code="permission_classes = [IsAuthenticated]", kind="completar", source="permissions"),
    c("d03", "drf", "¿Por qué asignar autor acá y no aceptarlo desde el body?", "El servidor usa la identidad autenticada y evita suplantación. autor debe ser read_only en el serializer.", code="""
        def perform_create(self, serializer):
            serializer.save(autor=self.request.user)
    """, kind="seguridad", source="views"),
    c("d04", "drf", "¿Qué URLs genera normalmente este router?", "Colección /posts/ para list/create; detalle /posts/{pk}/ para retrieve/update/partial_update/destroy; y rutas de actions.", code="""
        router = DefaultRouter()
        router.register("posts", PostViewSet)
        urlpatterns = router.urls
    """, kind="leer código", source="routers"),
    c("d05", "drf", "¿Cuándo necesitás basename al registrar un ViewSet?", "Cuando el router no puede inferirlo, por ejemplo si solo existe get_queryset y no un atributo queryset.", code='router.register("posts", PostViewSet, basename="post")', kind="explicar", difficulty="media", source="routers"),
    c("d06", "drf", "¿Qué significa detail=True y qué endpoint crea?", "Opera sobre un objeto concreto. Crea normalmente POST /posts/{pk}/like/.", code="""
        @action(detail=True, methods=["post"])
        def like(self, request, pk=None):
            post = self.get_object()
            post.likes.add(request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)
    """, kind="leer código", source="routers"),
    c("d07", "drf", "¿Qué bug funcional tiene este toggle con requests repetidas o concurrentes?", "El resultado depende del estado previo y dos requests pueden interferir. Es más predecible separar asegurar like y quitar like, con unicidad en base.", code="""
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    """, kind="debugging", difficulty="alta", source="views"),
    c("d08", "drf", "¿Por qué get_object es preferible a Post.objects.get dentro del ViewSet?", "Respeta get_queryset y lookup_field, ejecuta el flujo de permisos de objeto y convierte ausencia en 404.", code='post = self.get_object()', kind="decisión", difficulty="media", source="views"),
    c("d09", "drf", "¿Qué filtra y qué validación falta?", "Filtra por publicado si llega el parámetro. Falta validar valores permitidos; cualquier string distinto de true se interpreta como False.", code="""
        def get_queryset(self):
            qs = Post.objects.all()
            value = self.request.query_params.get("publicado")
            if value is not None:
                qs = qs.filter(publicado=value.lower() == "true")
            return qs
    """, kind="debugging", source="filtering"),
    c("d10", "drf", "¿Qué diferencia hay entre query_params y data?", "query_params contiene parámetros de URL. data contiene el body parseado por DRF.", code="""
        q = request.query_params.get("q")
        titulo = request.data.get("titulo")
    """, kind="comparar", source="requests"),
    c("d11", "drf", "Optimizá autor y likes para evitar N+1.", "select_related para autor y prefetch_related para likes.", code='queryset = Post.objects.all()', answer_code='queryset = Post.objects.select_related("autor").prefetch_related("likes")', kind="performance", difficulty="media", source="optimization"),
    c("d12", "drf", "¿Cuándo conviene get_queryset en vez de queryset fijo?", "Cuando depende de request.user, query params o action. No se debe reutilizar un QuerySet ya evaluado entre requests.", code="""
        def get_queryset(self):
            return Post.objects.filter(autor=self.request.user)
    """, kind="decisión", source="views"),
    c("d13", "drf", "¿Qué estructura suele tener la respuesta paginada?", "Un objeto con count, next, previous y results. ViewSets y generic views la aplican automáticamente.", code="""
        REST_FRAMEWORK = {
            "DEFAULT_PAGINATION_CLASS":
                "rest_framework.pagination.PageNumberPagination",
            "PAGE_SIZE": 20,
        }
    """, kind="leer código", source="pagination"),
    c("d14", "drf", "¿Qué error común hay al sobrescribir list así?", "Se pierde paginación y quizá filtros. Debería usar filter_queryset, paginate_queryset y get_paginated_response, o no sobrescribir list.", code="""
        def list(self, request):
            posts = self.get_queryset()
            return Response(PostSerializer(posts, many=True).data)
    """, kind="debugging", difficulty="media", source="pagination"),
    c("d15", "drf", "Completá una respuesta de creación exitosa.", "Debe devolver datos y 201 Created.", code="""
        return Response(
            serializer.data,
            status=________,
        )
    """, answer_code="status=status.HTTP_201_CREATED", kind="completar", source="status"),
    c("d16", "drf", "¿Cómo elegir un serializer pequeño para list sin duplicar ViewSets?", "Sobrescribiendo get_serializer_class y consultando self.action.", code="""
        def get_serializer_class(self):
            if self.action == "list":
                return PostListSerializer
            return PostDetailSerializer
    """, kind="diseño", difficulty="media", source="views"),

    # HTTP Y DISEÑO DE APIS
    c("h01", "http_api", "Mapeá cada request a operación y status exitoso común.", "GET lista (200), POST crea (201), PATCH modifica parcialmente (200), DELETE elimina (204).", code="""
        GET    /api/posts/
        POST   /api/posts/
        PATCH  /api/posts/7/
        DELETE /api/posts/7/
    """, kind="mapear", source="status"),
    c("h13", "http_api", "¿Qué diferencia semántica hay entre PUT y PATCH?", "PUT reemplaza la representación completa; PATCH aplica cambios parciales. En DRF son update y partial_update.", code="""
        PUT   /api/posts/7/   { representación completa }
        PATCH /api/posts/7/   { "titulo": "Nuevo" }
    """, kind="comparar", source="status"),
    c("h14", "http_api", "Completá: input inválido, sin autenticar, prohibido, inexistente y conflicto.", "400, 401, 403, 404 y 409, respectivamente.", code="""
        input inválido -> ?
        sin autenticar -> ?
        autenticado sin permiso -> ?
        recurso inexistente -> ?
        conflicto de estado -> ?
    """, answer_code="400 · 401 · 403 · 404 · 409", kind="completar", source="status"),
    c("h15", "http_api", "¿Por qué no devolver 200 con {'error': ...} para todo?", "Clientes, caches y observabilidad dependen de la semántica HTTP. El status representa el resultado; el body aporta detalles.", code='return Response({"error": "Post inexistente"}, status=200)', kind="debugging", source="status"),
    c("h16", "http_api", "¿Por qué este GET viola las propiedades safe e idempotente?", "GET no debería cambiar estado. Agregar un like tiene efecto lateral y repetirlo puede cambiar el resultado pretendido.", code="GET /api/posts/7/like/", kind="seguridad", source="requests"),
    c("h17", "http_api", "¿Qué problemas tiene este diseño?", "Usa un verbo en la ruta y POST para lectura. Sería natural GET /api/posts/?autor=ana o una ruta de recurso anidado.", code="POST /api/get-posts-by-user/", kind="diseño", source="requests"),
    c("h18", "http_api", "¿Qué indica Content-Type y qué indica Accept?", "Content-Type describe el body enviado. Accept expresa formatos aceptados para la respuesta.", code="""
        Content-Type: application/json
        Accept: application/json
    """, kind="comparar", source="requests"),
    c("h19", "http_api", "¿Por qué paginar aunque hoy haya pocos posts?", "Evita respuestas sin límite, reduce memoria/latencia y estabiliza el contrato antes del crecimiento.", code="GET /api/posts/?page=3", kind="decisión", source="pagination"),
    c("h20", "http_api", "¿Qué debe tener un error útil sin filtrar detalles internos?", "Status correcto, mensaje claro y errores por campo. No tracebacks, SQL ni secretos.", code='{"titulo": ["Este campo es obligatorio."]}', kind="diseño", source="responses"),
    c("h21", "http_api", "¿Cuál request es más cacheable por semántica?", "GET, porque representa lectura y los caches comprenden su semántica. POST no suele tratarse como lectura cacheable.", code="""
        GET  /api/posts/7/
        POST /api/posts/7/read/
    """, kind="razonamiento", source="requests"),

    # AUTH, PERMISSIONS Y SEGURIDAD
    c("p01", "auth_security", "¿Qué problema resuelve y cuándo se ejecuta has_object_permission?", "Impide modificar un objeto ajeno. Corre después de has_permission cuando la view obtiene un objeto y ejecuta el chequeo, como get_object.", code="""
        class IsOwner(BasePermission):
            def has_object_permission(self, request, view, obj):
                return obj.autor == request.user
    """, kind="leer código", source="permissions"),
    c("p02", "auth_security", "¿Por qué este permiso no evita que list muestre objetos ajenos?", "Los permisos de objeto no se aplican fila por fila al listado. Hay que restringir get_queryset.", code="""
        permission_classes = [IsOwner]
        def get_queryset(self):
            return Post.objects.all()
    """, answer_code='return Post.objects.filter(autor=self.request.user)', kind="debugging", difficulty="media", source="permissions"),
    c("p03", "auth_security", "Completá: lectura para cualquiera y escritura solo para el autor.", "Se permiten SAFE_METHODS y se compara ownership para el resto.", code="""
        class IsOwnerOrReadOnly(BasePermission):
            def has_object_permission(self, request, view, obj):
                ________
    """, answer_code="""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.autor == request.user
    """, kind="completar", source="permissions"),
    c("p04", "auth_security", "Diferenciá autenticación y autorización.", "Authentication identifica al usuario/token. Permissions decide si esa identidad puede ejecutar PATCH sobre ese post.", code="""
        PATCH /api/posts/9/
        Authorization: Token abc123
    """, kind="explicar", source="authentication"),
    c("p05", "auth_security", "¿Qué suelen significar request.user y request.auth?", "user es el usuario autenticado; auth suele ser el token/credencial. Sin autenticación son AnonymousUser y None.", code="""
        print(request.user)
        print(request.auth)
    """, kind="leer código", source="authentication"),
    c("p06", "auth_security", "¿Cuándo esperás 401 y cuándo 403?", "401 cuando faltan/fallan credenciales y el autenticador usa WWW-Authenticate. 403 cuando está autenticado pero no autorizado; ciertos esquemas pueden dar 403 al anónimo.", code="""
        # sin token válido -> 401/403 según autenticador
        # token válido, objeto ajeno -> 403
    """, kind="comparar", difficulty="media", source="permissions"),
    c("p07", "auth_security", "¿Qué vulnerabilidad introduce aceptar autor desde el body?", "Suplantación/broken access control: el cliente crea en nombre de otro. Debe derivarse de request.user.", code='serializer.save(autor_id=request.data["autor"])', answer_code='serializer.save(autor=request.user)', kind="seguridad", source="permissions"),
    c("p08", "auth_security", "¿Qué está mal al guardar una contraseña así?", "Queda sin hashing correcto. Debe usarse set_password o create_user.", code='User(username="ana", password=request.data["password"]).save()', answer_code="""
        user = User(username="ana")
        user.set_password(request.data["password"])
        user.save()
    """, kind="seguridad", source="authentication"),
    c("p09", "auth_security", "¿Qué protege CSRF y cuándo importa especialmente en DRF?", "Evita que otro sitio fuerce acciones con credenciales enviadas automáticamente por el navegador. Importa con sesión/cookies.", code='authentication_classes = [SessionAuthentication]', kind="seguridad", difficulty="media", source="security"),
    c("p10", "auth_security", "¿Por qué CORS no reemplaza permissions ni auth?", "CORS es una política del navegador sobre lectura entre orígenes. No impide otros clientes ni decide permisos.", code="Access-Control-Allow-Origin: https://frontend.example", kind="explicar", source="security"),
    c("p11", "auth_security", "¿Qué ataque evita el ORM y qué condición se mantiene?", "Parametriza valores y reduce SQL injection. Igual hay que validar la lógica y no concatenar raw SQL.", code='Post.objects.filter(titulo__icontains=request.query_params.get("q", ""))', kind="seguridad", source="security"),
    c("p12", "auth_security", "¿Qué riesgo existe al marcar contenido del usuario como safe?", "XSS almacenado: HTML o scripts maliciosos se renderizan sin escape. Hay que conservar autoescape salvo sanitización confiable.", code="{{ comentario.texto|safe }}", kind="seguridad", source="security"),
    c("p13", "auth_security", "¿Por qué este log es peligroso?", "Puede exponer passwords o tokens. Credenciales, cookies y bodies sensibles deben redactarse.", code='logger.info("login payload=%s", request.data)', kind="seguridad", source="security"),
    c("p14", "auth_security", "¿Qué controles sumarías a IsAuthenticated para una importación masiva?", "Throttling, validación estricta, límites de tamaño, monitoreo y quizá permisos de rol. Auth no frena abuso de un usuario válido.", code="""
        class ImportView(APIView):
            permission_classes = [IsAuthenticated]
    """, kind="diseño", difficulty="media", source="permissions"),

    # TESTING Y DEBUGGING
    c("t01", "testing", "¿Qué tres cosas importantes verifica este test?", "Status 201, persistencia y que el autor es el usuario autenticado.", code="""
        def test_crear_post_asigna_autor(self):
            self.client.force_authenticate(self.user)
            response = self.client.post(
                reverse("post-list"),
                {"titulo": "Hola", "contenido": "..."},
                format="json",
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertTrue(Post.objects.filter(autor=self.user).exists())
    """, kind="leer test", source="testing"),
    c("t02", "testing", "Completá: un anónimo no puede crear posts con TokenAuthentication.", "La expectativa es 401 Unauthorized.", code="""
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, ________)
    """, answer_code="self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)", kind="completar", source="testing"),
    c("t03", "testing", "¿Qué bug de permisos detecta este test?", "Que un usuario autenticado pueda editar el post de otro. Exige 403 y que el dato no cambie.", code="""
        self.client.force_authenticate(self.otro_usuario)
        response = self.client.patch(self.url, {"titulo": "Hack"})
        self.post.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertNotEqual(self.post.titulo, "Hack")
    """, kind="leer test", source="testing"),
    c("t04", "testing", "¿Por qué hace falta refresh_from_db?", "La instancia en memoria no se actualiza con cambios hechos por la request. refresh_from_db vuelve a leerla.", code="""
        response = self.client.patch(url, {"titulo": "Nuevo"})
        post.refresh_from_db()
        self.assertEqual(post.titulo, "Nuevo")
    """, kind="explicar", source="django_testing"),
    c("t05", "testing", "¿Qué problema tiene un test que solo afirma 200?", "Puede pasar con JSON, filtros o permisos incorrectos. Hay que probar contenido y efectos observables.", code="""
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    """, kind="debugging", source="testing"),
    c("t06", "testing", "Completá la aserción que prueba el filtro por autor.", "Conviene comprobar IDs, no solo cantidad.", code="""
        response = self.client.get(f"{url}?autor={ana.id}")
        ids = [item["id"] for item in response.data["results"]]
        ________
    """, answer_code="self.assertEqual(ids, [post_de_ana.id])", kind="completar", source="testing"),
    c("t07", "testing", "¿Qué mide assertNumQueries y qué regresión detecta?", "Afirma cantidad de queries y puede detectar que reaparezca N+1.", code="""
        with self.assertNumQueries(2):
            response = self.client.get(reverse("post-list"))
    """, kind="performance", difficulty="media", source="django_testing"),
    c("t08", "testing", "Pasa solo y falla en suite. ¿Qué sospechás?", "Estado compartido: orden, datos globales, cache, mocks, reloj o settings mutados. Cada test debe aislar precondiciones.", code="""
        python manage.py test foro.tests.TestPosts.test_list  # pasa
        python manage.py test                                # falla
    """, kind="debugging", difficulty="media", source="django_testing"),
    c("t09", "testing", "¿Qué diferencia hay entre setUp y setUpTestData?", "setUp corre antes de cada test. setUpTestData crea datos una vez por clase en TestCase y puede acelerar fixtures estables.", code="""
        @classmethod
        def setUpTestData(cls):
            cls.user = User.objects.create_user(username="ana")
    """, kind="comparar", source="django_testing"),
    c("t10", "testing", "¿Qué bordes faltan testear en este like?", "Like repetido, anónimo, post inexistente, unlike sin like, permisos y concurrencia/unicidad según el diseño.", code="""
        @action(detail=True, methods=["post"])
        def like(self, request, pk=None):
            self.get_object().likes.add(request.user)
            return Response(status=204)
    """, kind="diseñar tests", source="testing"),
    c("t11", "testing", "¿Cuándo unit test y cuándo API test?", "Unit para una función de dominio pura. API test para integrar routing, auth, permissions, serializer, status y base.", code="""
        calcular_reputacion(usuario)  # unit
        POST /api/posts/7/like/        # API
    """, kind="decisión", source="testing"),
    c("t12", "testing", "La API devuelve 500. Ordená un diagnóstico corto.", "Reproducir, leer traceback, ubicar la primera línea propia, revisar datos, agregar un test que falle, corregir y correr suite.", code="""
        Internal Server Error: /api/posts/
        Traceback (most recent call last):
          File "foro/serializers.py", line 27
    """, kind="debugging", source="django_testing"),

    # GIT Y DEPLOY
    c("g01", "git_deploy", "¿Qué diferencia hay entre working tree, staging y commit?", "Working tree contiene cambios; staging selecciona; commit guarda una instantánea versionada.", code="""
        git status
        git add foro/serializers.py
        git commit -m "Valida títulos de posts"
    """, kind="explicar", source="git"),
    c("g02", "git_deploy", "¿Por qué git add . es riesgoso sin mirar status?", "Puede incluir secretos, generados o cambios no relacionados. Hay que stagear intencionalmente.", code="""
        git add .
        git commit -m "cosas"
    """, kind="debugging", source="git"),
    c("g03", "git_deploy", "¿Qué debe hacer un buen commit?", "Ser pequeño, coherente y describir una intención; facilitar revisión y rollback.", code="""
        feat(api): agrega filtro de publicados
        fix(auth): impide editar posts ajenos
    """, kind="decisión", source="git"),
    c("g04", "git_deploy", "¿Qué hacés con este conflicto antes de commitear?", "Entender ambas versiones, editar el resultado, quitar marcadores, correr tests y git add.", code="""
        <<<<<<< HEAD
        permission_classes = [IsAuthenticated]
        =======
        permission_classes = [IsOwner]
        >>>>>>> feature
    """, kind="debugging", source="git"),
    c("g05", "git_deploy", "¿Dónde vive SECRET_KEY y por qué getenv puede fallar silenciosamente?", "En secretos del entorno. getenv devuelve None si falta; para un secreto requerido conviene fallar temprano.", code='SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")', answer_code='SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]', kind="seguridad", source="deploy"),
    c("g06", "git_deploy", "¿Qué settings revisarías además de DEBUG?", "ALLOWED_HOSTS, SECRET_KEY, HTTPS/cookies, CSRF origins, base externa, static files, logging y settings por entorno.", code="""
        DEBUG = False
        ALLOWED_HOSTS = ["api.example.com"]
        SESSION_COOKIE_SECURE = True
        CSRF_COOKIE_SECURE = True
    """, kind="deploy", source="deploy"),
    c("g07", "git_deploy", "¿Qué comando detecta errores comunes de producción?", "python manage.py check --deploy. No reemplaza tests ni revisión de infraestructura.", code="python manage.py check --deploy", kind="comando", source="deploy"),
    c("g08", "git_deploy", "¿Por qué ejecutar migrate como paso controlado?", "El código puede depender de nuevo esquema. Hay que coordinar orden, compatibilidad, backups y migraciones largas.", code="python manage.py migrate --noinput", kind="deploy", difficulty="media", source="migrations"),
    c("g09", "git_deploy", "¿Por qué SQLite suele quedar corto con varias instancias?", "Es un archivo local y no una base compartida robusta. PostgreSQL aporta concurrencia, red, backups y operación de producción.", code='DATABASE_URL = os.environ["DATABASE_URL"]', kind="arquitectura", source="postgres"),
    c("g10", "git_deploy", "Producción da 500 pero local funciona. ¿Qué comparás?", "Entorno, dependencias, migraciones, base, logs, static, hosts/CSRF, comando de arranque y health check.", code="GET /api/posts/  # local 200, producción 500", kind="debugging", source="deploy"),

    # PYTHON PARA BACKEND
    c("py01", "python", "¿Por qué comparte datos entre llamadas?", "El default se crea una sola vez. Usá None y creá la lista dentro.", code="""
        def agregar_error(error, errores=[]):
            errores.append(error)
            return errores
    """, answer_code="""
        def agregar_error(error, errores=None):
            if errores is None:
                errores = []
            errores.append(error)
            return errores
    """, kind="debugging", source="python"),
    c("py02", "python", "¿Qué diferencia hay entre is y ==?", "== compara valores; is compara identidad. Para None se usa is None.", code="""
        value == None
        value is None
    """, kind="comparar", source="python"),
    c("py03", "python", "¿Qué imprime y por qué?", "[1, 2]. a y b apuntan a la misma lista mutable.", code="""
        a = [1]
        b = a
        b.append(2)
        print(a)
    """, kind="leer código", source="python"),
    c("py04", "python", "¿Qué ventaja tiene un generador con muchos datos?", "Produce bajo demanda y evita cargar toda la colección en memoria.", code="""
        def ids_publicados(posts):
            for post in posts:
                if post.publicado:
                    yield post.id
    """, kind="explicar", source="python"),
    c("py05", "python", "¿Qué error de excepciones hay?", "Captura todo y oculta bugs. Debe capturar excepciones esperadas específicas.", code="""
        try:
            post = Post.objects.get(pk=pk)
        except Exception:
            return None
    """, answer_code="""
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None
    """, kind="debugging", source="python"),
    c("py06", "python", "¿Qué hace * en la firma?", "Obliga a pasar publicado por nombre y evita booleanos posicionales confusos.", code="""
        def crear_post(titulo: str, *, publicado: bool = False) -> Post:
            ...

        crear_post("Hola", publicado=True)
    """, kind="leer código", source="python"),
    c("py07", "python", "¿Por qué no usar una comprensión acá?", "Las comprensiones son para construir colecciones, no para esconder efectos laterales.", code="[enviar_email(user) for user in usuarios]", answer_code="""
        for user in usuarios:
            enviar_email(user)
    """, kind="refactor", source="python"),
    c("py08", "python", "¿Qué garantiza with aunque json.load falle?", "Ejecuta el context manager y cierra el archivo al salir.", code="""
        with open("posts.json", encoding="utf-8") as file:
            data = json.load(file)
    """, kind="leer código", source="python"),
    c("py09", "python", "¿Qué aporta el type hint y qué NO hace?", "Documenta y habilita análisis estático. No valida tipos en runtime por sí solo.", code="""
        def publicar(post: Post, actor: User) -> None:
            post.publicado = True
    """, kind="explicar", source="python"),
    c("py10", "python", "¿Qué comparte esta shallow copy?", "La lista exterior es nueva, pero el diccionario interno sigue compartido; cambiar id afecta ambos.", code="""
        original = [{"id": 1}]
        copia = original.copy()
        copia[0]["id"] = 9
    """, kind="razonamiento", source="python"),

    # ENTREVISTA JUNIOR
    c("e01", "entrevista", "Explicá este endpoint de punta a punta.", "El router dirige POST a create; auth identifica; permission permite; serializer valida; perform_create fija autor; INSERT guarda; vuelve 201.", code="""
        class PostViewSet(ModelViewSet):
            queryset = Post.objects.all()
            serializer_class = PostSerializer
            permission_classes = [IsAuthenticated]

            def perform_create(self, serializer):
                serializer.save(autor=self.request.user)
    """, kind="entrevista", source="views"),
    c("e02", "entrevista", "Encontrá al menos cuatro problemas reales.", "get puede fallar; no hay auth/ownership; acepta autor del cliente; no valida con serializer; responde 200 al crear; accede al body sin manejo.", code="""
        def create_post(request):
            user = User.objects.get(id=request.data["autor"])
            post = Post.objects.create(
                titulo=request.data["titulo"], autor=user
            )
            return Response({"id": post.id})
    """, kind="debugging", difficulty="media", source="views"),
    c("e03", "entrevista", "Completá una consulta sin N+1 para autor, likes y cantidad de comentarios.", "select_related, prefetch_related y annotate Count.", code="""
        posts = Post.objects.________("autor") \
            .________("likes") \
            .________(num_comentarios=Count("comentarios"))
    """, answer_code="""
        posts = (Post.objects
            .select_related("autor")
            .prefetch_related("likes")
            .annotate(num_comentarios=Count("comentarios")))
    """, kind="completar", difficulty="media", source="optimization"),
    c("e04", "entrevista", "¿Qué race condition existe y cómo la cerrarías?", "Dos requests pueden crear a la vez. UniqueConstraint es esencial; get_or_create y manejo de IntegrityError completan el flujo.", code="""
        if not Like.objects.filter(post=post, usuario=user).exists():
            Like.objects.create(post=post, usuario=user)
    """, kind="concurrencia", difficulty="alta", source="transactions"),
    c("e05", "entrevista", "El listado tarda 900 ms. ¿Cómo investigarías?", "Medir queries/tiempo, reproducir con volumen, inspeccionar SQL/EXPLAIN, buscar N+1 y serialización, revisar índices y volver a medir.", code="GET /api/posts/?page=1  # 900 ms, 203 queries", kind="performance", difficulty="media", source="optimization"),
    c("e06", "entrevista", "¿Cuál es el bug aunque IsAuthenticated esté presente?", "Cualquier autenticado puede borrar cualquier post si no hay ownership de objeto o restricción en queryset.", code="""
        class PostViewSet(ModelViewSet):
            permission_classes = [IsAuthenticated]
            queryset = Post.objects.all()
    """, kind="debugging", source="permissions"),
    c("e07", "entrevista", "¿Qué validarías en serializer y qué garantizarías en base?", "Serializer: mensajes y reglas de input. Base: integridad y unicidad bajo cualquier entrada/concurrencia.", code='UniqueConstraint(fields=["usuario", "post"], name="like_unico")', kind="diseño", source="models"),
    c("e08", "entrevista", "PATCH sin titulo falla con KeyError. ¿Cuál es la causa?", "La validación asume que todos los campos llegan. PATCH es parcial y debe manejar claves ausentes.", code='if not attrs["titulo"].strip(): ...', kind="debugging", source="serializers"),
    c("e09", "entrevista", "¿Qué debería responder DELETE exitoso?", "204 No Content y body vacío. JSON con 204 contradice la semántica de no contenido.", code="DELETE /api/posts/7/", kind="entrevista", source="status"),
    c("e10", "entrevista", "¿Por qué un índice común puede no acelerar esta búsqueda?", "icontains suele usar comodín; un B-tree común puede no ayudar. Puede requerir trigramas o full-text según el caso.", code='Post.objects.filter(contenido__icontains="django")', kind="performance", difficulty="alta", source="postgres"),
    c("e11", "entrevista", "Explicá select_related vs prefetch_related con el foro.", "select_related hace JOIN para autor; prefetch_related hace consultas separadas para likes/comentarios y une en Python.", code="""
        Post.objects \
            .select_related("autor") \
            .prefetch_related("likes", "comentarios")
    """, kind="entrevista", source="optimization"),
    c("e12", "entrevista", "Completá: cualquiera lee; solo el dueño escribe.", "IsAuthenticatedOrReadOnly y el permiso de ownership.", code='permission_classes = [________, ________]', answer_code='permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]', kind="completar", source="permissions"),
    c("e13", "entrevista", "Te piden JWT. ¿Qué preguntarías antes de elegirlo?", "Cliente, sesión/cookies, expiración/refresh, revocación, almacenamiento, CORS/CSRF, logout y operación. JWT no es automáticamente más seguro.", code="Authorization: Bearer <token>", kind="decisión", difficulty="media", source="authentication"),
    c("e14", "entrevista", "¿Por qué get_object puede dar 404 aunque exista el post?", "Usa get_queryset. Si filtra por autor, un post ajeno queda fuera y se oculta como 404.", code="""
        def get_queryset(self):
            return Post.objects.filter(autor=self.request.user)

        post = self.get_object()
    """, kind="razonamiento", difficulty="media", source="views"),
    c("e15", "entrevista", "El test esperaba lista pero recibió results. ¿Qué cambió?", "Se activó paginación; el contrato ahora usa count/next/previous/results.", code="""
        # antes: [{"id": 1}]
        # ahora: {"count": 1, "results": [{"id": 1}]}
    """, kind="debugging", source="pagination"),
    c("e16", "entrevista", "Una migración bloquea escrituras. ¿Qué enfoque proponés?", "Etapas compatibles: agregar nullable, desplegar, completar en lotes, agregar constraint y limpiar. Probar con volumen real.", code="ALTER TABLE post ADD COLUMN estado varchar(20) NOT NULL;", kind="deploy", difficulty="alta", source="migrations"),
    c("e17", "entrevista", "¿Qué loguearías sin filtrar secretos?", "Request ID, ruta, método, status, duración, user ID y error estructurado. Nunca tokens, passwords ni bodies sensibles.", code="""
        logger.info("request_done", extra={
            "path": request.path, "status": 200,
            "user_id": request.user.pk,
        })
    """, kind="seguridad", source="deploy"),
    c("e18", "entrevista", "¿Qué revisarías en una PR que agrega esta action?", "Contrato/status, validación, auth/permissions, queries, transacciones, tests, migraciones, seguridad y compatibilidad.", code="""
        @action(detail=True, methods=["post"])
        def reportar(self, request, pk=None):
            ...
    """, kind="entrevista", source="views"),
    c("e19", "entrevista", "¿Por qué ocultar Editar en frontend no protege?", "El cliente es controlable y puede llamar PATCH directo. El backend verifica permisos en cada request.", code="""
        if (post.autor_id === currentUser.id) {
          showEditButton();
        }
    """, kind="seguridad", source="permissions"),
    c("e20", "entrevista", "Respuesta breve: ¿qué hace un serializer?", "Convierte objetos a datos representables y, en entrada, parsea/valida antes de crear o actualizar. No reemplaza permissions ni el queryset.", code="""
        PostSerializer(post)          # salida
        PostSerializer(data=payload)  # entrada
    """, kind="entrevista", source="serializers"),

    # VEREDICTO — PRIMERO ELEGIR, DESPUÉS EXPLICAR
    c("v01", "drf", "¿Este código está bien o mal para crear un post? Elegí antes de ver la explicación.", "Está bien. El autor se deriva del usuario autenticado y no de un valor controlado por el cliente. El serializer también debería declarar autor como read_only.", code="""
        def perform_create(self, serializer):
            serializer.save(autor=self.request.user)
    """, kind="veredicto", source="views", verdict=True),
    c("v02", "drf", "¿Este código está bien o mal para asignar el autor?", "Está mal. Permite que el cliente envíe el ID de otra persona y cree contenido en su nombre. El servidor debe usar request.user.", code="""
        def perform_create(self, serializer):
            serializer.save(autor_id=self.request.data["autor"])
    """, kind="veredicto", source="permissions", verdict=False),
    c("v03", "orm_db", "¿Esta consulta está bien o mal para recorrer autores sin N+1?", "Está bien. autor es una ForeignKey y select_related hace el JOIN necesario para traerlo con cada post.", code="""
        posts = Post.objects.select_related("autor")
        for post in posts:
            print(post.autor.username)
    """, kind="veredicto", source="optimization", verdict=True),
    c("v04", "orm_db", "¿Esta optimización está bien o mal para una relación ManyToMany?", "Está mal. select_related no sirve para relaciones múltiples como likes. Corresponde prefetch_related('likes').", code='Post.objects.select_related("likes")', answer_code='Post.objects.prefetch_related("likes")', kind="veredicto", source="optimization", verdict=False),
    c("v05", "orm_db", "¿Esta consulta está bien o mal si puede haber muchos posts publicados?", "Está mal. get exige exactamente una fila y lanzará MultipleObjectsReturned si hay varias. Para varios resultados corresponde filter.", code='Post.objects.get(publicado=True)', answer_code='Post.objects.filter(publicado=True)', kind="veredicto", source="queries", verdict=False),
    c("v06", "orm_db", "¿Esta comprobación está bien o mal si solo importa saber si existe el like?", "Está bien. exists comunica la intención y evita materializar todos los objetos.", code="""
        ya_existe = Like.objects.filter(
            post=post,
            usuario=request.user,
        ).exists()
    """, kind="veredicto", source="optimization", verdict=True),
    c("v07", "auth_security", "¿Este permiso está bien o mal para impedir que list muestre posts ajenos?", "Está mal para listados. DRF no ejecuta has_object_permission sobre cada fila de list; la visibilidad debe limitarse en get_queryset.", code="""
        class IsOwner(BasePermission):
            def has_object_permission(self, request, view, obj):
                return obj.autor == request.user
    """, answer_code="""
        def get_queryset(self):
            return Post.objects.filter(autor=self.request.user)
    """, kind="veredicto", source="permissions", verdict=False),
    c("v08", "auth_security", "¿Este permiso está bien o mal para lectura pública y escritura del dueño?", "Está bien. GET, HEAD y OPTIONS son seguros; los demás métodos requieren que el usuario sea el autor.", code="""
        def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return True
            return obj.autor == request.user
    """, kind="veredicto", source="permissions", verdict=True),
    c("v09", "serializers", "¿Esta configuración está bien o mal para controlar el contrato de la API?", "Está bien. La lista explícita evita exponer accidentalmente campos nuevos y read_only protege valores administrados por el servidor.", code="""
        class Meta:
            model = Post
            fields = ["id", "titulo", "autor", "creado_en"]
            read_only_fields = ["id", "autor", "creado_en"]
    """, kind="veredicto", source="serializers", verdict=True),
    c("v10", "serializers", "¿Esta creación de usuario está bien o mal?", "Está mal. create no aplica automáticamente el hash esperado al password. Debe usarse create_user o set_password.", code="""
        user = User.objects.create(
            username="ana",
            password=request.data["password"],
        )
    """, answer_code='user = User.objects.create_user(username="ana", password=request.data["password"])', kind="veredicto", source="authentication", verdict=False),
    c("v11", "serializers", "¿Este serializer está bien o mal para un PATCH parcial?", "Está bien. partial=True permite omitir campos requeridos que no se quieren modificar.", code="""
        serializer = PostSerializer(
            post,
            data=request.data,
            partial=True,
        )
    """, kind="veredicto", source="serializers", verdict=True),
    c("v12", "http_api", "¿Esta respuesta está bien o mal después de borrar correctamente?", "Está mal como convención REST. Un DELETE exitoso normalmente responde 204 No Content y sin body.", code='return Response({"deleted": True}, status=200)', answer_code='return Response(status=status.HTTP_204_NO_CONTENT)', kind="veredicto", source="status", verdict=False),
    c("v13", "http_api", "¿Este endpoint está bien o mal diseñado?", "Está mal. GET debería ser una operación segura y no cambiar estado. Dar like debe usar un método de escritura como POST o PUT.", code="GET /api/posts/7/like/", answer_code="POST /api/posts/7/like/", kind="veredicto", source="requests", verdict=False),
    c("v14", "orm_db", "¿Este patrón está bien o mal para evitar que dos requests reserven el mismo turno?", "Está bien como base: atomic agrupa la operación y select_for_update bloquea la fila mientras se decide. Aun conviene sostener reglas con constraints cuando sea posible.", code="""
        with transaction.atomic():
            turno = Turno.objects.select_for_update().get(pk=pk)
            if not turno.disponible:
                raise ValidationError("Ocupado")
            turno.disponible = False
            turno.save(update_fields=["disponible"])
    """, kind="veredicto", difficulty="media", source="transactions", verdict=True),
    c("v15", "git_deploy", "¿Esta forma de obtener un secreto requerido está bien o mal?", "Está bien para producción: el proceso falla temprano si falta la variable, en vez de arrancar con una clave vacía o insegura.", code='SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]', kind="veredicto", source="deploy", verdict=True),
    c("v16", "git_deploy", "¿Esta configuración está bien o mal para producción?", "Está mal. DEBUG=True puede exponer trazas, settings y datos sensibles. Debe ser False en producción.", code="""
        DEBUG = True
        ALLOWED_HOSTS = ["api.example.com"]
    """, kind="veredicto", source="deploy", verdict=False),
    c("v17", "testing", "¿Este test está bien o mal como única prueba del endpoint?", "Está mal por incompleto. Un 200 no demuestra que el JSON, filtros, permisos o datos sean correctos. Hay que afirmar el comportamiento relevante.", code="""
        response = self.client.get(reverse("post-list"))
        self.assertEqual(response.status_code, 200)
    """, kind="veredicto", source="testing", verdict=False),
    c("v18", "testing", "¿Este test está bien o mal para comprobar ownership?", "Está bien. Autentica otro usuario, espera 403 y además comprueba que la base no haya cambiado.", code="""
        self.client.force_authenticate(self.otro_usuario)
        response = self.client.patch(url, {"titulo": "Hack"})
        post.refresh_from_db()
        self.assertEqual(response.status_code, 403)
        self.assertNotEqual(post.titulo, "Hack")
    """, kind="veredicto", source="testing", verdict=True),
    c("v19", "python", "¿Esta función está bien o mal para reutilizarla en muchas requests?", "Está mal. La lista por defecto es mutable y se comparte entre llamadas. Debe usarse None y crear una lista nueva dentro.", code="""
        def agregar_error(error, errores=[]):
            errores.append(error)
            return errores
    """, answer_code="""
        def agregar_error(error, errores=None):
            errores = [] if errores is None else errores
            errores.append(error)
            return errores
    """, kind="veredicto", source="python", verdict=False),
    c("v20", "python", "¿Esta comparación está bien o mal?", "Está bien. None es un singleton y se compara por identidad con is None.", code="""
        if value is None:
            return Response(status=204)
    """, kind="veredicto", source="python", verdict=True),
]
