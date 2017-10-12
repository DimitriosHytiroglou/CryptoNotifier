#Write code that loops through the 2 Service lists and checks each user
# Then checks the exchange rates array
# And finally if needed calls twilio to send text
import sys
sys.path.insert(0, '../db')
import shelve
from CryptoCheck import check_Divergence, check_Spike
import requests as rqst


def Cryptolog():
    #allCoins = 'BTC,ETH,XRP,BCH,LTC,DASH,XEM,NEO,XMR,BCC,MIOTA,ETC,QTUM,ADA,LSK,ZEC,WAVES,HSR,STRAT,XLM,ARK,BCN,STEEM,PIVX,KMD,DCR,FRST,FCT,SC,BTS,MONA,GAME,DOGE,BTCD,BLOCK,GBYTE,LKK,REC,DGB,NXS,ETP,XVG,SYS,BDL,GXS,NXT,VEN,PURA,IOC,VTC,UBQ,PART,NAV,SPRTS,ATB,FAIR,NLG,RISE,RDD,CLAM,PPC,XZC,XEL,CLOAK,NLC2,AEON,VIA,EMC,DMD,XAS,NEBL,BAY,CMP,DCT,XCP,TCC,CRW,ION,EMC2,RBY,SIB,LEO,PPY,OMNI,SKY,NMC,MUE,GOLOS,OK,ECN,KORE,POT,SMART,MOON,PZM,EXP,SLS,ZEN,ENRG,BLK,SHIFT,TOA,RADS,GRC,BURST,XDN,ODN,LBC,FLO,GAM,XC,LMC,XRB,UNO,VRC,EDR,DIME,XSPEC,NEOS,SPHR,VOX,BSD,SLR,HEAT,CNT,FTC,MUSIC,XBY,ATCC,EMB,GRS,PINK,NVC,IOP,SPR,XWC,BITB,ABY,BTX,DBIX,GCC,AUR,CURE,POSW,BCO,XST,SEQ,XBC,NTRN,TRC,NOTE,HTML5,EXCL,WBB,GLD,RAIN,PTC,SNRG,GCR,BLITZ,SWIFT,EQT,CRAVE,BELA,XVC,VISIO,CSC,DYN,PKB,ERC,ECC,HUSH,VRM,PASC,ZEIT,THC,PUT,BIS,SBD,ONION,DOPE,CHC,SYNX,VASH,ZCL,XMY,TX,TRUST,GEO,BRX,2GIVE,EGC,XPM,BTM,MEME,GRE,B3,MINT,BLU,VTR,MXT,CANN,BRK,CHIPS,SMLY,ESP,SIGT,CREA,ATMS,ZENI,HPC,PROC,XMG,BASH,MGC,START,RIC,VIVO,HUC,PND,SXC,ADC,EFL,808,UNIFY,LINDA,FST,CBX,RNS,ONX,ADZ,KOBO,1337,ETHD,XMCC,HTC,RUP,ZCC,CCRB,INFX,DOT,NETKO,GRWI,MAO,XHI,IFC,BYC,CPC,WDC,TES,USNBT,BRIT,XP,ZOI,BTA,HNC,TIPS,CRM,SUMO,ARC,SMC,MEC,FAL,LDOGE,BRO,INSN,TYCHO,BLAS,FJC,VSX,DP,FCN,TRI,MOIN,XFT,DCY,KRB,TZC,LINX,SHORTY,CWXT,SCORE,UNB,DFT,NET,UIS,NOBL,DNR,42,DAS,OHM,POST,DAXX,MAC,XCN,WOMEN,XVP,RBIES,BUCKS,TRUMP,ZER,DEM,PAK,XLR,ATOM,ENT,SWING,DSH,MOJO,MNM,XCS,ITZ,8BIT,WYV,SLM,HODL,LTB,FRN,XCXT,BRIA,RUPX,LANA,XJO,BBP,EL,BOLI,CNNC,MAY,VUC,TEK,STV,TSE,CTO,CJ,GB,REE,SAC,PXI,FLAX,ZNY,BSTY,XCT,QCN,TIX,CACH,PRC,BTPL,GPU,TSTR,DRXNE,GLT,HMP,ADCN,GCC,SOIL,URC,RBT,WORM,CMPCO,MSCN,VLTC,LCP,NEVA,TAJ,AMMO,JWL,KRONE,CREVA,BIOS,SFC,CTIC2,CNC,ACP,LTCU,WEX,LBTC,XNG,LVPS,EBT,HMC,DMB,APW,ADK,XTO,CV2,AC,YASH,HYP,QRK,EAC,CRYPT,LOG,FNC,IXC,NKA,FIMK,IFLT,MAX,CARBON,TOKEN,SDC,ZET,UFO,KEK,BITZ,METAL,ITI,USC,CDN,SUPER,UTC,TAG,RC,NYC,AMBER,BTB,PIE,TROLL,HBN,BITS,GCN,VLT,FC2,UNIT,MZC,ANC,GLC,I0C,ORB,TALK,DVC,PXC,TIT,PIGGY,GAIA,V,EMP,AU,STS,KRS,OPAL,XPTX,PR,ECA,CAGE,UNIC,XRA,PSB,BTCS,CORG,CNO,XPY,KED,VIDZ,FLT,SRC,CCN,ICN,VAL,USDE,FLY,TRK,FUNK,SLG,LOT,BUN,UNI,WAY,CAP,BERN,VC,JIN,HONEY,BLC,KUSH,XGR,CYP,TTC,GRT,CHESS,PUTIC,SPEX,FRC,CON,Q2C,DLC,CUBE,UNITS,KLC,XCO,J,GUN,ACOIN,XRE,TGC,NYAN,GP,YAC,EMD,EVIL,BXT,C2,BIGUP,DGC,MAD,ZUR,ELE,KIC,EVO,ECO,888,PASL,FRK,WMC,XPD,BIP,DBTC,CRX,ARCO,20,SPACE,BCF,BUMBA,MCRN,DUO,CAT,MST,ANTI,ARG,HAL,GTC,ARI,XBTC21,DRM,BOAT,MARS,GAP,SPT,ICOB,FIRE,VEC2,EUC,SLING,ALL,PONZI,RED,QTL,BTCR,SCRT,ISL,BLRY,NRO,AGLC,KURT,4CHN,IMS,ARB,PHS,PLNC,WARP,ERY,URO,TOR,BOST,LEA,CXT,611,TRADE,MEOW,FLVR,ASAFE2,MAR,CAB,BRAIN,CMT,PX,HXX,MND,RPC,GPL,CPN,ZYD,VPRC,POP,$$$,HKG,G3N,SOON,CESC,XCRE,MTLMC3,STEPS,PRX,LUNA,MILO,ICON,BVC,BENJI,GBC,JOBS,BSTAR,PHO,GBT,COAL,ZMC,ATX,BTQ,ORLY,LTCR,XBTS,WBC,DES,VTA,DRS,RIDE,VIP,FRAZ,CASH,OFF,SONG,BSC,BLZ,TAGR,ALTC,DLISK,SOCC,EGO,RSGP,CRT,FUZZ,PEX,SH,HVCO,IMX,1CR,SANDG,LIR,DPAY,IMPS,KNC,CONX,BIOB,OS76,SLEVIN,ZNE,IBANK,SCS,XOC,DOLLAR,MGM,NANOX,REV,BNX,VOLT,SDP,XRC,ARGUS,GEERT,P7C,PULSE,SLFI,ELS,NODC,SOJ,MNC,PIZZA,CF,BQC,PWR,FDC,ULA,DGCS,ENV,ABN,XEN,CALC,GBG,INF,FRGC,DMC,ACT,EBST,XTZ,XIN,MSD,TER,XBG,CLUB,MG,AURS,WHL,BTU,DEUS,BUZZ,THS,GOKU,YOC,MGC,DFS,BTCZ,BTDX,WA,MBL,SIGMA,PCS,XID,GSR,XQN,FLASH,GRN,TYC,ACC,COLX,AMS,MAGN,MTNC,BET,NAMO,BLAZR,CYDER,INDIA,PRIMU,REGA,MEN,LDCN,MRNG,HNC,XDE2,KAYI,LEPEN,SHND,PCN,MRJA,UNRC,ATMC,FID,BAT,ZBC,MOTO,SKULL,BUB,FUTC,ASN,PAC,XSTC,MARX,RUBIT,SKR,TOPAZ,FFC,HALLO,9COIN,TODAY,AV,QBC,NBIT,APC,BITOK,ACN,UR,TCOIN,RBBT,PAYP,VOYA,SFE,XTD,EDRC,QORA,XAU,PI,CME,CC,TELL,BEST,PRM,XLC,GAIN,BAC,BXC,DON,YES,TEAM,SAK,OCOW,ZSE,HYPER,IRL,AXIOM,UNC,TERA,UTA,GAY,FAZZ,EXL,TRICK,RHFC,LKC,BIT,X2,MONETA,COUPE,TCR,ELC,CLINT,ANI,GMX,GBRC,VGC,LAZ,FONZ,XRY,ACES,FRWC,DCRE,DBG,ANTX,WSX,MONEY,WEC,HCC,RICHX,ROYAL,AIB,TURBO,BIRDS,PEC,NBE,SKC,EGG,DISK,MAVRO,IVZ,TLE,BTG,PSY,RCN,XVE,OP,OPES,SHA,CYC,BGR,WOW,ASC,DASHS,GML,KASHH,OMC,PDG,LTH,GOLF,STCN,CBD,NTCC,CHEAP,POKE,QBT,SHELL,VTY,KARMA,AXF,WINK,DUB,MMXVI,SYNC,SPORT,SOUL,STRB,MIU,FLAP,TOP,BGC,DTF,MRC,FBC,FEDS'
    #request_string = rqst.get('https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms='+allCoins)
    request_string = rqst.get('https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms=USD,BTC,BCH,ETH,LTC,LSK,NEO,XRP')
    coin_dict = request_string.json()
    #print(coin_dict)
    return coin_dict

