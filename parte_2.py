
#import keyboard

#print("Presione la tecla P para detener el programa")
#while True:
#    if keyboard.is_pressed('p'):
#        break       
#print("Programa detenido por el usuario")   

import keyboard

print("Presione la tecla P para detener el programa")
while True:
    key = keyboard.read_key('p')
    print("key: ")
    if key == keyboard.key('p'):
        break       
print("Programa detenido por el usuario")   
