#!/usr/bin/env python
# encoding: utf-8
import math
import rand_generator

# Classe para geração de números aleatórios segundos várias distribuições
# Apenas a distribuição exponencial negativa está definida


def exponencial(media, stream):
	"""Gera um número segundo uma distribuição exponencial negativa de média m"""
	#return (-media*math.log(random.random()))
	return (-media*math.log(rand_generator.rand(stream)))

def normal(m, d, stream):
	v1 = 2 * rand_generator.rand(stream) - 1
	v2 = 2 * rand_generator.rand(stream) - 1
	
	w = pow(v1,2) + pow(v2,2)
	
	if w > 1 or w == 0:
		return normal(m, d, stream)
	
	y1 = v1 * math.sqrt((-2 * math.log(w)) / w)
	y2 = v2 * math.sqrt((-2 * math.log(w)) / w)
	
	return (m + y1 *d, m + y2 * d)