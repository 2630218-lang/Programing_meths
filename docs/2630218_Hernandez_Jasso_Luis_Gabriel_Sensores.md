# Sensores y actuadores en sistemas mecatrónicos

**Alumno:** Luis Gabriel Hernandez Jasso  
**Matrícula:** 2630218  
**Tema:** Conceptos básicos, clasificación y aplicaciones de sensores y actuadores

---

## 1. Conceptos básicos

### ¿Qué es un sensor?

Un sensor es un componente que detecta una característica del entorno o de un objeto y la convierte en una señal que un sistema puede interpretar. Puede medir, por ejemplo, temperatura, luz, presión, distancia o movimiento.

### ¿Qué es un actuador?

Un actuador es un dispositivo que recibe una señal de control y produce una acción física. Esa acción puede ser girar, empujar, levantar, abrir, cerrar o mover una pieza. Algunos actuadores usan electricidad y otros funcionan con aire comprimido o líquido a presión.

### Diferencia entre sensor y actuador

La diferencia principal es su función: el sensor **detecta o mide** algo, mientras que el actuador **realiza una acción**. En un sistema automático, el sensor obtiene información y el controlador decide qué hacer; después, el actuador ejecuta la acción indicada.

### Función dentro de un sistema mecatrónico

Los sensores permiten que el sistema conozca su estado y lo que ocurre a su alrededor. Los actuadores convierten las órdenes del controlador en movimiento o en otra acción física. Trabajando juntos ayudan a automatizar tareas, mantener condiciones y responder a cambios.

### Ejemplo: puerta automática

Una puerta automática utiliza un sensor de presencia o proximidad para detectar que una persona se acerca. El controlador recibe esa señal y activa un motor, que es el actuador encargado de abrir la puerta. Cuando la zona queda despejada, el sistema puede ordenar que se cierre, siempre que sus sensores de seguridad indiquen que no hay obstáculos.

**Funcionamiento básico:**

```text
Persona se acerca
       |
       v
Sensor de presencia
       |
       v
Controlador
       |
       v
Motor de la puerta
       |
       v
La puerta se abre
```

---

## 2. Investigación de sensores

Los sensores convierten una variable física en una señal que un controlador puede utilizar. La salida puede ser analógica, digital o una comunicación de datos, según el modelo.

| Tipo de sensor | Variable que mide o detecta | Principio básico de funcionamiento | Ejemplo comercial o real | Aplicación |
|---|---|---|---|---|
| Temperatura | Temperatura de un objeto, líquido o ambiente | Un termistor cambia su resistencia con la temperatura; otros sensores generan una tensión o entregan datos digitales | **DS18B20**, sensor digital de temperatura | Control de temperatura en incubadoras, equipos y sistemas de climatización |
| Luz | Intensidad luminosa | Una fotorresistencia cambia su resistencia al recibir más o menos luz; un fotodiodo convierte la luz en corriente | Fotorresistencia **LDR** o fotodiodo | Encendido automático de lámparas y ajuste del brillo de una pantalla |
| Proximidad | Presencia de un objeto a corta distancia, sin necesidad de tocarlo | Puede detectar cambios en un campo electromagnético, capacitancia o luz reflejada | Sensor inductivo **LJ12A3** para objetos metálicos; sensor fotoeléctrico industrial | Detectar piezas en una banda transportadora |
| Distancia | Separación entre el sensor y un objeto | Un sensor ultrasónico mide el tiempo que tarda en regresar un eco; uno láser puede medir el tiempo de vuelo o el desplazamiento de la luz | **HC-SR04**, sensor ultrasónico | Evitar obstáculos en un robot móvil o medir el nivel de un depósito |
| Presión | Fuerza por unidad de área ejercida por un gas o líquido | Un diafragma se deforma ligeramente y un elemento piezorresistivo o electrónico transforma esa deformación en una señal | Sensor de presión **MPX5700** (familia de sensores de presión) | Supervisar presión en sistemas neumáticos, hidráulicos o de aire |
| Humedad | Cantidad de vapor de agua en el aire o humedad de un material | En sensores de humedad relativa, un material cambia una propiedad eléctrica según la humedad | **DHT22/AM2302**, sensor de temperatura y humedad | Estaciones meteorológicas, invernaderos y control ambiental |
| Posición | Ubicación lineal o angular de una pieza | Un potenciómetro cambia su resistencia según la posición; un encoder detecta desplazamientos mediante pulsos | Potenciómetro de posición o encoder rotatorio | Conocer el ángulo de un eje o la posición de una articulación robótica |
| Velocidad o movimiento | Rapidez, giro o cambio de movimiento | Un encoder produce pulsos al girar; un sensor PIR detecta cambios en la radiación infrarroja de una escena | Encoder incremental rotatorio; sensor PIR | Medir la velocidad de una banda o detectar movimiento de personas |
| Fuerza o peso | Fuerza aplicada o peso de un objeto | Una galga extensométrica cambia su resistencia al deformarse; varias pueden formar un puente de medición | Celda de carga con galgas extensométricas | Básculas, máquinas de ensayo y control de peso en producción |

