#!/usr/bin/env python
# encoding: utf-8
import fila
import lista
import eventos

class Simulador:
	
	def insereEvento(self,event):
		self.event_list.insert_event(event)

	#Construtor
	def __init__(self, m_cheg_a, m_cheg_b, n_clientes, md_per_a, dv_per_a, nm_per_a, md_per_b, dv_per_b, nm_per_b, md_pol_a, dv_pol_a, nm_pol_a, md_pol_b, dv_pol_b, nm_pol_b, md_env, dv_env, nm_env,):
		"""
		#Médias das distribuições de chegadas e de atendimento no serviço
		self.media_cheg = 1
		self.media_serv = 1.5
		#Número de clientes que vão ser atendidos
		self.n_clientes = 100
		"""
		self.media_cheg_a = m_cheg_a
		self.media_cheg_b = m_cheg_b
		self.n_clientes = n_clientes		
		
		#Relógio de simulação - variável que contém o valor do tempo em cada instante
		self.instant = 0		#valor inicial a zero
		
		#Serviço - pode haver mais do que um num simulador
		#self.client_queue= fila.Fila(self)
		"""
		self.envernizamento = fila.Fila(self, 1.4, 0.3, 2, None)
		self.polimento_a = fila.Fila(self, 4, 1.2, 1, self.envernizamento)
		self.polimento_b = fila.Fila(self, 3, 1, 2, self.envernizamento)
		self.perfuracao_a = fila.Fila(self, 2, 0.7, 1, self.polimento_a)
		self.perfuracao_b = fila.Fila(self, 0.75, 0.3, 1, self.polimento_b)
		"""
		self.envernizamento = fila.Fila(self, md_env, dv_env, nm_env, None)
		self.polimento_a = fila.Fila(self, md_pol_a, dv_pol_a, nm_pol_a, self.envernizamento)
		self.polimento_b = fila.Fila(self, md_pol_b, dv_pol_b, nm_pol_b, self.envernizamento)
		self.perfuracao_a = fila.Fila(self, md_per_a, dv_per_a, nm_per_a, self.polimento_a)
		self.perfuracao_b = fila.Fila(self, md_per_b, dv_per_b, nm_per_b, self.polimento_b)
		#Lista de eventos - onde ficam registados todos os eventos que vão ocorrer na simulação
		#Cada simulador só tem uma
		self.event_list = lista.Lista(self)
		
		#Agendamento da primeira chegada
		#Se não for feito, o simulador não tem eventos para simular
		self.insereEvento(eventos.Chegada(self.instant,self,self.perfuracao_a,True))		#começa geração de A
		self.insereEvento(eventos.Chegada(self.instant,self,self.perfuracao_b,False))		#começa geração de B
	
	def executa(self):
		"""Método executivo do simulador"""
		#Enquanto não atender todos os clientes
		"""
		while(self.client_queue.atendidos < self.n_clientes):
			print (self.event_list) #Mostra lista de eventos - desnecessário; é apenas informativo
			event = self.event_list.remove_event()	#Retira primeiro evento (é o mais iminente) da lista de eventos
			self.instant = event.instant			#Actualiza relógio de simulação
			self.act_stats()					#Actualiza valores estatísticos
			event.executa(self.client_queue)		#Executa evento
		"""
		while(self.envernizamento.atendidos < self.n_clientes):
			#print(self.event_list)
			event = self.event_list.remove_event()
			self.instant=event.instant
			self.act_stats()
			event.executa()
		self.relat() #Apresenta resultados de simulação finais

	def act_stats(self):
		"""Método que actualiza os valores estatísticos do simulador"""
		self.perfuracao_a.act_stats()
		self.perfuracao_b.act_stats()
		self.polimento_a.act_stats()
		self.polimento_b.act_stats()
		self.envernizamento.act_stats()

	def relat(self):
		"""Método que apresenta os resultados de simulação finais"""
		print ("\n\n------------FINAL RESULTS---------------")
		print ("Tempo de simulacao",self.instant)
		print("\n------------Perfuracao A---------------")
		self.perfuracao_a.relat()
		print("\n------------Perfuracao B---------------")
		self.perfuracao_b.relat()		
		print("\n------------Polimento A---------------")
		self.polimento_a.relat()
		print("\n------------Polimento B---------------")
		self.polimento_b.relat()		
		print("\n------------Envernizamento---------------")
		self.envernizamento.relat()



#programa principal

#Cria um simulador e
s = Simulador(5, 1.33, 300, 2, 0.7, 1, 0.75, 0.3, 1, 4, 1.2, 1, 3, 1, 2, 1.4, 0.3, 2)
#põe-o em marcha
s.executa()
