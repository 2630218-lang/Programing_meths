# Investigación: configuraciones de ruedas en robots móviles

**Nombre:** Luis Gabriel Hernandez Jasso 
**Matrícula:** 2630218
**Asignatura:** Metodologia de la programacion
**Fecha:** 11/10/26

## 1. Conceptos básicos

### ¿Qué es un robot móvil?

Un robot móvil es una máquina que puede cambiar de lugar por sí misma
mediante ruedas, orugas, patas u otro sistema de locomoción. Utiliza
motores y, por lo general, sensores y un controlador para desplazarse y
responder a su entorno.

### Diferencia entre un robot móvil y un robot manipulador fijo

Un robot móvil está diseñado para trasladarse de un punto a otro. En
cambio, un manipulador fijo suele permanecer sujeto a una base y mueve
sus articulaciones para alcanzar, sujetar o trabajar con objetos dentro
de un área determinada. Por ejemplo, un carrito autónomo que transporta
cajas es móvil; un brazo industrial atornillado al piso es un
manipulador fijo.

### Función del sistema de locomoción

El sistema de locomoción transforma la energía de los motores en
movimiento. Su diseño determina cómo se mueve el robot, qué superficies
puede recorrer, cuánto peso puede transportar y qué tan bien puede girar
o superar obstáculos.

### ¿Qué significa movilidad omnidireccional?

Significa que el robot puede moverse en distintas direcciones del plano
---hacia adelante, atrás, a los lados y en diagonal--- sin tener que
orientar primero todo el chasis hacia la dirección deseada. Algunos
sistemas también pueden trasladarse y girar al mismo tiempo.

### Relación entre la disposición de las ruedas y el movimiento

La ubicación, orientación y tipo de rueda determinan qué fuerzas pueden
producirse contra el suelo. Dos ruedas motrices paralelas permiten
avanzar y girar variando sus velocidades; las ruedas Omni o Mecanum
permiten movimientos laterales; y la dirección Ackermann hace que las
ruedas delanteras sigan una trayectoria curva parecida a la de un
automóvil.

### ¿Dónde se utilizan robots móviles?

-   Almacenes y centros de distribución para transportar productos.
-   Hospitales para llevar medicamentos, ropa o alimentos.
-   Fábricas para mover materiales entre estaciones.
-   Agricultura para revisar cultivos y recorrer terrenos.
-   Exploración espacial y ambientes peligrosos.
-   Hogares, por ejemplo, en aspiradoras robotizadas.
-   Investigación, educación y competencias de robótica.

## 2. Robot diferencial con rueda de castor

Esta configuración tiene dos ruedas motrices, una a cada lado del
chasis, normalmente montadas sobre un mismo eje transversal. Una rueda
de castor o rueda loca sostiene parte del peso y gira libremente para
acomodarse al sentido de avance. No suele ser motriz.

### Funcionamiento

-   **Avance recto:** las dos ruedas motrices giran hacia adelante a la
    misma velocidad.
-   **Retroceso recto:** ambas giran hacia atrás a la misma velocidad.
-   **Giro a la izquierda o derecha:** las ruedas giran a velocidades
    diferentes.
-   **Una rueda detenida:** el robot describe una curva alrededor de la
    rueda detenida.
-   **Giro sobre su propio centro:** las ruedas giran en sentidos
    opuestos y con velocidades de magnitud parecida.
-   **Diferente velocidad:** el robot se curva hacia el lado de la rueda
    que avanza más despacio, suponiendo que ambas se mueven hacia
    delante.

### Diagrama visto desde arriba

``` text
                       FRENTE
                         ↑ avance
               ┌──────────────────┐
               │                  │
 Rueda         O                  O         Rueda
 izquierda    (L)                (R)        derecha
               │                  │
               │      CHASIS      │
               │                  │
               └─────────┬────────┘
                         o
                   Rueda de castor
                   (rueda loca)

       Eje motriz: línea imaginaria entre L y R.
       Giro sobre el eje: L hacia atrás y R hacia delante,
       o viceversa, aproximadamente a la misma velocidad.
```