### Aclaraciones sobre las señales

- **Analógica:** cambia de forma continua dentro de un rango, por ejemplo, una tensión que aumenta con la temperatura.
- **Digital:** representa estados o datos discretos, como encendido/apagado o una lectura enviada mediante un protocolo digital.
- **Pulsos o comunicación de datos:** algunos sensores entregan una secuencia de pulsos o información por interfaces como I²C, SPI o una conexión industrial.
- El tipo de señal exacto depende del modelo. Dos sensores que miden la misma variable no necesariamente entregan la misma salida.

---

## 3. Clasificación de sensores

### Sensores analógicos y digitales

**Sensores analógicos:** su salida puede tomar muchos valores dentro de un intervalo continuo. La señal cambia gradualmente conforme cambia la variable medida. Por ejemplo, una salida de 1,2 V podría representar una temperatura menor que una salida de 2,1 V.

**Sensores digitales:** entregan información en estados definidos o como datos codificados digitalmente. Un interruptor de límite, por ejemplo, indica si una pieza llegó o no a una posición; un sensor digital de temperatura transmite un número que representa la medición.

**¿Qué característica determina la categoría?** La forma de la señal de salida. No depende únicamente de lo que mide el sensor, sino de cómo entrega la información. Una misma variable, como la temperatura, puede medirse con sensores analógicos o digitales.

### Sensores de contacto y sin contacto

**De contacto:** necesitan tocar el objeto o recibir directamente su fuerza para detectar la variable. Un final de carrera mecánico, por ejemplo, cambia de estado cuando una pieza presiona su palanca.

**Sin contacto:** detectan una variable sin tocar directamente el objeto. Pueden utilizar luz, ultrasonido, campos magnéticos o campos eléctricos. Un sensor inductivo puede detectar una pieza metálica sin que esta lo golpee.

**¿Qué característica determina la categoría?** Si la detección requiere contacto físico entre el sensor y el objeto. Esta diferencia importa cuando hay desgaste, riesgo de daño, movimiento rápido o necesidad de mantener separación.

### Sensores activos y pasivos

Esta clasificación se refiere a cómo se obtiene la señal de medición y puede variar un poco según el área técnica.

**Activos:** generan una señal eléctrica a partir de la magnitud medida o emplean un elemento que emite energía para detectar el entorno. Por ejemplo, un termopar genera una pequeña tensión por una diferencia de temperatura, y un sensor ultrasónico activo emite un pulso de sonido y analiza su eco.

**Pasivos:** necesitan una excitación o alimentación externa para que el cambio producido por la variable pueda convertirse en una señal útil. Por ejemplo, una fotorresistencia necesita un circuito de alimentación para medir su cambio de resistencia, y un termistor suele leerse mediante un divisor de tensión.

**¿Qué característica determina la categoría?** Si el elemento genera directamente una señal a partir de la magnitud física o si requiere excitación externa para convertir su cambio en una medición. La terminología no es completamente uniforme: en algunas áreas, “activo” y “pasivo” se clasifican según si el sensor emite energía al entorno. Por eso conviene revisar la definición utilizada por el fabricante o el curso.

---

## 4. Investigación de actuadores

Un actuador convierte una orden de control en una acción física. La selección depende de la fuerza requerida, el tipo de movimiento, la precisión, la velocidad y el entorno de trabajo.

