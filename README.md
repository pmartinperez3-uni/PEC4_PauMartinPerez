PEC4 - Análisis de LaLiga 1995-2025

Autor: Pau Martín Pérez
Asignatura: 22.503 · Programación para la Ciencia de Datos
Grado: Ciencia de Datos Aplicada — Estudios de Informática, Multimedia y Telecomunicación
Universitat Oberta de Catalunya (UOC)
Dataset: `LaLiga_Matches.csv` (1995-2025)


1. Descripción del proyecto

Este proyecto implementa el análisis de datos históricos de LaLiga española de fútbol desde la temporada 1995-96 hasta la 2025-26, utilizando un dataset con 11.664 partidos y las siguientes columnas:

Columna | Descripción
Season | Temporada (ej. "1995-96") 
Date | Fecha del partido 
HomeTeam | Equipo local 
AwayTeam | Equipo visitante 
FTHG | Full Time Home Goals (goles del local) 
FTAG | Full Time Away Goals (goles del visitante) 
FTR | Full Time Result (H=Local, A=Visitante, D=Empate) 
HTHG, HTAG , HTR | Datos al descanso (eliminados en el EDA) 

El análisis se compone de 7 ejercicios que abarcan desde la carga inicial y el análisis exploratorio hasta la construcción de un grafo de conexiones entre los equipos con más éxito histórico.


2. Estructura del proyecto

```
pec4/
├── src/
│   ├── main.py              # Punto de entrada principal con argparse
│   ├── config.py            # Variables globales (nom_alumne, date_time)
│   ├── exercises/
│   │   ├── __init__.py
│   │   ├── ex1.py           # Carga y EDA
│   │   ├── ex2.py           # Partidos totales
│   │   ├── ex3.py           # Distribución de goles
│   │   ├── ex4.py           # Resultados FTR
│   │   ├── ex5.py           # Clasificación global
│   │   ├── ex6.py           # Summary y podium
│   │   └── ex7.py           # Grafo de conexiones
│   ├── data/
│   │   └── LaLiga_Matches.csv
│   └── img/                 # Gráficas generadas
├── tests/
│   └── tests_ex6.py         # Tests unitarios para el ejercicio 6
├── doc/                     # Documentación generada con pydoc
├── screenshots/             # Capturas de pantalla con autoría
├── requirements.txt
├── LICENSE
└── README.md
```

3. Instalación

3.1. Requisitos previos

- Python 3.9 o superior
- pip

3.2. Crear entorno virtual e instalar requirements

```bash
- Crear entorno virtual
  python -m venv .venv

- Activar entorno virtual
  .venv\Scripts\activate     

- Instalar dependencias
  pip install -r requirements.txt
```

Requirements.txt:

```
pandas>=1.5.0
matplotlib>=3.6.0
networkx>=3.0
numpy>=1.23.0
```


4. Ejecución del proyecto

Desde la carpeta src/:

```bash
cd src

Ejecutar todos los ejercicios (1-7)
python main.py

Ejecutar solo hasta el ejercicio N
python main.py -ex 5

Mostrar la ayuda
python main.py -h
```

Las gráficas se guardan automáticamente en src/img/ con el formato:
grafica_exX_<nom_alumne>_<timestamp>.png


5. Resumen analítico de los ejercicios

- Ejercicio 1 — Carga del dataset y EDA

Se carga el CSV y se eliminan las columnas de tiempo de descanso (HTHG, HTAG, HTR). El dataset resultante contiene 11.664 partidos con 7 columnas.

Estadísticas clave:
- Goles medios del local (FTHG): 1.55
- Goles medios del visitante (FTAG): 1.12
- Máximo de goles del local en un partido: 10
- Máximo de goles del visitante en un partido: 8

El boxplot evidencia que la mediana de goles del local es mayor que la del visitante, confirmando la ventaja de jugar en casa.

- Ejercicio 2 — Partidos totales jugados

Para contar los partidos jugados por cada equipo se suman las apariciones como local (HomeTeam) y como visitante (AwayTeam) mediante value_counts() y add(fill_value=0).

Equipos siempre en Primera División (1158 partidos):

Equipo | Partidos 
Ath Bilbao | 1158 
Barcelona | 1158 
Real Madrid | 1158
Valencia | 1158 

Son los cuatro únicos clubes que nunca han descendido a Segunda División en el período 1995-2025.

- Ejercicio 3 — Distribución de goles

Se calcula la frecuencia de cada marcador con value_counts().sort_index(). El marcador más frecuente para el local es 1 gol. En cambio, para el visitante el marcador más frecuente es 0 goles. Las distribuciones son asimétricas con cola larga a la derecha.

- Ejercicio 4 — Resultados FTR

Resultado | Partidos 
H (gana local) | 5.500
A (gana visitante) | 3.172
D (empate) | 2.992 

Porcentaje de partidos ganados por el local: 47.15%, frente al 27.21% del visitante y al 25.64% de empates. Este es uno de los efectos estadísticos más estudiados del fútbol, que aunque deberia ser la mismo porcentaje entre local y visitante, existe una ventaja del local.

