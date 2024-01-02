from Funcion_torque import Fun_tor
import math

def Fun_gama(Torque,Rad_ext,Rad_int,Modulo,Ang_r,Rel_ang,long,caso):
    if Torque!=0 and Rad_int!=0 and Rad_ext!=0 and Modulo!=0:
        gama=(Rad_int/Rad_ext)*(((Torque*Rad_ext)/((math.pi*(Rad_ext**4))/4))/Modulo)
        return gama
    elif Torque==0 and Rad_int!=0 and Rad_ext!=0:
        gama=(Rad_int/Rad_ext)*Fun_tor(Ang_r,Rel_ang,Rad_ext,Modulo,long)
        return gama
    
def Fun_esf(Torque,Rad_ext,Rad_int,Ang_r,Rel_ang,Modulo,long,caso):
    if Torque!=0:
        if (caso=="def_uni_max" or caso=="esf_max") and Rad_ext!=0:
            Esf_r=(Torque*Rad_ext)/((math.pi*(Rad_ext**4))/4)
            return Esf_r
        elif (caso=="def_uni" or caso=="esf_r") and Rad_ext!=0 and Rad_int!=0:
            Esf_r=(Torque*Rad_int)/((math.pi*(Rad_ext**4))/4)
            return Esf_r
    else:
        if (caso=="def_uni_max" or caso=="esf_max") and Rad_ext!=0:
            Esf_r=(Fun_tor(Ang_r,Rel_ang,Rad_ext,Modulo,long)*Rad_ext)/((math.pi*(Rad_ext**4))/4)
            return Esf_r
        elif (caso=="def_uni" or caso=="esf_r") and Rad_ext!=0 and Rad_int!=0:
            Esf_r=(Fun_tor(Ang_r,Rel_ang,Rad_ext,Modulo,long)*Rad_int)/((math.pi*(Rad_ext**4))/4)
            return Esf_r