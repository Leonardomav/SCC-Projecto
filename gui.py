#!/usr/bin/env python
# encoding: utf-8
from tkinter import *
import simulador

root = Tk()
root.wm_title("SCC - Fabrica")

trigger = True
results = []

def isint(string):
	try:
		int(string)
		return True
	except ValueError:
		return False

def isfloat(string):
	try:
		float(string)
		return True
	except ValueError:
		return False

def StatusError(msg):
	status=Label(root, text=msg, bd=0, anchor=N, fg="red")
	status.pack(side=TOP)
	return status

def run(results):
	popup = Toplevel()
	popup.wm_title("Resultados")

	topPop = Frame(popup)
	topPop.pack()
	botPop = Frame(popup)
	botPop.pack()

	timeSpent = Label(topPop, text="Tempo da Simulação: "+str(results[0]))
	timeSpent.pack()

	PerfA = Label(botPop, text="Perfuração A", relief = GROOVE, bd = 4,width=20,height=3)
	PerfB = Label(botPop, text="Perfuração B",relief = GROOVE,bd = 4,width=20,height=3)
	PolA = Label(botPop, text="Polimento A",relief = GROOVE, bd = 4,width=20,height=3)
	PolB = Label(botPop, text="Polimento B",relief = GROOVE, bd = 4,width=20,height=3)
	Enver = Label(botPop, text="Envernizamento",relief = GROOVE, bd = 4,width=20,height=3)

	Col1 = Label(botPop, text="Tempo Médio de Espera",relief = GROOVE, bd = 4,width=25,height=3)
	Col2 = Label(botPop, text="Comp Médio de Espera",relief = GROOVE, bd = 4,width=25,height=3)
	Col3 = Label(botPop, text="Utilização de Serviço",relief = GROOVE,bd = 4,width=25,height=3)
	Col4 = Label(botPop, text="Nº de Clientes Atendidos",relief = GROOVE, bd = 4,width=25,height=3)
	Col5 = Label(botPop, text="Nº de Clientes na Fila",relief = GROOVE, bd = 4,width=25,height=3)

	PerfA.grid(row=1, column=0)
	PerfB.grid(row=2, column=0)
	PolA.grid(row=3, column=0)
	PolB.grid(row=4, column=0)
	Enver.grid(row=5, column=0)

	Col1.grid(row=0, column=1)
	Col2.grid(row=0, column=2)
	Col3.grid(row=0, column=3)
	Col4.grid(row=0, column=4)
	Col5.grid(row=0, column=5)
	k=1
	for i in range(6):
		for j in range(6):
			if i!=0 and j!=0:
				cell=Label(botPop, text=results[k],relief = GROOVE, bd = 2,width=25,height=3)
				cell.grid(row=i, column=j)
				k+=1




	popup.resizable(width=False , height=False)
	popup.mainloop()


