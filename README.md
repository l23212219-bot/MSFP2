[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=l23212219-bot/MSFP2)

# Práctica 2: Modelo del sistema cardiovascular

## Información del estudiante

Sergio Andree Navarro Rodriguez; 23212219; [l23212219@tijuana.tecnm.mx]

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente

Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, ya que permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos. Se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos.

Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas, con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional.

Lo anterior se logra al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante experimentación *in silico* brinda herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: utilizar las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, integrando los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano, con el objetivo de modelizar, analizar, controlar, ilustrar y predecir la dinámica de sistemas fisiológicos complejos.

## Objetivos

1. Representar el comportamiento dinámico del sistema cardiovascular mediante una analogía eléctrica basada en elementos RLC.
2. Obtener la función de transferencia correspondiente al modelo cardiovascular.
3. Analizar los polos y la estabilidad del sistema.
4. Modelizar diferentes condiciones cardiovasculares mediante la modificación de los parámetros del circuito.
5. Simular las respuestas correspondientes a un individuo hipotenso, normotenso e hipertenso.
6. Comparar el comportamiento de las diferentes condiciones cardiovasculares mediante simulaciones en MATLAB y Python.
7. Diseñar y sintonizar controladores PID para modificar la respuesta de los modelos hipotenso e hipertenso.
8. Utilizar como referencia el comportamiento del individuo normotenso para evaluar la respuesta de los sistemas controlados.
9. Obtener y comparar las respuestas en lazo abierto y lazo cerrado.
10. Implementar el modelo computacional mediante MATLAB, Simulink y Python.

## Descripción detallada del sistema

El sistema cardiovascular puede representarse mediante una analogía eléctrica en la que diferentes propiedades del flujo sanguíneo y de los vasos sanguíneos se relacionan con los componentes de un circuito eléctrico.

En el modelo utilizado, la resistencia **R** representa la oposición al flujo sanguíneo producida por el sistema vascular, mientras que la capacitancia **C** representa la distensibilidad o *compliance* de los vasos sanguíneos, es decir, su capacidad para almacenar volumen de sangre cuando cambia la presión.

La inductancia **L** representa la inertancia de la sangre, asociada con la resistencia del fluido a cambios rápidos en su velocidad. El parámetro **Z** representa una impedancia característica asociada con el comportamiento del sistema vascular.

A partir de estos parámetros se construye una función de transferencia que permite estudiar la respuesta dinámica del sistema cardiovascular. En esta práctica se consideran tres condiciones fisiológicas:

- **Hipotenso:** representa una condición de presión arterial inferior a la condición de referencia.
- **Normotenso:** representa el comportamiento considerado normal y se utiliza como referencia para el sistema.
- **Hipertenso:** representa una condición de presión arterial superior a la condición de referencia.

Las tres condiciones se obtienen mediante cambios en los parámetros del modelo, principalmente en la capacitancia vascular, permitiendo observar cómo las modificaciones en las propiedades del sistema cardiovascular afectan su respuesta dinámica.

La función de transferencia empleada en las simulaciones se construye a partir de los parámetros \(Z\), \(R\), \(L\) y \(C\):

\[
H(s)=
\frac{LRs+RZ}
{CLRZs^2+(LR+LZ)s+ZR}
\]

Para realizar las simulaciones se utilizan los siguientes conjuntos de parámetros:

| Condición | Z | R | L | C |
|---|---:|---:|---:|---:|
| Hipotenso | 0.01 | 1.000 | 0.001 | 3.500 |
| Normotenso | 0.01 | 1.000 | 0.001 | 1.500 |
| Hipertenso | 0.010 | 1.00 | 0.001 | 1.000 |

El modelo normotenso funciona como referencia. Posteriormente se aplican controladores PID a los modelos hipotenso e hipertenso con el propósito de reducir la diferencia entre sus respuestas y la respuesta correspondiente al individuo normotenso.

Para el sistema hipotenso se utilizan las ganancias:

\[
K_P=458.483
\]

\[
K_I=1118300.387
\]

\[
K_D=0.00627
\]

Para el sistema hipertenso se utilizan:

\[
K_P=126.595
\]

\[
K_I=293327.703
\]

\[
K_D=0.00140
\]

De esta manera es posible comparar el comportamiento del sistema antes y después de aplicar el controlador, evaluando la capacidad del control PID para aproximar las condiciones alteradas al comportamiento del modelo normotenso.

**Palabras clave:** Circuito RLC; Sistema cardiovascular; Hipotensión; Normotensión; Hipertensión; Controlador PID; Función de transferencia; Modelo matemático; MATLAB; Simulink; Python; Simulación numérica.

## Lista de archivos incluidos en el repositorio

1. Cuaderno computacional de MATLAB:
   - `Navarro23212219.mlx`
   - `Navarro23212219.pdf`

2. Modelo de Simulink:
   - `sistem.slx`

3. Código de Python:
   - `Navarro23212219.py`

4. Archivo con la señal utilizada en las simulaciones:
   - `signal.xlsx`

5. Análisis matemático del modelo:
   - `Análisis matemático.pdf`

6. Diagrama o representación del sistema cardiovascular:
   - `Biorender.jpeg`

7. Resultados de las simulaciones realizadas en MATLAB:
   - `Individual_matlab.pdf`
   - `Normotenso_matlab.pdf`
   - `Hipotenso_matlab.pdf`
   - `Hipertenso_matlab.pdf`

8. Resultados de las simulaciones realizadas en Python:
   - `Individuos_python.pdf`
   - `hipotenso_python.pdf`
   - `Hipertenso_python.pdf`

9. Imágenes con los parámetros utilizados para los controladores:
   - `hipotensoparametros.jpeg`
   - `hipertensoparametros.jpeg`

10. Archivo de licencia:
   - `LICENSE`

## Software utilizado

- MATLAB
- Simulink
- Python
- NumPy
- Pandas
- SciPy
- Matplotlib
- Python Control Systems Library

## Referencias

\[1] P. A. Valle, *Syllabus para Modelado de Sistemas Fisiológicos*, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México.
