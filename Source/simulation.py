import numpy as np
import math
import random
i=0
Rd_le=6000                  #Length of Road in meters
tt=6*60*60               #Total time
ht_BS=50                    #Height of Base Station in meters
P_Tx=43                   #Total power
L=2                      #Line Loss
AG_Tx=15                  #Antenna Gain 
N_ch=15                   #Number of Chanels
freq_a=860                   #Frequency of alpha
freq_b=865                   #Frequency of Beta
ht_mob=1.5                   #Height of Mobile
hom=3                    #Handoff Margin
RSL_Thres=-102                #RSL thershold
u=320                    #Number of Users
call_rt=2                     #Call Rate
call_rt_prob=2/3600               #probability that user create call in a second
H=180                    #Average Duration of calls
u_vel=15                    #User Speed
Eb=P_Tx+AG_Tx-L            #EIRP at Bore Sight
s=np.random.normal(0,2,Rd_le/10)   #shadowing loss
global activeusers                     #Active users list
activeusers=[]
archive=[]                         #Archives
succ_a=0                    #Successful cals in Alpha sector 
succ_b=0                     #Successful cals in Beta sector 
drop_a=0                      #Call drops in Alpha sector
drop_b=0                       #Call drops in Beta sector
droponalphac=0
droponbetac=0
handofffaila=0                      #Number of handoffs fail
handofffailb=0
handoffsucc=0                      #Number of handoffs success
FreeCh_a=15                   #Free channels in Alpha sector
FreeCh_b=15                    #Free channels in Beta sector
Block_a=0                     #Blocked calls in Alpha sector
Block_b=0                      #Blocked calls in Beta sector 
antenna_dis=[0,	0.02,	0.04,	0.06,	0.09,	0.12,	0.15,	0.19,	0.24,	0.3,	0.35,	0.41,	0.48,	0.55,	0.63,	0.71,	0.8,	0.89,	0.98,	1.09,	1.19,	1.3,	1.42,	1.54,	1.66,	1.79,	1.93,	2.07,	2.21,	2.36,	2.5,	2.66,	2.83,	2.99,	3.15,	3.32,	3.5,	3.68,	3.88,	4.06,	4.26,	4.46,	4.67,	4.87,	5.08,	5.29,	5.5,	5.73,	5.96,	6.2,	6.44,	6.67,	6.91,	7.15,	7.39,	7.64,	7.91,	8.17,	8.43,	8.71,	8.98,	9.24,	9.51,	9.79,	10.07,	10.35,	10.65,	10.94,	11.24,	11.53,	11.83,	12.11,	12.4,	12.79,	13.1,	13.43,	13.75,	14.1,	14.44,	14.78,	15.13,	15.48,	15.84,	16.19,	16.56,	16.95,	17.33,	17.73,	18.12,	18.51,	18.9,	19.33,	19.76,	20.16,	20.61,	21.04,	21.48,	21.92,	22.36,	22.82,	23.26,	23.72,	24.17,	24.62,	25.08,	25.52,	25.98,	26.43,	26.85,	27.28,	27.7,	28.04,	28.4,	28.73,	29.06,	29.42,	29.73,	30.03,	30.34,	30.57,	30.81,	31,	31.22,	31.41,	31.65,	31.86,	32.06,	32.28,	32.47,	32.68,	32.94,	33.21,	33.41,	33.6,	33.89,	34.04,	34.32,	34.65,	34.98,	35.26,	35.51,	35.8,	36.09,	36.29,	36.48,	36.69,	36.84,	37.03,	37.12,	37.08,	37.13,	37.03,	36.97,	36.76,	36.56,	36.33,	35.98,	35.68,	35.28,	34.89,	34.44,	34.04,	33.63,	33.24,	32.83,	32.5,	32.16,	31.81,	31.48,	31.23,	30.96,	30.66,	30.36,	30.15,	29.93,	29.74,	29.56,	29.36,	29.2,	29.06,	29.04,	29.04,	28.92,	28.91,	28.86,	28.8,	28.8,	28.8,	28.74,	28.74,	28.79,	28.81,	28.87,	28.98,	29.04,	29.12,	29.25,	29.38,	29.48,	29.64,	29.81,	29.98,	30.19,	30.42,	30.6,	30.86,	31.06,	31.35,	31.63,	31.95,	32.24,	32.61,	32.97,	33.34,	33.8,	34.23,	34.57,	35.02,	35.55,	36.01,	36.53,	37.12,	37.55,	38.16,	38.72,	39.17,	39.59,	40.04,	40.03,	39.93,	39.8,	39.38,	38.82,	38.24,	37.51,	36.72,	36.02,	35.21,	34.37,	33.68,	32.89,	32.17,	31.47,	30.76,	30.09,	29.46,	28.8,	28.15,	27.57,	26.97,	26.38,	25.81,	25.26,	24.73,	24.21,	23.68,	23.21,	22.74,	22.28,	21.81,	21.39,	20.96,	20.53,	20.11,	19.73,	19.34,	18.96,	18.6,	18.21,	17.84,	17.5,	17.15,	16.81,	16.45,	16.11,	15.78,	15.45,	15.11,	14.8,	14.47,	14.15,	13.84,	13.51,	13.19,	12.89,	12.58,	12.27,	11.96,	11.65,	11.35,	11.04,	10.75,	10.46,	10.17,	9.88,	9.6,	9.31,	9.03,	8.76,	8.48,	8.22,	7.94,	7.69,	7.42,	7.16,	6.92,	6.67,	6.42,	6.19,	5.95,	5.72,	5.5,	5.28,	5.06,	4.85,	4.64,	4.43,	4.22,	4.02,	3.83,	3.64,	3.46,	3.27,	3.1,	2.93,	2.76,	2.59,	2.44,	2.28,	2.14,	2,	1.86,	1.73,	1.61,	1.48,	1.36,	1.25,	1.14,	1.03,	0.93,	0.84,	0.75,	0.67,	0.59,	0.51,	0.44,	0.37,	0.31,	0.26,	0.21,	0.16,	0.12,	0.1,	0.07,	0.04,	0.02,	0.01,	0,	0,	0]
class activeuser:                  #Active Users Class
    def __init__(self,location,direction,timeremain,sector,RSL):
        self.location=location
        self.direction=direction
        self.timeremain=timeremain
        self.sector=sector
        self.RSL=RSL