- Ejercicio 5 — Clasificación global 1995-2025

Aplicando el sistema de puntuación moderno de victoria = 3 pts, empate = 1 pt y derrota = 0 pts, mediante np.select con condiciones múltiples, se calculan los puntos acumulados por equipo.

Top 10 equipos por puntos acumulados:

Equipo | Puntos 
Barcelona | 2.483
Real Madrid | 2.458 
Ath Madrid | 1.898 
Valencia | 1.812 
Ath Bilbao | 1.631 
Sevilla | 1.572 
Sociedad | 1.464
Villarreal | 1.423
Betis | 1.369 
Espanol | 1.354 

El ganador histórico de LaLiga 1995-2025 es el Barcelona con 2.483 puntos, solo 25 puntos por delante del Real Madrid.

- Ejercicio 6 — Summary y Podium

Goles totales en 30 temporadas de LaLiga:
- Goles del local: 18.040 (~58%)
- Goles del visitante: 13.053 (~42%)
- Total: 31.093 goles

El DataFrame summary combina puntos y goles por equipo. El podio histórico está formado por Barcelona (oro), Real Madrid (plata) y Atlético de Madrid (bronce).

- Ejercicio 7 — Grafo de conexiones

Se selecciona el top 5 (Barcelona, Real Madrid, Ath Madrid, Valencia, Ath Bilbao) y se construye un grafo no dirigido con networkx. Los 4 equipos que siempre han estado en Primera tienen 60 enfrentamientos directos entre sí, es decir, 2 partidos × 30 temporadas. El Atlético tiene 56 con cada uno, debido a su descenso a Segunda en la temporada 2000-01.


6. Comprobación del linting (Pylint)

Pylint es la herramienta usada en la asignatura para verificar la calidad del código. Para ejecutarla:

```bash
pip install pylint

cd src
pylint exercises/ config.py main.py
```

Para personalizar la configuración:

```bash
pylint --generate-rcfile > .pylintrc
```

El código actual tiene una puntuación de 6.35 sobre 10. 


7. Generación de la documentación (pydoc)

Para generar la documentación HTML de los módulos:

```bash
cd src
python -m pydoc -w exercises.ex1 exercises.ex2 exercises.ex3 \
    exercises.ex4 exercises.ex5 exercises.ex6 exercises.ex7
mv *.html ../doc/
```

Para visualizar la documentación en el navegador en modo servidor:

```bash
python -m pydoc -b
```


8. Ejecución de los tests

Los tests del ejercicio 6 cubren la función fun_total_goals con 5 casos: goles de local, goles de visitante, suma total, tipos de retorno y comportamiento ante un DataFrame vacío.

```bash
cd tests
python -m unittest tests_ex6.py -v

```

Salida esperada: `Ran 5 tests in 0.00Xs - OK`


9. GitHub

Para subir el proyecto a un repositorio de GitHub:

```bash
git init
git add .
git commit -m "PEC4 - Análisis de LaLiga 1995-2025"
git branch -M main
git remote add origin https://github.com/pmartinperez3-uni/PEC4_PauMartinPerez.git
git push -u origin main
```


10. Referencias y bibliografía

Materiales de la asignatura

- Subirats Maté, L., Calvo González, M. Programación para la Ciencia de Datos. Materiales docentes UOC.
- Apuntes del módulo de testing, despliegue y mantenimiento de la asignatura.

Dataset

- LaLiga Results 1995-2020 dataset disponible en Kaggle:
  https://www.kaggle.com/datasets/kishan305/la-liga-results-19952020
  Extendido hasta 2025 para esta práctica.

Documentación oficial de las librerías

- pandas: https://pandas.pydata.org/docs/ — Manejo de DataFrames, groupby, value_counts, concat, add(fill_value).
- NumPy: https://numpy.org/doc/stable/ — Función np.select usada para asignar puntos según condiciones múltiples en el Ejercicio 5.
- Matplotlib: https://matplotlib.org/stable/contents.html — Gráficas de boxplot, barras y configuración de figuras.
- NetworkX: https://networkx.org/documentation/stable/ — Construcción de grafos, circular_layout, draw_networkx_.

Recursos adicionales consultados

- McKinney, W. (2022). Python for Data Analysis (3rd ed.). O'Reilly Media. Capítulos sobre groupby y agregaciones para los ejercicios 5 y 6.
- Hagberg, A., Schult, D., Swart, P. (2008). Exploring network structure, dynamics, and function using NetworkX. Referencia base para el ejercicio 7.
- Documentación oficial de Pylint: https://pylint.readthedocs.io/ — Convenciones de estilo y mejoras de calidad de código.
- Documentación de pydoc: https://docs.python.org/3/library/pydoc.html — Generación automática de documentación.
- Documentación de unittest: https://docs.python.org/3/library/unittest.html — Marco de testing usado en tests_ex6.py.


11. Licencia

Este proyecto está distribuido bajo licencia MIT License. Ver el fichero [`LICENSE`](LICENSE) para los detalles completos.


Pau Martín Pérez — PEC4 — UOC 2026