### Tabla de movimientos

  -----------------------------------------------------------------------
  Rueda izquierda         Rueda derecha           Movimiento aproximado
                                                  del robot
  ----------------------- ----------------------- -----------------------
  Avanza                  Avanza                  Avanza recto si las
                                                  velocidades son
                                                  iguales.

  Detenida                Avanza                  Gira hacia la izquierda
                                                  alrededor de la rueda
                                                  izquierda.

  Avanza                  Detenida                Gira hacia la derecha
                                                  alrededor de la rueda
                                                  derecha.

  Avanza                  Retrocede               Gira sobre su propio
                                                  eje; el sentido depende
                                                  de cuál avanza y cuál
                                                  retrocede.

  Retrocede               Avanza                  Gira sobre su propio
                                                  eje en el sentido
                                                  contrario al caso
                                                  anterior.

  Retrocede               Retrocede               Retrocede recto si las
                                                  velocidades son
                                                  iguales.
  -----------------------------------------------------------------------

### Ventajas

-   Diseño sencillo y económico.
-   Puede usar solamente dos motores de tracción.
-   Es relativamente fácil de programar y reparar.
-   Puede girar en espacios reducidos, incluso sobre su centro si las
    ruedas lo permiten.

### Limitaciones

-   No puede desplazarse directamente hacia un costado manteniendo la
    misma orientación.
-   La rueda loca puede vibrar o cambiar bruscamente de orientación.
-   En superficies resbaladizas puede perder precisión.
-   Los giros pueden desgastar las ruedas o el suelo.

### Aplicaciones

Se usa en robots educativos, pequeños robots seguidores de línea,
plataformas de investigación, robots de servicio y algunos robots
móviles de almacén.

## 3. Robots omnidireccionales con ruedas Omni

### ¿Cómo está construida una rueda Omni?

Una rueda Omni tiene una rueda principal con pequeños rodillos colocados
alrededor de su perímetro. La rueda principal puede transmitir fuerza en
la dirección de rodadura, mientras que los rodillos giran libremente y
permiten que la rueda se deslice lateralmente con poca resistencia.

### ¿Por qué permite moverse lateralmente?

Una rueda convencional ofrece resistencia al movimiento lateral porque
su banda de rodadura debe deslizarse de lado. En una rueda Omni, los
rodillos periféricos giran cuando aparece ese movimiento transversal.
Así, el robot puede combinar fuerzas de varias ruedas para producir
desplazamientos que no serían posibles con ruedas convencionales sin
girar primero el chasis.

### Configuración omnidireccional de tres ruedas

Las tres ruedas se colocan normalmente alrededor del chasis, separadas
aproximadamente **120°** entre sí. Cada rueda se orienta tangencialmente
o según el diseño del conjunto, de modo que sus fuerzas se combinan para
controlar el movimiento del robot en el plano.

``` text
                    Frente
                      ↑
                      O  Rueda 1
                     / \
                    /   \
       Rueda 3  O--/-----\--O  Rueda 2
                 \   ●   /
                  \     /
                   \___/

   Vista conceptual desde arriba.
   O = rueda Omni; ● = centro aproximado del chasis.
   Las ruedas están distribuidas aproximadamente cada 120°.
   La orientación exacta depende del diseño y del montaje.
```

### Movimientos posibles

-   **Adelante y atrás:** se coordinan las velocidades de las tres
    ruedas para que las componentes de fuerza se sumen en el eje
    longitudinal.
-   **Lateralmente:** las ruedas producen componentes transversales que
    se combinan para trasladar el chasis hacia un lado.
-   **En diagonal:** se combinan las órdenes de avance y desplazamiento
    lateral.