| Actuador | Energía utilizada | Movimiento | Funcionamiento general | Ventaja | Limitación | Aplicación |
|---|---|---|---|---|---|---|
| Motor de corriente directa (DC) | Eléctrica | Rotatorio continuo | La corriente en sus bobinas interactúa con un campo magnético y produce giro | Fácil de controlar en velocidad y suele ser económico | Sin sensores o control adicional, no conoce con precisión su posición | Ventiladores, juguetes, pequeños robots y bandas |
| Servomotor | Eléctrica | Normalmente rotatorio con posición controlada; existen servos lineales | Un sistema de control compara la posición solicitada con la real y corrige el movimiento | Permite controlar posición y, según el modelo, velocidad o par | Suele ser más costoso y requiere un controlador compatible | Articulaciones robóticas, mecanismos de dirección y máquinas CNC |
| Motor paso a paso | Eléctrica | Rotatorio en pasos discretos | Sus bobinas se energizan en una secuencia que hace avanzar el rotor por incrementos | Puede posicionarse por pasos sin un encoder en aplicaciones adecuadas | Puede perder pasos si la carga es excesiva y puede vibrar o calentarse | Impresoras 3D, posicionadores y equipos de automatización |
| Solenoide | Eléctrica | Lineal, generalmente de recorrido corto | Una bobina crea un campo magnético que desplaza un núcleo metálico | Respuesta rápida y estructura sencilla | Recorrido limitado y puede calentarse si se energiza durante demasiado tiempo | Cerraduras eléctricas, válvulas y mecanismos de liberación |
| Cilindro neumático | Aire comprimido | Lineal de avance y retroceso | El aire a presión empuja un pistón dentro de un cilindro | Rápido, limpio y útil para movimientos repetitivos | El aire es compresible, por lo que controlar una posición intermedia con precisión puede ser difícil | Empujar, sujetar o separar piezas en una línea de producción |
| Cilindro hidráulico | Líquido a presión, normalmente aceite | Lineal de avance y retroceso | El fluido presurizado empuja un pistón y genera fuerza | Puede producir fuerzas muy elevadas en un conjunto compacto | Puede haber fugas; requiere mantenimiento del fluido y del circuito | Prensas, elevadores, maquinaria de construcción y equipos pesados |

**Nota:** un servomotor no es solamente un motor de un tipo específico; normalmente es un conjunto de motor, realimentación y control. Existen servos de diferentes tecnologías y rangos de potencia.

---

## 5. Comparación de actuadores

### Motor DC y servomotor

Un motor DC común gira cuando recibe energía y su velocidad puede regularse, pero por sí solo no confirma el ángulo exacto al que llegó. Un servomotor incorpora realimentación y control para alcanzar una posición o seguir una orden con mayor precisión, de acuerdo con sus especificaciones.

**¿Cuándo elegiría cada uno?**

- Elegiría un **motor DC** para mover las ruedas de un robot sencillo cuando lo principal sea avanzar, retroceder y ajustar la velocidad con un circuito básico.
- Elegiría un **servomotor** para orientar una cámara o mover una articulación a un ángulo determinado, porque necesito controlar la posición y corregir el error.

### Servomotor y motor paso a paso

Un servomotor utiliza realimentación para corregir la diferencia entre la posición ordenada y la posición real. Un motor paso a paso se mueve en incrementos definidos por la secuencia de sus bobinas; en un sistema básico puede funcionar sin realimentación, aunque también puede combinarse con un encoder.

**¿Cuándo elegiría cada uno?**

- Elegiría un **motor paso a paso** para un mecanismo de una impresora 3D o un pequeño posicionador, si la carga y la precisión requerida permiten trabajar por pasos.
- Elegiría un **servomotor** para una articulación sometida a cargas cambiantes o que necesite corregir su posición durante el funcionamiento.

### Actuador neumático e hidráulico

Los dos pueden producir movimiento lineal, pero utilizan fluidos diferentes. El sistema neumático usa aire comprimido y suele ser apropiado para movimientos rápidos y repetitivos. El hidráulico usa un líquido a presión y puede generar fuerzas mayores para trabajos pesados.

**¿Cuándo elegiría cada uno?**

- Elegiría un **cilindro neumático** para empujar cajas o separar piezas ligeras en una línea de producción, porque el movimiento puede ser rápido y el sistema relativamente sencillo.
- Elegiría un **cilindro hidráulico** para levantar una carga pesada o accionar una prensa, porque puede entregar una fuerza elevada. En ese caso también tendría que considerar fugas, mantenimiento y medidas de seguridad.

---

## 6. Sensores y actuadores en un sistema real