def pathloss(locat,f):
    d=math.sqrt((abs(locat-Rd_le/2)**2) + 20*20)
    a_hre=(1.1*math.log10(f)-0.7)*ht_mob-(1.56*math.log10(f)-0.8)
    pl=69.55 + 26.16 * math.log10(f) - 13.82 * math.log10(ht_BS)- a_hre +(44.9 - 6.55 * math.log10(ht_BS)) * math.log10(d/1000)
    return(pl)
    
def shadowing(loca):
    sd=s[int(loca/10)-1]
    return(sd)
    
def fading():
    x=np.random.normal(0,1,10)      #Real part in Rayleigh distribution 
    y=np.random.normal(0,1,10)      #Imaginary part in Rayleigh distribution
    z=x+y*(1j)                      #Combining Both real and imaginary part
    fd=np.abs(z)                    #Magnitude of the distribution
    fd.sort()
    return(10*math.log10(fd[1]))

def Eirp(loc,sector):                #Caluculation of RSL
    U =[20.0 ,Rd_le/2 -loc]
    if sector=='a':
        V=[0.0,1.0]
    else:
        V=[math.sqrt(3)/2,-1.0/2]
    Cross=np.cross(U,V)
    ang=180.0*np.arccos(np.dot(U,V)/np.linalg.norm(U)*np.linalg.norm(V))/np.pi
    if Cross>=0:
        ang=ang
    else:
        ang=360.0-ang
    eirp=Eb-antenna_dis[int(ang)]#Caluculation if EIRP 
    return(eirp)