-   **Giro sobre el eje:** las ruedas generan fuerzas tangenciales
    alrededor del centro, haciendo rotar el chasis.
-   **Velocidades diferentes:** las velocidades y sentidos de giro
    determinan una combinación de traslación y rotación. No basta con
    asignar cualquier velocidad; se requiere una relación calculada para
    obtener la trayectoria deseada.

### Configuración omnidireccional de cuatro ruedas

En un diseño de cuatro ruedas Omni, estas suelen ubicarse en las
esquinas de una plataforma y se orientan de forma que sus componentes de
fuerza permitan el movimiento en el plano. La geometría concreta varía
entre fabricantes y diseños.

Frente al sistema de tres ruedas, cuatro ruedas pueden repartir mejor la
carga y dar más puntos de apoyo, pero necesitan una coordinación
adecuada de los motores. Si las ruedas no están alineadas o sus
diámetros difieren, pueden producirse esfuerzos internos, deslizamientos
o trayectorias imprecisas.

**Ventajas:** movimiento lateral, diagonal y rotación sin reorientar el
chasis; plataforma compacta y maniobrable.\
**Limitaciones:** más motores y control que un diferencial sencillo;
rodillos que pueden desgastarse; rendimiento menor en superficies
rugosas o con huecos.

## 4. Robot omnidireccional con ruedas Mecanum

### Construcción y orientación

Una rueda Mecanum posee rodillos alrededor de su perímetro montados en
un ángulo, comúnmente cercano a **45°** respecto al eje de la rueda. A
diferencia de la rueda Omni típica, cuyos rodillos suelen estar
orientados aproximadamente perpendiculares al plano de la rueda, los
rodillos inclinados de Mecanum convierten parte de la fuerza de rodadura
en una componente lateral.

Se suelen instalar cuatro ruedas, una en cada esquina del chasis. La
orientación de los rodillos debe formar el patrón correcto, conocido a
menudo como disposición en **X** o en **O**, según el diseño. Si se
montan mal, algunos movimientos no se producirán como se espera. El
sentido de giro indicado en la tabla supone una disposición Mecanum
común en X vista desde arriba; conviene verificarla con el manual del
fabricante.

``` text
                         FRENTE
                           ↑
             DELANTERA IZQ.       DELANTERA DER.
                 ┌─────┐             ┌─────┐
                 │  /  │             │  \  │
                 └─────┘             └─────┘
              ┌─────────────────────────────┐
              │                             │
              │            CHASIS           │
              │                             │
              └─────────────────────────────┘
                 ┌─────┐             ┌─────┐
                 │  \  │             │  /  │
                 └─────┘             └─────┘
              TRASERA IZQ.          TRASERA DER.

      Las líneas diagonales representan de manera esquemática
      la orientación de los rodillos. Confirma el patrón real
      con el manual de las ruedas utilizadas.
```

### Cómo se combinan las velocidades

En una configuración Mecanum de cuatro ruedas, el controlador mezcla las
órdenes de avance, desplazamiento lateral y rotación. Cada rueda aporta
una componente de fuerza; la suma de las cuatro permite obtener el
movimiento deseado.

**Convención para la tabla:** `+` significa giro hacia delante según el
montaje y cableado del robot; `−` significa giro contrario. La
convención exacta puede invertirse según el motor, el montaje y el
patrón de rodillos. Las combinaciones siguientes corresponden a una
disposición Mecanum común en X.

  -------------------------------------------------------------------------
  Movimiento         Delantera      Delantera        Trasera        Trasera
                     izquierda        derecha      izquierda        derecha
  ------------- -------------- -------------- -------------- --------------
  Avanzar                   \+             \+             \+             \+

  Retroceder                 −              −              −              −

  Desplazarse a              −             \+             \+              −
  la izquierda                                               

  Desplazarse a             \+              −              −             \+
  la derecha                                                 

  Girar a la                 −             \+              −             \+
  izquierda                                                  
  sobre el                                                   
  centro                                                     

  Girar a la                \+              −             \+              −
  derecha sobre                                              
  el centro                                                  
  -------------------------------------------------------------------------

