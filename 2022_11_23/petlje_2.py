#for while

'''

#######
 ######
  #####
   ####
    ###
     ##
      #

''' 

# for x in range(1000):
#     for y in range(800): 
#         if y > x:
#             print("#", end=" ")
#         else:
#             print( " ", end="")
#     print()

automobil = 0
cilj = 100

brzina = 5
gorivo = 10

while automobil < cilj:
    print("Voznja je u toku")
    automobil += brzina
    gorivo -= 0.2
    if gorivo == 0:
        print("Nemate vise goriva")
        break

else:
    print("Stigli ste.")
    print("Ostalo vam je goriva samo",gorivo)

