# Modulo_4_Desafio_2.1

El prototipo debe desarrollarse utilizando una aplicación de consola escrita en Python, que
conste de un script principal que ejecute el juego, y una clase que permita crear personajes,
que debe ser importada en el script principal. Las opciones de juego del usuario, así como el
nombre de su personaje, se deben solicitar mediante input.

La clase que permite crear personajes debe considerar lo siguiente:
- Cada personaje tiene un nombre, el cual debe ser especificado al momento de crear
un personaje.
- Cada personaje recién creado tiene nivel 1 y experiencia 0 (estos son los únicos
valores posibles al momento de crear un personaje).
- A cada personaje es posible consultarle o asignarle un estado. Al solicitar el estado
de un personaje, se debe mostrar en pantalla su nombre, su nivel y su experiencia. Al
asignar un valor al estado, este valor corresponderá a la experiencia recibida por el
personaje. Según la experiencia recibida, se debe modificar la experiencia actual del
personaje y su nivel de acuerdo a lo siguiente:
- Los valores posibles de experiencia son entre 0 y 99 inclusive.
- El nivel mínimo es 1 y no hay máximo.
- Cada 100 puntos de experiencia recibidos, el personaje sube 1 nivel (su nivel
aumenta en 1). Ejemplo: El personaje tiene actualmente nivel 1 y experiencia
- Si se asigna 250 a su estado, pasará a tener nivel 3 y experiencia 50.
- Si la experiencia recibida es negativa, se debe restar a la experiencia actual
del personaje. Cada vez que la experiencia sea menor a 0, el personaje baja
de nivel (su nivel disminuye en 
1). Ejemplo: El personaje tiene actualmente
nivel 3 y experiencia 50. Si se asigna -150 a su estado, pasará a tener nivel 2 y
experiencia 0. Si el personaje ya tiene nivel 1 y experiencia 0, no se altera su
nivel ni su experiencia al recibir experiencia negativa


------------------------------------------

## Prerequisitos

- Sistema Operativos: Windows 10, 11, Linux, iOS
- Python 3.12

## Ejecución

***Windows***

`python juego.py`

***Linux & iOS***

`python3 juego.py`

------------------------------------------
## Colaboradores
- [Francisco Colomer](https://github.com/Cy5k0) 
- [Francisco Monroy](https://github.com/fmonroy75)
- [Natalia Peña](https://github.com/StudentNPD)
