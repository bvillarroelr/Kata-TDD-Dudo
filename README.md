# Kata TDD: Simulador de Dudo chileno
Simulador del juego de apuestas Dudo, siguiendo los principios de TDD. Las reglas del juego fueron extraidas de https://www.donpichuncho.cl/aprende-a-jugar-dudo-en-cacho

# Instalación y uso
Para la instalación de dependencias, utilizamos el entorno virtual de pipenv, en caso de no tenerlo instalado, ejecutar el siguiente comando:
``
pip install pipenv
``

Luego, para instalar las dependencias provenientes del Pipfile:

```
pipenv install
```

Y finalmente, activar el entorno virtual:
```
pipenv shell
```

Ahora se pueden ejecutar los test con normalidad.

```
pytest
```

Para ver el coverage:
```
pytest --cov=src --cov-report=term-missing
```

# Integrantes
Andrés Ignacio Chaparro Maldonado
Benjamín Cristóbal Villarroel Rubio