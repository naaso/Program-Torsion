import math

def Fun_tor(Ang_r,Rel_ang,Rad_ext,Modulo,long):
    if Rel_ang!=0 and Modulo!=0 and Rad_ext!=0:
        fun_tor=Rel_ang*Modulo*((math.pi*Rad_ext**4)/4)
        return fun_tor
    elif Ang_r!=0 and Rad_ext!=0 and Modulo!=0 and long!=0:
        fun_tor=(Ang_r/long)*Modulo*((math.pi*Rad_ext**4)/4)
        return fun_tor