def checkValues():
	if n_sim.get()=="" or m_cheg_a.get()=="" or m_cheg_b.get()=="" or nm_per_a.get()=="" or md_per_a.get()=="" or dv_per_a.get()=="" or nm_per_b.get()=="" or md_per_b.get()=="" or dv_per_b.get()=="" or nm_pol_a.get()=="" or md_pol_a.get()=="" or dv_pol_a.get()=="" or nm_pol_b.get()=="" or md_pol_b.get()=="" or dv_pol_b.get()=="" or nm_env.get()=="" or md_env.get()=="" or dv_env.get()=="" or seed_1.get()=="" or seed_2.get()=="" or seed_3.get()=="" or seed_4.get()=="" or seed_5.get()=="" or seed_6.get()=="" or seed_7.get()=="":
		status.config(text='ERRO - Por favor complete todos os campos...')

	elif trigger == True:
		if isfloat(n_sim.get())==False or isfloat(m_cheg_a.get())==False or isfloat(m_cheg_b.get())==False or isint(nm_per_a.get())==False or isfloat(md_per_a.get())==False or isfloat(dv_per_a.get())==False or isint(nm_per_b.get())==False or isfloat(md_per_b.get())==False or isfloat(dv_per_b.get())==False or isint(nm_pol_a.get())==False or isfloat(md_pol_a.get())==False or isfloat(dv_pol_a.get())==False or isint(nm_pol_b.get())==False or isfloat(md_pol_b.get())==False or isfloat(dv_pol_b.get())==False or isint(nm_env.get())==False or isfloat(md_env.get())==False or isfloat(dv_env.get())==False or isint(seed_1.get())==False or isint(seed_2.get())==False or isint(seed_3.get())==False or isint(seed_4.get())==False or isint(seed_5.get())==False or isint(seed_6.get())==False or isint(seed_7.get())==False:
			status.config(text='ERRO - Por favor verifique os valores inteiros e decimais...')

		elif float(n_sim.get())<=0 or float(m_cheg_a.get())<=0 or float(m_cheg_b.get())<=0 or int(nm_per_a.get())<=0 or float(md_per_a.get())<0 or float(dv_per_a.get())<0 or int(nm_per_b.get())<=0 or float(md_per_b.get())<0 or float(dv_per_b.get())<0 or int(nm_pol_a.get())<=0 or float(md_pol_a.get())<0 or float(dv_pol_a.get())<0 or int(nm_pol_b.get())<=0 or float(md_pol_b.get())<0 or float(dv_pol_b.get())<0 or int(nm_env.get())<=0 or float(md_env.get())<0 or float(dv_env.get())<0 or int(seed_1.get())<0 or int(seed_2.get())<0 or int(seed_3.get())<0 or int(seed_4.get())<0 or int(seed_5.get())<0 or int(seed_6.get())<0 or int(seed_7.get())<0:
			status.config(text='ERRO - Por favor verifique se existem valores fora dos limites')

		else:
			status.config(text='')
			results = simulador.Simulador(float(m_cheg_a.get()), float(m_cheg_b.get()), float(n_sim.get()), trigger, float(md_per_a.get()), float(dv_per_a.get()), int(nm_per_a.get()), float(md_per_b.get()), float(dv_per_b.get()), int(nm_per_b.get()), float(md_pol_a.get()), float(dv_pol_a.get()), int(nm_pol_a.get()), float(md_pol_b.get()), float(dv_pol_b.get()), int(nm_pol_b.get()), float(md_env.get()), float(dv_env.get()), float(nm_env.get()), int(seed_1.get()), int(seed_2.get()), int(seed_3.get()), int(seed_4.get()), int(seed_5.get()), int(seed_6.get()), int(seed_7.get())).executa()
			run(results)

	elif trigger == False:
		if isint(n_sim.get())==False or isfloat(m_cheg_a.get())==False or isfloat(m_cheg_b.get())==False or isint(nm_per_a.get())==False or isfloat(md_per_a.get())==False or isfloat(dv_per_a.get())==False or isint(nm_per_b.get())==False or isfloat(md_per_b.get())==False or isfloat(dv_per_b.get())==False or isint(nm_pol_a.get())==False or isfloat(md_pol_a.get())==False or isfloat(dv_pol_a.get())==False or isint(nm_pol_b.get())==False or isfloat(md_pol_b.get())==False or isfloat(dv_pol_b.get())==False or isint(nm_env.get())==False or isfloat(md_env.get())==False or isfloat(dv_env.get())==False or isint(seed_1.get())==False or isint(seed_2.get())==False or isint(seed_3.get())==False or isint(seed_4.get())==False or isint(seed_5.get())==False or isint(seed_6.get())==False or isint(seed_7.get())==False:
			status.config(text='ERRO - Por favor verifique os valores inteiros e decimais...')

		elif int(n_sim.get())<=0 or float(m_cheg_a.get())<=0 or float(m_cheg_b.get())<=0 or int(nm_per_a.get())<=0 or float(md_per_a.get())<0 or float(dv_per_a.get())<0 or int(nm_per_b.get())<=0 or float(md_per_b.get())<0 or float(dv_per_b.get())<0 or int(nm_pol_a.get())<=0 or float(md_pol_a.get())<0 or float(dv_pol_a.get())<0 or int(nm_pol_b.get())<=0 or float(md_pol_b.get())<0 or float(dv_pol_b.get())<0 or int(nm_env.get())<=0 or float(md_env.get())<0 or float(dv_env.get())<0 or int(seed_1.get())<0 or int(seed_2.get())<0 or int(seed_3.get())<0 or int(seed_4.get())<0 or int(seed_5.get())<0 or int(seed_6.get())<0 or int(seed_7.get())<0:
			status.config(text='ERRO - Por favor verifique se existem valores fora dos limites')

		else:
			status.config(text='')
			results = simulador.Simulador(int(m_cheg_a.get()), float(m_cheg_b.get()), int(n_sim.get()), trigger, float(md_per_a.get()), float(dv_per_a.get()), int(nm_per_a.get()), float(md_per_b.get()), float(dv_per_b.get()), int(nm_per_b.get()), float(md_pol_a.get()), float(dv_pol_a.get()), int(nm_pol_a.get()), float(md_pol_b.get()), float(dv_pol_b.get()), int(nm_pol_b.get()), float(md_env.get()), float(dv_env.get()), float(nm_env.get()), int(seed_1.get()), int(seed_2.get()), int(seed_3.get()), int(seed_4.get()), int(seed_5.get()), int(seed_6.get()), int(seed_7.get())).executa()
			run(results)


