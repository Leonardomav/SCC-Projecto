#!/usr/bin/env python
# encoding: utf-8
class Lista:
	"""Classe que contém, em cada instante, os eventos a serem executados, ordenados por instantes de ocorrência crescentes.
	Funciona como uma agenda."""
	
	#Construtor
	def __init__(self,sim):
		self.simulator=sim #Simulador a que pertence a lista de eventos
		self.list = []

	def __str__(self):
		"""Método informativo apenas. Imprime o conteúdo da lista de eventos em cada instante"""
		s = "["+str(self.simulator.instant)+"] List:\n"
		for i in range(len(self.list)):
			s = s+"\t["+str(i+1)+"] "+str(self.list[i])+"\n"
		return s
	
	#Método para inserir um evento na lista de eventos
	def insert_event(self,event):
		self.list.append(event)	#coloca o evento na lista
		self.list.sort(key=lambda x: x.instant)		#ordena a lista ##100 vezes mais simples que java!

	def remove_event(self):
		return self.list.pop(0)

