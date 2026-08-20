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


CURRICULUM_LEVELS = [
    {
        "id": 0,
        "name": "Mapa inicial",
        "short": "El vocabulario y las piezas antes de leer backend.",
        "goal": "Reconocer qué es cada pieza y seguir una request completa sin asumir conocimientos previos.",
    },
    {
        "id": 1,
        "name": "Fundamentos aplicados",
        "short": "HTTP, Django, datos y DRF en código sencillo.",
        "goal": "Usar el mapa inicial para leer y explicar el recorrido de código backend real.",
    },
    {
        "id": 2,
        "name": "Construir APIs",
        "short": "CRUD, relaciones, validación, permisos y tests.",
        "goal": "Construir una REST API pequeña, correcta y mantenible.",
    },
    {
        "id": 3,
        "name": "Backend sólido",
        "short": "Performance, seguridad, datos y producción.",
        "goal": "Razonar sobre fallos reales más allá del happy path.",
    },
    {
        "id": 4,
        "name": "Entrevista Junior",
        "short": "Explicar decisiones y resolver mini-casos.",
        "goal": "Responder con claridad, fundamentos y criterio técnico.",
    },
]


# Level 0 teaches the map and vocabulary before asking the learner to interpret
# framework code. Existing backend primers are interleaved with smaller bridges.
LEVEL_ZERO_SEQUENCE = [
    "z01", "z02", "b01", "b02", "z03", "b03", "z04", "b04",
    "b13", "b14", "b16",
    "z05", "z06", "z07", "z08", "z09", "z10",
    "z11", "z12", "b11", "b05", "b06",
    "b07", "z13", "b08", "b09", "z14", "b10", "b12", "b15",
    "z15", "z16", "z17", "z18",
]


# Level 1 is deliberately ordered by dependency. In particular, get_object is
# introduced only after QuerySets, ViewSets, get_queryset and permissions.
FOUNDATION_SEQUENCE = [
    "h01", "h18", "h13", "h14", "h15",
    "dj01", "dj02", "dj03", "dj07", "dj08", "dj09", "dj10",
    "m04", "m20", "m17", "m21", "m24",
    "o01", "o15", "o19", "o18", "o20",
    "s01", "s10", "s14", "s12", "s11",
    "d01", "d04", "d10", "d12",
    "p04", "p05", "p06", "d08",
    "t01", "t04", "t05",
    "g01", "g05",
]


# Some prompts are intentionally short, like they would be in an interview. These
# notes provide the missing scenario without giving away the answer. Explanations
# then rebuild the answer from the underlying invariant instead of adding trivia.
CARD_CONTEXTS = {
    "dj01": "Un cliente pide el detalle de un post. Seguí la petición desde que entra al servidor hasta que Django arma la respuesta.",
    "dj04": "El navegador pide /api/posts/, pero Django responde 404. La función views.posts sí existe y no está fallando al ejecutarse.",
    "m18": "El endpoint de likes puede recibir dos POST casi al mismo tiempo y ambos pasan por procesos distintos del servidor.",
    "m22": "La migración se aplicará sobre una tabla que ya contiene posts; PostgreSQL debe poder asignar un valor válido a cada fila existente.",
    "o16": "El listado devuelve 100 posts y el template accede al username del autor de cada uno. Medí las consultas, no solo el tiempo de Python.",
    "o17": "Cada post puede tener muchos likes y cada usuario puede likear muchos posts. El listado necesita mostrar los usuarios de cada relación.",
    "o28": "Reservar un turno es una operación de lectura y escritura. Dos workers pueden leer el mismo estado antes de que alguno guarde.",
    "s02": "Este serializer también acepta datos de escritura y el modelo seguirá sumando campos a medida que crezca el producto.",
    "s06": "El mismo serializer atiende PUT y PATCH. En PATCH el cliente envía únicamente el campo que quiere cambiar.",
    "s08": "El endpoint serializa una página de 50 posts y calcula num_likes para cada instancia.",
    "d07": "La action /like/ funciona como toggle: la misma request agrega o quita el like según el estado que encuentre al llegar.",
    "d09": "La API admite ?publicado=true y ?publicado=false. Considerá también errores de tipeo como ?publicado=si.",
    "d14": "El proyecto tiene filtros y paginación global configurados. Esta implementación reemplaza el list provisto por DRF.",
    "h15": "Un cliente móvil, un monitor y un cache consumen la misma API; todos deben distinguir éxito de error sin interpretar cada body.",
    "h16": "Un crawler, un navegador o un cache pueden repetir un GET sin pedir confirmación. La ruta propuesta agrega un like.",
    "p02": "El endpoint GET /posts/ devuelve una colección. IsOwner solo implementa has_object_permission y el queryset incluye todos los posts.",
    "p06": "Compará dos casos: una request sin credenciales válidas y otra de un usuario identificado que intenta editar un post ajeno.",
    "p09": "El frontend y la API usan una sesión guardada en cookie; el navegador adjunta esa cookie automáticamente a cada request.",
    "p10": "La API puede recibir requests desde navegadores, scripts, curl y otros servidores. CORS solo lo interpreta el navegador.",
    "t05": "Este es el único test de un listado que además filtra resultados según el usuario autenticado.",
    "t08": "El test es determinista cuando corre aislado, pero cambia de resultado según qué tests se ejecutaron antes.",
    "t12": "El objetivo no es solo apagar el 500: necesitás entender la causa y dejar una prueba que impida que vuelva.",
    "g05": "La aplicación no puede operar de forma segura sin SECRET_KEY. El valor llega como variable de entorno durante el arranque.",
    "g08": "El deploy puede tener varias instancias sirviendo tráfico mientras cambia el esquema compartido de la base.",
    "g10": "El mismo commit funciona localmente, pero falla al desplegar. Asumí que el error depende del entorno hasta demostrar lo contrario.",
    "py01": "La función puede ejecutarse muchas veces durante la vida del mismo proceso web.",
    "e02": "Este endpoint recibe datos de internet y crea un post. Evaluá errores, seguridad, contrato HTTP y validación.",
    "e04": "Hay una regla de negocio: un usuario solo puede tener un like por post. La app corre con más de un worker.",
    "e05": "La respuesta es correcta pero hace 203 queries para devolver una sola página. Tenés acceso a logs, SQL y una copia con datos realistas.",
    "e06": "La API permite que cada usuario borre sus propios posts, pero nunca los de otra persona.",
    "e07": "La misma regla puede ser atravesada por la API, el admin, un script o dos requests concurrentes.",
    "e13": "JWT sería una decisión de arquitectura para una API nueva, no un requisito ya justificado por el tipo de cliente.",
    "e16": "La tabla es grande, recibe escrituras continuamente y el deploy debe evitar una ventana de indisponibilidad.",
    "e18": "La action reportar cambia estado y llegará a producción como parte de una API ya consumida por clientes.",
}


FIRST_PRINCIPLES = {
    "dj01": "HTTP entra como una petición y debe salir como una respuesta. El URLconf es la tabla que traduce path a código; la view es el límite que transforma el request en una HttpResponse. Si no hay patrón, la view ni siquiera se ejecuta.",
    "dj04": "Un 404 de routing ocurre antes de la lógica de la view. Por eso se reconstruye la ruta efectiva de afuera hacia adentro: URLconf raíz, prefijo de include, patrones de la app y orden de coincidencia.",
    "m18": "Una comprobación en Python solo describe lo que vio un proceso en un instante. La unicidad es una propiedad de los datos y debe vivir en la base, que es el único punto compartido por todos los workers.",
    "m22": "Una columna NOT NULL afirma que cada fila tiene un valor. Al agregarla, las filas viejas no desaparecen: primero hay que definir cómo obtienen ese valor y recién después exigir la restricción.",
    "o16": "El costo real es cantidad de viajes a la base. Si una consulta trae posts y cada acceso a autor dispara otra, N objetos producen 1 + N queries. Un JOIN permite traer la relación de valor único en el mismo viaje.",
    "o17": "Una relación múltiple no cabe en una sola fila sin repetir datos del post. prefetch_related hace pocas consultas separadas y arma el mapa post → likes en memoria, evitando una consulta por post.",
    "o28": "Una reserva válida exige que observar 'disponible' y cambiarlo sea una sola decisión indivisible. La transacción define el límite y el lock impide que otro proceso tome esa decisión sobre la misma fila al mismo tiempo.",
    "s02": "Un serializer es una frontera de confianza. fields define qué atraviesa esa frontera; una allowlist explícita mantiene cerrado todo campo nuevo hasta que alguien decida exponerlo.",
    "s06": "PATCH significa modificación parcial, así que ausencia no equivale a valor vacío. La validación debe combinar lo recibido con el estado actual en vez de asumir que todas las claves existen.",
    "s08": "SerializerMethodField ejecuta Python por objeto. Si ese Python consulta la base, el costo crece con la página. La agregación debe ocurrir en el queryset para que la base calcule todo en conjunto.",
    "d07": "Una operación idempotente expresa un estado deseado: 'que exista el like' o 'que no exista'. Un toggle expresa 'invertí lo que veas', por eso reintentos y concurrencia pueden producir un resultado distinto al solicitado.",
    "d09": "Los query params son texto no confiable. Convertir cualquier valor desconocido a False transforma un error del cliente en una consulta válida pero equivocada; primero se valida el vocabulario y luego se convierte.",
    "d14": "El list de DRF no solo serializa: compone filtros, paginación y formato de respuesta. Al reemplazarlo, también reemplazás esas garantías y debés reintroducirlas explícitamente.",
    "h15": "El status es la señal común del protocolo y el body es el detalle de la aplicación. Si todo es 200, cada consumidor debe inventar su propia forma de descubrir que la operación falló.",
    "h16": "Safe significa que la intención del método es observar, no modificar. La infraestructura puede repetir o anticipar lecturas; si un GET escribe, una optimización legítima se convierte en un efecto lateral inesperado.",
    "p02": "Autorizar un objeto y seleccionar una colección son problemas distintos. En retrieve hay un objeto sobre el que evaluar ownership; en list primero hay que definir qué filas son visibles mediante el queryset.",
    "p06": "Autenticación responde '¿quién sos?' y autorización responde '¿podés hacer esto?'. 401 pertenece al primer fallo; 403, al segundo, con el matiz de que el autenticador elegido determina la respuesta al anónimo.",
    "p09": "CSRF existe porque el navegador adjunta cookies aunque la request haya sido iniciada por otro sitio. El token agrega una prueba que ese sitio atacante no puede conocer, ligando la acción al frontend legítimo.",
    "p10": "CORS limita qué respuestas deja leer un navegador. No valida identidad, no protege el endpoint de otros clientes y no decide si un usuario puede modificar un recurso; esas decisiones siguen siendo del backend.",
    "t05": "Un test vale por la propiedad observable que protege. El 200 solo prueba que hubo una respuesta exitosa; no demuestra que sean los datos correctos, en el orden correcto ni visibles para el usuario correcto.",
    "t08": "Un test debe partir de un mundo conocido. Si depende del orden, algún estado escapó de su límite: base, cache, reloj, mock o configuración. Aislar ese estado elimina la casualidad, no solo el síntoma.",
    "t12": "El traceback es una cadena causal. Se reproduce para fijar el fenómeno, se encuentra la primera línea propia que rompe el contrato y se captura ese caso en un test antes de corregirlo.",
    "g05": "Un secreto requerido es una precondición del proceso. Fallar al arrancar mantiene el error cerca de su causa; aceptar None desplaza el fallo a una request posterior y puede dejar la aplicación en un estado inseguro.",
    "g08": "Código y esquema no cambian exactamente al mismo tiempo. Una migración segura conserva compatibilidad durante la transición: primero habilita ambos mundos, después mueve datos y por último elimina lo viejo.",
    "g10": "Si el código es el mismo, la variable está en lo que lo rodea: configuración, dependencias, datos, esquema, red o proceso de arranque. Comparar esos inputs reduce el espacio de búsqueda de forma sistemática.",
    "py01": "Python evalúa los valores por defecto una vez, al definir la función. Una lista es mutable, así que cada llamada recibe el mismo objeto; None funciona como señal para crear un objeto nuevo por invocación.",
    "e02": "Una request es input no confiable. El flujo robusto identifica al actor, valida datos, aplica permisos y recién entonces persiste; cada fallo esperado se convierte en una respuesta HTTP explícita.",
    "e04": "exists seguido de create son dos operaciones, y otro worker puede entrar entre ambas. La constraint vuelve atómica la regla de unicidad; la aplicación se ocupa de traducir el conflicto a una respuesta útil.",
    "e05": "Optimizar empieza por medir dónde se consume el tiempo. El número 203 sugiere trabajo repetido: se identifica el patrón de queries, se cambia la carga de datos y se vuelve a medir con el mismo escenario.",
    "e06": "Estar autenticado solo prueba identidad. Ownership es una regla adicional sobre la relación usuario–recurso y debe comprobarse en el backend para cada operación sensible.",
    "e07": "El serializer mejora la experiencia en una entrada concreta; la constraint protege la verdad global de los datos. Se usan ambas porque tienen alcances y fallos distintos.",
    "e13": "Un mecanismo de autenticación se elige desde las amenazas y el ciclo de vida de la sesión. El formato del token no resuelve por sí solo almacenamiento, revocación, expiración ni protección del navegador.",
    "e16": "La disponibilidad exige evitar un cambio que necesite reescribir o validar toda la tabla de una vez. Expandir, completar por lotes y contraer divide el riesgo en pasos compatibles y reversibles.",
    "e18": "Una action es una nueva capacidad pública. Se revisa desde sus invariantes: quién puede ejecutarla, qué entrada acepta, qué cambia, cómo falla y cómo se demuestra todo eso con tests.",
}


