sn = 2
def code_a():
    s1.min()
    s2.mid()
    s3.mid()
    s4.mid()
    s5.mid()
    s6.mid()

    sleep(sn)

def code_b():
    s1.min()
    s2.min()
    s3.mid()
    s4.mid()
    s5.mid()
    s6.mid()
    sleep(sn)

def code_c():
    s1.min()
    s2.mid()
    s3.mid()
    s4.min()
    s5.mid()
    s6.mid()
    sleep(sn)

def code_d():
    s1.min()
    s2.mid()
    s3.mid()
    s4.min()
    s5.min()
    s6.mid()
    sleep(sn)

def code_e():
    s1.min()
    s2.mid()
    s3.mid()
    s4.mid()
    s5.min()
    s6.mid()
    sleep(sn)

def code_f():
    s1.min()
    s2.min()
    s3.mid()
    s4.min()
    s5.mid()
    s6.mid()
    sleep(sn)

def code_g():
    s1.min()
    s2.min()
    s3.mid()
    s4.min()
    s5.min()
    s6.mid()
    sleep(sn)

def code_h():
    s1.min()
    s2.min()
    s3.mid()
    s4.mid()
    s5.min()
    s6.mid()
    sleep(sn)

def code_i():
    s1.mid()
    s2.min()
    s3.mid()
    s4.min()
    s5.mid()
    s6.mid()
    sleep(sn)

def code_j():
    s1.mid()
    s2.min()
    s3.mid()
    s4.min()
    s5.min()
    s6.mid()
    sleep(sn)

def code_k():
    s1.min()
    s2.mid()
    s3.min()
    s4.mid()
    s5.mid()
    s6.mid()
    sleep(sn)

def code_l():
    s1.min()
    s2.min()
    s3.min()
    s4.mid()
    s5.mid()
    s6.mid()
    sleep(sn)

def code_m():
    s1.min()
    s2.mid()
    s3.min()
    s4.min()
    s5.mid()
    s6.mid()
    sleep(sn)
    
def code_n():
    s1.min()
    s2.mid()
    s3.min()
    s4.min()
    s5.min()
    s6.mid()
    sleep(sn)

def code_o():
    s1.min()
    s2.mid()
    s3.min()
    s4.mid()
    s5.min()
    s6.mid()
    sleep(sn)

def code_p():
    s1.min()
    s2.min()
    s3.min()
    s4.min()
    s5.mid()
    s6.mid()
    sleep(sn)

def code_q():
    s1.min()
    s2.min()
    s3.min()
    s4.min()
    s5.min()
    s6.mid()
    sleep(sn)

def code_r():
    s1.min()
    s2.min()
    s3.min()
    s4.mid()
    s5.min()
    s6.mid()
    sleep(sn)

def code_s():
    s1.mid()
    s2.min()
    s3.min()
    s4.min()
    s5.mid()
    s6.mid()
    sleep(sn)

def code_t():
    s1.mid()
    s2.min()
    s3.min()
    s4.min()
    s5.min()
    s6.mid()
    sleep(sn)

def code_u():
    s1.min()
    s2.mid()
    s3.min()
    s4.mid()
    s5.mid()
    s6.min()
    sleep(sn)

def code_v():
    s1.min()
    s2.min()
    s3.min()
    s4.mid()
    s5.mid()
    s6.min()
    sleep(sn)

def code_w():
    s1.mid()
    s2.min()
    s3.mid()
    s4.min()
    s5.min()
    s6.min()
    sleep(sn)

def code_x():
    s1.min()
    s2.mid()
    s3.min()
    s4.min()
    s5.mid()
    s6.min()
    sleep(sn)

def code_y():
    s1.min()
    s2.mid()
    s3.min()
    s4.min()
    s5.min()
    s6.min()
    sleep(sn)

def code_z():
    s1.min()
    s2.mid()
    s3.min()
    s4.mid()
    s5.min()
    s6.min()
    sleep(sn)

