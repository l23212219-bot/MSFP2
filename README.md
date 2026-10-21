[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=l23212219-bot/MSFP2)

# Práctica 2: Modelado y control del sistema cardiovascular

Repositorio correspondiente a la **Práctica 2 de Modelado de Sistemas Fisiológicos**, enfocada en la representación matemática y computacional del sistema cardiovascular mediante una analogía eléctrica RLC.

En esta práctica se estudian tres condiciones cardiovasculares —**hipotensión, normotensión e hipertensión**— mediante modelos de función de transferencia. Posteriormente, se implementan controladores PID para modificar la respuesta de los modelos hipotenso e hipertenso y aproximarla al comportamiento del sistema normotenso.

Las simulaciones se desarrollan y comparan utilizando **MATLAB, Simulink y Python**.

---

## Información académica

**Estudiante:** Sergio Andree Navarro Rodriguez  
**Número de control:** 23212219  
**Correo:** l23212219@tijuana.tecnm.mx  

**Asignatura:** Modelado de Sistemas Fisiológicos  
**Carrera:** Ingeniería Biomédica  

### Docente

**Dr. Paul Antonio Valle Trujillo**  
paul.valle@tectijuana.edu.mx  

Departamento de Ingeniería Eléctrica y Electrónica  
Tecnológico Nacional de México / Instituto Tecnológico de Tijuana  
Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

---

## Descripción de la asignatura

El modelado de sistemas fisiológicos permite representar mediante herramientas matemáticas, eléctricas y computacionales el comportamiento dinámico de diferentes procesos del cuerpo humano.

Dentro de Ingeniería Biomédica, estas técnicas permiten integrar conocimientos de **fisiología, electrónica, matemáticas, programación e ingeniería de control** para analizar sistemas biológicos, predecir su comportamiento y evaluar estrategias de control mediante experimentación *in silico*.

En esta asignatura se utilizan analogías entre sistemas fisiológicos y circuitos eléctricos RLC para obtener modelos matemáticos, funciones de transferencia y simulaciones computacionales que permitan estudiar la dinámica de los sistemas fisiológicos bajo diferentes condiciones.

---

## Objetivos de la práctica

1. Representar el comportamiento del sistema cardiovascular mediante una analogía eléctrica.

2. Obtener la función de transferencia correspondiente al modelo cardiovascular.

3. Analizar los polos y el comportamiento dinámico del sistema.

4. Modelar diferentes condiciones cardiovasculares modificando los parámetros del modelo.

5. Simular las condiciones de un individuo **hipotenso, normotenso e hipertenso**.

6. Comparar las respuestas de los tres modelos en lazo abierto.

7. Utilizar el modelo normotenso como referencia para el diseño del sistema de control.

8. Implementar controladores PID para los modelos hipotenso e hipertenso.

9. Comparar las respuestas en lazo abierto y lazo cerrado.

10. Implementar y contrastar el modelo utilizando **MATLAB, Simulink y Python**.

---

# Modelo del sistema cardiovascular

El sistema cardiovascular puede representarse de forma simplificada mediante una analogía entre variables fisiológicas y componentes de un circuito eléctrico.

En el modelo utilizado en esta práctica se consideran los parámetros:

| Parámetro | Interpretación en el modelo |
|:---:|---|
| **R** | Resistencia vascular al flujo sanguíneo |
| **L** | Inertancia asociada al movimiento de la sangre |
| **C** | Capacitancia o *compliance* vascular |
| **Z** | Impedancia característica del sistema |

La **resistencia vascular** representa la oposición que encuentra la sangre al desplazarse por los vasos.

La **inertancia** representa la tendencia de la masa sanguínea a oponerse a cambios rápidos en su movimiento.

La **compliance vascular** representa la capacidad de los vasos sanguíneos para expandirse y almacenar volumen cuando cambia la presión.

Mediante estos elementos es posible construir un modelo dinámico que relacione una señal de entrada con la respuesta cardiovascular del sistema.

---

## Representación del sistema

![Representación del sistema cardiovascular](Biorender.jpeg)

---

# Función de transferencia

La función de transferencia utilizada para representar el sistema cardiovascular es:

$$
H(s)=
\frac{LRs+RZ}
{CLRZs^2+(LR+LZ)s+ZR}
$$

donde:

- \(R\) = resistencia.
- \(L\) = inertancia.
- \(C\) = capacitancia o *compliance*.
- \(Z\) = impedancia característica.
- \(s\) = variable compleja de Laplace.

