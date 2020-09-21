#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    x = -5.5
    return abs(x)


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    list = []
    for letters in prefixes:
        list.append(letters + suffixes)
    return list


def prime_integer_summation() -> int:
    count = 0
    somme = 0
    liste_premiers = []
    for i in range(2,101):
        for z in range(2,101):
            if z <= i:
                if i % z == 0:
                    count += 1
        if count == 1:
            liste_premiers.append(i)
        count = 0

    for i in liste_premiers:
        somme += i
    return somme, liste_premiers

def factorial(number: int) -> int:
    factoriel = 1
    for i in range(1, number+1):
        factoriel *= i
    return factoriel


def use_continue() -> None:
    list = []
    for i in range(1,11):
        if i == 5:
            continue
        else:
            pass
        list.append(i)
    return list

def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est: {use_continue()}")


if __name__ == '__main__':
    main()
