# "Sistema Digital de Pedidos en Linea-con Stock para keylupets"

## :feet: "INTRODUCCIÓN"
Los inventarios no son solo "pilas de cosas" guardadas en un rincón; son dinero en forma de mercancía. En el mundo del software y los negocios, un inventario es el puente entre lo que compras y lo que vende. Algunas empresas o microempresas, emprendedores entre otros, no tienen un sistema de inventario y esto hace que tengan dificultades incluso en ocasiones problemas; porque no saben lo que ingresa o lo que tienen dentro de la empresa.  

También en la era digital actual, las empresas que limitan sus ventas únicamente al mostrador físico pierden una gran cuota del mercado. Lo que queremos lograr con este proyecto es que cuenten con un sistema garantizado y con efectividad y eficacia para que lleven un control de calidad interno, y que al mismo tiempo expanda sus fronteras comerciales mediante un carrito de compras en línea, permitiendo a los clientes comprar desde la comodidad de sus casas. 

 

El presente proyecto propone el desarrollo de un sistema digital de pedidos en línea para KeyluPets, que permita a los clientes realizar solicitudes de productos de manera sencilla, mientras que el sistema administrativo actualiza automáticamente el inventario con cada venta registrada. De esta forma, se garantiza un mejor control del stock, evitando inconsistencias y facilitando la toma de decisiones. 

## **Sistema de Gestión de Inventario para Keylupets**


Keylupets es una tienda ubicada en Soacha, Porvenir, dedicada a la venta de comida para perros y gatos, juguetes y accesorios para mascotas. También ofrece servicio de domicilios cercanos a la tienda.
Actualmente el control de productos se realiza de forma manual, lo que puede generar errores en el conteo, pérdida de información o desorganización en el inventario.
Aquí va una justificación rápida del proyecto:


## **Justificación**

KeyluPets es una tienda de mascotas ubicada en Soacha, Porvenir, que actualmente gestiona su inventario de forma manual mediante un cuaderno de registro. Este método genera errores frecuentes como olvidos, anotaciones incompletas y diferencias entre el stock físico y el registrado, lo que dificulta la toma de decisiones y pone en riesgo la operación del negocio.
Además, al limitarse únicamente a la venta presencial, la tienda pierde la oportunidad de llegar a clientes que prefieren realizar sus compras desde casa, lo que representa una desventaja competitiva en el contexto digital actual.
Por estas razones, se propone el desarrollo de un Sistema Digital de Pedidos en Línea con Stock para KeyluPets, que permita automatizar el control del inventario, reducir los errores humanos en el registro de entradas y salidas, y habilitar un canal de ventas en línea mediante un carrito de compras. De esta forma, el negocio podrá operar con mayor eficiencia, organización y proyección comercial.


## **Problema Identificado**

Actualmente, la tienda de mascotas *KeyluPets*, ubicada en Soacha, Porvenir, enfrenta una gestión operativa ineficiente debido a la dependencia absoluta de procesos manuales para el control de sus activos. El uso de un cuaderno físico como única herramienta de registro para las entradas y salidas de mercancía, precios y niveles de stock, ha derivado en una serie de debilidades técnicas y comerciales que limitan el crecimiento del negocio. 

## Análisis de Deficiencias Técnicas:

- Inconsistencia de Datos y Errores Humanos: El registro manual es susceptible a omisiones, anotaciones incompletas y errores de cálculo, lo que genera una brecha crítica entre el inventario físico y el reportado en papel. 

- Ausencia de Trazabilidad y Reportes: No existe un historial estructurado que permita consultar movimientos de productos en tiempo real, imposibilitando la generación de reportes precisos sobre el flujo de caja y la rotación de mercancía. 

- Ruptura de Stock no Detectada: Al no contar con alertas automatizadas, la tienda desconoce con exactitud cuándo un producto de alta rotación (como alimentos para perros y gatos) llega a su nivel crítico, lo que afecta la disponibilidad inmediata para el cliente. 

- Fuga de Información y Capital: La falta de un sistema de auditoría digital facilita la pérdida de mercancía por falta de registro, lo que se traduce en pérdidas económicas directas al no poder justificar las diferencias en el cuadre mensual. 

- Limitación de Canales de Venta: El modelo de negocio se encuentra restringido al mostrador físico, desperdiciando el potencial del mercado digital y las preferencias de consumo actuales de los clientes que buscan realizar pedidos desde su hogar. 