coin_dict = Cryptolog()
#Test Ether in Bitcoins 0.0615 0.061                 #DELETE THIS EXAMPLE
#ex_rate = 1                                         #DELETE THIS EXAMPLE

userDB = shelve.open('../db/persondb')

#Go through the Divergence subscribes
DivergenceDB = shelve.open('../db/personDivergenceDB')                                  # Open database for divergence service

i = 1
while i <= len(DivergenceDB['DivergenceServiceList'].members)-1:                        # Go through the list of divergence service instances to perform notification checks

    userID =  DivergenceDB['DivergenceServiceList'].members[i][0]                       # Retrieve the userID for each listed service instance
    userServicePosition = DivergenceDB['DivergenceServiceList'].members[i][1]           # Retrieve the position of the service instance in the list

    # print(userID)
    #print(userServicePosition)
    #print(DivergenceDB[userID].Services[userServicePosition - 1])

    coin1 = DivergenceDB[userID].Services[userServicePosition - 1][0]                   # Retrieve coin1 for the service instance
    coin2 = DivergenceDB[userID].Services[userServicePosition - 1][1]                   # Retrieve coin2 for the service instance
    user_signal = float(DivergenceDB[userID].Services[userServicePosition - 1][2])      # Retrieve user_signal for the service instance

    #print(coin1)
    #print(coin2)
    #print(user_signal)

    for user in userDB:                                                                 # Retrieve user_name corresponding to the ID of this instance
        print(userDB[user])                                                             # A hash table will be implemented combining IDs with usernames
        if userDB[user].serviceID == userID:                                            #to avoid this search that takes time
            #print(user)
            user_name = user
            print("username is: "+str(user))

            first_name = userDB[user_name].first_name
            telephone = userDB[user_name].telephone

            #print(first_name)
            #print(telephone)

    #print(coin_dict[coin1])
    #print(coin_dict[coin2])

    ex_rate = float(coin_dict[coin2])/float(coin_dict[coin1])                           # Calculate the exchange rate of interest fo this service instance

    i+=1

    check_Divergence(coin1, coin2, user_signal, ex_rate, first_name, telephone)         # Pass all the variable retrieved above to call the check function to determine if notification is necessary

