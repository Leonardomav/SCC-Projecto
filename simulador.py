#!/usr/bin/env python
# encoding: utf-8
import fila
import lista
import eventos
import rand_generator

class Simulador:
	
	def insereEvento(self,event):
		self.event_list.insert_event(event)

	#Construtor
	def __init__(self, m_cheg_a, m_cheg_b, n_sim, toggle_sim, md_per_a, dv_per_a, nm_per_a, md_per_b, dv_per_b, nm_per_b, md_pol_a, dv_pol_a, nm_pol_a, md_pol_b, dv_pol_b, nm_pol_b, md_env, dv_env, nm_env, s_cheg_a, s_cheg_b, s_per_a, s_per_b, s_pol_a, s_pol_b, s_env):
		self.media_cheg_a = m_cheg_a
		self.media_cheg_b = m_cheg_b
		self.n_sim = n_sim
		self.toggle_sim = toggle_sim
		
		if s_cheg_a != 0:
			rand_generator.randst(s_cheg_a, 0)
		if s_cheg_b != 0:
			rand_generator.randst(s_cheg_b, 1)
		if s_per_a != 0:
			rand_generator.randst(s_per_a, 2)
		if s_per_b != 0:
			rand_generator.randst(s_per_b, 3)
		if s_pol_a != 0:
			rand_generator.randst(s_pol_a, 4)
		if s_pol_b != 0:
			rand_generator.randst(s_pol_b, 5)		
		if s_env != 0:
			rand_generator.randst(s_env, 6)			
		
		#Relógio de simulação - variável que contém o valor do tempo em cada instante
		self.instant = 0		#valor inicial a zero
		
		self.envernizamento = fila.Fila(self, md_env, dv_env, nm_env, None, 6)
		self.polimento_b = fila.Fila(self, md_pol_b, dv_pol_b, nm_pol_b, self.envernizamento, 5)
		self.polimento_a = fila.Fila(self, md_pol_a, dv_pol_a, nm_pol_a, self.envernizamento, 4)
		self.perfuracao_b = fila.Fila(self, md_per_b, dv_per_b, nm_per_b, self.polimento_b, 3)
		self.perfuracao_a = fila.Fila(self, md_per_a, dv_per_a, nm_per_a, self.polimento_a, 2)
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
		if self.toggle_sim:
			while(self.instant < self.n_sim):
				#print(self.event_list)
				event = self.event_list.remove_event()
				self.instant=event.instant
				self.act_stats()
				event.executa()
			#self.relat() #Apresenta resultados de simulação
			return self.results()
		else:
			while(self.envernizamento.atendidos < self.n_sim):
				#print(self.event_list)
				event = self.event_list.remove_event()
				self.instant=event.instant
				self.act_stats()
				event.executa()
			#self.relat() #Apresenta resultados de simulação
			return self.results()

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

	def results(self):
		output = [self.instant]
		output.extend(self.perfuracao_a.results())
		output.extend(self.perfuracao_b.results())
		output.extend(self.polimento_a.results())
		output.extend(self.polimento_b.results())
		output.extend(self.envernizamento.results())
		return output



#programa principal
if __name__ == '__main__':
	#Cria um simulador e
	#s = Simulador(5, 1.33, 60, False, 2, 0.7, 1, 0.75, 0.3, 1, 4, 1.2, 1, 3, 1, 2, 1.4, 0.3, 2)
	#s = Simulador(5, 1.33, 60, False, 2, 0.7, 1, 0.75, 0.3, 1, 4, 1.2, 1, 3, 1, 2, 1.4, 0.3, 2, 0, 0, 0, 0, 0, 0, 0)
	#põe-o em marcha
	#s.executa()
	pass