def change():
	global trigger
	if trigger:
		change.config(text='Tempo')
		label_1.config(text='Clientes na Simulação   ')
		trigger=False
	else:
		change.config(text='Clientes')
		label_1.config(text='Tempo de Simulação   ')
		trigger=True

topFrame = Frame(root)
topFrame.pack()


bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


change = Button(topFrame, text="Clientes", command=change)
simular = Button(bottomFrame, text="Simular", command=checkValues)
sair = Button(bottomFrame, text="Exit", command=root.destroy)

simular.pack(side=LEFT)
sair.pack(side=LEFT)

label_1=Label(topFrame, text="Tempo de Simulação   ")
label_2=Label(topFrame, text="Média de chegada de A e Seed (0->Default)   ")
label_3=Label(topFrame, text="Média de chegada de B e Seed (0->Default)   ")
label_4=Label(topFrame, text="Número de Máquinas de Perfuração A   ")
label_5=Label(topFrame, text="Média, Desvio Padrão e Seed (0->Default)   ")
label_6=Label(topFrame, text="Número de Máquinas de Perfuração B    ")
label_7=Label(topFrame, text="Média, Desvio Padrão e Seed (0->Default)   ")
label_8=Label(topFrame, text="Número de Máquinas de Polimento A   ")
label_9=Label(topFrame, text="Média, Desvio Padrão e Seed (0->Default)   ")
label_10=Label(topFrame, text="Número de Máquinas de Polimento B   ")
label_11=Label(topFrame, text="Média, Desvio Padrãoe e Seed (0->Default)  ")
label_12=Label(topFrame, text="Número de Máquinas de Envernizamento   ")
label_13=Label(topFrame, text="Média, Desvio Padrão e Seed (0->Default)   ")

n_sim=Entry(topFrame)
m_cheg_a=Entry(topFrame)
m_cheg_b=Entry(topFrame)
nm_per_a=Entry(topFrame)
md_per_a=Entry(topFrame)
dv_per_a=Entry(topFrame)
nm_per_b=Entry(topFrame)
md_per_b=Entry(topFrame)
dv_per_b=Entry(topFrame)
nm_pol_a=Entry(topFrame)
md_pol_a=Entry(topFrame)
dv_pol_a=Entry(topFrame)
nm_pol_b=Entry(topFrame)
md_pol_b=Entry(topFrame)
dv_pol_b=Entry(topFrame)
nm_env=Entry(topFrame)
md_env=Entry(topFrame)
dv_env=Entry(topFrame)
seed_1=Entry(topFrame)
seed_2=Entry(topFrame)
seed_3=Entry(topFrame)
seed_4=Entry(topFrame)
seed_5=Entry(topFrame)
seed_6=Entry(topFrame)
seed_7=Entry(topFrame)



label_1.grid(row=0,pady=10, sticky=E)
label_2.grid(row=2,pady=10, sticky=E)
label_3.grid(row=3,pady=10, sticky=E)
label_4.grid(row=5,pady=10, sticky=E)
label_5.grid(row=6,pady=10, sticky=E)
label_6.grid(row=8,pady=10, sticky=E)
label_7.grid(row=9,pady=10, sticky=E)
label_8.grid(row=11,pady=10, sticky=E)
label_9.grid(row=12,pady=10, sticky=E)
label_10.grid(row=14,pady=10, sticky=E)
label_11.grid(row=15,pady=10, sticky=E)
label_12.grid(row=17,pady=10, sticky=E)
label_13.grid(row=18,pady=10, sticky=E)

n_sim.grid(row=0, column=1)
change.grid(row=0, column=2)
m_cheg_a.grid(row=2, column=1)
m_cheg_b.grid(row=3, column=1)
nm_per_a.grid(row=5, column=1)
md_per_a.grid(row=6, column=1,padx=15)
dv_per_a.grid(row=6, column=2)
nm_per_b.grid(row=8, column=1)
md_per_b.grid(row=9, column=1)
dv_per_b.grid(row=9, column=2)
nm_pol_a.grid(row=11, column=1)
md_pol_a.grid(row=12, column=1)
dv_pol_a.grid(row=12, column=2)
nm_pol_b.grid(row=14, column=1)
md_pol_b.grid(row=15, column=1)
dv_pol_b.grid(row=15, column=2)
nm_env.grid(row=17, column=1)
md_env.grid(row=18, column=1)
dv_env.grid(row=18, column=2)
seed_1.grid(row=2, column=2)
seed_2.grid(row=3, column=2)
seed_3.grid(row=6, column=3)
seed_4.grid(row=9, column=3)
seed_5.grid(row=12, column=3,padx=15)
seed_6.grid(row=15, column=3)
seed_7.grid(row=18, column=3)

status = StatusError("")
root.resizable(width=False , height=False)
root.mainloop()