## **Objetivo General**

Diseñar una plataforma web integral de gestión comercial bajo una arquitectura cliente-servidor para la tienda KeyluPets. El sistema deberá centralizar la operación mediante un carrito de compras sincronizado a una base de datos relacional, permitiendo la automatización de la persistencia de datos de inventario. El objetivo es garantizar la integridad de la información, optimizar la trazabilidad de los procesos de entrada/salida para asegurar la consistencia del stock en tiempo real frente a la demanda digital y presencial. 

 

## **Objetivos Específicos**

- Permitir a los clientes realizar pedidos de productos a través de una plataforma digital. 

- Gestionar los pedidos desde el módulo administrativo del sistema. 

- Actualizar automáticamente el inventario cuando se registre una venta. 

- Consultar en tiempo real la cantidad disponible de cada producto. 

- Generar reportes de productos agotados o con bajas existencias. 

- Implementar un historial de ventas que permita llevar un control y seguimiento de los pedidos realizados. 

- Alcance del Proyecto 

- El sistema para desarrollar para KeyluPets abarcará los siguientes aspectos: 

## **Lo que incluye:**

- Módulo de inventario con registro automático de entradas y salidas de productos, alertas de stock bajo y clasificación por categorías (alimentos, accesorios, juguetes). 

- Módulo de ventas con carrito de compras, cálculo automático de totales, selección de medio de pago y registro de datos del cliente. 

- Historial de ventas vinculado al cliente para trazabilidad y gestión de devoluciones. 

- Reportes de productos más vendidos y de menor existencia. 

- Sistema de roles con dos perfiles: administrador y vendedor, con permisos diferenciados. 

- Interfaz web con identidad visual de KeyluPets (blanco, negro, tipografía moderna).


## **Lo que no incluye:**

- Integración con pasarelas de pago en línea (pagos digitales externos). 

- Aplicación móvil nativa. 

- Gestión contable o facturación electrónica oficial. 

- Servicio de domicilios o seguimiento de entregas.


## **Análisis General del Bloque 1**


Las respuestas de este bloque revelan dos necesidades fundamentales que deben guiar el desarrollo del sistema. Por un lado, la automatización del registro de inventario es urgente e innegociable: el método actual no ofrece confiabilidad y expone al negocio a pérdidas de información y errores operativos. Por otro lado, la facilidad de uso es tan importante como la funcionalidad misma; un sistema potente pero difícil de usar será rechazado o subutilizado. En conjunto, estos hallazgos establecen que el sistema debe ser preciso, automatizado y, sobre todo, simple de operar desde el primer día. 


**Bloque 2: Estructura y control del Inventario**


**P1:** Teniendo en cuenta la variedad de alimentos, juguetes y accesorios, ¿qué características específicas (como marca, peso del bulto, etapa de la mascota) son indispensables para clasificar y buscar un producto rápidamente en el sistema? 
***Respuesta:*** Para comida marca, peso del bulto, etapa de la mascota, para accesorio o juguetes tipo, color, marca. 

**P2:** Para evitar quedarse sin mercancía, ¿con qué nivel de stock (cantidad mínima) de los productos de mayor rotación consideran que el sistema debería generar una alerta automática de reabastecimiento? 
***Respuesta*** Minimo con 3


**P3:** Al finalizar la semana o el mes, ¿qué tipo de información les resultaría más útil ver en un reporte de inventario para tomar decisiones sobre qué productos comprar más o cuáles promocionar? 
**Respuesta:** Que en el reporte aparezcan los más vendidos y los que menos se tenga stock.


´´´**Análisis Descriptivo, Bloque N2**´´´

**Análisis:** La definición de un umbral concreto de 3 unidades demuestra que el administrador tiene claridad sobre el ritmo de rotación de sus productos. Este valor permite al sistema actuar de forma preventiva antes de que un producto se agote por completo, dando margen para gestionar la compra a tiempo. Aunque 3 unidades es el parámetro establecido, es recomendable que este umbral sea configurable por producto, ya que algunos ítems pueden tener una rotación mucho más alta o baja que otros.


**Análisis P1:** Para Accesorios y juguetes, el tipo y el color son los diferenciadores principales. Esto indica que el sistema debe manejar un modelo de datos flexible, con campos específicos según la categoría del producto, evitando formularios genéricos que dificulten la búsqueda y clasificación. 