# Every foundation card has its own primer. These are intentionally explicit:
# a learner should be able to reveal an unfamiliar term and rebuild the answer
# from the underlying model instead of memorising framework vocabulary.
FIRST_PRINCIPLES.update({
    "py02": "Una variable de Python referencia un objeto. == pregunta si dos objetos representan el mismo valor; is pregunta si ambas referencias apuntan al mismo objeto. None es un objeto único y por eso se comprueba con is None.",
    "py03": "Asignar una lista a otra variable no copia sus elementos: crea una segunda referencia al mismo objeto mutable. Cuando una referencia modifica la lista, la otra observa el cambio porque nunca existieron dos listas independientes.",
    "py01": "Python evalúa los valores por defecto cuando define la función, no cada vez que la llama. Si el valor es una lista mutable, todas las llamadas comparten ese objeto; usar None permite crear una lista nueva por invocación.",
    "py05": "Una excepción comunica que una operación no pudo cumplir su contrato. Capturar Exception atrapa también errores de programación inesperados y destruye evidencia; se capturan solo los fallos que realmente se saben interpretar o recuperar.",
    "py08": "Un context manager define qué debe ocurrir al entrar y al salir de un bloque. with garantiza la salida incluso ante una excepción, por eso recursos finitos como archivos, locks o conexiones pueden liberarse de forma confiable.",
    "h01": "HTTP describe operaciones sobre recursos mediante método, URL, headers y body. El status resume el resultado de la operación: 200 para una lectura exitosa, 201 para creación y 204 cuando el éxito no necesita contenido de respuesta.",
    "h18": "Una representación viaja como bytes y ambas partes deben saber cómo interpretarlos. Content-Type describe el formato del body que efectivamente se envía; Accept declara qué formatos sabe recibir el cliente en la respuesta.",
    "h13": "PUT expresa reemplazar la representación del recurso y PATCH expresa aplicar un conjunto parcial de cambios. La diferencia importa porque un campo ausente puede significar eliminarlo en un reemplazo, pero dejarlo intacto en una modificación parcial.",
    "h14": "Los status codes son un vocabulario compartido entre servidores, clientes, proxies y métricas. 400 señala input inválido, 401 falta de identidad válida, 403 falta de autorización, 404 ausencia y 409 conflicto con el estado actual.",
    "h15": "El status pertenece al protocolo y permite reconocer éxito o fallo sin entender el JSON particular de cada API. El body agrega detalles. Responder 200 ante un error rompe esa separación y obliga a cada consumidor a inventar detección propia.",
    "dj01": "Django recibe una petición HTTP y debe producir una respuesta HTTP. El URLconf traduce el path a una función o clase; la view recibe el request, coordina la lógica necesaria y devuelve una HttpResponse o una subclase.",
    "dj02": "La URL puede transportar pares clave-valor después de ?. Django los parsea en request.GET, un QueryDict de strings. get permite leer una clave y elegir un valor por defecto cuando el cliente no la envió.",
    "dj03": "Un template es texto con lugares que se completan usando un contexto. render combina template y contexto para producir HTML y luego lo envuelve en una HttpResponse; no guarda datos ni cambia por sí mismo la base.",
    "dj07": "El proyecto contiene configuración y puntos de entrada de toda la instalación. Una app agrupa una capacidad del dominio que puede tener modelos, URLs, views y tests. Separarlos reduce acoplamiento y da límites comprensibles al código.",
    "dj08": "Las URLs forman un árbol. include delega un prefijo a otro URLconf: el archivo raíz decide la zona general y cada app decide sus rutas internas. Así una app puede evolucionar sin convertir el router raíz en una lista global inmanejable.",
    "dj09": "request es la representación que Django construye a partir del mensaje HTTP. Reúne método, path, headers, query params, body, cookies y archivos; middleware y autenticación pueden agregar información como session y user.",
    "dj10": "Pedir un objeto por identidad supone que debe existir exactamente uno. get expresa esa expectativa y lanza una excepción si falla; get_object_or_404 traduce la ausencia esperable del dominio web a una respuesta HTTP 404.",
    "m04": "Una ForeignKey representa que muchas filas de una tabla pueden referirse a una fila de otra. La columna con el identificador vive en el lado muchos: cada Post guarda autor_id para señalar a su User.",
    "m20": "La base y la validación resuelven preguntas diferentes. null controla si la columna admite SQL NULL; blank controla si formularios o serializers aceptan un valor vacío. En texto, cadena vacía suele evitar dos representaciones de ausencia.",
    "m17": "Una clave foránea crea una dependencia entre filas. on_delete define qué ocurre cuando desaparece el objeto referenciado: CASCADE elimina dependientes; PROTECT rechaza el borrado cuando conservarlos es una regla del dominio.",
    "m21": "Cambiar una clase de modelo no cambia automáticamente una base existente. makemigrations describe la diferencia como una operación versionada; migrate ejecuta en orden esas operaciones sobre el esquema real.",
    "m24": "Una ForeignKey permite navegar desde el objeto que guarda la referencia hacia el relacionado. related_name pone nombre al camino inverso, para preguntar desde un User por todas las filas que lo referencian sin escribir SQL manual.",
    "o01": "Un QuerySet es una descripción componible de una consulta, no necesariamente sus resultados. filter conserva la posibilidad de cero, una o muchas filas; get exige exactamente una y por eso necesita excepciones para cero o varias.",
    "o15": "get representa la afirmación de que el criterio identifica una única fila. Si publicado=True describe muchas, la afirmación es falsa y Django lanza MultipleObjectsReturned. filter modela correctamente una colección de tamaño variable.",
    "o19": "Una búsqueda de colección puede no encontrar filas sin que el sistema haya fallado. filter devuelve un QuerySet vacío; su valor booleano refleja si tiene resultados, aunque exists expresa mejor y con menos trabajo la pregunta de existencia.",
    "o18": "La evaluación lazy permite seguir agregando filtros antes de hablar con la base. La consulta se ejecuta cuando Python necesita datos concretos: al iterar, convertir a list, pedir len, evaluar como bool o consumir un resultado.",
    "o20": "Si la única pregunta es si existe al menos una fila, traer objetos completos realiza trabajo que nadie usará. exists permite a la base detenerse al encontrar una coincidencia y comunica exactamente la intención del código.",
    "s01": "Un serializer separa input no confiable de datos que la aplicación puede usar. is_valid parsea tipos y ejecuta reglas; solo después de pasar, validated_data contiene valores normalizados aptos para crear o actualizar objetos.",
    "s10": "validated_data mira hacia la entrada: contiene únicamente campos aceptados después de validar. data mira hacia la salida: es la representación que se enviará al cliente. Son etapas distintas aunque a veces compartan nombres de campos.",
    "s14": "La validación fallida es un resultado esperado de una API, no un error 500. raise_exception convierte los errores del serializer en ValidationError y DRF los transforma mediante su manejador en una respuesta 400 estructurada.",
    "s12": "save decide entre dos operaciones según exista una instance. Sin instance todavía no hay objeto y llama create(validated_data); con instance el objetivo es modificarlo y llama update(instance, validated_data).",
    "s11": "Un serializer normalmente exige todos los campos requeridos. partial=True cambia el contrato: las claves ausentes significan conservar el valor actual. Esa es la semántica que DRF usa para PATCH frente al reemplazo de PUT.",
    "d01": "Un ViewSet agrupa operaciones sobre un mismo recurso. ModelViewSet conecta métodos HTTP con acciones estándar: list y retrieve leen, create inserta, update o partial_update modifican y destroy elimina.",
    "d04": "Un router observa las acciones del ViewSet y construye rutas de colección y detalle. /posts/ no necesita un pk y atiende list/create; /posts/{pk}/ identifica una instancia y atiende retrieve, update y destroy.",
    "d10": "DRF separa de dónde vienen los datos. query_params representa opciones incluidas en la URL, normalmente para búsqueda o filtros; data contiene el body parseado, normalmente la representación que se quiere crear o modificar.",
    "d12": "queryset es una base fija para buscar objetos. get_queryset es un método que se ejecuta en el contexto de la request y permite que la colección dependa del usuario, filtros o action sin compartir resultados evaluados entre requests.",
    "p04": "Autenticación establece una identidad a partir de sesión, token u otra credencial. Autorización toma esa identidad y decide si puede realizar una acción concreta. Saber quién es alguien no implica permitirle modificar cualquier objeto.",
    "p05": "Los autenticadores de DRF producen dos piezas: request.user representa la identidad y request.auth conserva normalmente la credencial o información asociada. Si nadie se autentica, user es AnonymousUser y auth suele ser None.",
    "p06": "401 significa que la request no presentó una identidad válida para el esquema elegido; 403 significa que el servidor conoce la identidad pero rechaza la acción. Algunos autenticadores sin WWW-Authenticate responden 403 también al anónimo.",
    "d08": "self.get_object() es el camino estándar de un ViewSet para obtener la instancia indicada por la URL. Parte de get_queryset, aplica lookup_field, convierte ausencia en 404 y ejecuta permisos de objeto; un get directo omite parte de ese flujo.",
    "t01": "Un test útil protege comportamiento observable, no solo que el código terminó. En una creación conviene verificar el status del contrato, la fila persistida y una regla del dominio como que el autor provenga del usuario autenticado.",
    "t04": "La instancia Python del test y la fila de la base son copias en momentos distintos. Una request puede cambiar la fila sin mutar el objeto que ya estaba en memoria; refresh_from_db lo reemplaza con el estado persistido actual.",
    "t05": "Un 200 solo demuestra que el servidor clasificó la request como exitosa. No demuestra datos, filtros, permisos ni efectos. El test debe afirmar la propiedad que se rompería si la implementación estuviera equivocada.",
    "g01": "Git distingue el trabajo actual, la selección para la próxima instantánea y la historia confirmada. El working tree contiene ediciones, staging decide qué entra y commit guarda una instantánea identificable y recuperable.",
    "g05": "Un secreto requerido es una precondición de arranque, no un valor opcional. Debe llegar desde el entorno y la aplicación debe fallar temprano si falta; continuar con None desplaza el error y puede iniciar con una configuración insegura.",
})


