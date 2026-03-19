from tkinter import *
from tkinter import ttk

# As váriaves

score = 0
clicker_power = 1

# Os Custos do Upgrade

custo1 = 10
custo2 = 50
custo3 = 100
custo4 = 150
custo5 = 200
custo6 = 250
custo7 = 300
custo8 = 350
custo9 = 400
custo10 = 450
custo11 = 500
custo12 = 550
custo13 = 600
custo14 = 650
custo15 = 700
custo16 = 750
custo17 = 850
custo18 = 900
custo19 = 950
custo20 = 1000
custo21 = 1050
custo22 = 1100
custo23 = 1150
custo24 = 1200
custo25 = 1250
custo26 = 1300
custo27 = 1350
custo28 = 1400
custo29 = 1450
custo30 = 99999999999999999999

# As Funções

def Clicker():
    global score
    score += clicker_power
    label1.config(text=f"Pontos: {score}")

def comprar_upgrade1():
    global score, clicker_power, custo1
    if score >= custo1:
        score -= custo1
        clicker_power += 10
        custo1 = int(custo1 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade2():
    global score, clicker_power, custo2
    
    if score >= custo2:
        score -= custo2
        clicker_power += 20
        custo2 = int(custo2 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade3():
    global score, clicker_power, custo3
    
    if score >= custo3:
        score -= custo3
        clicker_power += 30
        custo3 = int(custo3 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade4():
    global score, clicker_power, custo4
    
    if score >= custo4:
        score -= custo4
        clicker_power += 40
        custo4 = int(custo4 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade5():
    global score, clicker_power, custo5

    if score >= custo5:
        score -= custo5
        clicker_power += 50
        custo5 = int(custo5 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade6():
    global score, clicker_power, custo6

    if score >= custo6:
        score -= custo6
        clicker_power += 60
        custo6 = int(custo6 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade7():
    global score, clicker_power, custo7

    if score >= custo7:
        score -= custo7
        clicker_power += 70
        custo7 = int(custo7 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade8():
    global score, clicker_power, custo8

    if score >= custo8:
        score -= custo8
        clicker_power += 80
        custo8 = int(custo8 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade9():
    global score, clicker_power, custo9
    
    if score >= custo9:
        score -= custo9
        clicker_power += 90
        custo9 = int(custo9 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade10():
    global score, clicker_power, custo10
    
    if score >= custo10:
        score -= custo10
        clicker_power += 100
        custo10 = int(custo10 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade11():
    global score, clicker_power, custo11
    
    if score >= custo11:
        score -= custo11
        clicker_power += 110
        custo11 = int(custo11 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade12():
    global score, clicker_power, custo12

    if score >= custo12:
        score -= custo12
        clicker_power += 120
        custo12 = int(custo12 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade13():
    global score, clicker_power, custo13

    if score >= custo13:
        score -= custo13
        clicker_power += 130
        custo13 = int(custo13 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade14():
    global score, clicker_power, custo14

    if score >= custo14:
        score -= custo14
        clicker_power += 140
        custo14 = int(custo14 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade15():
    global score, clicker_power, custo15

    if score >= custo15:
        score -= custo15
        clicker_power += 150
        custo15 = int(custo15 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade16():
    global score, clicker_power, custo16
    
    if score >= custo16:
        score -= custo16
        clicker_power += 160
        custo16 = int(custo16 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade17():
    global score, clicker_power, custo17
    
    if score >= custo17:
        score -= custo17
        clicker_power += 170
        custo17 = int(custo17 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade18():
    global score, clicker_power, custo18
    
    if score >= custo18:
        score -= custo18
        clicker_power += 180
        custo18 = int(custo18 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade19():
    global score, clicker_power, custo19

    if score >= custo19:
        score -= custo19
        clicker_power += 190
        custo19 = int(custo19 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade20():
    global score, clicker_power, custo20

    if score >= custo20:
        score -= custo20
        clicker_power += 200
        custo20 = int(custo20 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade21():
    global score, clicker_power, custo21

    if score >= custo21:
        score -= custo21
        clicker_power += 210
        custo21 = int(custo21 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade22():
    global score, clicker_power, custo22
    if score >= custo22:
        score -= custo22
        clicker_power += 220
        custo22 = int(custo22 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade23():
    global score, clicker_power, custo23
    
    if score >= custo23:
        score -= custo23
        clicker_power += 230
        custo23 = int(custo23 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade24():
    global score, clicker_power, custo24
    
    if score >= custo24:
        score -= custo24
        clicker_power += 240
        custo24 = int(custo24 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade25():
    global score, clicker_power, custo25
    
    if score >= custo25:
        score -= custo25
        clicker_power += 250
        custo25 = int(custo25 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade26():
    global score, clicker_power, custo26

    if score >= custo26:
        score -= custo26
        clicker_power += 260
        custo26 = int(custo26 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade27():
    global score, clicker_power, custo27

    if score >= custo27:
        score -= custo27
        clicker_power += 270
        custo27 = int(custo27 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade28():
    global score, clicker_power, custo28

    if score >= custo28:
        score -= custo28
        clicker_power += 280
        custo28 = int(custo28 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade29():
    global score, clicker_power, custo29

    if score >= custo29:
        score -= custo29
        clicker_power += 290
        custo29 = int(custo29 * 1.5)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def comprar_upgrade30():
    global score, clicker_power, custo30

    if score >= custo30:
        score -= custo30
        clicker_power += 9999999999
        custo30 = int(custo30 * 30)
        atualiza_interface()
    else:    
        label1.config(text="Sem Pontos!")
        janela.after(500, lambda: label1.config(text=f"Pontos: {score}"))

def atualiza_interface():
    label1.config(text=f"Pontos: {score}")
    label2.config(text=f"Clicker: {clicker_power}")
    bt1.config(text="Clicker")
    bt_upgrad1.config(text=f"Upgrade 1 (Custo: {custo1})")
    bt_upgrad2.config(text=f"Upgrade 2 (Custo: {custo2})")
    bt_upgrad3.config(text=f"Upgrade 3 (Custo: {custo3})")
    bt_upgrad4.config(text=f"Upgrade 4 (Custo: {custo4})")
    bt_upgrad5.config(text=f"Upgrade 5 (Custo: {custo5})")
    bt_upgrad6.config(text=f"Upgrade 6 (Custo: {custo6})")
    bt_upgrad7.config(text=f"Upgrade 7 (Custo: {custo7})")
    bt_upgrad8.config(text=f"Upgrade 8 (Custo: {custo8})")
    bt_upgrad9.config(text=f"Upgrade 9 (Custo: {custo9})")
    bt_upgrad10.config(text=f"Upgrade 10 (Custo: {custo10})")
    bt_upgrad11.config(text=f"Upgrade 11 (Custo: {custo11})")
    bt_upgrad12.config(text=f"Upgrade 12 (Custo: {custo12})")
    bt_upgrad13.config(text=f"Upgrade 13 (Custo: {custo13})")
    bt_upgrad14.config(text=f"Upgrade 14 (Custo: {custo14})")
    bt_upgrad15.config(text=f"Upgrade 15 (Custo: {custo15})")
    bt_upgrad16.config(text=f"Upgrade 16 (Custo: {custo16})")
    bt_upgrad17.config(text=f"Upgrade 17 (Custo: {custo17})")
    bt_upgrad18.config(text=f"Upgrade 18 (Custo: {custo18})")
    bt_upgrad19.config(text=f"Upgrade 19 (Custo: {custo19})")
    bt_upgrad20.config(text=f"Upgrade 20 (Custo: {custo20})")
    bt_upgrad21.config(text=f"Upgrade 21 (Custo: {custo21})")
    bt_upgrad22.config(text=f"Upgrade 22 (Custo: {custo22})")
    bt_upgrad23.config(text=f"Upgrade 23 (Custo: {custo23})")
    bt_upgrad24.config(text=f"Upgrade 24 (Custo: {custo24})")
    bt_upgrad25.config(text=f"Upgrade 25 (Custo: {custo25})")
    bt_upgrad26.config(text=f"Upgrade 26 (Custo: {custo26})")
    bt_upgrad27.config(text=f"Upgrade 27 (Custo: {custo27})")
    bt_upgrad28.config(text=f"Upgrade 28 (Custo: {custo28})")
    bt_upgrad29.config(text=f"Upgrade 29 (Custo: {custo29})")
    bt_upgrad30.config(text=f"Upgrade 30 (Custo: {custo30})")

# A Interface Gráfica

janela = Tk()
janela.title("Clicker Game")
janela.geometry("1050x340")
janela.resizable(width=False,height=False)

label1 = ttk.Label(janela, text=f"Pontos: {score}", font=("Arial",20))
label1.pack(pady=5)

label2 = ttk.Label(janela, text=f"Clicker: {clicker_power}", font=("Arial",12))
label2.pack(pady=5)

# Os Upgrades

bt1 = ttk.Button(janela, text="Clicker", width=20, command=Clicker)
bt1.pack(pady=5)

bt_upgrad1 = ttk.Button(janela, text="", command=comprar_upgrade1)
bt_upgrad1.place(x=10, y=120)

bt_upgrad2 = ttk.Button(janela, text="", command=comprar_upgrade2)
bt_upgrad2.place(x=10, y=150)

bt_upgrad3 = ttk.Button(janela, text="", command=comprar_upgrade3)
bt_upgrad3.place(x=10, y=180)

bt_upgrad4 = ttk.Button(janela, text="", command=comprar_upgrade4)
bt_upgrad4.place(x=10, y=210)

bt_upgrad5 = ttk.Button(janela, text="", command=comprar_upgrade5)
bt_upgrad5.place(x=10, y=240)

bt_upgrad6 = ttk.Button(janela, text="", command=comprar_upgrade6)
bt_upgrad6.place(x=10, y=270)

bt_upgrad7 = ttk.Button(janela, text="", command=comprar_upgrade7)
bt_upgrad7.place(x=10, y=300)

bt_upgrad8 = ttk.Button(janela, text="", command=comprar_upgrade8)
bt_upgrad8.place(x=200, y=120)

bt_upgrad9 = ttk.Button(janela, text="", command=comprar_upgrade9)
bt_upgrad9.place(x=200, y=150)

bt_upgrad10 = ttk.Button(janela, text="", command=comprar_upgrade10)
bt_upgrad10.place(x=200, y=180)

bt_upgrad11 = ttk.Button(janela, text="", command=comprar_upgrade11)
bt_upgrad11.place(x=200, y=210)

bt_upgrad12 = ttk.Button(janela, text="", command=comprar_upgrade12)
bt_upgrad12.place(x=200, y=240)

bt_upgrad13 = ttk.Button(janela, text="", command=comprar_upgrade13)
bt_upgrad13.place(x=200, y=270)

bt_upgrad14 = ttk.Button(janela, text="", command=comprar_upgrade14)
bt_upgrad14.place(x=200, y=300)

bt_upgrad15 = ttk.Button(janela, text="", command=comprar_upgrade15)
bt_upgrad15.place(x=400, y=120)

bt_upgrad16 = ttk.Button(janela, text="", command=comprar_upgrade16)
bt_upgrad16.place(x=400, y=150)

bt_upgrad17 = ttk.Button(janela, text="", command=comprar_upgrade17)
bt_upgrad17.place(x=400, y=180)

bt_upgrad18 = ttk.Button(janela, text="", command=comprar_upgrade18)
bt_upgrad18.place(x=400, y=210)

bt_upgrad19 = ttk.Button(janela, text="", command=comprar_upgrade19)
bt_upgrad19.place(x=400, y=240)

bt_upgrad20 = ttk.Button(janela, text="", command=comprar_upgrade20)
bt_upgrad20.place(x=400, y=270)

bt_upgrad21 = ttk.Button(janela, text="", command=comprar_upgrade21)
bt_upgrad21.place(x=400, y=300)

bt_upgrad22 = ttk.Button(janela, text="", command=comprar_upgrade22)
bt_upgrad22.place(x=600, y=120)

bt_upgrad23 = ttk.Button(janela, text="", command=comprar_upgrade23)
bt_upgrad23.place(x=600, y=150)

bt_upgrad24 = ttk.Button(janela, text="", command=comprar_upgrade24)
bt_upgrad24.place(x=600, y=180)

bt_upgrad25 = ttk.Button(janela, text="", command=comprar_upgrade25)
bt_upgrad25.place(x=600, y=210)

bt_upgrad26 = ttk.Button(janela, text="", command=comprar_upgrade26)
bt_upgrad26.place(x=600, y=240)

bt_upgrad27 = ttk.Button(janela, text="", command=comprar_upgrade27)
bt_upgrad27.place(x=600, y=270)

bt_upgrad28 = ttk.Button(janela, text="", command=comprar_upgrade28)
bt_upgrad28.place(x=600, y=300)

bt_upgrad29 = ttk.Button(janela, text="", command=comprar_upgrade29)
bt_upgrad29.place(x=800, y=120)

bt_upgrad30 = ttk.Button(janela, text="", command=comprar_upgrade30)
bt_upgrad30.place(x=800, y=150)

atualiza_interface()
janela.mainloop()