### Ventajas y limitaciones

**Ventajas** - Se desplaza hacia los lados y en diagonal sin cambiar la
orientación del chasis. - Puede girar sobre su centro. - Es útil en
pasillos y espacios reducidos.

**Limitaciones** - Necesita cuatro motores y un control coordinado. -
Los rodillos sufren desgaste y pueden vibrar. - Pierde eficiencia en
superficies rugosas, sueltas o con obstáculos. - La carga, el diámetro
de las ruedas y la geometría afectan el control.

## 5. Robot con dirección Ackermann

La geometría Ackermann es el principio de dirección utilizado por muchos
automóviles. Normalmente hay dos ruedas delanteras que cambian de ángulo
para dirigir el vehículo y dos ruedas traseras que permanecen
aproximadamente paralelas al chasis. La tracción puede estar en las
ruedas delanteras, traseras o en las cuatro, según el vehículo.

Durante una curva, la rueda interior recorre un círculo más pequeño que
la exterior. Por eso, ambas ruedas delanteras necesitan ángulos de
dirección distintos: la interior gira más que la exterior. Esta
geometría reduce el arrastre lateral de los neumáticos.

El **radio de giro** es la distancia entre el centro instantáneo de
rotación y un punto de referencia del vehículo, como el centro del eje
trasero. Depende de la distancia entre ejes y del ángulo de dirección.

Un vehículo Ackermann no puede desplazarse directamente hacia un costado
manteniendo la orientación porque sus ruedas están diseñadas para rodar
hacia delante o hacia atrás siguiendo trayectorias curvas. Para cambiar
su posición lateral debe describir una curva y, por lo general, avanzar
o retroceder.

### Diagrama de una curva

``` text
                       Dirección de avance
                              ↗
                 Rueda exterior  /
                     O----------/
                    /  Eje delantero
                   / 
                  /  O  Rueda interior
                 /
                /      . . . . . .
               /     .             .
              /    . Centro aprox.  .
             /     .   de giro  C   .
            /       .             .
           /          . . . . . .

   Esquema conceptual, no a escala:
   - La rueda interior gira con un ángulo mayor.
   - La rueda exterior gira con un ángulo menor.
   - Las trayectorias de ambas ruedas convergen hacia el
     centro instantáneo de giro C.
```

### Semejanzas y aplicaciones

Se parece a la dirección de un automóvil convencional: las ruedas
delanteras orientan el vehículo y el desplazamiento lateral se consigue
siguiendo una curva, no mediante una traslación lateral pura.

Se utiliza en automóviles, pequeños vehículos autónomos de reparto,
robots de investigación tipo automóvil, tractores autónomos y
plataformas de pruebas para conducción autónoma.

## 6. Comparación de configuraciones

  ---------------------------------------------------------------------------------------------------------
  Configuración   Número típico Movimiento   Giro sobre su  Complejidad   Complejidad   Aplicaciones
                      de ruedas lateral      eje            mecánica      de control    
                                directo                                                 
  --------------- ------------- ------------ -------------- ------------- ------------- -------------------
  Diferencial +      3 o más (2 No           Sí, si las     Baja          Baja          Robots educativos,
  castor             motrices y              ruedas giran                               seguidores de
                         apoyo)              en sentidos                                línea, transporte
                                             opuestos                                   sencillo

  Omni de 3                   3 Sí           Sí             Media         Media-alta    Plataformas
  ruedas                                                                                compactas de
                                                                                        investigación y
                                                                                        competencias

  Omni de 4                   4 Sí, si la    Sí, según el   Media         Media-alta    Plataformas móviles
  ruedas                        geometría lo diseño                                     omnidireccionales
                                permite                                                 

  Mecanum                     4 Sí           Sí             Media-alta    Alta          Almacenes,
                                                                                        laboratorios y
                                                                                        robots que
                                                                                        maniobran en
                                                                                        espacios reducidos

  Ackermann       4 normalmente No           No de forma    Media-alta    Media         Vehículos autónomos
                                             estacionaria                               y robots tipo
                                                                                        automóvil
  ---------------------------------------------------------------------------------------------------------

