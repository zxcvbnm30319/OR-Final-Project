# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 19:36:51 2022

@author: wcsl
"""



from pyomo.environ import *
import numpy as np
facility = ['customers', 'distribution centers', 'warehouses', 'manufacturers', 'TM', 'TW','TD','type i','type j']
distance = ['MW','MD''DC']

demc = {'customers_0':1000,
        'customers_1':1000,
        'customers_2':1000,
        'customers_3':1000,
        'customers_4':1000,
        'customers_5':1000,
        'customers_6':1000,
        'customers_7':1000,
        'customers_8':1000,
        'customers_9':1000,
        'customers_10':1000,
        'customers_11':1000,
        'customers_12':1000,
        'customers_13':1000,
        'customers_14':1000,
        'customers_15':1000
        }
#demf = {'manufacturers':40,'warehouses':50,'distribution centers':70}
crm = {'type i':100,'type j':50}
c = {'TM':10,'TW':20,'TD':30}
dis = {'MW':200,'WD':400,'DC':600}
fc = {'manufacturers':1000,'warehouses':800,'distribution centers':600}
lt = {'manufacturers':250,'warehouses':160}
vc = {'manufacturers':1200,'warehouses':1000,'distribution centers':800}
inv = {'warehouses':200,'distribution centers':200}
nrr = {'type i':20,'type j':30}
p = 1000
ca = {'manufacturers':10000,'warehouses':10000,'distribution centers':10000,'TM':8000,'TW':8000,'TD':8000}

#manufacturers
demm = {'manufacturers_0':50,'manufacturers_1':80,'manufacturers_2':100}
fcm={'manufacturers_0':100,'manufacturers_1':120,'manufacturers_2':180}
vcm={'manufacturers_0':150,'manufacturers_1':200,'manufacturers_2':250}
invm={'manufacturers_0':30,'manufacturers_1':50,'manufacturers_2':80}
cam={'manufacturers_0':1000,'manufacturers_1':1000,'manufacturers_2':1000}


#---warehouses---
demw={'warehouses_0':120,'warehouses_1':150,'warehouses_2':180,'warehouses_3':200}
fcw={'warehouses_0':200,'warehouses_1':250,'warehouses_2':280,'warehouses_3':350}
vcw={'warehouses_0':100,'warehouses_1':100,'warehouses_2':150,'warehouses_3':150}
invw={'warehouses_0':100,'warehouses_1':150,'warehouses_2':200,'warehouses_3':250}
caw={'warehouses_0':1000,'warehouses_1':1000,'warehouses_2':1000,'warehouses_3':1000}

#--- distribution centers------   
demd={'distribution centers_0':250,'distribution centers_1':280,'distribution centers_2':300,'distribution centers_3':320,'distribution centers_4':350}
fcd = {'distribution centers_0':200,'distribution centers_1':250,'distribution centers_2':300,'distribution centers_3':300,'distribution centers_4':300}
vcd={'distribution centers_0':150,'distribution centers_1':200,'distribution centers_2':350,'distribution centers_3':250,'distribution centers_4':250}
invd={'distribution centers_0':200,'distribution centers_1':200,'distribution centers_2':300,'distribution centers_3':400,'distribution centers_4':500}
cad={'distribution centers_0':1000,'distribution centers_1':1000,'distribution centers_2':1000,'distribution centers_3':1000,'distribution centers_4':1000}

#Transportation
TM={'TM1':100,'TM2':150,'TM3':200,'TM4':500}
TW={'TW1':150,'TW2':200,'TW3':250}
TD={'TD1':200,'TD2':250,'TD3':300}



GN={'manufacturers':30,'warehouses':50,'distribution centers':60,'TM':10,'TW':20,'TD':35}
GC={'manufacturers':10,'warehouses':30,'distribution centers':90,'TM':30,'TW':25,'TD':50}
GO={'manufacturers':20,'warehouses':40,'distribution centers':50,'TM':100,'TW':40,'TD':40}

#DECSION VARIABLES
model = ConcreteModel()
model.xm = Var(demm,domain=Binary)
model.xw = Var(demw,within = Binary)
model.xd = Var(demd,within = Binary)
model.xtm = Var(TM,bounds=(0, None),domain=NonNegativeReals)
model.xtw = Var(TW,bounds=(0, None),domain=NonNegativeReals)
model.xtd = Var(TD,bounds=(0, None),domain=NonNegativeReals)
model.xim = Var(bounds=(0, None),domain=NonNegativeReals)
model.xjm = Var(bounds=(0, None),domain=NonNegativeReals)
model.od = Var()
model.ow = Var()

#OBJ
model.obj = Objective(expr=sum(fcm[i]*model.xm[k] for i in fcm for k in model.xm)
                 +sum(fcw[i]*model.xw[k] for i in fcw for k in model.xw)\
                +sum(fcd[i]*model.xd[k] for i in fcd for k in model.xd)\
                +sum(vcm[i]*demm[k] for i in vcm for k in demm)\
                +sum(vcw[i]*demw[k] for i in vcw for k in demw)\
                +sum(vcd[i]*demd[k] for i in vcd for k in demd)\
                +sum(model.xtm[i]*dis['MW']*TM[k] for i in model.xtm for k in TM)\
                +sum(model.xtw[i]*dis['WD']*TW[k] for i in model.xtw for k in TW)\
                +sum(model.xtd[i]*dis['DC']*TD[k] for i in model.xtd for k in TD)\
                +(model.xim*crm['type i'])+model.xjm*crm['type j']\
                +sum((demc[i]-model.xtd[k])*p for i in demc for k in model.xtd)\
                +sum(invw[i]*5+invd[k]*10 for i in invw for k in invd) ,sense=minimize) 
'''


                      

model.obj = Objective(expr = sum(model.xim[i]*GN['manufacturers']+model.xjm[j]*GN['manufacturers'] for i in model.xim for j in model.xjm)
                              +sum(demw[i]*GN['warehouses'] for i in demw)
                              +sum(demd[i]*GN['distribution centers'] for i in demd)\
                              +sum(model.xtm[i]*GN['TM']*dis['MW'] for i in model.xtm)
                              +sum(model.xtw[i]*GN['TW']*dis['WD'] for i in model.xtw)
                              +sum(model.xtd[i]*GN['TD']*dis['DC'] for i in model.xtd)\
                              +sum(model.xim[i]*GC['manufacturers']+model.xjm[j]*GC['manufacturers'] for i in model.xim for j in model.xjm)
                              +sum(demw[i]*GC['warehouses'] for i in demw)
                              +sum(demd[i]*GC['distribution centers'] for i in demd)\
                              +sum(model.xtm[i]*GC['TM']*dis['MW'] for i in model.xtm)
                              +sum(model.xtw[i]*GC['TW']*dis['WD'] for i in model.xtw)
                              +sum(model.xtd[i]*GC['TD']*dis['DC'] for i in model.xtd)\
                              +sum(model.xim[i]*GO['manufacturers']+model.xjm[j]*GO['manufacturers'] for i in model.xim for j in model.xjm)
                              +sum(demw[i]*GO['warehouses'] for i in demw)
                              +sum(demd[i]*GO['distribution centers'] for i in demd)\
                              +sum(model.xtm[i]*GO['TM']*dis['MW'] for i in model.xtm)
                              +sum(model.xtw[i]*GO['TW']*dis['WD'] for i in model.xtw)
                             +sum(model.xtd[i]*GO['TD']*dis['DC'] for i in model.xtd),sense= minimize)
               
 '''                                 

#constraint
#(12)~(14) 製造商、倉庫、配送中心的需求=運輸的數量
for i in demm:
        model.c1 = Constraint(expr = (demm[i]  <= sum(model.xtm[k]   for k in model.xtm )))
for i in demw:
        model.c2 = Constraint(expr = (demw[i]  <= sum(model.xtw[k]   for k in model.xtw )))
for i in demd:
        model.c3 = Constraint(expr = (demd[i]  <= sum(model.xtd[k]   for k in model.xtd )))        

#(15)~(18)
oc=3
za=1
model.c4=Constraint(expr = model.od == sum(oc*model.xtd[i]/demd[k] for i in model.xtd for k in demd))
model.c6=Constraint(expr = model.ow == sum(model.od*model.xtw[i]/demw[k] for i in model.xtw for k in demw))
for i in invd:
    for j in demd:
        model.c7=Constraint(expr = invd[i] <= demd[j]*0.5+za*model.od*sum(model.xtw[k] for k in model.xtw)*(lt['warehouses']**0.5 )/demd[j])
for i in invw:
    for j in demw:
        model.c5=Constraint(expr = invw[i] <= demw[j]*0.5+za*model.ow*sum(model.xtm[k] for k in model.xtm)*(lt['manufacturers']**0.5)/demw[j])

#(19)~(21)
for i in cam:
    for j in model.xm :
        model.c8=Constraint(expr = (cam[i]*model.xm[j] >= sum(model.xtm[k] for k in model.xtm)))
        
for i in caw:
    for j in model.xw :
        model.c9=Constraint(expr = (caw[i]*model.xw[j] >= sum(model.xtw[k] for k in model.xtw)))

for i in cad:
    for j in model.xd :
        model.c10=Constraint(expr = (cad[i]*model.xd[j] >= sum(model.xtd[k] for k in model.xtd)))          


#(22)~(24)
for i in model.xm:
    for k in model.xtm:
        model.c11=Constraint(expr = model.xm[i] <= model.xtm[k])
for i in model.xw:
    for k in model.xtw:
        model.c12=Constraint(expr = model.xw[i] <= model.xtw[k])
for i in model.xd:
    for k in model.xtd:
        model.c13=Constraint(expr = model.xd[i] <= model.xtd[k])        



#(25)(26)
for k in demm:
    model.c14=Constraint(expr = sum(model.xim[i] for i in model.xim) == demm[k]*nrr['type i'] )
for k in demm:
    model.c15=Constraint(expr = sum(model.xjm[i] for i in model.xjm) == demm[k]*nrr['type j'] )    


#(27)~(29)
for i in demw:
    model.c16=Constraint(expr = sum(model.xtm[k] for k in model.xtm) <= demw[i])
for i in demd:
    model.c17=Constraint(expr = sum(model.xtw[k] for k in model.xtw) <= demd[i])
    
for i in demc:
    model.c18=Constraint(expr = sum(model.xtd[k] for k in model.xtd) <= demc[i])
      

#(30)~(32)

model.c19=Constraint(expr=sum(model.xtm[i] for i in model.xtm) <= ca['TM'])
model.c20=Constraint(expr=sum(model.xtw[i] for i in model.xtw) <= ca['TW'])
model.c21=Constraint(expr=sum(model.xtd[i] for i in model.xtd) <= ca['TD'])

'''
#constraint cost
model.c22 = Constraint(expr = sum(fcm[i]*model.xm[k] for i in fcm for k in model.xm)
                 +sum(fcw[i]*model.xw[k] for i in fcw for k in model.xw)\
                +sum(fcd[i]*model.xd[k] for i in fcd for k in model.xd)\
                +sum(vcm[i]*demm[k] for i in vcm for k in demm)\
                +sum(vcw[i]*demw[k] for i in vcw for k in demw)\
                +sum(vcd[i]*demd[k] for i in vcd for k in demd)\
                +sum(model.xtm[i]*dis['MW']*TM[k] for i in model.xtm for k in TM)\
                +sum(model.xtw[i]*dis['WD']*TW[k] for i in model.xtw for k in TW)\
                +sum(model.xtd[i]*dis['DC']*TD[k] for i in model.xtd for k in TD)\
                +(model.xim*crm['type i'])+model.xjm*crm['type j']\
                +sum((demc[i]-model.xtd[k])*p for i in demc for k in model.xtd)\
                +sum(invw[i]*5+invd[k]*10 for i in invw for k in invd) >= 378149662)
'''


solver=SolverFactory('ipopt')
solver.solve(model, tee=True)
print(value(model.obj))




def VC():
    a=0
    b=0
    c=0
    m=0
    w=0
    d=0
    for i in  vcm:
        for k in demm:
            a=vcm[i]*demm[k]
            m+=a
    for i in  vcw:
        for k in demw:
            b=vcw[i]*demw[k]
            w=w+b
    for i in  vcd:
        for k in demd:
            c=vcd[i]*demd[k]
            d+=c
    VC=(m+w+d)/round(value(model.obj),0)*100         
    print("VC=",VC)                            
VC() 


def FC():
    a=0
    b=0
    c=0
    m=0
    w=0
    d=0
    for i in  fcm:
        for k in model.xm:
            a=(fcm[i]*value(model.xm[k]))
            m+=a
    for i in  fcw:
        for k in model.xw:
            b=fcw[i]*value(model.xw[k])
            w=w+b
    for i in  fcd:
        for k in model.xd:
            c=fcd[i]*value(model.xd[k])
            d+=c
    FC=(m+w+d)/round(value(model.obj),0)*100         
    print("FC=",FC)                            
FC()

def TC():
    a=0
    b=0
    c=0
    m=0
    w=0
    d=0
    for i in model.xtm:
        for k in TM:
            a=value(model.xtm[i])*dis['MW']*TM[k]
            m+=a
    for i in model.xtw:
        for k in TW:
            b=value(model.xtw[i])*dis['WD']*TW[k]
            w+=b
    for i in model.xtd:
        for k in TD:
            c=value(model.xtd[i])*dis['DC']*TD[k]
            d+=c
    TC=(m+w+d)/round(value(model.obj),0)*100          
    print("TC=",TC)   
TC()


def RC():
    RC=0
    RC=value(model.xim)*crm['type i']+value(model.xjm)*crm['type j']
    RC=RC/round(value(model.obj),0)*100 
    print("RC=",RC)
RC()

def BC():
    BC=0
    a=0
    for i in demc:
        for k in model.xtd:
           a=(demc[i]-value(model.xtd[k]))*p
           BC+=a
    BC=BC/round(value(model.obj),0)*100        
    print("BC=",BC)       
BC() 

def HC():
    HC=0
    for i in invw:
        for k in invd:
         a=invw[i]*5+invd[k]*10
         HC+=a
    HC=HC/round(value(model.obj),0)*100      
    print("HC=",HC)
   
HC()