DivergenceDB.close()                                                                    # Close database for this Service

#Go through the Spike subscribes

SpikeDB = shelve.open('../db/personSpikeDB')                                            #Open database for Spike service

i = 1
while i <= len(SpikeDB['SpikeServiceList'].members)-1:                                  # Go through the list of divergence service instances to perform notification checks

    print("")
    userID =  SpikeDB['SpikeServiceList'].members[i][0]                                 # Retrieve the userID for each listed service instance
    print(userID)
    userServicePosition = SpikeDB['SpikeServiceList'].members[i][1]                     # Retrieve the position of the service instance in the list

    # print(userID)
    #print(userServicePosition)
    #print(DivergenceDB[userID].Services[userServicePosition - 1])

    coin1 = SpikeDB[userID].Services[userServicePosition - 1][0]                        # Retrieve coin1 for the service instance
    #coin2 = SpikeDB[userID].Services[userServicePosition - 1][1]                        # Retrieve coin2 for the service instance
    user_signal = float(SpikeDB[userID].Services[userServicePosition - 1][2])           # Retrieve user_signal for the service instance
    direction = SpikeDB[userID].Services[userServicePosition - 1][3]  # Retrieve user_signal for the service instance

    print(direction)
    #print(coin1)
    #print(coin2)
    print(user_signal)

    for user in userDB:                                                                 # Retrieve user_name corresponding to the ID of this service instance

        if userDB[user].serviceID == userID:
            print(userDB[user])
            #print(user)
            user_name = user
            #print("username is: "+str(user))

            first_name = userDB[user_name].first_name
            telephone = userDB[user_name].telephone

            #print(first_name)
            print(telephone)

    #print(coin_dict[coin1])
    #print(coin_dict[coin2])
    price = float(1/coin_dict[coin1])                           # Calculate the necessary exchange rate to perform check for this service instance
    print(price)

    i+=1

    check_Spike(coin1, user_signal, price, direction, first_name, telephone)              # Pass all the variable retrieved above to call the check function to determine if notification is necessary

SpikeDB.close()


userDB.close()                                                                          #Close userDB at the end of the whole check cycle

####
#### Add username - userID join table, saved in another shelve DB to avoid the for loop
####

#Add code to ensure that initializeDB runs on first time