La expresión corresponde a un sistema dinámico de **segundo orden**, cuyos polos pueden calcularse a partir de las raíces del denominador.

---

# Condiciones cardiovasculares

Para estudiar el efecto que tienen las propiedades del sistema sobre su respuesta dinámica se implementan tres conjuntos de parámetros.

| Condición | \(Z\) | \(R\) | \(L\) | \(C\) |
|---|---:|---:|---:|---:|
| **Hipotenso** | 0.01 | 1.000 | 0.001 | 3.500 |
| **Normotenso** | 0.01 | 1.000 | 0.001 | 1.500 |
| **Hipertenso** | 0.010 | 1.00 | 0.001 | 1.000 |

La principal modificación realizada entre los tres modelos corresponde al parámetro \(C\).

De esta forma pueden compararse las respuestas de los sistemas bajo diferentes condiciones y analizar cómo una variación de las propiedades del modelo modifica su comportamiento dinámico.

El modelo **normotenso** se utiliza como condición de referencia.

---

# Simulación en lazo abierto

La simulación comienza utilizando la señal almacenada en:

```text
signal.xlsx
```

La señal es remuestreada para trabajar en un intervalo de:

$$
0 \leq t \leq 15\;s
$$

con un paso de simulación de:

$$
\Delta t=1\times10^{-3}\;s
$$

Posteriormente se calculan las respuestas correspondientes a:

- Individuo hipotenso.
- Individuo normotenso.
- Individuo hipertenso.

Estas respuestas permiten observar las diferencias entre los modelos antes de aplicar algún sistema de control.

El resultado comparativo generado en Python se almacena en:

```text
Individuos_python.pdf
```

---

# Control PID

Después de analizar las respuestas en lazo abierto, se implementa un controlador **PID (Proporcional-Integral-Derivativo)**.

La forma general de un controlador PID es:

$$
C(s)=K_P+\frac{K_I}{s}+K_Ds
$$

donde:

- \(K_P\) corresponde a la acción proporcional.
- \(K_I\) corresponde a la acción integral.
- \(K_D\) corresponde a la acción derivativa.

El objetivo del controlador es modificar la respuesta de los sistemas hipotenso e hipertenso para aproximarla al comportamiento del individuo normotenso.

---

## Control del sistema hipotenso

Las ganancias utilizadas son:

| Ganancia | Valor |
|:---:|---:|
| \(K_P\) | 458.483 |
| \(K_I\) | 1,118,300.387 |
| \(K_D\) | 0.00627 |

Se compara:

- Respuesta del individuo hipotenso.
- Respuesta del individuo normotenso.
- Respuesta del individuo hipotenso con controlador PID.

El resultado generado en Python se almacena en:

```text
hipotenso_python.pdf
```

---

## Control del sistema hipertenso

Las ganancias utilizadas son:

| Ganancia | Valor |
|:---:|---:|
| \(K_P\) | 126.595 |
| \(K_I\) | 293,327.703 |
| \(K_D\) | 0.00140 |

Se compara:

- Respuesta del individuo hipertenso.
- Respuesta del individuo normotenso.
- Respuesta del individuo hipertenso con controlador PID.

El resultado generado en Python se almacena en:

```text
Hipertenso_python.pdf
```

---

# Metodología general

El desarrollo de la práctica sigue el siguiente flujo:

```text
Señal de entrada
      │
      ▼
Modelo matemático cardiovascular
      │
      ▼
Obtención de funciones de transferencia
      │
      ▼
 ┌────────────┬─────────────┬─────────────┐
 │ Hipotenso  │ Normotenso  │ Hipertenso  │
 └────────────┴─────────────┴─────────────┘
      │
      ▼
Comparación en lazo abierto
      │
      ▼
Diseño y sintonización PID
      │
      ├───────────────┐
      ▼               ▼
PID hipotenso     PID hipertenso
      │               │
      └───────┬───────┘
              ▼
Comparación con el modelo normotenso
              │
              ▼
       Análisis de resultados
```

---

# Implementación computacional

La práctica se desarrolla mediante tres herramientas principales.

### MATLAB

El cuaderno:

```text
Navarro23212219.mlx
```

contiene el desarrollo computacional realizado en MATLAB.

También se incluye su versión exportada:

```text
Navarro23212219.pdf
```

El botón ubicado al inicio de este README permite abrir el repositorio directamente en **MATLAB Online**.

