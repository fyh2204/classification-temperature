#!/bin/python3

import os

def classify_temperature(temp):
    if temp < 15:
        return "Froid"
    elif temp < 25:
        return "Modéré"
    else:
        return "Chaud"

if __name__ == '__main__':
    temperature = float(input("Entrez la température en °C : ").strip())

    label = classify_temperature(temperature)
    print(f"La météo est : {label}")
