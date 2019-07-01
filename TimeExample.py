import time

lin = time.time()
mes = time.time()
lout = time.time()
lin1 = time.localtime(lin)
mes = time.localtime(mes)
lout1 = time.localtime(lout)
login = time.asctime(lin1)
message = time.asctime(mes)
logout = time.asctime(lout1)

print(login)

print(message)

print(logout)

# USED IN DATA COLLECTION