def code_c1():
    s1.min()
    s2.mid()
    s3.mid()
    s4.mid()
    s5.mid()
    s6.min()
    sleep(sn)

def code_g1():
    s1.min()
    s2.min()
    s3.mid()
    s4.mid()
    s5.mid()
    s6.min()
    sleep(sn)

def code_i1():
    s1.mid()
    s2.mid()
    s3.min()
    s4.mid()
    s5.min()
    s6.mid()
    sleep(sn)

def code_o1():
    s1.mid()
    s2.min()
    s3.mid()
    s4.min()
    s5.mid()
    s6.min()
    sleep(sn)

def code_s1():
    s1.min()
    s2.mid()
    s3.mid()
    s4.min()
    s5.mid()
    s6.min()
    sleep(sn)

def code_u1():
    s1.min()
    s2.min()
    s3.mid()
    s4.mid()
    s5.min()
    s6.min()
    sleep(sn)


from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory()
# 1. değer bağlı oldukları pinler, 2-3 move rangeleri, 4 unkown
s1 = Servo(14, min_pulse_width= (0.5 /1000), max_pulse_width= (2.5/ 1000), pin_factory = factory)
s2 = Servo(15, min_pulse_width= (0.5 /1000), max_pulse_width= (2.5/ 1000), pin_factory = factory)
s3 = Servo(18, min_pulse_width= (0.5 /1000), max_pulse_width= (2.5/ 1000), pin_factory = factory)
s4 = Servo(23, min_pulse_width= (0.5 /1000), max_pulse_width= (2.5/ 1000), pin_factory = factory)
s5 = Servo(24, min_pulse_width= (0.5 /1000), max_pulse_width= (2.5/ 1000), pin_factory = factory)
s6 = Servo(25, min_pulse_width= (0.5 /1000), max_pulse_width= (2.5/ 1000), pin_factory = factory)


kelime = "engelsiz yaşam"



s1.min()
s2.min()
s3.min()
s4.min()
s5.min()
s6.min()

for i in range (len(kelime)):
    print(i)
    if(kelime[i] == 'a'):
        code_a()
    elif(kelime[i] == 'b'):
        code_b()
    elif(kelime[i] == 'c'):
        code_c()
    elif(kelime[i] == 'd'):
        code_d()
    elif(kelime[i] == 'e'):
        code_e()
    elif(kelime[i] == 'f'):
        code_f()
    elif(kelime[i] == 'g'):
        code_g()
    elif(kelime[i] == 'h'):
        code_h()
    elif(kelime[i] == 'i'):
        code_i()
    elif(kelime[i] == 'j'):
        code_j()
    elif(kelime[i] == 'k'):
        code_k()
    elif(kelime[i] == 'l'):
        code_l()
    elif(kelime[i] == 'm'):
        code_m()
    elif(kelime[i] == 'n'):
        code_n()
    elif(kelime[i] == 'o'):
        code_o()
    elif(kelime[i] == 'p'):
        code_p()
    elif(kelime[i] == 'q'):
        code_q()
    elif(kelime[i] == 'r'):
        code_r()
    elif(kelime[i] == 's'):
        code_s()
    elif(kelime[i] == 't'):
        code_t()
    elif(kelime[i] == 'u'):
        code_u()
    elif(kelime[i] == 'v'):
        code_v()
    elif(kelime[i] == 'w'):
        code_w()
    elif(kelime[i] == 'x'):
        code_x()
    elif(kelime[i] == 'y'):
        code_y()
    elif(kelime[i] == 'z'):
        code_z()
    elif(kelime[i] == 'ç'):
        code_c1()
    elif(kelime[i] == 'ğ'):
        code_g1()
    elif(kelime[i] == 'ı'):
        code_ı()
    elif(kelime[i] == 'ö'):
        code_o1()
    elif(kelime[i] == 'ş'):
        code_s1()
    elif(kelime[i] == 'ü'):
        code_u1()