### Sistema seleccionado: robot móvil que evita obstáculos

Un robot móvil puede desplazarse por un espacio y utilizar sensores para reconocer obstáculos. Para este ejemplo se considera un robot pequeño de dos ruedas motrices y una rueda de apoyo.

| Elemento | Tipo | Función |
|---|---|---|
| Sensor ultrasónico HC-SR04 | Sensor de distancia | Estima la distancia al obstáculo mediante el tiempo que tarda en regresar el eco del ultrasonido |
| Controlador, por ejemplo Arduino Uno | Controlador, no es sensor ni actuador | Lee la distancia y decide si el robot puede avanzar o debe detenerse y girar |
| Dos motores DC con ruedas | Actuadores | Hacen girar las ruedas para avanzar, retroceder o cambiar de dirección |
| Puente H, por ejemplo TB6612FNG | Etapa de potencia para motores | Permite al controlador ordenar el sentido de giro y regular la potencia de los motores |
| Batería | Fuente de energía | Suministra energía al controlador y al circuito de motores, usando las tensiones adecuadas |

### ¿Cómo funciona?

1. El sensor ultrasónico envía un pulso y mide cuánto tarda en regresar el eco.
2. El controlador utiliza ese tiempo para calcular una distancia aproximada.
3. Si no hay un obstáculo cerca, ordena a los motores avanzar.
4. Si la distancia es menor que el límite programado, ordena reducir la velocidad o detenerse y girar.
5. El sensor vuelve a medir para que el robot pueda tomar otra decisión.

El umbral debe ajustarse al tamaño, velocidad y distancia de frenado del robot. Un sensor ultrasónico puede tener dificultades con superficies blandas, inclinadas o muy pequeñas, por lo que no debe considerarse un sistema de seguridad infalible.

### Diagrama de funcionamiento

```text
       Obstáculo frente al robot
                  |
                  v
       +---------------------+
       | Sensor ultrasónico  |
       | mide la distancia   |
       +---------------------+
                  |
                  v
       +---------------------+
       | Arduino Uno         |
       | compara la lectura  |
       | con el límite       |
       +---------------------+
                  |
          +-------+-------+
          |               |
   Distancia segura   Obstáculo cerca
          |               |
          v               v
   +-------------+   +----------------+
   | Avanzar     |   | Detenerse y    |
   | motores DC  |   | girar          |
   +-------------+   +----------------+
          |               |
          +-------+-------+
                  |
                  v
         Medir nuevamente
```

---

## 7. Selección de componentes

| Situación | Componente que elegiría | Razón de la selección |
|---|---|---|
| Detectar si una persona se encuentra frente a una puerta automática | Sensor de presencia por microondas o sensor fotoeléctrico apropiado para puertas | Detecta la aproximación sin que la persona tenga que tocar la puerta. El modelo debe ser apto para puertas automáticas y complementarse con sensores de seguridad para evitar cierres sobre personas u objetos |
| Medir la temperatura dentro de un salón | Sensor digital **DHT22** si también interesa la humedad, o un **DS18B20** para temperatura | Permite obtener lecturas de temperatura para registrar o controlar el ambiente. El DHT22 también mide humedad; el DS18B20 es específico para temperatura |
| Detectar el nivel de agua de un depósito | Sensor de nivel por flotador para detectar un nivel límite; sensor de presión hidrostática o ultrasónico si se requiere una medición más continua | El flotador es sencillo para indicar lleno o vacío. Para conocer cuánto líquido hay en un rango más amplio, conviene seleccionar un sensor diseñado para la profundidad y el tipo de depósito |
| Mover una rueda de un robot móvil | Motor DC con caja reductora | Produce giro continuo y la caja reductora aumenta el par para mover el robot. Se recomienda un controlador de motor compatible |
| Controlar con precisión el ángulo de una pequeña articulación robótica | Servomotor con rango de giro y par adecuados | Recibe una posición objetivo y utiliza realimentación interna para corregir su movimiento. Debe seleccionarse según la carga y el recorrido requeridos |
| Empujar una pieza en una línea de producción | Cilindro neumático | Produce un desplazamiento lineal rápido y repetitivo. Debe incluir válvula, regulación y resguardos apropiados |
| Medir la distancia entre un robot y una pared | Sensor ultrasónico como el HC-SR04 para un prototipo sencillo | Calcula la distancia mediante el tiempo de vuelo del sonido. Para exteriores, superficies difíciles o mayor precisión puede convenir otro tipo de sensor |
| Detectar si una habitación está iluminada | Fotorresistencia LDR o sensor digital de luz | Su señal cambia según la luz recibida. Puede usarse para encender lámparas cuando la iluminación cae por debajo de un nivel definido |