### Simulink

El archivo:

```text
sistem.slx
```

contiene la implementación gráfica del modelo mediante bloques de Simulink.

### Python

El archivo:

```text
Navarro23212219.py
```

implementa:

- Lectura de la señal de entrada.
- Remuestreo de la señal.
- Construcción de las funciones de transferencia.
- Cálculo de los polos.
- Simulación de las condiciones cardiovasculares.
- Simulación en lazo abierto.
- Implementación de los controladores PID.
- Simulación en lazo cerrado.
- Generación y exportación de las gráficas.

---

# Estructura del repositorio

| Archivo | Descripción |
|---|---|
| `Navarro23212219.mlx` | Cuaderno computacional principal de MATLAB |
| `Navarro23212219.pdf` | Versión PDF del cuaderno de MATLAB |
| `Navarro23212219.py` | Implementación del modelo y control PID en Python |
| `sistem.slx` | Modelo desarrollado en Simulink |
| `signal.xlsx` | Señal utilizada como entrada para las simulaciones |
| `Análisis matemático.pdf` | Desarrollo matemático del modelo cardiovascular |
| `Biorender.jpeg` | Representación gráfica del sistema cardiovascular |
| `Individual_matlab.pdf` | Comparación de individuos obtenida en MATLAB |
| `Individuos_python.pdf` | Comparación de individuos obtenida en Python |
| `Normotenso_matlab.pdf` | Resultado correspondiente al caso normotenso en MATLAB |
| `Hipotenso_matlab.pdf` | Resultado del caso hipotenso en MATLAB |
| `Hipertenso_matlab.pdf` | Resultado del caso hipertenso en MATLAB |
| `hipotenso_python.pdf` | Respuesta del sistema hipotenso y su controlador en Python |
| `Hipertenso_python.pdf` | Respuesta del sistema hipertenso y su controlador en Python |
| `hipotensoparametros.jpeg` | Parámetros utilizados para el control del sistema hipotenso |
| `hipertensoparametros.jpeg` | Parámetros utilizados para el control del sistema hipertenso |
| `LICENSE` | Licencia del repositorio |

---

# Requisitos

## MATLAB

Para ejecutar los archivos de MATLAB se requiere:

- MATLAB.
- Simulink.
- Herramientas necesarias para trabajar con funciones de transferencia y sistemas de control.

También es posible abrir el proyecto mediante **MATLAB Online** utilizando el botón ubicado al inicio del README.

---

## Python

El código utiliza las siguientes bibliotecas:

```text
numpy
pandas
scipy
matplotlib
control
openpyxl
```

Pueden instalarse mediante:

```bash
pip install numpy pandas scipy matplotlib control openpyxl
```

---

# Ejecución en Python

Clonar el repositorio:

```bash
git clone https://github.com/l23212219-bot/MSFP2.git
```

Entrar en la carpeta:

```bash
cd MSFP2
```

Ejecutar:

```bash
python Navarro23212219.py
```

El archivo:

```text
signal.xlsx
```

debe permanecer en el mismo directorio que el programa de Python para que pueda ser leído correctamente.

Al finalizar la simulación se generan las gráficas correspondientes a las condiciones cardiovasculares y a los sistemas controlados.

---

# Resultados

El proyecto permite comparar el comportamiento dinámico de los tres modelos cardiovasculares y visualizar el efecto producido por los controladores PID.

Los principales resultados corresponden a:

1. Respuesta en lazo abierto de los individuos hipotenso, normotenso e hipertenso.
2. Comparación entre el individuo hipotenso y el sistema hipotenso controlado.
3. Comparación entre el individuo hipertenso y el sistema hipertenso controlado.
4. Análisis de la aproximación de los sistemas controlados hacia la respuesta del modelo normotenso.
5. Comparación de las implementaciones realizadas en MATLAB y Python.

---

## Palabras clave

`Sistema cardiovascular` · `Modelado fisiológico` · `Circuito RLC` · `Función de transferencia` · `Control PID` · `Hipotensión` · `Normotensión` · `Hipertensión` · `MATLAB` · `Simulink` · `Python` · `Ingeniería Biomédica`

---

# Referencia

[1] P. A. Valle, *Syllabus para Modelado de Sistemas Fisiológicos*, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México.

---

# Licencia

Este repositorio se distribuye bajo la licencia **BSD 2-Clause**. Para más información, consultar el archivo [`LICENSE`](LICENSE).
