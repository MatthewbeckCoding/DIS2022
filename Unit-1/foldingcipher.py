
message = "TFDHSB*VSE*SPN*WIDAEN*AHO*E*ANEE*I*LOA*DINCGMGILCRPBORCBTSEULR*NDO*EESDI*RLTYUU*I*GLACG*DOSS*EPIOY**RTIMEHOPO*DIFS"
key = (ord(message[0]) - 64)%3 +3
rows = len(message)//3
if len(message)%3 > 0:
    rows+=1

clean_message = ""

for i in range(0, rows):
    clean_message += message[i]
    for j in range(1,key):
        clean_message += message(int[i+(rows*j)])
print(clean_message)


