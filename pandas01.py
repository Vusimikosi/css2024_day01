#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 21:41:45 2024

@author: vusani
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

print(file.info())

print(file.describe())

import pandas
file = pandas.read_csv("iris.csv")

print(file)

print(file.info())

print(file.describe())

import pandas

file = pandas.read_csv("insurance_data.csv",'skiprows5')

print(file)

print(file.info())

print(file.describe())

import pandas

file = pandas.read_csv("diab_data.csv")

print(file)
print(file.info())
print(file.describe())