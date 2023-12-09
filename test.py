carotte=(75,97)
ecran=(1920,1080)


ratioc=carotte[0]/carotte[1]
ratioe=ecran[0]/ecran[1]

w_carotte=0.05*ecran[0]
h_carotte=w_carotte*ratioc

print(ratioc, ratioe, w_carotte, h_carotte)