### ¿Qué configuración elegiría?

-   **Robot pequeño para aprender programación y control:** diferencial
    con rueda de castor, porque requiere pocos motores y sus movimientos
    son fáciles de entender.
-   **Robot para un almacén con espacios reducidos:** Mecanum si
    necesita maniobrar lateralmente; si la superficie es irregular o la
    carga es pesada, evaluaría ruedas convencionales por su robustez.
-   **Plataforma que se mueve lateralmente sin cambiar su orientación:**
    Mecanum u Omni, porque combinan componentes de fuerza para
    trasladarse de lado.
-   **Vehículo autónomo similar a un automóvil:** Ackermann, porque
    reproduce la geometría de dirección de un automóvil real.
-   **Competencia que requiere cambiar rápidamente de dirección:** Omni
    o Mecanum, siempre que el reglamento y el suelo sean compatibles.
-   **Robot móvil sencillo con solo dos motores:** diferencial con rueda
    de castor, porque cada motor controla una rueda motriz.

## 7. Análisis del movimiento

### Diferencial: ¿qué debe hacer cada rueda para girar sobre su propio eje?

Una rueda debe avanzar y la otra retroceder con velocidades parecidas.
Como las ruedas están separadas a ambos lados del centro del robot, cada
una produce una fuerza longitudinal en sentido contrario a la otra.
Estas fuerzas forman un par que hace rotar el chasis, mientras que sus
componentes de avance se compensan aproximadamente. Si las velocidades
no tienen la misma magnitud, además de girar el robot también se
desplazará.

### Omni: ¿por qué los rodillos permiten generar movimiento lateral?

Los rodillos pueden girar libremente en una dirección transversal a la
rodadura principal. Por eso, cuando el chasis se mueve lateralmente, no
es necesario que toda la banda de la rueda se arrastre sobre el suelo:
los rodillos giran y reducen la resistencia. Con varias ruedas colocadas
en ángulos distintos, el controlador combina las fuerzas que cada una
puede transmitir para crear una fuerza resultante lateral.

### Mecanum: ¿por qué se desplaza lateralmente aunque ninguna rueda apunte directamente hacia el costado?

Los rodillos inclinados transmiten fuerzas que tienen componentes tanto
longitudinales como laterales. Al coordinar el giro de las cuatro
ruedas, las componentes hacia delante pueden cancelarse y las
componentes laterales sumarse. Así, el chasis se desplaza de costado
aunque los ejes de las ruedas estén instalados en la dirección habitual
de avance.

### Ackermann: ¿por qué necesita avanzar o retroceder para cambiar de posición lateral?

Las ruedas están orientadas para rodar a lo largo de su plano y no
cuentan con rodillos laterales que permitan una traslación transversal.
Al girar las ruedas de dirección, el vehículo cambia la curvatura de su
trayectoria. Para alcanzar otra posición lateral, debe recorrer esa
curva hacia delante o hacia atrás; no puede trasladarse de lado
manteniendo la misma orientación como sí puede hacerlo una plataforma
Omni o Mecanum.

## 8. Aplicación en un robot real

### TurtleBot 3 Burger

-   **Fabricante/desarrollador:** ROBOTIS, en colaboración con la
    comunidad de robótica de código abierto.
-   **Tipo de locomoción:** diferencial.
-   **Número y tipo de ruedas:** dos ruedas motrices y una rueda de
    apoyo pasiva, según la configuración habitual.
-   **Sensores principales:** el conjunto puede incluir un sensor láser
    LDS para medir distancias, sensores de distancia y sensores internos
    del controlador; la configuración exacta depende de la versión.
