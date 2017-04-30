#!/usr/bin/env python
# encoding: utf-8
import eventos
import aleatorio

class Fila:
	"""Classe que representa um serviço com uma fila de espera associada"""

	# Construtor
	def __init__(self, sim, media_serv, desvio, n_maquinas, proxima, stream):
		self.fila=[]					#Fila de espera do serviço
		self.simulator = sim			#Referência para o simulador a que pertence o serviço
		self.estado = 0					#Variável que regista o estado do serviço: <n_maquinas - livre; n_maquinas - ocupado
		self.temp_last = sim.instant	#Tempo que passou desde o último evento. Neste caso 0, porque a simulação ainda não começou.
		self.atendidos = 0				#Número de clientes atendidos até ao momento
		self.soma_temp_esp = 0
		self.soma_temp_serv = 0
		self.media_serv = media_serv
		self.desvio = desvio
		self.n_maquinas = n_maquinas
		self.proxima = proxima			#proxima Fila
		self.stream = stream
		self.proximo_n = None

	def insereClient(self,client):
		"""Método que insere cliente (client) no serviço"""
		if(self.estado<self.n_maquinas):	#Se serviço livre,
			self.estado = self.estado+1 #fica ocupado e
			#agenda saída do cliente c para daqui a self.media_serv instantes
			#self.simulator.insereEvento(eventos.Saida(self.simulator.instant + self.media_serv, self.simulator, self, client)) #sem randomizacao
			self.simulator.insereEvento(eventos.Saida(self.simulator.instant + self.variacao_normal(), self.simulator, self, client))
		else:
			self.fila.append(client) #Se serviço ocupado, o cliente vai para a fila de espera

	
	def removeClient(self):
		"""Método que remove cliente do serviço"""
		self.atendidos = self.atendidos+1 #Regista que acabou de atender + 1 cliente
		if(self.fila==[]):	#Se a fila está vazia,
			self.estado=self.estado-1	# liberta o serviço
		else: #Se não,
			#vai buscar próximo cliente à fila de espera e
			client = self.fila.pop(0)
			#agenda a sua saida para daqui a self.media_serv instantes
			#self.simulator.insereEvento(eventos.Saida(self.simulator.instant + self.media_serv, self.simulator, self, client)) #sem randomizacao
			#self.simulator.insereEvento(eventos.Saida(self.simulator.instant + random.normalvariate(self.media_serv, self.desvio), self.simulator, self, client))
			self.simulator.insereEvento(eventos.Saida(self.simulator.instant + self.variacao_normal(), self.simulator, self, client))

	def variacao_normal(self):
		if self.desvio == 0:
			return self.media_serv
		if self.proximo_n:
			temp = self.proximo_n
			self.proximo_n = None
			return temp
		(temp1, temp2) = aleatorio.normal(self.media_serv, self.desvio, self.stream)
		while temp1 < 0 and temp2 <0:
			(temp1, temp2) = aleatorio.normal(self.media_serv, self.desvio, self.stream)
		if temp1>=0:
			if temp2>=0:
				self.proximo_n=temp2
			return temp1
		return temp2

	def act_stats(self):
		"""Método que calcula valores para estatísticas, em cada passo da simulação ou evento"""
		#Calcula tempo que passou desde o último evento
		temp_desd_ult=self.simulator.instant - self.temp_last
		#Actualiza variável para o próximo passo/evento
		self.temp_last=self.simulator.instant
		#Contabiliza tempo de espera na fila
		#para todos os clientes que estiveram na fila durante o intervalo
		self.soma_temp_esp = self.soma_temp_esp + (len(self.fila) * temp_desd_ult)
		#Contabiliza tempo de atendimento
		self.soma_temp_serv = self.soma_temp_serv + (self.estado * temp_desd_ult) / self.n_maquinas
	
	def relat(self):
		"""Método que calcula valores finais estatísticos"""
		#Tempo médio de espera na fila
		temp_med_fila = self.soma_temp_esp / (self.atendidos+len(self.fila))
		#Comprimento médio da fila de espera
		#self.simulator.instant neste momento é o valor do tempo de simulação,
		#uma vez que a simulação começou em 0 e este método só é chamdo no fim da simulação
		comp_med_fila = self.soma_temp_esp / self.simulator.instant
		#Tempo médio de atendimento no serviço
		utilizacao_serv = self.soma_temp_serv / self.simulator.instant
		
		#Apresenta resultados
		print ("Tempo medio de espera",temp_med_fila)
		print ("Comp. medio da fila",comp_med_fila)
		print ("Utilizacao do servico",utilizacao_serv)
		print ("Numero de clientes atendidos", self.atendidos)
		print ("Numero de clientes na fila", len(self.fila))
		
	def results(self):
		utilizacao_serv = self.soma_temp_serv / self.simulator.instant
		if (self.atendidos+len(self.fila)) == 0:
			return [0, 0, utilizacao_serv, 0, 0]
		temp_med_fila = self.soma_temp_esp / (self.atendidos+len(self.fila))
		comp_med_fila = self.soma_temp_esp / self.simulator.instant
		return [temp_med_fila, comp_med_fila, utilizacao_serv, self.atendidos, len(self.fila)]