**Importante:** los nombres de componentes son ejemplos, no una garantía de que sean adecuados para cualquier instalación. Antes de conectar un componente hay que comprobar su tensión, corriente, rango de medición, compatibilidad eléctrica y condiciones de uso.

---

## Reflexión final

Medir una variable y realizar una acción física son tareas diferentes. Medir significa obtener información sobre algo, como la temperatura de una habitación o la distancia a una pared. Realizar una acción física significa cambiar algo en el entorno, por ejemplo, mover una rueda, abrir una puerta o empujar una pieza.

Un sistema mecatrónico normalmente necesita sensores y actuadores porque debe conocer lo que sucede y también actuar. El sensor proporciona información al controlador; el controlador la interpreta y envía órdenes; el actuador convierte esas órdenes en movimiento o fuerza. Sin sensores, muchos sistemas automáticos no podrían adaptarse a los cambios del entorno. Sin actuadores, podrían detectar una situación, pero no realizar una acción para responder.

El componente que me pareció más interesante fue el sensor ultrasónico, porque permite estimar la distancia sin tocar el objeto. Su funcionamiento se entiende comparando el tiempo de salida y regreso de una onda sonora. Esto lo hace útil en robots móviles y sistemas de medición sencillos. También aprendí que su lectura puede variar según la superficie y la posición del objeto, por lo que es importante conocer sus limitaciones y probarlo en el entorno donde se va a utilizar.

En general, investigar estos componentes ayuda a entender que la mecatrónica combina la parte mecánica, la electrónica y la programación. La elección correcta depende de lo que se necesita medir o mover, de la precisión esperada, del ambiente de trabajo y de las condiciones de seguridad.

---

## Referencias

1. Analog Devices. (s. f.). *Temperature Sensors*. Analog Devices. https://www.analog.com/en/product-category/temperature-sensors.html
2. Analog Devices. (s. f.). *Pressure Sensors*. Analog Devices. https://www.analog.com/en/product-category/pressure-sensors.html
3. Arduino. (s. f.). *Arduino Uno Rev3*. Arduino Documentation. https://docs.arduino.cc/hardware/uno-rev3/
4. Aosong Electronics. (s. f.). *DHT22 (AM2302) Digital Temperature and Humidity Sensor* (documentación del producto). Sitio del fabricante: https://www.aosong.com/
5. Honeywell. (s. f.). *Basic Pressure Sensors* (información de productos y tecnología de sensores de presión). Honeywell. https://sensing.honeywell.com/
6. MaxBotix. (s. f.). *Ultrasonic Sensors*. MaxBotix Inc. https://maxbotix.com/
7. Microchip Technology. (s. f.). *Stepper Motors* (recursos técnicos sobre motores paso a paso). Microchip Technology. https://www.microchip.com/
8. OMRON. (s. f.). *Proximity Sensors* (información técnica de sensores de proximidad). OMRON Industrial Automation. https://www.ia.omron.com/products/category/sensors/proximity-sensors/
9. Pololu. (s. f.). *TB6612FNG Dual Motor Driver Carrier*. Pololu Robotics & Electronics. https://www.pololu.com/product/713
10. STMicroelectronics. (s. f.). *LIS and MEMS sensor resources* (documentación técnica de sensores electrónicos). STMicroelectronics. https://www.st.com/
11. Texas Instruments. (s. f.). *DRV8833 Dual H-Bridge Motor Driver* (hoja de datos y documentación técnica). Texas Instruments. https://www.ti.com/product/DRV8833
12. Tekscan. (s. f.). *Force Sensors and Load Cells* (información sobre medición de fuerza). Tekscan. https://www.tekscan.com/

**Nota sobre las referencias:** se incluyen sitios oficiales de fabricantes y documentación técnica para orientar la consulta. Para la versión final que se entregue, conviene abrir las páginas y anotar el título exacto, modelo y fecha de la hoja técnica específica que se haya consultado, especialmente para los sensores DHT22, HC-SR04, MPX5700 y los actuadores elegidos.
