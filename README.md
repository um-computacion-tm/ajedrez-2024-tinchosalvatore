# ajedrez-2024-tinchosalvatore
Proyecto de Ajedrez en Python Orientado a Objetos realizado por Martin Salvatore.
Legajo 63181

## Reglamento
El juego es un ajedrez completo, excepto porque no hay jaque mate, ni enroque.
La forma de que termine la partida es capturar el rey contrario

## Como ejecutar
El juego no cuenta con interfaz gráfica, por lo que se ejecuta desde la línea de comandos.

## Ejecucion usando Docker
Para ejecutar el juego usando Docker, antes debes instalar Docker en tu computadora.
Una vez instalado Docker, puedes ejecutar el juego con los siguientes comandos:

### Comandos:

#### Crear imagen Docker
```
$ sudo docker buildx build -t ajedrez --no-cache .
```
#### Para ejecutar el juego
```
$ sudo docker run -i ajedrez
```

# :books: Documentación
## CHANGELOG
El changelog contiene una lista de las versiones del proyecto, con los cambios, eliminaciones y adiciones realizados en cada versión.

## Comentarios en el codigo
En el codigo se pueden encontrar comentarios en inglés, para ayudar a los usuarios a entender mejor el funcionamiento del juego.

# :hammer_and_wrench: Herramientas de correccion utilizadas en este proyecto

## CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-tinchosalvatore/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-tinchosalvatore/tree/main)

## :mountain_snow: Code Climate

### Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/45a1254696619ce5a5c1/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-tinchosalvatore/maintainability)

### Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/45a1254696619ce5a5c1/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-tinchosalvatore/test_coverage)