def block(value):
    return dedent(value).strip()


def c(card_id, module, question, answer, *, code="", answer_code="", context="", explanation="", kind="razonamiento", difficulty="base", source="django", verdict=None):
    return {
        "id": card_id, "module": module, "question": question, "answer": answer,
        "code": block(code) if code else "", "answer_code": block(answer_code) if answer_code else "",
        "context": context or CARD_CONTEXTS.get(card_id, ""),
        "explanation": explanation or FIRST_PRINCIPLES.get(card_id, ""),
        "kind": kind, "difficulty": difficulty,
        "source": DOCS[source], "verdict": verdict,
    }


CARDS = [
    # NIVEL 0 — MAPA Y VOCABULARIO ANTES DE LEER FRAMEWORKS
    c(
        "z01", "django",
        "¿Quiénes participan cuando una persona toca “Ver posts” en una aplicación?",
        "La persona usa un cliente —por ejemplo, un navegador o una app móvil—. Ese cliente envía un pedido a un servidor, donde corre el backend, y el backend puede consultar una base de datos antes de responder.",
        context="Antes de memorizar nombres de Django, ubicá los participantes reales de la conversación y quién inicia cada paso.",
        code="""
            persona → cliente → servidor/backend → base de datos
                    ← pantalla ← response       ← datos
        """,
        explanation="Cliente y servidor son roles en una comunicación. El cliente inicia un pedido; el servidor escucha y responde. El backend es el programa que corre del lado servidor. La base de datos conserva información, pero normalmente no queda expuesta directamente al cliente.",
        kind="mapa", difficulty="inicio", source="django",
    ),
    c(
        "z02", "django",
        "Diferenciá frontend, backend, servidor y base de datos sin usarlos como sinónimos.",
        "El frontend es la interfaz que usa la persona; el backend aplica reglas y ofrece datos; el servidor es el entorno o proceso donde ese backend se ejecuta; la base de datos persiste información.",
        context="Las cuatro piezas pueden estar en máquinas distintas y cada una tiene una responsabilidad diferente.",
        code="""
            FRONTEND          BACKEND             BASE DE DATOS
            muestra UI   →    aplica reglas   →   guarda estado
                         ←    arma respuestas ←
        """,
        explanation="Frontend y backend describen responsabilidades de software. Servidor describe el rol que recibe conexiones y también puede referirse a la máquina o proceso que ejecuta el programa. La base de datos es otro sistema especializado: almacenar, relacionar y consultar información durable.",
        kind="vocabulario", difficulty="inicio", source="django",
    ),
    c(
        "z03", "http_api",
        "Leé esta URL: ¿qué significan protocolo, host, puerto, path y query string?",
        "https es el protocolo, api.ejemplo.com el host, 443 el puerto, /posts/7/ el path y ?detalle=true la query string. El path identifica una ruta; la query agrega opciones a esa petición.",
        context="Una URL es una dirección estructurada. Separar sus partes evita llamar endpoint, parámetro y dirección completa a la misma cosa.",
        code="""
            https://api.ejemplo.com:443/posts/7/?detalle=true
            └─protocolo  └─host       └path    └query string
        """,
        explanation="El protocolo define cómo conversar; el host señala qué servidor; el puerto identifica el servicio dentro de ese host; el path selecciona una ruta y la query string transporta pares clave-valor opcionales. En localhost, el host apunta a tu propia computadora.",
        kind="vocabulario", difficulty="inicio", source="requests",
    ),
    c(
        "z04", "http_api",
        "¿Qué es JSON y qué tipos de valores reconocés en este ejemplo?",
        "JSON es un formato de texto para intercambiar datos. El ejemplo contiene un objeto con strings, un número, un booleano, null y una lista. No es un objeto de Python aunque luego el framework lo convierta.",
        context="El body de muchas APIs viaja como JSON. Primero hay que reconocer el formato antes de hablar de request.data o serializers.",
        code="""
            {
              "titulo": "Hola",
              "visitas": 3,
              "publicado": true,
              "resumen": null,
              "tags": ["django", "api"]
            }
        """,
        explanation="JSON representa objetos, listas, texto, números, booleanos y null mediante una sintaxis compartida entre lenguajes. Viaja como texto o bytes. Un parser lo transforma después en estructuras propias del lenguaje, como dict, list, str, int, bool y None en Python.",
        kind="leer datos", difficulty="inicio", source="requests",
    ),
    c(
        "z05", "python",
        "¿Qué son una variable y un valor? Reconocé los tipos básicos del ejemplo.",
        "Una variable es un nombre que referencia un valor. titulo referencia un string, visitas un entero, publicado un booleano, tags una lista y metadata un diccionario.",
        context="El código backend usa nombres para conservar y mover datos. El signo = asigna una referencia; no expresa igualdad matemática.",
        code="""
            titulo = "Hola"             # str
            visitas = 3                 # int
            publicado = True            # bool
            tags = ["django", "api"]   # list
            metadata = {"autor": 7}     # dict
        """,
        explanation="Python trabaja con objetos de distintos tipos y variables que los referencian. El tipo determina qué representa un valor y qué operaciones admite. List agrupa elementos por posición; dict los organiza por claves. None representa ausencia de valor.",
        kind="leer Python", difficulty="inicio", source="python",
    ),
    c(
        "z06", "python",
        "En esta función, ¿qué son nombre, 'Ana', saludo y return?",
        "nombre es un parámetro, 'Ana' es el argumento de la llamada, saludo es una variable local y return entrega el resultado al código que llamó la función.",
        context="Una función agrupa pasos bajo un nombre. Definirla no la ejecuta; se ejecuta cuando otro código la llama con paréntesis.",
        code="""
            def saludar(nombre):
                saludo = f"Hola {nombre}"
                return saludo

            mensaje = saludar("Ana")
        """,
        explanation="def crea una función con parámetros que recibirán valores. Una llamada suministra argumentos y abre una ejecución local. return termina esa ejecución y devuelve un valor. En una view, ocurre la misma idea: Django llama una función con request y recibe una response.",
        kind="leer Python", difficulty="inicio", source="python",
    ),
    c(
        "z07", "python",
        "Diferenciá clase, objeto o instancia, atributo y método.",
        "Una clase define una clase de objetos; una instancia es un objeto concreto. post.titulo accede a un atributo y post.publicar() llama un método, es decir, comportamiento asociado al objeto.",
        context="Django y DRF usan clases y objetos todo el tiempo: Model, Serializer y ViewSet son clases; post, serializer y request son objetos concretos.",
        code="""
            class Post:
                def publicar(self):
                    self.publicado = True

            post = Post()          # objeto o instancia
            post.titulo = "Hola"  # atributo
            post.publicar()        # método
        """,
        explanation="La clase describe estructura y comportamiento compartido; la instancia conserva el estado concreto. El punto permite acceder a nombres pertenecientes a un objeto o módulo. Un método es una función vinculada a una instancia y self representa esa instancia durante la llamada.",
        kind="leer Python", difficulty="inicio", source="python",
    ),
    c(
        "z08", "python",
        "¿Qué hacen import y el punto en models.Model o post.autor.username?",
        "import vuelve disponible código de otro módulo. El punto navega un nombre dentro de un módulo u objeto: models contiene Model; post contiene autor y ese usuario contiene username.",
        context="Mucho código de framework parece una sola palabra larga, pero suele ser una navegación de izquierda a derecha por objetos conocidos.",
        code="""
            from django.db import models

            class Post(models.Model):
                ...

            nombre = post.autor.username
        """,
        explanation="Los módulos organizan código y los imports permiten reutilizarlo sin copiarlo. La notación con punto expresa acceso a atributos. Leerla de izquierda a derecha ayuda a reconstruir la cadena: qué objeto tengo, qué miembro pido y qué valor o comportamiento devuelve.",
        kind="leer Python", difficulty="inicio", source="python",
    ),
    c(
        "z09", "python",
        "¿Qué operaciones expresan paréntesis, corchetes y encadenamiento con puntos?",
        "Los paréntesis suelen llamar una función o método; los corchetes acceden por clave o posición; los puntos encadenan accesos o llamadas sobre el resultado anterior.",
        context="No necesitás conocer todavía el ORM para separar la forma del código de lo que hace cada operación particular.",
        code="""
            request.data["titulo"]
            Post.objects.filter(publicado=True).first()
            nombres[0]
        """,
        explanation="La sintaxis ofrece pistas estables. [] selecciona un elemento; () ejecuta algo invocable; . accede a un miembro. En una cadena, cada paso recibe el resultado del anterior. Después se aprende el contrato particular de data, filter o first sin volver a descifrar la gramática.",
        kind="leer Python", difficulty="inicio", source="python",
    ),
    c(
        "z10", "python",
        "¿Para qué sirven if, for y una excepción?",
        "if elige un camino según una condición, for repite un bloque para varios elementos y una excepción comunica que una operación no pudo cumplir lo esperado.",
        context="Los backends deciden, recorren colecciones y manejan fallos. Estas tres formas aparecen luego en views, queries, validaciones y tests.",
        code="""
            if request.user.is_authenticated:
                for post in posts:
                    print(post.titulo)
            else:
                raise PermissionError("Falta autenticación")
        """,
        explanation="El flujo normal no es siempre lineal. Una condición abre ramas; un bucle aplica trabajo repetido; una excepción interrumpe el camino cuando el contrato falla y puede ser traducida por una capa superior. No toda excepción es un error HTTP, pero los frameworks suelen mapear algunas.",
        kind="leer Python", difficulty="inicio", source="python",
    ),
    c(
        "z11", "django",
        "¿Qué son un framework, Django y Django REST Framework?",
        "Un framework aporta estructura y piezas reutilizables. Django es un framework web de Python. Django REST Framework se monta sobre Django y agrega herramientas especializadas para construir APIs, como serializers, ViewSets y Response.",
        context="DRF no reemplaza a Django y Django no reemplaza a Python: son capas que agregan contratos y automatización sobre la anterior.",
        code="""
            Python
              └─ Django
                   └─ Django REST Framework (DRF)
        """,
        explanation="Python es el lenguaje; Django resuelve routing, requests, responses, modelos y otras necesidades web; DRF reutiliza esas bases y añade abstracciones para APIs. Saber en qué capa vive una pieza ayuda a buscar documentación y ubicar responsabilidades.",
        kind="mapa", difficulty="inicio", source="django",
    ),
    c(
        "z12", "django",
        "¿Qué hacen la terminal, manage.py y runserver durante el desarrollo?",
        "La terminal permite ejecutar comandos. manage.py carga el proyecto Django para tareas administrativas. runserver inicia un servidor local de desarrollo que escucha requests, normalmente en localhost:8000.",
        context="Editar archivos no pone el backend a escuchar automáticamente. Hace falta iniciar un proceso y observar su salida para probarlo.",
        code="""
            python manage.py runserver

            navegador → http://127.0.0.1:8000/ → Django local
        """,
        explanation="Un archivo contiene código; un proceso es ese código ejecutándose. El comando crea un proceso de desarrollo y lo conecta a un puerto local. manage.py también expone tareas como test, makemigrations y migrate usando la configuración correcta del proyecto.",
        kind="flujo de trabajo", difficulty="inicio", source="django",
    ),
    c(
        "z13", "modelos",
        "¿Cómo se relacionan un Model, una tabla y una migración?",
        "El Model describe en Python la estructura y reglas cercanas de una entidad; normalmente se representa en una tabla. Una migración es un cambio versionado que lleva el esquema real de la base de un estado a otro.",
        context="Cambiar models.py cambia código, pero una base ya creada necesita instrucciones explícitas para modificar sus tablas y columnas.",
        code="""
            class Post(models.Model):       tabla post
                titulo = models.CharField   columna titulo

            cambio de Model → migración → cambio de esquema
        """,
        explanation="El Model es la descripción usada por Django; la tabla es la estructura persistente administrada por la base. No son el mismo objeto. Las migraciones registran operaciones reproducibles para que desarrollo, tests y producción evolucionen el esquema en el mismo orden.",
        kind="mapa", difficulty="inicio", source="migrations",
    ),
    c(
        "z14", "auth_security",
        "En el mapa de una API, ¿qué preguntan autenticación, autorización y validación?",
        "Autenticación pregunta quién hace la request; autorización, si puede realizar esa acción; validación, si los datos enviados cumplen el contrato. Son controles diferentes y pueden fallar por separado.",
        context="Tener un JSON válido no otorga permiso, y reconocer a un usuario no vuelve válidos todos los datos que mande.",
        code="""
            identidad válida ──> autenticación
            acción permitida ──> autorización / permissions
            datos correctos  ──> validación / serializer
        """,
        explanation="Una API recibe identidad, intención y datos no confiables. Cada control reduce una incertidumbre distinta. Separarlos evita errores como aceptar autor desde el body, usar el serializer como permiso o creer que estar autenticado habilita modificar cualquier recurso.",
        kind="mapa", difficulty="inicio", source="authentication",
    ),
    c(
        "z15", "testing",
        "¿Qué es un test automatizado y qué significan preparar, actuar y afirmar?",
        "Es código que ejecuta un escenario y comprueba un resultado esperado. Primero prepara un mundo conocido, después realiza la acción y finalmente usa assertions para verificar la respuesta y los efectos.",
        context="Un test no demuestra que toda la aplicación sea correcta; protege propiedades concretas y avisa cuando un cambio las rompe.",
        code="""
            # preparar
            post = Post.objects.create(titulo="Antes")
            # actuar
            response = client.patch(url, {"titulo": "Después"})
            # afirmar
            self.assertEqual(response.status_code, 200)
        """,
        explanation="La preparación controla el estado inicial; la acción atraviesa el comportamiento que interesa; la afirmación compara lo observable con el contrato. Un buen test falla por una razón comprensible y comprueba tanto la respuesta como los cambios persistidos cuando corresponde.",
        kind="mapa", difficulty="inicio", source="django_testing",
    ),
    c(
        "z16", "git_deploy",
        "¿Qué problema resuelve Git y qué es un repositorio?",
        "Git registra versiones del código. Un repositorio es la carpeta de trabajo junto con su historia versionada; permite comparar cambios, crear ramas y volver a estados conocidos.",
        context="Guardar un archivo conserva su contenido actual. Hacer un commit registra una instantánea intencional dentro de una historia compartible.",
        code="""
            editar archivo → seleccionar cambios → commit
                              git add            git commit
        """,
        explanation="El control de versiones conserva decisiones en el tiempo y permite coordinar trabajo. Git distingue los archivos actuales, los cambios seleccionados para la próxima instantánea y los commits ya registrados. GitHub puede alojar el repositorio, pero no es Git mismo.",
        kind="mapa", difficulty="inicio", source="git",
    ),
    c(
        "z17", "git_deploy",
        "¿Qué son configuración, variable de entorno y secreto?",
        "La configuración cambia el comportamiento según el entorno. Una variable de entorno entrega un valor al proceso sin escribirlo en el código. Un secreto es configuración sensible, como una clave, que no debe publicarse en Git.",
        context="El mismo código puede ejecutarse en desarrollo y producción con dominios, bases y credenciales diferentes.",
        code="""
            código compartido + configuración del entorno = proceso configurado

            DJANGO_SECRET_KEY=valor_privado
        """,
        explanation="Separar código de configuración permite desplegar la misma versión en varios entornos. Las variables de entorno son un mecanismo para inyectar valores al arrancar. No vuelven seguro un valor por sí solas: el sistema de deploy debe almacenarlo y limitar su acceso.",
        kind="mapa", difficulty="inicio", source="deploy",
    ),
    c(
        "z18", "drf",
        "Contá de punta a punta qué ocurre en GET /api/posts/7/ usando una frase por capa.",
        "El cliente envía la request; el router elige el ViewSet; autenticación y permissions determinan identidad y acceso; el ORM obtiene el Model desde la base; el serializer arma datos; el ViewSet devuelve una Response HTTP.",
        context="Esta tarjeta cierra el Nivel 0: el objetivo no es conocer cada método, sino poder ubicar cada palabra del Nivel 1 en un recorrido común.",
        code="""
            cliente → router → ViewSet → auth/permission
                              ↓
                         ORM ↔ base de datos
                              ↓
                         serializer → Response → cliente
        """,
        explanation="El recorrido es un mapa de responsabilidades, no una secuencia rígida de todas las líneas internas. Routing selecciona, seguridad controla, ORM persiste, serializer traduce y la view coordina el caso de uso. El Nivel 1 profundiza cada vínculo leyendo código pequeño.",
        kind="integración", difficulty="inicio", source="views",
    ),

    # FUNDAMENTOS DE BACKEND — antes de introducir abstracciones de Django/DRF
    c(
        "b01", "django",
        "¿Qué es un backend y de qué es responsable cuando una app pide información?",
        "Es el software que recibe requests de clientes, aplica reglas y permisos, lee o modifica datos y devuelve responses. El frontend presenta la experiencia; el backend protege y sostiene la verdad del sistema.",
        context="Una aplicación móvil necesita mostrar posts. La pantalla no accede directamente a PostgreSQL: habla con un servicio que controla los datos.",
        code="""
            cliente  ──request──>  backend  ──consulta──>  base de datos
            cliente  <─response──  backend  <─filas─────  base de datos
        """,
        explanation="Un cliente controla su interfaz y puede enviar cualquier cosa, por eso no puede ser la autoridad de las reglas ni de los datos compartidos. El backend es el límite confiable: interpreta la intención, valida quién puede hacerla, coordina persistencia y devuelve un resultado estable para muchos clientes.",
        kind="fundamento", source="django",
    ),
    c(
        "b02", "http_api",
        "¿Qué son una request y una response? Identificá quién inicia cada una.",
        "La request es el mensaje que el cliente envía al servidor para pedir una operación. La response es el mensaje con el que el servidor informa el resultado, mediante status, headers y un body opcional.",
        context="El usuario toca “Ver posts”. Ese gesto local debe convertirse en una conversación por red con el backend.",
        code="""
            REQUEST                       RESPONSE
            GET /api/posts/ HTTP/1.1      HTTP/1.1 200 OK
            Accept: application/json      Content-Type: application/json
                                          [{"id": 1, "titulo": "Hola"}]
        """,
        explanation="En HTTP el cliente siempre inicia el intercambio y el servidor responde a ese mensaje concreto. Separar request de response permite razonar con claridad: qué pidió el cliente, qué información entregó, qué decidió el servidor y cómo comunicó el resultado.",
        kind="fundamento", source="requests",
    ),
    c(
        "b03", "http_api",
        "Desarmá esta request: ¿qué expresa el método, el path, los query params, los headers y el body?",
        "El método expresa la operación, el path identifica el recurso, los query params modifican la consulta, los headers describen el intercambio y el body transporta datos de entrada cuando corresponde.",
        context="Antes de aprender request.data o request.query_params, necesitás reconocer las partes del mensaje HTTP que Django y DRF van a parsear.",
        code="""
            POST /api/posts/?notificar=true HTTP/1.1
            Authorization: Token abc123
            Content-Type: application/json

            {"titulo": "Mi primer post"}
        """,
        explanation="Un framework no inventa estos datos: organiza piezas que ya viajaban en el mensaje HTTP. Cada pieza tiene una responsabilidad diferente; mezclarlas produce APIs confusas, por ejemplo usar el body para identificar una ruta o un query param para enviar una representación completa.",
        kind="fundamento", source="requests",
    ),
    c(
        "b04", "http_api",
        "¿Qué diferencia hay entre una API, un recurso y un endpoint?",
        "La API es el contrato completo para comunicarse con el sistema. Un recurso es una entidad del dominio, como Post. Un endpoint es una combinación concreta de método y URL que permite operar sobre recursos.",
        context="Un mismo backend ofrece varias operaciones y los clientes necesitan saber qué pueden pedir sin conocer su implementación interna.",
        code="""
            API:       contrato de comunicación
            recurso:   Post
            endpoints: GET  /api/posts/
                       POST /api/posts/
                       GET  /api/posts/7/
        """,
        explanation="Una API define una frontera: entradas aceptadas, resultados y errores observables. REST organiza esa frontera alrededor de recursos y usa la semántica de HTTP para operar sobre ellos. El endpoint es la puerta específica; no es toda la API ni el objeto guardado.",
        kind="fundamento", source="requests",
    ),
    c(
        "b05", "django",
        "Seguí una request dentro de Django: ¿qué ocurre desde que llega hasta que sale la response?",
        "Django construye un request, lo atraviesa por middleware, resuelve la URL, ejecuta la view y devuelve la response nuevamente por middleware hacia el servidor web.",
        context="El cliente ya envió GET /api/posts/7/. Ahora seguí únicamente el recorrido dentro de la aplicación Django.",
        code="""
            HTTP request
                ↓
            middleware → URLconf → view → dominio/ORM
                ↓
            HttpResponse → middleware → cliente
        """,
        explanation="Un backend es una cadena de transformaciones con límites claros. El routing elige código, la view coordina el caso de uso y la response vuelve al protocolo. Middleware envuelve el recorrido para responsabilidades transversales como sesión, seguridad o logging.",
        kind="fundamento", source="django",
    ),
    c(
        "b06", "django",
        "¿Qué responsabilidad tiene el URLconf y cuál tiene la view?",
        "El URLconf decide qué view corresponde al path; la view recibe el request, coordina la operación y construye una response. La ruta selecciona, pero no debería contener la lógica del negocio.",
        context="Django debe transformar /posts/7/ en una ejecución concreta sin llenar un único archivo con toda la aplicación.",
        code="""
            # urls.py: selección
            path("posts/<int:pk>/", views.post_detail)

            # views.py: coordinación
            def post_detail(request, pk):
                ...
        """,
        explanation="Primero hay que traducir una dirección externa a código interno; después ese código decide cómo cumplir la operación. Mantener routing y coordinación separados evita que la forma de la URL se convierta en lógica y permite probar o cambiar cada responsabilidad por separado.",
        kind="fundamento", source="urls",
    ),
    c(
        "b07", "modelos",
        "¿Qué representan tabla, fila, columna, primary key y foreign key en una base relacional?",
        "Una tabla agrupa entidades del mismo tipo; una fila es una entidad; una columna es un atributo. La primary key identifica una fila y la foreign key conecta una fila con otra tabla.",
        context="El foro necesita guardar usuarios y posts de forma persistente, incluso cuando el proceso Django se reinicia.",
        code="""
            user                         post
            id (PK) | username           id (PK) | titulo | autor_id (FK)
            3       | ana                7       | Hola   | 3
        """,
        explanation="La memoria del proceso es temporal; la base conserva estado compartido y aplica relaciones. Una identidad estable permite volver a encontrar una fila, y una foreign key representa vínculos sin duplicar todos los datos del objeto relacionado en cada registro.",
        kind="fundamento", source="postgres",
    ),
    c(
        "b08", "orm_db",
        "¿Qué problema resuelve el ORM y cómo se relacionan Model, QuerySet y SQL?",
        "El Model describe datos y comportamiento en Python; el QuerySet describe una consulta; el ORM traduce esa consulta a SQL y convierte las filas resultantes nuevamente en objetos.",
        context="Django necesita consultar PostgreSQL, pero queremos expresar la mayoría de las operaciones usando conceptos del dominio en Python.",
        code="""
            Post.objects.filter(publicado=True)
                       ↓ ORM
            SELECT * FROM post WHERE publicado = true;
        """,
        explanation="PostgreSQL entiende SQL, no clases de Python. El ORM es una capa de traducción que conserva la potencia de la base mientras ofrece una interfaz componible. No elimina SQL: para razonar sobre performance y resultados hay que recordar siempre qué consulta terminará ejecutándose.",
        kind="fundamento", source="queries",
    ),
    c(
        "b09", "serializers",
        "¿Por qué una API necesita un serializer entre el JSON y el Model?",
        "Porque JSON externo y objetos internos tienen contratos distintos. El serializer convierte objetos a datos de salida y, en entrada, parsea, valida y normaliza antes de permitir una escritura.",
        context="El cliente puede enviar strings, campos faltantes o valores maliciosos. El Model no debería recibir directamente un diccionario sin validar.",
        code="""
            JSON no confiable → serializer.is_valid() → validated_data → Model
            Model            → serializer.data      → JSON de respuesta
        """,
        explanation="Cruzar una frontera exige traducir representación y confianza. El serializer define qué campos forman parte del contrato y qué reglas debe cumplir el input. No reemplaza permisos ni base de datos: responde específicamente cómo entran y salen los datos.",
        kind="fundamento", source="serializers",
    ),
    c(
        "b10", "drf",
        "Ubicá router, ViewSet, serializer, permission y ORM dentro de una request de DRF.",
        "El router dirige la URL al ViewSet; autenticación y permissions controlan acceso; el serializer valida o representa; el ORM consulta o persiste; el ViewSet coordina todo y produce la Response.",
        context="Ya conocés las piezas aisladas. Ahora armá el mapa que usarás para leer cualquier endpoint de Django REST Framework.",
        code="""
            router → ViewSet → permission
                         ↓
                    serializer
                         ↓
                      ORM/DB
                         ↓
                     Response
        """,
        explanation="Cada capa contesta una pregunta: a qué código llega, quién puede actuar, qué datos son válidos, cómo se persisten y qué se responde. Un buen junior puede seguir ese recorrido y ubicar un bug en la capa que realmente posee la responsabilidad.",
        kind="fundamento", source="views",
    ),
    c(
        "b11", "django",
        "¿Qué es el objeto request que recibe una view y de dónde sale?",
        "Es la representación en Python que Django construye a partir de la petición HTTP recibida. Organiza método, URL, headers, query params, body, cookies, archivos y datos agregados por capas como user.",
        context="La red entrega bytes y texto HTTP. La view necesita una interfaz práctica para consultar esos datos sin parsear manualmente el protocolo.",
        code="""
            def post_list(request):
                request.method       # "GET", "POST", ...
                request.path         # "/api/posts/"
                request.headers      # Accept, Authorization, ...
                request.GET          # query params en Django
                request.user         # agregado por autenticación
        """,
        explanation="request no es la petición viajando por la red: es el objeto que el framework crea para representarla dentro del programa. Cada atributo conserva una parte del mensaje o información derivada por middleware, parsers y autenticadores antes de llegar a la view.",
        kind="fundamento", source="django",
    ),
    c(
        "b12", "drf",
        "¿Dónde leés un dato que viene en la URL, un query param, el JSON y un header?",
        "Los parámetros del path llegan como argumentos de la view; los query params están en request.query_params; el JSON parseado está en request.data; los headers están en request.headers.",
        context="La API recibe PATCH /posts/7/?notificar=true con un token y un JSON que cambia el título.",
        code="""
            def partial_update(self, request, pk=None):
                pk                         # path: 7
                request.query_params       # notificar=true
                request.data               # {"titulo": "Nuevo"}
                request.headers            # Authorization: Token ...
        """,
        explanation="La ubicación comunica intención. El path identifica el recurso, la query modifica cómo se procesa o busca, el body describe datos de la operación y los headers llevan metadatos del intercambio. DRF conserva esas fuentes separadas para que el contrato sea legible.",
        kind="fundamento", source="requests",
    ),
    c(
        "b13", "http_api",
        "¿Cómo elegís entre GET, POST, PUT, PATCH y DELETE?",
        "GET lee, POST crea o dispara una operación, PUT reemplaza, PATCH modifica parcialmente y DELETE elimina. La elección describe la intención y permite que clientes e infraestructura entiendan la request.",
        context="El mismo recurso Post necesita operaciones distintas. No alcanza con cambiar la URL: el método forma parte del contrato del endpoint.",
        code="""
            GET    /api/posts/       # listar
            POST   /api/posts/       # crear
            PUT    /api/posts/7/     # reemplazar
            PATCH  /api/posts/7/     # modificar parte
            DELETE /api/posts/7/     # eliminar
        """,
        explanation="HTTP separa el objeto sobre el que se actúa de la clase de operación. Usar métodos con semántica consistente permite razonar sobre seguridad, reintentos, cache y respuestas sin inventar un protocolo nuevo para cada endpoint.",
        kind="fundamento", source="requests",
    ),
    c(
        "b14", "http_api",
        "¿Qué debe decidir el backend al construir una response?",
        "Debe elegir un status que describa el resultado, un body con los datos o errores necesarios y headers que expliquen esa representación. No todas las respuestas exitosas necesitan body.",
        context="La view terminó su trabajo. Ahora tiene que comunicar de forma inequívoca si creó, encontró un error de validación o no halló el recurso.",
        code="""
            return Response(
                {"id": 7, "titulo": "Hola"},
                status=201,
                headers={"Location": "/api/posts/7/"},
            )
        """,
        explanation="La response es el único resultado que observa el cliente. El status ofrece una clasificación estándar, el body aporta detalle específico y los headers describen la representación o el intercambio. Si esas piezas se contradicen, el contrato se vuelve ambiguo.",
        kind="fundamento", source="responses",
    ),
    c(
        "b15", "drf",
        "¿Cómo se maneja una petición HTTP dentro de una view sin mezclar todos los pasos?",
        "Primero se identifica la operación, luego autenticación y permisos controlan acceso, el serializer valida la entrada, la lógica usa el ORM y finalmente se construye una Response. Un fallo esperado corta el flujo con un 4xx.",
        context="POST /api/posts/ trae JSON no confiable y pretende crear una fila asociada al usuario autenticado.",
        code="""
            def create(self, request):
                serializer = PostSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                post = serializer.save(autor=request.user)
                return Response(PostSerializer(post).data, status=201)
        """,
        explanation="Manejar una request significa convertir input externo en una transición válida del sistema. El orden importa: no se escribe antes de validar ni se confía en identidad enviada por el cliente. Cada capa reduce incertidumbre hasta producir un resultado seguro.",
        kind="fundamento", source="views",
    ),
    c(
        "b16", "http_api",
        "¿Cuál es la diferencia entre un error esperado 4xx y un fallo interno 5xx?",
        "Un 4xx comunica que la request no puede completarse por sus datos, identidad, permisos o recurso. Un 5xx indica que el servidor no pudo cumplir una request que no debería haber fallado de esa manera.",
        context="La API debe distinguir un título vacío, un usuario sin permiso, un post inexistente y una excepción inesperada al consultar la base.",
        code="""
            400  input inválido
            401  sin autenticación válida
            403  sin autorización
            404  recurso inexistente
            500  fallo inesperado del servidor
        """,
        explanation="No todo fallo es un bug y no todo error debe ocultarse como 500. Los 4xx forman parte del contrato y permiten al cliente corregir o detenerse. Los 5xx señalan una incapacidad del servidor y deben producir observabilidad para investigar la causa.",
        kind="fundamento", source="status",
    ),

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
    c("d08", "drf", "¿Qué es self.get_object(), qué pasos ejecuta y por qué puede devolver 404?", "Es el método del ViewSet que busca la instancia indicada por la URL dentro de get_queryset. Aplica lookup_field, convierte la ausencia en 404 y ejecuta los permisos de objeto.", code='post = self.get_object()', kind="decisión", difficulty="media", source="views"),
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
    c(
        "e21",
        "entrevista",
        "El proveedor reintenta el mismo webhook y se crean dos pedidos. ¿Qué cambiarías para que procesarlo dos veces produzca un solo resultado?",
        "Usaría el event_id como clave idempotente, con una UniqueConstraint en la base. Dentro de transaction.atomic intentaría registrar el evento y crearía el pedido una sola vez; un duplicado devolvería éxito sin repetir el efecto.",
        context="Una tienda recibe webhooks de pago. Si el proveedor no obtiene respuesta rápido, vuelve a enviar exactamente el mismo evento con el mismo event_id.",
        code="""
            def pago_confirmado(request):
                pedido = Pedido.objects.create(
                    compra_id=request.data["compra_id"],
                    estado="pagado",
                )
                enviar_email(pedido)
                return Response(status=200)
        """,
        answer_code="""
            class EventoProcesado(models.Model):
                event_id = models.CharField(max_length=100, unique=True)

            with transaction.atomic():
                evento, creado = EventoProcesado.objects.get_or_create(
                    event_id=request.data["event_id"]
                )
                if creado:
                    procesar_pago(request.data)
        """,
        explanation="Una red no garantiza que cada mensaje llegue exactamente una vez: una respuesta puede perderse aunque el servidor haya terminado el trabajo. Por eso el consumidor debe reconocer la identidad de la operación y guardar esa identidad junto con el efecto. La unicidad en base convierte 'este evento ya fue procesado' en una garantía compartida por todos los workers.",
        kind="mini caso",
        difficulty="media",
        source="transactions",
    ),
    c(
        "e22",
        "entrevista",
        "La respuesta es correcta, pero pasó de 25 a 126 queries al aumentar el tamaño de página. ¿Dónde nace el crecimiento y cómo lo corregirías?",
        "Hay una query inicial, una por autor y una por count de comentarios para cada post: 1 + 2N. Cargaría autor con select_related y anotaría la cantidad de comentarios con Count en el queryset.",
        context="El feed funcionaba bien con 12 posts. Producto subió PAGE_SIZE a 50 y la latencia aumentó aunque el JSON no cambió.",
        code="""
            class PostSerializer(serializers.ModelSerializer):
                autor = serializers.CharField(source="autor.username")
                comentarios = serializers.SerializerMethodField()

                def get_comentarios(self, post):
                    return post.comentarios.count()

            queryset = Post.objects.all()
        """,
        answer_code="""
            queryset = (
                Post.objects
                .select_related("autor")
                .annotate(num_comentarios=Count("comentarios"))
            )

            num_comentarios = serializers.IntegerField(read_only=True)
        """,
        explanation="La señal importante no es solo que haya muchas queries, sino que su cantidad crezca con cada fila devuelta. Cuando el costo es 1 + 2N, duplicar la página casi duplica los viajes a la base. La corrección mueve el trabajo desde accesos individuales del serializer hacia una consulta que carga y agrega los datos del conjunto completo.",
        kind="mini caso",
        difficulty="media",
        source="optimization",
    ),
    c(
        "e23",
        "entrevista",
        "Un usuario ve borradores ajenos en el listado, aunque IsOwnerOrReadOnly funciona al editar. ¿Dónde corregís la filtración?",
        "En get_queryset. El listado debe seleccionar posts publicados más los borradores del usuario actual; el permiso de objeto sigue protegiendo las operaciones sobre un post concreto.",
        context="En el foro cualquiera puede leer posts publicados. Un borrador solo debe ser visible para su autor, pero GET /api/posts/ devuelve Post.objects.all().",
        code="""
            class PostViewSet(ModelViewSet):
                queryset = Post.objects.all()
                permission_classes = [IsOwnerOrReadOnly]
        """,
        answer_code="""
            def get_queryset(self):
                if self.request.user.is_authenticated:
                    return Post.objects.filter(
                        Q(publicado=True) | Q(autor=self.request.user)
                    )
                return Post.objects.filter(publicado=True)
        """,
        explanation="Un permiso de objeto decide si una acción puede ejecutarse sobre una instancia que ya fue seleccionada. Un listado empieza un paso antes: debe decidir qué filas entran en el universo visible. Si el queryset incluye un borrador ajeno, DRF no aplica has_object_permission fila por fila para quitarlo.",
        kind="mini caso",
        difficulty="media",
        source="permissions",
    ),
    c(
        "e24",
        "entrevista",
        "Necesitás agregar estado como NOT NULL sin bloquear una tabla grande. ¿En qué etapas harías el cambio?",
        "Primero agregaría el campo nullable, desplegaría código compatible, completaría los datos en lotes y recién después agregaría el default o la constraint NOT NULL. Al final retiraría la compatibilidad temporal.",
        context="Post tiene dos millones de filas y recibe escrituras todo el día. La aplicación nueva necesita estado='borrador' para los registros existentes.",
        code="""
            class Post(models.Model):
                estado = models.CharField(
                    max_length=20,
                    null=False,
                    default="borrador",
                )
        """,
        answer_code="""
            # 1. Expandir: campo nullable
            # 2. Desplegar código compatible
            # 3. Backfill en lotes
            # 4. Validar y agregar NOT NULL
            # 5. Limpiar compatibilidad temporal
        """,
        explanation="Un deploy no cambia código, procesos y esquema en el mismo instante. La estrategia segura conserva válidos tanto el código viejo como el nuevo durante la transición. Separar estructura, movimiento de datos y restricción evita convertir una única migración larga en el punto de fallo de todo el sistema.",
        kind="mini caso",
        difficulty="alta",
        source="migrations",
    ),
    c(
        "e25",
        "entrevista",
        "El cliente recibió el email de confirmación, pero el pedido no existe. ¿Cómo evitás ese estado imposible?",
        "Programaría el envío con transaction.on_commit para que ocurra únicamente después de confirmar la transacción. Si la actualización de stock falla y hay rollback, el callback no se ejecuta.",
        context="Crear el pedido y descontar stock están dentro de atomic. El email se envía antes de actualizar stock, y esa segunda escritura a veces falla.",
        code="""
            with transaction.atomic():
                pedido = Pedido.objects.create(usuario=request.user)
                enviar_confirmacion(pedido.id)
                descontar_stock(items)  # puede lanzar una excepción
        """,
        answer_code="""
            with transaction.atomic():
                pedido = Pedido.objects.create(usuario=request.user)
                descontar_stock(items)
                transaction.on_commit(
                    lambda: enviar_confirmacion(pedido.id)
                )
        """,
        explanation="La base puede revertir sus propias escrituras, pero no puede des-enviar un email ni deshacer una llamada HTTP. Los efectos externos deben cruzar el límite solo cuando el estado que describen ya es durable. on_commit conecta esos dos momentos sin mentirle al usuario.",
        kind="mini caso",
        difficulty="media",
        source="transactions",
    ),
    c(
        "e26",
        "entrevista",
        "Al pasar de la página 1 a la 2 aparecen posts repetidos y faltan otros. ¿Qué propiedad le falta a la consulta?",
        "Le falta un orden total y estable. Ordenaría por creado_en y agregaría pk como desempate determinista; si el feed cambia con mucha frecuencia, evaluaría cursor pagination.",
        context="Muchos posts comparten el mismo creado_en porque fueron importados juntos. La API pagina de a 20 usando offset.",
        code="""
            queryset = Post.objects.order_by("-creado_en")
            # ?page=1, luego ?page=2
        """,
        answer_code="""
            queryset = Post.objects.order_by("-creado_en", "-pk")
        """,
        explanation="Paginar significa cortar una secuencia en fronteras. Si varias filas empatan y no existe una regla final de desempate, la base puede devolverlas en distinto orden entre requests. Agregar una clave única convierte el orden parcial en un orden total reproducible.",
        kind="mini caso",
        difficulty="media",
        source="pagination",
    ),
    c(
        "e27",
        "entrevista",
        "Un usuario logra que el servidor consulte http://169.254.169.254. ¿Qué vulnerabilidad es y dónde pondrías la defensa?",
        "Es SSRF. No permitiría que una URL arbitraria controle el destino: usaría una allowlist de hosts y esquemas, resolvería y bloquearía IPs privadas o de metadata, limitaría redirects, tamaño y timeout, y aislaría la salida de red.",
        context="La API permite importar una imagen desde avatar_url. El backend descarga la dirección recibida para guardarla en su propio storage.",
        code="""
            avatar_url = request.data["avatar_url"]
            response = requests.get(avatar_url, timeout=5)
            guardar_avatar(response.content)
        """,
        answer_code="""
            # Validar esquema y host contra una allowlist.
            # Resolver DNS y rechazar rangos privados/metadata.
            # Limitar redirects, timeout y tamaño de respuesta.
        """,
        explanation="Desde la perspectiva de la red, la request la hace el servidor y hereda su acceso a servicios internos. Validar que el texto parezca una URL no alcanza: la garantía necesaria es que el destino efectivo, incluso después de DNS y redirects, pertenezca al conjunto explícitamente permitido.",
        kind="mini caso",
        difficulty="alta",
        source="security",
    ),
    c(
        "e28",
        "entrevista",
        "Los tests pasan, pero bajo carga se pierden visitas. ¿Qué operación está compitiendo y cómo la volvés atómica?",
        "Dos workers leen el mismo valor y luego guardan el mismo incremento. Haría el cálculo en la base con update(visitas=F('visitas') + 1), evitando separar lectura y escritura.",
        context="Cada request al detalle de un post incrementa visitas. Con una sola request funciona; con varias simultáneas el contador termina por debajo del total real.",
        code="""
            post = Post.objects.get(pk=pk)
            post.visitas += 1
            post.save(update_fields=["visitas"])
        """,
        answer_code="""
            Post.objects.filter(pk=pk).update(
                visitas=F("visitas") + 1
            )
        """,
        explanation="El bug vive en el espacio entre leer y escribir. Si dos procesos leen 10, ambos calculan 11 y uno pisa al otro. Una expresión F envía la regla 'sumá uno al valor actual' a la base, donde cada UPDATE opera sobre el último valor confirmado.",
        kind="mini caso",
        difficulty="media",
        source="queries",
    ),
    c(
        "e29",
        "entrevista",
        "El tercer ítem es inválido, pero el pedido y los dos primeros quedaron guardados. ¿Cómo hacés que la operación sea todo o nada?",
        "Validaría la estructura completa antes de escribir y envolvería la creación del pedido y sus ítems en transaction.atomic. Cualquier ValidationError debe salir del bloque para provocar rollback.",
        context="POST /pedidos/ crea una cabecera y luego recorre los ítems enviados. Cada create se confirma aunque uno posterior falle.",
        code="""
            pedido = Pedido.objects.create(usuario=request.user)
            for data in request.data["items"]:
                ItemPedido.objects.create(pedido=pedido, **data)
        """,
        answer_code="""
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                pedido = Pedido.objects.create(usuario=request.user)
                ItemPedido.objects.bulk_create([
                    ItemPedido(pedido=pedido, **item)
                    for item in serializer.validated_data["items"]
                ])
        """,
        explanation="El pedido y sus ítems representan una sola transición del dominio: o existe el conjunto válido o no existe nada. Validar primero reduce fallos previsibles y la transacción convierte todas las escrituras en una unidad que la base confirma o revierte junta.",
        kind="mini caso",
        difficulty="media",
        source="transactions",
    ),
    c(
        "e30",
        "entrevista",
        "Intentaste optimizar con only(), pero ahora el endpoint hace más queries. ¿Por qué y qué medirías antes de conservarlo?",
        "only difiere los campos no incluidos. Si el serializer accede a contenido o autor, Django los consulta después y puede crear N+1. Incluiría los campos realmente usados y select_related para autor, verificándolo con el número de queries.",
        context="El listado serializa id, titulo, contenido y autor.username. El queryset fue reducido para traer supuestamente menos datos.",
        code="""
            queryset = Post.objects.only("id", "titulo")
        """,
        answer_code="""
            queryset = (
                Post.objects
                .select_related("autor")
                .only("id", "titulo", "contenido", "autor__username")
            )
        """,
        explanation="Un campo diferido no desaparece: su costo se posterga hasta el primer acceso. Si ese acceso ocurre para cada objeto, ahorrar bytes en la consulta inicial agrega viajes individuales a la base. La optimización correcta parte del patrón real de lectura del consumidor.",
        kind="mini caso",
        difficulty="media",
        source="optimization",
    ),
    c(
        "e31",
        "entrevista",
        "La auditoría dejó de registrar posts cuando se cambió create() por bulk_create(). ¿Qué supuesto se rompió?",
        "bulk_create no llama save() por instancia ni emite normalmente las señales pre_save/post_save. Movería la regla crítica a una operación de servicio explícita o crearía los registros de auditoría dentro del mismo flujo y transacción.",
        context="Post.save() o una señal post_save crea RegistroAuditoria. Una importación masiva usa bulk_create para mejorar rendimiento.",
        code="""
            Post.objects.bulk_create([
                Post(titulo=row["titulo"]) for row in filas
            ])
        """,
        answer_code="""
            with transaction.atomic():
                posts = Post.objects.bulk_create(posts_pendientes)
                RegistroAuditoria.objects.bulk_create([
                    RegistroAuditoria(post=post, accion="importado")
                    for post in posts
                ])
        """,
        explanation="Las operaciones bulk optimizan precisamente al evitar el ciclo de vida individual de cada modelo. Una regla de negocio que depende de un efecto implícito en save o en una señal deja de ser universal. Las invariantes críticas deben formar parte explícita de la operación que escribe los datos.",
        kind="mini caso",
        difficulty="media",
        source="models",
    ),
    c(
        "e32",
        "entrevista",
        "Una custom action permite archivar posts ajenos. ¿Qué parte del flujo de DRF fue salteada?",
        "Post.objects.get evita get_queryset, el manejo de 404 y el chequeo de permisos de objeto del ViewSet. Usaría self.get_object() y mantendría IsOwner o el permiso correspondiente.",
        context="El ViewSet tiene IsAuthenticated y un permiso de ownership. retrieve y update funcionan bien; solo falla la action archivar.",
        code="""
            @action(detail=True, methods=["post"])
            def archivar(self, request, pk=None):
                post = Post.objects.get(pk=pk)
                post.archivado = True
                post.save()
        """,
        answer_code="""
            @action(detail=True, methods=["post"])
            def archivar(self, request, pk=None):
                post = self.get_object()
                post.archivado = True
                post.save(update_fields=["archivado"])
                return Response(status=204)
        """,
        explanation="La seguridad no está en el nombre del ViewSet sino en el camino que recorre cada objeto. self.get_object compone selección, búsqueda y autorización; consultar el manager directamente crea un camino alternativo que no hereda esas garantías.",
        kind="mini caso",
        difficulty="media",
        source="views",
    ),
    c(
        "e33",
        "entrevista",
        "Dos editores abren el mismo post y el último PATCH pisa cambios del primero. ¿Cómo detectarías una edición basada en datos viejos?",
        "Agregaría una versión o usaría updated_at como token de concurrencia. El cliente envía la versión leída y el UPDATE exige que siga siendo la actual; si no coincide, respondería 409 o 412 para que recargue y resuelva el conflicto.",
        context="Ana y Luis cargan la versión 7. Ana guarda y crea la versión 8; Luis envía después cambios calculados sobre la versión 7.",
        code="""
            post.titulo = request.data["titulo"]
            post.save(update_fields=["titulo"])
        """,
        answer_code="""
            updated = Post.objects.filter(
                pk=pk,
                version=request.data["version"],
            ).update(
                titulo=request.data["titulo"],
                version=F("version") + 1,
            )
            if not updated:
                return Response(status=409)
        """,
        explanation="El problema no es que dos usuarios escriban, sino que uno decide usando un estado que ya dejó de existir. La versión hace visible esa precondición y el UPDATE condicional une comprobación y escritura en una sola operación atómica.",
        kind="mini caso",
        difficulty="alta",
        source="transactions",
    ),
    c(
        "e34",
        "entrevista",
        "Generar el reporte demora un minuto y el proxy corta la request. ¿Qué contrato HTTP propondrías?",
        "Crearía un trabajo en background, respondería 202 Accepted con un job_id y expondría un recurso para consultar estado y resultado. La creación del trabajo debería ser idempotente si el cliente puede reintentar.",
        context="POST /reportes/ arma un PDF grande de forma sincrónica. El cliente no necesita recibir el archivo en la misma conexión.",
        code="""
            def crear_reporte(request):
                archivo = generar_pdf(request.user)
                return FileResponse(archivo)
        """,
        answer_code="""
            trabajo = crear_trabajo_reporte(request.user)
            encolar_reporte(trabajo.id)
            return Response(
                {"job_id": trabajo.id, "status": "pendiente"},
                status=202,
            )
        """,
        explanation="Una request HTTP tiene una ventana de tiempo limitada; un trabajo puede durar mucho más. Separar aceptación de finalización convierte la tarea en un recurso durable que puede observarse, reintentarse y fallar sin mantener una conexión abierta.",
        kind="mini caso",
        difficulty="media",
        source="responses",
    ),
    c(
        "e35",
        "entrevista",
        "Un atacante prueba miles de contraseñas válidas contra una misma cuenta. ¿Por qué IsAuthenticated no ayuda y qué controles sumarías?",
        "El login ocurre antes de estar autenticado. Aplicaría throttling por IP y por identidad objetivo, demoras o bloqueos progresivos, monitoreo y MFA; cuidaría no crear un mecanismo fácil de denegación de servicio contra una cuenta.",
        context="POST /login/ no tiene límites. Las credenciales incorrectas responden rápido y el atacante distribuye requests entre varias IPs.",
        code="""
            user = authenticate(
                username=request.data["username"],
                password=request.data["password"],
            )
        """,
        answer_code="""
            # Combinar límites por IP y por cuenta.
            # Registrar intentos y aplicar backoff progresivo.
            # Alertar y ofrecer MFA para cuentas sensibles.
        """,
        explanation="Autenticación comprueba una credencial, pero no limita cuántas veces puede intentarse. Cada intento entrega información y consume capacidad. La defensa reduce la velocidad y el valor de probar combinaciones, sin confiar en una sola identidad de red que el atacante puede cambiar.",
        kind="mini caso",
        difficulty="media",
        source="security",
    ),
    c(
        "e36",
        "entrevista",
        "Un archivo llamado foto.jpg agota memoria y contiene HTML ejecutable. ¿Qué debe validar el backend además de la extensión?",
        "Limitaría tamaño antes y durante la lectura, detectaría el tipo real del contenido, generaría un nombre propio, almacenaría fuera del árbol ejecutable y serviría con Content-Type y Content-Disposition seguros. Para imágenes, decodificaría y reescribiría el archivo.",
        context="El endpoint de avatar acepta cualquier UploadedFile y conserva el nombre y Content-Type enviados por el cliente.",
        code="""
            avatar = request.FILES["avatar"]
            user.avatar.save(avatar.name, avatar)
        """,
        answer_code="""
            # Límite de bytes y dimensiones.
            # Verificar contenido real, no solo nombre/MIME declarado.
            # Renombrar, aislar el storage y servir sin ejecución inline.
        """,
        explanation="Nombre, extensión y MIME son afirmaciones del atacante. La garantía necesaria se refiere a los bytes reales y a cómo serán interpretados después. Validar recursos, normalizar el contenido y aislar su entrega evita que una carga se convierta en consumo ilimitado o código activo.",
        kind="mini caso",
        difficulty="media",
        source="security",
    ),
    c(
        "e37",
        "entrevista",
        "El cache muestra el panel de Ana cuando entra Bruno. ¿Qué dato faltó representar en la clave?",
        "La respuesta depende del usuario, pero la clave solo depende de la ruta. Incluiría la identidad y cualquier otro input que cambie la representación, o cachearía únicamente datos públicos y compondría lo privado fuera del cache compartido.",
        context="GET /dashboard/ se cachea por path durante cinco minutos. El HTML incluye nombre, métricas y notificaciones del usuario autenticado.",
        code="""
            key = f"page:{request.path}"
            cache.set(key, render_dashboard(request.user), 300)
        """,
        answer_code="""
            key = f"dashboard:user:{request.user.pk}:v1"
            # O no almacenar respuestas privadas en un cache compartido.
        """,
        explanation="Una clave de cache debe identificar todos los inputs que determinan el valor. Si dos requests distintas colisionan en la misma clave, el cache afirma falsamente que sus respuestas son equivalentes. Con datos privados, ese error de identidad se convierte además en una filtración.",
        kind="mini caso",
        difficulty="alta",
        source="security",
    ),
    c(
        "e38",
        "entrevista",
        "El worker recibe un pedido que todavía no puede consultar. ¿Por qué ocurre aunque create() se ejecutó antes de encolar?",
        "El pedido existe solo dentro de una transacción aún no confirmada. Encolaría la tarea con transaction.on_commit para publicarla después del commit; además haría la tarea idempotente porque una cola puede reentregarla.",
        context="La API crea un pedido dentro de atomic y publica inmediatamente su ID en una cola. El worker usa otra conexión a la base.",
        code="""
            with transaction.atomic():
                pedido = Pedido.objects.create(usuario=request.user)
                procesar_pedido.delay(pedido.id)
        """,
        answer_code="""
            with transaction.atomic():
                pedido = Pedido.objects.create(usuario=request.user)
                transaction.on_commit(
                    lambda: procesar_pedido.delay(pedido.id)
                )
        """,
        explanation="Las conexiones no ven normalmente escrituras no confirmadas de otra transacción. Publicar el mensaje antes del commit permite que el mundo externo observe una referencia que todavía no es durable y que incluso podría desaparecer por rollback. on_commit alinea ambos límites.",
        kind="mini caso",
        difficulty="media",
        source="transactions",
    ),
    c(
        "e39",
        "entrevista",
        "Dos transferencias opuestas quedan en deadlock. ¿Qué cambiarías además de usar atomic?",
        "Bloquearía siempre las cuentas en un orden determinista, por ejemplo por pk, para que todas las transacciones adquieran locks en la misma secuencia. También manejaría el deadlock con un reintento acotado de la transacción completa.",
        context="Una transferencia de A hacia B bloquea A y luego B; al mismo tiempo otra de B hacia A bloquea B y luego A.",
        code="""
            with transaction.atomic():
                origen = Cuenta.objects.select_for_update().get(pk=origen_id)
                destino = Cuenta.objects.select_for_update().get(pk=destino_id)
        """,
        answer_code="""
            ids = sorted([origen_id, destino_id])
            cuentas = {
                c.pk: c for c in Cuenta.objects
                .select_for_update()
                .filter(pk__in=ids)
                .order_by("pk")
            }
        """,
        explanation="Un deadlock aparece cuando cada transacción posee un recurso que la otra necesita y ambas esperan. atomic garantiza rollback, pero no elimina ese ciclo. Un orden global de adquisición hace imposible la espera circular; el reintento cubre conflictos residuales que la base detecte.",
        kind="mini caso",
        difficulty="alta",
        source="transactions",
    ),
    c(
        "e40",
        "entrevista",
        "Agregaste un índice a publicado y la consulta sigue haciendo sequential scan. ¿Por qué puede ser una decisión correcta del planner?",
        "Si casi todas las filas tienen publicado=True, el índice no descarta suficiente información y leerlo más visitar la tabla cuesta más que recorrerla. Evaluaría un índice parcial o compuesto alineado con el filtro y el orden reales.",
        context="El 97% de los posts está publicado. El feed filtra publicado=True y ordena por creado_en descendente con límite 20.",
        code="""
            Post.objects.filter(publicado=True).order_by("-creado_en")[:20]
            # índice actual: (publicado)
        """,
        answer_code="""
            models.Index(
                fields=["-creado_en"],
                condition=Q(publicado=True),
                name="posts_publicados_recientes",
            )
        """,
        explanation="Un índice es útil cuando reduce trabajo, no por existir. Un booleano tiene muy pocos valores y puede seleccionar casi toda la tabla. El diseño debe seguir la consulta completa: qué filas se excluyen, en qué orden se necesitan y cuántas se leen realmente.",
        kind="mini caso",
        difficulty="alta",
        source="postgres",
    ),
    c(
        "e41",
        "entrevista",
        "get_or_create devolvió dos suscripciones iguales bajo concurrencia. ¿Qué condición faltaba para que fuera una garantía?",
        "Faltaba una restricción única sobre usuario y newsletter. get_or_create ayuda al flujo, pero solo la base puede arbitrar entre workers; agregaría UniqueConstraint y manejaría un posible IntegrityError.",
        context="La app corre con varios workers. El modelo permite repetir el mismo par usuario-newsletter y dos requests llegan casi juntas.",
        code="""
            Suscripcion.objects.get_or_create(
                usuario=user,
                newsletter=newsletter,
            )
        """,
        answer_code="""
            models.UniqueConstraint(
                fields=["usuario", "newsletter"],
                name="suscripcion_unica",
            )
        """,
        explanation="Buscar y crear siguen siendo decisiones separadas desde la perspectiva de dos procesos. Ambos pueden observar ausencia. get_or_create puede apoyarse en el conflicto de unicidad, pero si el esquema permite duplicados no existe un árbitro compartido que declare ganador a uno solo.",
        kind="mini caso",
        difficulty="media",
        source="models",
    ),
    c(
        "e42",
        "entrevista",
        "Capturaste IntegrityError dentro de atomic y la siguiente query falla con TransactionManagementError. ¿Dónde debe vivir el try/except?",
        "El IntegrityError debe salir del bloque atomic que quedó roto. Lo capturaría por fuera, o usaría un atomic interno como savepoint y atraparía la excepción después de salir de ese bloque.",
        context="La función intenta crear un username y, si ya existe, quiere continuar consultando alternativas dentro de la transacción principal.",
        code="""
            with transaction.atomic():
                try:
                    User.objects.create(username=username)
                except IntegrityError:
                    pass
                User.objects.exists()  # falla
        """,
        answer_code="""
            with transaction.atomic():
                try:
                    with transaction.atomic():
                        User.objects.create(username=username)
                except IntegrityError:
                    manejar_duplicado()
                User.objects.exists()
        """,
        explanation="Una excepción de base puede dejar la transacción actual marcada para rollback porque su estado ya no es confiable. Ocultarla dentro del mismo límite no repara ese estado. Un savepoint crea un límite menor que puede revertirse antes de continuar con la transacción exterior.",
        kind="mini caso",
        difficulty="alta",
        source="transactions",
    ),
    c(
        "e43",
        "entrevista",
        "La API externa no responde y todos los workers quedan ocupados. ¿Qué faltó definir en la llamada?",
        "Faltó un timeout explícito. Definiría límites de conexión y lectura, manejaría el error, y solo reintentaría con backoff y jitter cuando la operación sea segura o idempotente.",
        context="Cada request consulta un proveedor de cotizaciones. requests.get usa sus valores por defecto y el endpoint web espera la respuesta.",
        code="""
            response = requests.get(PROVEEDOR_URL)
            response.raise_for_status()
        """,
        answer_code="""
            response = requests.get(
                PROVEEDOR_URL,
                timeout=(2, 5),
            )
            response.raise_for_status()
        """,
        explanation="Un recurso compartido necesita un tiempo máximo de ocupación. Sin timeout, una dependencia lenta puede retener todos los workers y convertir un fallo parcial en caída total. Reintentar también consume capacidad, por eso requiere límites y una operación que tolere repetición.",
        kind="mini caso",
        difficulty="media",
        source="testing",
    ),
    c(
        "e44",
        "entrevista",
        "Un test de expiración falla solo cerca del cambio de segundo. ¿Cómo eliminarías la dependencia del instante exacto?",
        "Congelaría o inyectaría el reloj y compararía contra un now controlado. También probaría explícitamente los bordes: justo antes, exactamente al vencer y justo después.",
        context="El código llama timezone.now() varias veces y el test crea un token con expiración de un segundo.",
        code="""
            token.expira_en = timezone.now() + timedelta(seconds=1)
            self.assertFalse(token.expirado())
        """,
        answer_code="""
            instante = timezone.now()
            token.expira_en = instante + timedelta(seconds=1)
            self.assertFalse(token.expirado(ahora=instante))
            self.assertTrue(token.expirado(ahora=token.expira_en))
        """,
        explanation="Un test determinista controla todos los inputs, y el tiempo también es un input. Si cada llamada observa un instante distinto, el resultado depende de la velocidad del entorno. Inyectar el reloj transforma el paso del tiempo en datos reproducibles y hace visibles las reglas de borde.",
        kind="mini caso",
        difficulty="media",
        source="django_testing",
    ),
    c(
        "e45",
        "entrevista",
        "La nueva versión elimina autor_nombre y rompe una app móvil todavía instalada. ¿Cómo evolucionarías el contrato?",
        "Mantendría autor_nombre durante una ventana de deprecación y agregaría el nuevo campo de forma aditiva. Mediría su uso, comunicaría el retiro y solo lo eliminaría en una versión incompatible explícita.",
        context="El backend quiere reemplazar autor_nombre por un objeto autor. No todos los clientes móviles se actualizan al mismo tiempo.",
        code="""
            # antes
            {"id": 7, "autor_nombre": "Ana"}

            # nuevo
            {"id": 7, "autor": {"id": 3, "nombre": "Ana"}}
        """,
        answer_code="""
            {
                "id": 7,
                "autor_nombre": "Ana",  # temporalmente compatible
                "autor": {"id": 3, "nombre": "Ana"},
            }
        """,
        explanation="El contrato vive en todos sus consumidores, no solo en el servidor. Un cambio destructivo exige que todos migren en el mismo instante, algo que no se controla en clientes distribuidos. Expandir primero permite que versiones viejas y nuevas convivan durante la transición.",
        kind="mini caso",
        difficulty="media",
        source="responses",
    ),
    c(
        "e46",
        "entrevista",
        "Una caída breve de la base hace que el orquestador reinicie todas las instancias en bucle. ¿Qué mezcló el health check?",
        "Mezcló liveness con readiness. Liveness debería indicar si el proceso puede seguir ejecutándose; readiness puede quitarlo del tráfico cuando la base no está disponible sin forzar un reinicio constante.",
        context="El único /health/ consulta PostgreSQL. Si falla una vez devuelve 500 y la plataforma mata inmediatamente el proceso.",
        code="""
            def health(request):
                connection.ensure_connection()
                return JsonResponse({"ok": True})
        """,
        answer_code="""
            # /live/  -> el proceso responde; no depende de PostgreSQL
            # /ready/ -> comprueba dependencias necesarias para recibir tráfico
        """,
        explanation="Reiniciar solo ayuda cuando el proceso está roto; no repara una dependencia externa caída. Liveness responde si reiniciar tiene sentido. Readiness responde si esta instancia puede atender ahora. Separarlas evita amplificar un fallo transitorio mediante reinicios coordinados.",
        kind="mini caso",
        difficulty="media",
        source="deploy",
    ),
    c(
        "e47",
        "entrevista",
        "Necesitás investigar un 500, pero el log actual guarda tokens y contraseñas. ¿Qué registrarías para conservar trazabilidad sin secretos?",
        "Usaría logs estructurados con request_id, ruta, método, status, duración, user_id y tipo de error. Redactaría Authorization, cookies, passwords y cuerpos sensibles; el traceback quedaría restringido al entorno seguro.",
        context="El equipo registra request.headers y request.data completos para poder reproducir errores de producción.",
        code="""
            logger.exception(
                "request failed headers=%s body=%s",
                request.headers,
                request.data,
            )
        """,
        answer_code="""
            logger.exception("request_failed", extra={
                "request_id": request.id,
                "path": request.path,
                "method": request.method,
                "user_id": request.user.pk,
            })
        """,
        explanation="Observabilidad y confidencialidad no son objetivos opuestos: se necesita identificar la operación y su fallo, no copiar todas sus entradas. Los secretos en logs multiplican su exposición, retención y acceso; los identificadores permiten correlacionar eventos sin almacenar credenciales.",
        kind="mini caso",
        difficulty="media",
        source="security",
    ),
    c(
        "e48",
        "entrevista",
        "Exportar un millón de filas consume toda la memoria aunque el QuerySet sea lazy. ¿Qué está materializando el proceso?",
        "list fuerza a cargar todo el QuerySet y construir todas las filas antes de responder. Iteraría por chunks con iterator y produciría una respuesta streaming, evitando además relaciones que disparen queries por fila.",
        context="Un endpoint exporta posts a CSV. Funciona con pocos datos, pero el worker muere cuando la tabla crece.",
        code="""
            posts = list(Post.objects.all())
            rows = [serializar_csv(post) for post in posts]
            return HttpResponse("".join(rows))
        """,
        answer_code="""
            def filas():
                yield "id,titulo\\n"
                for post in Post.objects.iterator(chunk_size=2000):
                    yield serializar_csv(post)

            return StreamingHttpResponse(filas(), content_type="text/csv")
        """,
        explanation="Lazy significa que la consulta espera hasta ser consumida, no que su resultado ocupe memoria constante. list y la comprensión materializan toda la colección. El streaming conserva solo una ventana pequeña de datos y entrega cada parte antes de producir la siguiente.",
        kind="mini caso",
        difficulty="media",
        source="optimization",
    ),

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


PREREQUISITES = {
    "d08": ["o01", "d12", "p04"],
    "e01": ["d01", "s01", "p04"],
    "e11": ["o16", "o17"],
    "e14": ["d08"],
}

_level_zero_order = {card_id: index for index, card_id in enumerate(LEVEL_ZERO_SEQUENCE)}
_foundation_order = {card_id: index for index, card_id in enumerate(FOUNDATION_SEQUENCE)}
_level_positions = {level["id"]: 0 for level in CURRICULUM_LEVELS}

for _catalog_index, _card in enumerate(CARDS):
    if _card["id"] in _level_zero_order:
        _level = 0
        _sequence = _level_zero_order[_card["id"]]
    elif _card["id"] in _foundation_order:
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

del _catalog_index, _card, _level, _sequence, _level_info
