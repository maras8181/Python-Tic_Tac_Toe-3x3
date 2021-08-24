Engeto: Project 2
===

Popis programu
---

Popis zadání
---
Cílem této hry je umístit 3 hrací kameny (křížek X nebo kolečko O), a to horizontálně, vertikálně nebo diagonálně. Jde o hru pro dva hráče (příp. počítač)

Program obsahuje následující:
1.  Program pozdraví uživatele
2.  Vypíše v krátkosti pravidla hry
3.  Zobrazí hrací plochu
4.  Vyzve prvního hráče, aby zvolil pozici pro umístění hracího kamene
5.  Pokud hráč zadá jiné číslo, než je nabídka hracího pole, program jej upozorní.
6.  Pokud hráč zadá jiný vstup, než číselný, program jej opět upozorní.
7.  Pokud se na vybraném poli nachází hrací kámen druhého hráče, program jej upozorní, že je pole obsazené
8.  Jakmile hráč úspěšně vybere pole, zobrazíme nový stav hrací plochy
9.  Program vyhodnocuje, jestli horizontálně/vertikálně/diagonálně není některý hrací kámen tříkrát. Pokud ano, vyhrává hráč, kterému tyto tři kameny patří
10. Pokud nezbývá žádné volné hrací pole a žádný hráč nevyhrál, jde o remízu.

Program po spuštění:

```
Welcome to Tic Tac Toe
========================================
              GAME RULES:               
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
          Let's start the game          
----------------------------------------
             +---+---+---+              
             |   |   |   |              
             +---+---+---+              
             |   |   |   |              
             +---+---+---+              
             |   |   |   |              
             +---+---+---+              
Player X | Please enter your move number: 3
             +---+---+---+              
             |   |   | X |              
             +---+---+---+              
             |   |   |   |              
             +---+---+---+              
             |   |   |   |              
             +---+---+---+              
Player O | Please enter your move number: abc
ValueError: Your entry is not a number.
             +---+---+---+              
             |   |   | X |              
             +---+---+---+              
             |   |   |   |              
             +---+---+---+              
             |   |   |   |              
             +---+---+---+              
Player O | Please enter your move number: 4
             +---+---+---+              
             |   |   | X |              
             +---+---+---+              
             | O |   |   |              
             +---+---+---+              
             |   |   |   |              
             +---+---+---+              
Player X | Please enter your move number: 6
             +---+---+---+              
             |   |   | X |              
             +---+---+---+              
             | O |   | X |              
             +---+---+---+              
             |   |   |   |              
             +---+---+---+              
Player O | Please enter your move number: 6
This field is occupied. Try it again...
             +---+---+---+              
             |   |   | X |              
             +---+---+---+              
             | O |   | X |              
             +---+---+---+              
             |   |   |   |              
             +---+---+---+              
Player O | Please enter your move number: 8
             +---+---+---+              
             |   |   | X |              
             +---+---+---+              
             | O |   | X |              
             +---+---+---+              
             |   | O |   |              
             +---+---+---+              
Player X | Please enter your move number: 9
             +---+---+---+              
             |   |   | X |              
             +---+---+---+              
             | O |   | X |              
             +---+---+---+              
             |   | O | X |              
             +---+---+---+              
========================================
        Player X won. Game Over.        
========================================
```