while(tt!=0):                                        #Total time to run program in seconds
    for user in activeusers:                         #Serving the active users already in call
        if(user.direction=='south'):                   #Checking the direction of the user and make changes acording to it.
            user.location=user.location+15 
        else:
            user.location=user.location-15
        user.timeremain=user.timeremain-1                        #Reduce time of the user by one second
        if(user.timeremain<=0):
            #Checking the user if he stopped the call
            if(user.sector=='a'):                      #If call is cancelled by user it is successfull call,so check the sector and update values
                succ_a=succ_a+1        #If cahnnel is on Alpha update successfull calls record 
                FreeCh_a=FreeCh_a+1        #Free the channel used by the user to give to incoming user
            else:
                succ_b=succ_b+1          #If sector is Beta update successfull calls record 
                FreeCh_b=FreeCh_b+1          #Free the channel used by the user to give to incoming user
            archive.append(user)                     #Append this user in to Archives
            activeusers.remove(user)                 #Remove this user  record from active list users
            continue                                 #done with existing user and cuntinue to next user
        
        else:                                                #If Call was not ended
            if(user.location>Rd_le or user.location<0):       #Check if user moved out of the 6000 meter road
                
                if(user.sector=='a'):                          #If user moved out conside as succesfull and haded over to next base station
                    succ_a=succ_a+1            #Update the record of successful calls
                    FreeCh_a=FreeCh_a+1            #Free the channel used by the user
                else:
                    succ_b=succ_b+1              #Update the record of successful calls
                    FreeCh_b=FreeCh_b+1              #Free the channel used by the user
                archive.append(user)                         #Append this user to Archives 
                activeusers.remove(user)                     #Remove the user from active users list 
                continue                                     #done with the user and cuntinue to other user in the list
            else:                                            #If user is with in the road given 
                if(user.sector=='a'):
                    f=freq_a
                else:
                    f=freq_b
                user.RSL=Eirp(user.location,user.sector)- pathloss(user.location,f) + shadowing(user.location) + fading()      #update the RSl value of the user with new location   
                if(user.RSL<RSL_Thres):
                    #Check if users RSL value fall below the threshold value given
                    if(user.sector=='a'):                      #If RSL value fall below threshold value then it is dropped call Check the sector and update value 
                        drop_a=drop_a+1            #Update the dropped calls record inthe sector
                        FreeCh_a=FreeCh_a+1        #Free the channel for the futrure use
                    else:
                        drop_b=drop_b+1              #Update the dropped calls record inthe sector 
                        FreeCh_b=FreeCh_b+1          #Free the channel for the futrure use
                    activeusers.remove(user)                 #Remove the user from the active users list 
                    continue                                 #Done with this user move to next user
                else:                                        #If RSL is above the threshold value given
                    if(user.sector=='a'):                      #Check the sector of this user and get the other sector
                        anothersec='b'
                        anotherfreq=freq_b
                    else:
                        anothersec='a'
                        anotherfreq=freq_a
                    rslother=Eirp(user.location,anothersec)- pathloss(user.location,anotherfreq) + shadowing(user.location) + fading()  #Caluculate the RSL value  of the another sector 
                    if(rslother>=user.RSL+hom):                   #Check if the RSL value is greater than the thershold and hand off margin value 
                        if(anothersec=='a'):                   #For sector Alpha 
                            if(FreeCh_a<1):             #Check if there are free channels on the sector
                                handofffaila=handofffaila+1    #If there are no free channels on the sector then it is a handoff failure in this sector
                            else:                            #If channel is available
                                handoffsucc=handoffsucc+1    #Make it successful handoff  
                                user.sector='a'                #Change the sector of the user to another sector
                                FreeCh_a=FreeCh_a-1#Take one the channel on this sector  
                                FreeCh_b=FreeCh_b+1  #Free the channel on this sector
                        else:                                #For sector Beta  
                            if(FreeCh_b<1):             
                                handofffailb=handofffailb+1
                            else:
                                handoffsucc=handoffsucc+1
                                user.sector='b'
                                FreeCh_a=FreeCh_a+1
                                FreeCh_b=FreeCh_b-1
                        
    while(i<=u-len(activeusers)):                               #For all non active users 
        i=i+1
        epro=random.randrange(0,10000000,1)
        epro=epro/10000000
        if(epro<=call_rt_prob):                                       #If user requested call
            nloc=(int(np.random.uniform(0,Rd_le)))                    #Get the location of the user from uniform distribution
            ndirec=random.choice(['south','north'])              #Get the direction from the random choice between north and south 
            nrsla=Eirp(nloc,'a')- pathloss(nloc,freq_a) + shadowing(nloc) + fading()                                #Get RSL value for sector Alpha
            nrslb=Eirp(nloc,'b')- pathloss(nloc,freq_b) + shadowing(nloc) + fading()                               #Get RSL value for sector Btea
            rsl=max(nrsla,nrslb)                             #Take the maximum between the two RSL values 
            if(rsl<RSL_Thres):                                    #Check the RSl with the Threshold value given
                if(rsl==nrsla):                              #If RSL value is less than threshold value Then it is droped call
                    drop_a=drop_a+1                #Check the sector and uodate the record for droped calls
                else:
                    drop_b=drop_b+1
                continue                                     #Done with user and move to another user
            else:                                            #If RSL value greater than the threshold value
                if(rsl==nrsla):                              #Check for the sector 
                    nsec='a'
                else:
                    nsec='b'
                if(nsec=='a'):                                 #Fir sector Alpha
                    if(FreeCh_a<1):                     #Check the availability of the channel 
                        Block_a=Block_a+1          #If channel is not available then it is blocked call and update the record
                        if(nrslb>RSL_Thres):
                            if(FreeCh_b<1):
                                print('dropdcal')
                                droponalphac=droponalphac+1
                                continue
                            else:
                                nsec='b'
                                nlen=np.random.exponential(H)
                                activeusers.append(activeuser(nloc,ndirec,nlen,nsec,nrslb))
                                FreeCh_b=FreeCh_b-1
                                continue
                        else:
                            continue
                                
                    else:                                    #If channel is available
                        nlen=np.random.exponential(H)        #Get the duration the call from exponential distribution with mean H
                        activeusers.append(activeuser(nloc,ndirec,nlen,nsec,rsl))  #Make the new Acctive user instance with records
                        FreeCh_a=FreeCh_a-1
                        continue                                   #Get one channel for call
                               #Append this user to active users list 
                else:                                                                   #For sector Beta 
                    if(FreeCh_b<1):
                        Block_b=Block_b+1
                        if(nrsla>RSL_Thres):
                            if(FreeCh_a<1):
                                print('dropdc')
                                droponbetac=droponbetac+1
                                continue
                            else:
                                nsec='a'
                                nlen=np.random.exponential(H)
                                activeusers.append(activeuser(nloc,ndirec,nlen,nsec,nrsla))
                                FreeCh_a=FreeCh_a-1
                                continue
                        else:
                            continue
                        
                    else:
                        nlen=np.random.exponential(H)
                        activeusers.append(activeuser(nloc,ndirec,nlen,nsec,rsl))
                        FreeCh_b=FreeCh_b-1
                        continue
                
        else:
            continue
         
    if(tt%(3600)==0):
        print('Number of channels currently in use         :'+str(30-FreeCh_a-FreeCh_b))
        print('Number of call Attempts                     :'+str(succ_a+succ_b+drop_a+drop_b+Block_a+Block_b))
        print('Succesfull calls on ALPHA                   :'+str(succ_a)+'  Succesfull calls on BETA                   :'+str(succ_b)+'  Total Succesfull Calls:'+str(succ_a+succ_b))
        print('Number of Succesfull Handoffs               :'+str(handoffsucc))
        print('Number Handoffs fail into ALPHA             :'+str(handofffaila)+'  Number Handoffs fail into BETA               :'+str(handofffailb))
        print('Dropped calls due to Signal Stregth on ALPHA:'+str(drop_a)+'  Dropped calls due to Signal Stregth on BETA:'+str(drop_b))
        print('Dropped calls due to capacity on ALPHA      :'+str(droponalphac)+'  Dropped calls due to capacity on BETA      :'+str(droponbetac))
        print('Blocked calls due to Capacity on ALPHA      :'+str(Block_a)+'  Blocked calls due to Capacity on ALPHA    :'+str(Block_b))
        print('\n')
    tt=tt-1
    i=0
        
if(tt==0):
    print('--------------------------FINAL REPORT OF BASE STATION----------------------------')
    print('Number of channels currently in use         :'+str(30-FreeCh_a-FreeCh_b))
    print('Number of call Attempts                     :'+str(succ_a+succ_b+drop_a+drop_b+Block_a+Block_b))
    print('Succesfull calls on ALPHA                   :'+str(succ_a)+'  Succesfull calls on BETA                   :'+str(succ_b)+'  Total Succesfull Calls:'+str(succ_a+succ_b))
    print('Number of Succesfull Handoffs               :'+str(handoffsucc))
    print('Number Handoffs fail into ALPHA             :'+str(handofffaila)+'  Number Handoffs fail into BETA               :'+str(handofffailb))
    print('Dropped calls due to Signal Stregth on ALPHA:'+str(drop_a)+'  Dropped calls due to Signal Stregth on BETA:'+str(drop_b))
    print('Dropped calls due to capacity on ALPHA      :'+str(droponalphac)+'  Dropped calls due to capacity on BETA      :'+str(droponbetac))
    print('Blocked calls due to Capacity on ALPHA      :'+str(Block_a)+'  Blocked calls due to Capacity on BETA     :'+str(Block_b))
    
    
                        
            
