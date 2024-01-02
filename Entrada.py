from Segundas_condiciones import Fun_gama,Fun_esf
from Funcion_torque import Fun_tor
import math

def Var_dep():
    
    fin="no"
    while fin=="no":
        
        caso=input("¿Que desea calcular?: ")
        print("Ingreso de datos")
        long=float(input("Longitud del tramo: "))
        gama_max=float(input("Def_uni_max: "))
        Rad_ext=float(input("Rad_ext: "))
        Rad_int=float(input("Rad_Int: "))
        Modulo=float(input("Modulo: "))
        Esf_Max=float(input("Esf_Max: "))
        Torque=float(input("Torque: "))
        Ang_r=float(input("Angulo de torsión: "))
        Rel_ang=float(input("Razón de torsión: "))

        Tor=Fun_tor(Ang_r,Rel_ang,Rad_ext,Modulo,long)
        
        if caso=="def_uni":
            if gama_max!=0 and Rad_int!=0 and Rad_ext!=0:
                gama=(Rad_int/Rad_ext)*gama_max
                return f"Def_uni({Rad_int}) = {round(gama,5)} Rad"
            elif Modulo!=0 and Esf_Max!=0 and Rad_int!=0 and Rad_ext!=0:
                gama=(Rad_int/Rad_ext)*(Esf_Max/Modulo)
                return f"Def_uni({Rad_int}) = {round(gama,5)} Rad"
            elif Esf_Max==0 and Rad_int!=0 and Rad_ext!=0: 
                gama=Fun_gama(Torque,Rad_ext,Rad_int,Modulo,Ang_r,Rel_ang,long,caso)    
                return f"Def_uni({Rad_int}) = {round(gama,5)} Rad"
        
        elif caso=="def_uni_max" and  Modulo!=0:
            if  Esf_Max!=0:
                gama_max=Esf_Max/Modulo
                return f"Def_uni_max= {round(gama_max,5)} Rad"
            else:
                gama_max=Fun_esf(Torque,Rad_ext,Rad_int,Ang_r,Rel_ang,Modulo,long,caso)/Modulo
                return f"Def_uni_max= {round(gama_max,9)} Rad"
            
        elif caso=="esf_r" and Rad_ext!=0 and Rad_int!=0:
            if Esf_Max!=0:
                Esf_r=(Rad_int/Rad_ext)*Esf_Max
                return f"Esf_r({Rad_int}) = {round(Esf_r,2)} Pa"
            else:
                Esf_r=Fun_esf(Torque,Rad_ext,Rad_int,Ang_r,Rel_ang,Modulo,long,caso)    
                return f"Esf_r({Rad_int}) = {round(Esf_r,2)} Pa"
        
        elif caso=="esf_max" and Rad_ext!=0 and Rad_int!=0:
            if Torque!=0:
                Esf_Max=(Torque*Rad_ext)/((math.pi*(Rad_ext**4))/4)
                return f"Esfuerzo maximo= {round(Esf_Max,2)} Pa"
            else:
                Esf_Max=Fun_esf(Torque,Rad_ext,Rad_int,Ang_r,Rel_ang,Modulo,long,caso)
                return f"Esfuerzo maximo= {round(Esf_Max,2)} Pa"
        
        elif caso=="ang_tor" and Rad_ext!=0 and Modulo!=0 and long!=0:
            
            if Torque!=0:
                ang_r=(Torque*long)/(Modulo*((math.pi*(Rad_ext**4))/4))
                return f"Ang_tor = {round(ang_r,2)}°"
            else:
                ang_r=(Tor*long)/(Modulo*((math.pi*(Rad_ext**4))/4))
                return f"Ang_tor = {round(ang_r,2)}°"
        
        elif caso=="raz_tor" and long!=0:
            
            if Ang_r!=0:
                Rel_ang=Ang_r/long
                return f"Raz_tor = {round(Rel_ang,2)}°/m"
            elif Torque!=0 and Modulo!=0 and Rad_ext!=0:
                Rel_ang=((Torque*long)/(Modulo*((math.pi*(Rad_ext**4))/4)))/long
                return f"Raz_tor = {round(Rel_ang,2)}°/m"
            elif Torque==0 and Modulo!=0 and Rad_ext!=0:
                Rel_ang=((Tor*long)/(Modulo*((math.pi*(Rad_ext**4))/4)))/long
                return f"Raz_tor = {round(Rel_ang,2)}°/m"
        
        elif caso=="torque":
            return f"Torque = {round(Tor,2)}N-m"
            
        else:
            print("Revise si escogió corectamente su petición y/o ingresó los datos mínimos para el cálculo")
            fin=input("Si desea terminar el programa, escriba si, si no, no: ")