-   **Actuadores:** dos motores con reductora y realimentación de
    posición para controlar las ruedas motrices.
-   **Aplicaciones:** educación, investigación, navegación autónoma,
    mapeo y experimentos con ROS.

La locomoción diferencial es adecuada para el TurtleBot 3 Burger porque
permite mantener un diseño compacto y relativamente económico. Dos
motores bastan para controlar avance, retroceso y giro; además, el robot
puede girar en pasillos estrechos. Aunque no puede desplazarse
lateralmente sin girar, esa limitación suele ser aceptable para tareas
educativas y de navegación.

**Imagen del robot:**\
![TurtleBot 3 
Burger](https://emanual.robotis.com/assets/images/platform/turtlebot3/overview/turtlebot3_burger.png)

*Fuente de la imagen y documentación técnica: ROBOTIS, TurtleBot3
e-Manual.*

## Reflexión final

La configuración que me pareció más sencilla de comprender fue la
diferencial con rueda de castor, porque se puede relacionar directamente
la velocidad de cada motor con el movimiento del robot. La que ofrece
mayor libertad de movimiento entre las estudiadas es la omnidireccional,
especialmente la Mecanum, ya que puede avanzar, retroceder, moverse
lateralmente, desplazarse en diagonal y girar sin tener que cambiar
primero la orientación del chasis.

Para construir mi primer robot móvil utilizaría una configuración
diferencial. Es económica, utiliza dos motores de tracción y permite
aprender conceptos esenciales como velocidad, dirección, control de
motores y lectura de sensores sin complicar demasiado la mecánica.

No existe una sola configuración adecuada para todos los robots porque
cada aplicación tiene requisitos diferentes. Un robot de almacén puede
necesitar maniobrar lateralmente, mientras que un vehículo autónomo debe
comportarse de manera parecida a un automóvil. También importan el
costo, la carga, la superficie, el espacio disponible, la precisión y la
facilidad de mantenimiento. La mejor elección es la que satisface las
necesidades reales de la tarea.

## Referencias

1.  Siegwart, R., Nourbakhsh, I. R. y Scaramuzza, D. (2011).
    *Introduction to Autonomous Mobile Robots* (2.ª ed.). MIT Press.
    https://mitpress.mit.edu/9780262015356/introduction-to-autonomous-mobile-robots/
2.  ROBOTIS. (s. f.). *TurtleBot3 e-Manual*. Documentación técnica de la
    plataforma TurtleBot3.
    https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/
3.  ROBOTIS. (s. f.). *TurtleBot3 Burger*. Información del modelo y
    componentes.
    https://emanual.robotis.com/docs/en/platform/turtlebot3/features/
4.  ROS 2 Documentation. (s. f.). *Differential drive controller*.
    Documentación del controlador de tracción diferencial.
    https://control.ros.org/
5.  NASA. (s. f.). *Robotics*. Información general sobre robótica y
    aplicaciones en exploración. https://www.nasa.gov/
6.  Mecanum Wheels. (s. f.). *Mecanum wheel basics and motion*. Para la
    entrega final, consulta también la hoja técnica del fabricante de
    las ruedas Mecanum que se utilicen, ya que la orientación y el
    sentido de giro pueden variar entre montajes.
7.  Campion, G., Bastin, G. y d'Andréa-Novel, B. (1996). Structural
    properties and classification of kinematic and dynamic models of
    wheeled mobile robots. *IEEE Transactions on Robotics and
    Automation, 12*(1), 47--62. https://doi.org/10.1109/70.481750

> **Recomendación:** antes de entregar, abre los enlaces, confirma los
> datos técnicos de la versión del robot que describas y agrega la fecha
> de consulta si tu docente la solicita. Los diagramas incluidos son
> esquemáticos; la orientación exacta de ruedas Omni y Mecanum depende
> del diseño concreto.
