#!/usr/bin/env python
# encoding: utf-8
import cliente
import aleatorio

class Evento:
	"""Classe de onde vão ser derivados todos os eventos.
	Contem apenas os atributos e métodos comuns a todos os eventos.
	Não haverá instâncias desta classe num simulador."""

	#construtor
	def __init__(self,i,sim,serv,clt):
		self.instant = i		#Instante de ocorrencia do evento
		self.simulator = sim	#Simulador onde ocorre o evento
		self.servico = serv
		self.cliente = clt


class Chegada(Evento):
	"""Classe que representa a chegada de um cliente. Deriva de Evento."""
	#Construtor
	def __init__(self,i,sim,serv,size):
		Evento.__init__(self,i,sim,serv,cliente.Client(size))	#chegadas sao sempre na perfuracao e com um novo 

	def __str__(self):
		"""Método que descreve o evento.
		Para ser usado na listagem da lista de eventos."""
		#return "Chegada\t\t["+str(self.instant)+"]"
		return "Chegada\t\t["+str(self.instant)+"]"+"\t\t"+str(self.servico.media_serv)+str(self.cliente.size)
	
	
	def executa(self):
		"""Método que executa as acções correspondentes à chegada de um cliente"""
		#Coloca cliente no serviço - na fila ou a ser atendido, conforme o caso
		self.servico.insereClient(self.cliente) 		
		if self.cliente.size:		#se for A
			#Agenda nova chegada para daqui a aleatorio.exponencial(self.simulator.media_cheg) instantes
			self.simulator.insereEvento(Chegada(self.simulator.instant+self.simulator.media_cheg_a,self.simulator,self.servico,self.cliente.size)) #sem randomizacao
			#self.simulator.insereEvento(Chegada(self.simulator.instant+aleatorio.exponencial(self.simulator.media_cheg_a),self.simulator,self.servico,self.cliente.size))
		else:						#se for B
			self.simulator.insereEvento(Chegada(self.simulator.instant+self.simulator.media_cheg_b,self.simulator,self.servico,self.cliente.size)) #sem randomizacao
			#self.simulator.insereEvento(Chegada(self.simulator.instant+aleatorio.exponencial(self.simulator.media_cheg_b),self.simulator,self.servico,self.cliente.size))

class Saida(Evento):
	"""Classe que representa a saída de um cliente. Deriva de Evento."""
	#Construtor
	def __init__(self,i,sim,serv,clt):
		Evento.__init__(self,i,sim,serv,clt)

	def __str__(self):
		"""Método que descreve o evento.
		Para ser usado na listagem da lista de eventos."""
		#return "Saida\t\t["+str(self.instant)+"]
		return "Saida\t\t["+str(self.instant)+"]"+"\t\t"+str(self.servico.media_serv)+str(self.cliente.size)

	
	def executa(self):
		"""Método que executa as acções correspondentes à saída de um cliente"""
		self.servico.removeClient() #Retira cliente do serviço
		if(self.servico.proxima):
			self.servico.proxima.insereClient(self.cliente)

