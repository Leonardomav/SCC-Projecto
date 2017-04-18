#!/usr/bin/env python
# encoding: utf-8
import random
import math

# Classe para geração de números aleatórios segundos várias distribuições
# Apenas a distribuição exponencial negativa está definida


def exponencial(media):
	"""Gera um número segundo uma distribuição exponencial negativa de média m"""
	return (-media*math.log(random.random()))

#print Aleatorio().exponencial(2) #test