**Análisis P2:**Este valor permite al sistema actuar de forma preventiva antes de que un producto se agote por completo, dando margen para gestionar la compra a tiempo. Aunque 3 unidades es el parámetro establecido, es recomendable que este umbral sea configurable por producto, ya que algunos ítems pueden tener una rotación mucho más alta o baja que otros.

**Análisis P3:** El entrevistado orienta los reportes hacia la acción: saber qué comprar más y qué promover. Los productos más vendidos deben mantenerse siempre disponibles, mientras que los de menor stock requieren atención inmediata.


## **Análisis General del Bloque 2:** 
Este bloque deja claro que el inventario de KeyluPets requiere un sistema flexible, con atributos diferenciados por tipo de producto, alertas automáticas de stock bajo y reportes que orienten decisiones de compra. Estos tres elementos definen el núcleo funcional del módulo de inventario 


**Bloque 3: Módulo de Ventas y Carrito de Compras**


**P1:** Durante una venta en el mostrador, ¿qué funcionalidades consideran vitales en el "carrito de compras" para agilizar la atención al cliente (ej. búsqueda rápida por nombre/código, cálculo automático de cambio, aplicación de descuentos)? 
***Respuesta:*** Búsquedas por código, nombre precio, total, medio de pago y datos del cliente en caso de necesitar factura. 

**P2:** Cuando un cliente lleva varios artículos, ¿qué información visual necesitan que el carrito de compras muestre claramente en la pantalla antes de confirmar el cobro total?
**Respuesta:** Cantidad de cada producto y su descripción. 


**P3:** Si por algún error de conteo previo un producto figura disponible en el sistema, pero al momento de agregarlo al carrito de compras el vendedor nota que físicamente está dañado o no existe, ¿cómo prefieren que el sistema permita manejar esta corrección en medio de la venta?
**Respuesta:**  Con un botón de restar en la parte derecha del producto. 


| **Análisis Descriptivo, Bloque N3** |


**Análisis P1:** El cálculo automático del total elimina errores aritméticos, y el registro del medio de pago junto con los datos del cliente convierte cada venta en un registro formal y trazable. Estas funcionalidades indican que el carrito debe operar como una herramienta integral de ventas, no solo como una lista de productos.


**Análisis P2:** Antes de cerrar la venta, el vendedor necesita una pantalla de resumen clara que permita verificar que todo es correcto. Mostrar la cantidad y descripción de cada ítem reduce errores de cobro y genera confianza tanto en el vendedor como en el cliente. Esto define una pantalla de confirmación previa al pago como un paso obligatorio dentro del flujo de venta.


**Análisis P3:**  La solución propuesta es simple y efectiva: un control directo sobre cada ítem del carrito sin necesidad de cancelar la venta. Esto refleja la necesidad de un flujo de venta continuo que permita correcciones sobre la marcha, minimizando interrupciones en la atención al cliente y evitando frustraciones tanto para el vendedor como para el comprador.


## **Análisis General del Bloque 3**

El módulo de ventas debe ser ágil, completo y tolerante a errores. Las respuestas de este bloque definen un carrito de compras con búsqueda flexible, resumen visual antes del cobro y controles de ajuste en tiempo real. En conjunto, estas funcionalidades garantizan una experiencia de venta fluida y confiable para el equipo de KeyluPets. 


## **Bloque 4: Seguridad, Roles y Proyección**


**P1:** Para proteger la información del negocio, ¿qué permisos específicos debería tener la persona que atiende en el mostrador (que usará principalmente el carrito de compras) frente a la persona encargada de administrar (que ingresará nueva mercancía al inventario)?
***Respuesta:*** El personal que atiende solo acceso a registrar ventas y visualizar inventario, el administrador a agregar y borrar inventario además de ver reportes de ventas y administrar los usuarios. 


**P2:**  Una vez que el carrito de compras procesa una venta y descuenta automáticamente el inventario, ¿les gustaría que el sistema guarde un historial asociando la compra a un cliente específico (para fidelización) o prefieren manejar únicamente ventas rápidas anónimas?
***Respuesta:*** Me gustaría manejar el historial de lo que se vende y a quien ya que pude servir en caso de alguna devolución o reclamo. Bloque 5: Perfil del Usuario y Diseño Visual de la Interfaz (UI/UX) 


