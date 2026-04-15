import json
import re
import math

class Myparseline:
    lsmovement=""
    lsplane=""
    lstiprotation=""
    lsrotation=""
    lstipfedrejt=""
    lssklop=""
    koord_x = 0.00000
    koord_y = 0.00000
    koord_z = 0.00000
    ls_x = 0.00000
    ls_y = 0.00000
    ls_z = 0.00000
    ls_i=0.00000
    ls_j=0.00000
    ls_k=0.00000
    D=0.00000

    
    
    def __init__(self):
        self.lsmovement=""
        self.lsplane=""
        self.lstiprotation=""
        self.lsrotation=""
        self.lstipfedrejt=""
        self.lssklop=""
        self.ls_x = 0.000
        self.ls_y = 0.000
        self.ls_z = 0.000
        self.ls_i = 0.000
        self.ls_j = 0.000
        self.ls_k = 0.000
        self.D = 0.000
        
    def parseline(self, line):

            if not line.strip():
                print(end="")
            
            elif "$$ OPERATION NAME :" in line:
                opname = line.split(":")
                opname1 = opname[0].strip()
                opname2 = opname[1].strip()
            
                if "Tool" in opname2:
                    print(end="")
                else:
                    print(f"#{opname2}")
            
            elif line.startswith("SWITCH") or line.startswith("LOADTL") or line.startswith("CUTTER") or line.startswith("TOOLNO") or line.startswith("INTOL") or line.startswith("OUTTOL") or line.startswith("AUTOPS") or line.startswith ("$$"):
                print(end="")
            
            elif "CIRCLE" in line:
                elements = re.split(r'[ ,/()]+', line)
                centar_x = elements[3].strip()
                centar_y = elements[4].strip()
                centar_z = elements[5].strip()
                radius = elements[6].strip()
                centar2_x = elements[9].strip()
                centar2_y = elements[10].strip()
                centar2_z = elements[11].strip()
                kraj_x = elements[12].strip()
                kraj_y = elements[13].strip()
                kraj_z = elements[14].strip()
                
                kraj_x = float(kraj_x)
                kraj_y = float(kraj_y)
                kraj_z = float(kraj_z)
                
                kraj_x = round(kraj_x, 3)
                kraj_y = round(kraj_y, 3)
                kraj_z = round(kraj_z, 3)

                if centar_x!=centar2_x or centar_y!=centar2_y or centar_z!=centar2_z:
                    print(f"Provjeriti {line} centri se ne poklapaju")
                else:
                    print(end="")
            
                if self.lsplane == "G18":
                    vektor2_x=float(self.ls_x)-float(centar_x)
                    vektor2_z=float(self.ls_z)-float(centar_z)
                    D=float(self.ls_i)*vektor2_z-vektor2_x*float(self.ls_k)
                    
                    vektor2_x=round(vektor2_x, 3)
                    vektor2_z=round(vektor2_z, 3)
                
                    if D<0:
                        movement="G2"
                    elif D>0:
                        movement="G3"
                    else:
                        print("Provjeriti koord " + line)
                        
                    koord=f"X{kraj_x} Z{kraj_z} I{vektor2_x} K{vektor2_z}"
                    
                elif self.lsplane == "G17":
                    vektor2_y=float(self.ls_y)-float(centar_y)
                    vektor2_x=float(self.ls_x)-float(centar_x)
                    D=float(self.ls_i)*vektor2_y-vektor2_x*float(self.ls_j)

                    vektor2_y=round(vektor2_y, 3)
                    vektor2_x=round(vektor2_x, 3)
                    
                    if D<0:
                        movement="G2"
                    elif D>0:
                        movement="G3"
                    else:
                        print("Provjeriti koord " + line)
                         
                    koord=f"X{kraj_x} Y{kraj_y} I{vektor2_x} J{vektor2_y}"
                    
                elif self.lsplane == "G19":
                    vektor2_y=float(self.ls_y)-float(centar_y)
                    vektor2_z=float(self.ls_z)-float(centar_z)
                    D=float(self.ls_j)*vektor2_z-vektor2_y*float(self.ls_k)

                    vektor2_y=round(vektor2_y, 3)
                    vektor2_z=round(vektor2_z, 3)  
                    
                    if D<0:
                        movement="G2"
                    elif D>0:
                        movement="G3"
                    else:
                        print("Provjeriti koord " + line)
                    koord=f"Y{kraj_y} Z{kraj_z} J{vektor2_y} K{vektor2_z}"
                else:
                    print(f"Provjeriti ravninu: {line}")
            
                print(movement, koord)
            
                self.ls_x=kraj_x
                self.ls_y=kraj_y
                self.ls_z=kraj_z
                self.lsmovement=movement
                      
            elif line.startswith("GOTO"):
                coords = re.split(r'[,/]+', line)
                x = coords[1].strip()
                y = coords[2].strip()
                z = coords[3].strip()
                
                x = float(x)
                y = float(y)
                z = float(z)
                
                if y==self.ls_y:
                    self.koord_y=" "
                    ravnina="G18"
                    if x==self.ls_x:
                        self.koord_x=" "
                    else:
                        self.koord_x=(f"X{x}")
                    if z==self.ls_z:
                        self.koord_z=" "                    
                    else:
                        self.koord_z=(f"Z{z}")      
                elif x!=self.ls_x:
                    self.koord_z=" "
                    ravnina="G17"
                    if x==self.ls_x:
                        self.koord_x=" "
                    else:
                        self.koord_x=(f"X{x}")
                    if y==self.ls_y:
                        self.koord_y=" "
                    else:
                        self.koord_y=(f"Y{y}")       
                elif z!=self.ls_z:
                    self.koord_x=" "
                    ravnina="G19"
                    if y==self.ls_y:
                        self.koord_y=" "
                    else:
                        self.koord_y=(f"Y{y}")
                    if z==self.ls_z:
                        self.koord_z=" "                    
                    else:
                        self.koord_z=(f"Z{z}")       
                else:
                    print(f"Provjeriti koordinate: {line}")
                           
                if self.lsplane != ravnina:
                    print(ravnina, end=" ")
                    self.lsplane=ravnina                  
                else:
                    print(end="")
                    
                print(self.koord_x, self.koord_y, self.koord_z)
                self.ls_x=x
                self.ls_y=y
                self.ls_z=z
                
            elif line.startswith("SPINDL"):
                spindlDT = re.split(r'[,/]+', line)
                num = spindlDT[1].strip()
                tip = spindlDT[2].strip()
                rotation = spindlDT[3].strip()
                
                if tip == "SFM":
                    tipfedrejt=("G96 ")
                elif tip == "RPM":
                    tipfedrejt=("G97 ")
                else:
                    print(f"Provjeriti tip vrijednosti(spm ili rpm): {line}")
                    
                if self.lstiprotation != tipfedrejt:
                    print(tipfedrejt, end=" ")
                    self.lstiprotation=tipfedrejt
                else:
                    print(end="")
                    
                if rotation == "CLW":
                    smjervrtnje=("M3 ")
                elif rotation == "CCLW":
                    smjervrtnje=("M4 ")
                else:
                    print(f"Provjeriti treću vrijednost (smjer vrtnje): {line}")
                    
                if self.lsrotation != smjervrtnje:
                    print(smjervrtnje, end=" ")
                    self.lsrotation=smjervrtnje
                else:
                    print(end="")
                    
                print("S"+num)
                
            elif line.startswith("FEDRAT"):
                feed = re.split(r'[,/]+', line)
                numf = feed[1].strip()
                vrstaf = feed[2].strip()
                
                if vrstaf == "MMPR":
                    fedrejt=("G95")   
                elif vrstaf == "MMPM":  
                    fedrejt=("G94")
                else:
                    print(f"Provjeriti feedrate vrijednost: {line}")
                    
                if self.lstipfedrejt != fedrejt:
                    print(fedrejt, end=" ")
                    self.lstipfedrejt=fedrejt
                else:
                    print(end="")
                    
                movement="G1"
                
                if self.lsmovement != movement:
                        print(movement, end=" ")
                        self.lsmovement=movement
                else:
                        print(end="")
                
                print("F"+numf)
                
            elif line.startswith("TPRINT"):
                izbor_alat = re.split(r'[,/]+', line)
                sklop = izbor_alat[1].strip()
                drzac = izbor_alat[2].strip()
                ostrica = izbor_alat[3].strip()
                
                if self.lssklop != sklop:
                    print(f"T={sklop}")
                    self.lssklop=sklop
                else:
                    print(end="")
                
            elif line.startswith("INDIRV"):
                vektor = re.split(r'[,/]+', line)
                self.ls_i=vektor[1].strip()
                self.ls_j=vektor[2].strip()
                self.ls_k=vektor[3].strip()
                
            elif line.startswith("RAPID"):
                if self.lsmovement != "G0":
                    print("G0 ")
                    self.lsmovement="G0"
                else:
                    print(end="")
            
            elif line.startswith("FINI"):
                print(" G18 G0 X40 Z90\n M30")
            
            elif line.startswith("PARTNO"):
                print("G55" + "\n" + "DIAMOF" + "\n" + "#DEFINIRATI SIROVAC")
           
            else:
                print("Provjeriti: " + line)
      