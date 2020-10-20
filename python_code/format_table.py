#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
#  format.py
#
ListasAlumnos = [['Juan', 'Carmelo', 5, 7, 9, 7], ['Laura', 'Jazmine', 7, 8, 5, 6.66],
 ['Dario', 'Villalobos', 5, 6, 3, 4.66], ['Marito', 'Tasolo', 4, 7, 9, 6.666],
  ['Esteban', 'Quito', 9, 9, 8, 8.66]]
Tabla = """\
+---------------------------------------------------------------------+
| Nombre    Apellido        Primero Segundo Tercero     Promedio anual|
|---------------------------------------------------------------------|
{}
+---------------------------------------------------------------------+\
"""
Tabla = (Tabla.format('\n'.join("| {:<8} {:<10} {:>8} {:>6} {:>7} {:>23} |".format(*fila)
 for fila in ListasAlumnos)))
print (Tabla)