**P3:(Datos personales y creacion de perfil):** Para configurar el perfil principal de administrador en el nuevo sistema, ¿cargo exacto o rol que desempeña en el día a día de Keylupets?
**Respuesta:** Administrador


**P4: (Experiencia y usabilidad):** Pensando en la facilidad de uso del programa, ¿qué tan familiarizado está con el manejo de computadores o aplicaciones de ventas, y qué es lo que más le suele frustrar de los sistemas digitales que ha utilizado antes?
**Respuesta:** _He manejado sistemas de inventarios tanto en Excel como aplicaciones móviles lo más complejo ha sido aquellas interfaces que no son intuitivas. 


**P5: (Colores e identidad visual):** En cuanto a la apariencia visual del sistema y del carrito de compras, ¿cuáles son los colores representativos de Keylupets que le gustaría que destaquen en la pantalla y qué estilo de letra prefiere (por ejemplo, un estilo moderno y redondeado, o algo más clásico y formal)? 
**Respuesta:**  Los colores pueden ser los del logo que son blanco y negro y una letra estilo moderno ya que es más llamativa. 


**P6: (Manejo de imágenes en el catálogo):**  Para que la búsqueda en el inventario y en el carrito sea muy visual, ¿cómo le gustaría que se muestren los productos? ¿Prefiere que el sistema tenga fotos reales tomadas por ustedes, imágenes de catálogo de los proveedores, o prefiere una vista más rápida solo con texto e íconos?
**Respuesta:** Imagenes tomadas por nosotros.


**P7: (Interacciones y alertas visuales):** Cuando el vendedor realice una acción, como agregar un producto al carrito o confirmar una venta exitosa, ¿qué tipo de interacción prefiere que tenga el sistema? (Por ejemplo: un mensaje emergente en el centro de la pantalla, un sonido de confirmación tipo "caja registradora", o botones que cambien de color).

 
**Respuesta:** Una ventana emergente en la pantalla que diga algo como “venta exitosa” o “venta confirmada”.


## **Análisis Descriptivo — Bloque 4: Seguridad, Roles y Proyección**


**Análisis P1:**  El vendedor opera en un entorno restringido que le permite cumplir su función sin acceder a información sensible ni modificar el catálogo. El administrador tiene control total del sistema. Esta distinción protege la integridad de la información y evita modificaciones accidentales o no autorizadas, siendo un requisito de seguridad fundamental desde el inicio del desarrollo.


**Análisis P2:** La elección del historial trazable responde a una necesidad operativa concreta: respaldar decisiones ante devoluciones o reclamos. Esto implica que el sistema debe incluir un módulo básico de registro de clientes y asociar cada venta a un perfil, sentando además las bases para estrategias de fidelización a futuro. 


**Análisis P3:** El entrevistado es el usuario principal y decisor del sistema. Su perfil abarca tanto la operación diaria como la gestión estratégica, lo que confirma que el sistema debe responder a ambos niveles: operativo para el vendedor y gerencial para el administrador.


**Análisiss p4:** El administrador tiene experiencia digital suficiente para adoptar el sistema sin dificultad, pero su principal barrera ha sido la falta de intuitivita. Esto refuerza que el diseño debe ser limpio, directo y con el menor número de pasos posible para completar cada tarea.


**Análisis P5:**   La paleta cromática del sistema debe respetar la identidad visual de KeyluPets. El blanco y negro transmite sobriedad y profesionalismo, y combinado con una tipografía moderna genera una interfaz contemporánea y coherente con la imagen de la tienda.


**Análisis P6:** El uso de fotografías propias humaniza el catálogo y genera mayor confianza en el cliente. Técnicamente, implica implementar un módulo de carga y gestión de imágenes por producto, con visualización adaptada según el contexto: inventario, carrito o catálogo en línea. 


**Análisis P7:**  La preferencia por mensajes emergentes indica que el usuario valora la retroalimentación visual clara e inmediata. Este tipo de confirmación debe aplicarse a todas las acciones críticas del sistema, usando un lenguaje positivo que refuerce la confianza del vendedor en cada operación.

**Análisis General del Bloque 5**
Este bloque define la experiencia que debe tener el usuario al interactuar con el sistema. La interfaz debe ser intuitiva, visualmente coherente con la marca KeyluPets, con soporte para imágenes propias y confirmaciones visuales en cada acción importante. El diseño no es un detalle secundario; es un factor determinante para la adopción exitosa del sistema. 
