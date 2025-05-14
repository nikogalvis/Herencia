---
title: Juego de Blackjack
---
classDiagram
    Mano "1" --* "1"Jugador
    Carta "52" --* "1" Baraja
    Baraja : +list< carta > 
    Baraja: +repartir() carta
    Baraja "1" --* "1" BlackJack
    Jugador "2" --> "1" BlackJack
    

    class Mano{
        +list < carta >
        +int valor
        +mayorque21(valor)
    }    
    class BlackJack{
        +Baraja Baraja
    }

    class Carta{
      +str palo 
      +int valor
    }

    class Jugador{
      +pedir() void
      +mantenerse() void

    }
