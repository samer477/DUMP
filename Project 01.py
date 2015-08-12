import random
while 1!=2:
    Y = raw_input("the calculator: C\nthe game : G\ninformations about the solar system : I\nTest astro : T\nto quit : Q\n... ")
    if Y == "Q" or Y == "q":
        exit()
    if Y == "I" or Y == "i":
        while 1!=2:
            print "you are now in the information section"
            P=raw_input("Mercure : 1\nVenus : 2\nTerre : 3\nMars : 4\nJupiter : 5\nSaturne : 6\nUranis : 7\nNeptune : 8\nPluton : 9\nreturn : r\n... ")
            if P == "r" or P == "R":
                break
            elif P == "1" :
                print"_Masse comparé à la Terre : 0.056"
                print"_Diamétre à l'équateur (km): 4860"
                print"_Densité moyenne (g/cm3): 5.6"
                print"_Journée: 58j15h"
                print"_Révolution: 88j"
                print"_Distance au soleil (Mkm): 58"
            elif P == "2":
                print"_Masse comparé à la Terre: 0.82"
                print"_Diamétre à l'équateur (Km): 12140"
                print"_Densité moyenne (g/cm): 5.2"
                print"_Journée: 243j"
                print"_Révolution: 225j"
                print"_Distance au Soleil (Mkm): 108"
            elif P == "3":
                print"_Masse comparé à la Terre: 1\n_Diamétre à l'équateur(Km): 12760\n_Densité moyenne(g/cm3): 5.5\n_Journée: 23h56mn\n_Révolution: 365j6h\n_Distance au Soleil(Mkm): 150"
            elif P == "4":
                print"_Masse comparé à la Terre: 0.11\n_Diamètre à l'equateur: 6800\n_Densité moyenne (g/cm3): 3.9\n_Journée: 24h37mn\n_Révolution: 1an11m\n_Distance au Soleil(Mkm): 228"
            elif P == "5":
                print"_Masse comparé à la Terre: 318\n_Diamétre à l'équteur: 143200\n_Densité moyenne(g/cm3): 1.3\n_Journée: 9h45mn\n_Révolution: 11an11m\n_Distance au Soleil(Mkm): 778"
            elif P == "6":
                print"_Masse comparé à la Terre: 95\n_Diamétre à l'équateur: 12000\n_Densité moyenne(g/cm3): 0.7\n_Journée: 10h39mn\n_Révolution: 29a6m\n_Distance au Soleil(Mkm): 1400"
            elif P == "7":
                print"_Masse comparé à la Terre: 15\n_Diamétre à l'equateur: 52000\n_Densité moyenne(g/cm3): 1.2\n_Journée: 17h15mn\n_Révolution: 84an\n_Distance au Soleil(Mkm): 2870"
            elif P == "8":
                print"_Masse comparé à la Terre: 17\n_Diamétre à l'equateur: 50000\n_Densité moyenne(g/cm3): 1.7\n_Journée: 17h36mn\n_Révolution: 165an\n_Distance au Soleil(Mkm): 4500"
            elif P == "9":
                print"_Masse comparé à la Terre: 0.003\n_Diamétre à l'equateur: 2300\n_Densité moyenne(g/cm3): 2\n_Journée: 6j10h\n_Révolution: 248an\n_Distance au Soleil(Mkm): 5900"
    if Y == "T" or Y == "t":
        while 1!=2:
            print"you are now in the Test section"
            P=raw_input("If you want to return write : r but if u want to continue write : c\n")
            if P == "r" or P == "R":
                break
            elif P == "c" or P == "C":
                print"Ok now you'll be asked 10 questions..."
                L=0
                K=0
                o=raw_input("_1st of all who's the first human been that went to the moon?\n*Neil Armstrong[n]\n*Josef Fourier[j]\n*Stieve Woziniak[S]\n...")
                if o == "n":
                    print"Success you are right!\n-------------------------------------------------------------------------"
                    K+=1
                else:
                    print"Are you sure? because it's the wrong answer the right one is :\nNeil Armstrong\n------------------------------------------------------------------------"
                    L+=1
                o1=raw_input("_When the human been discovered Mars?\n*1378[a]\n*1786[a1]\n*1543[a2]\n...")
                if o1 == "a2":
                    print"Success you are right!\n-------------------------------------------------------------------------"
                    K+=1
                else:
                    print"Are you sure? because it's the wrong answer the right one is :\n1543\n------------------------------------------------------------------------"
                    L+=1
                o2=raw_input("_The first rocket that successfully went to the moon?\n*Apolo11[a]\n*Manathan[m]\n*URUL[u]\n...")
                if o2 == "a":
                    print"Success you are right!\n-------------------------------------------------------------------------"
                    K+=1
                else:
                    print"Are you sure? because it's the wrong answer the right one is :\nApolo11\n------------------------------------------------------------------------"
                    L+=1
                o3=raw_input("_What's the name of the robot that transports in Mars?\n*spacehub[s]\n*Rover[r]\n*discover213[d]\n...")
                if o3 == "r":
                    print"Success you are right!\n-------------------------------------------------------------------------"
                    K+=1
                else:
                    print"Are you sure? because it's the wrong answer the right one is :\nRover\n------------------------------------------------------------------------"
                    L+=1
                o4=raw_input("_When Kepler 452b is discovred?\n*2005[1]\n*2015[2]\n*2011[3]\n...")
                if o4 == "2":
                    print"Success you are right!\n-------------------------------------------------------------------------"
                    K+=1
                else:
                    print"Are you sure? because it's the wrong answer the right one is :\n2015\n------------------------------------------------------------------------"
                    L+=1
                o5=raw_input("_When the NASA was created?\n*1958[1]\n*1947[2]\n*1963[3]\n...")
                if o5 == "1":
                    print"Success you are right!\n-------------------------------------------------------------------------"
                    K+=1
                else:
                    print"Are you sure? because it's the wrong answer the right one is :\n1958\n------------------------------------------------------------------------"
                    L+=1
                o6=raw_input("_how many planets are there in the solar system?\n*8[8]\n*9[9]\n*10[10]\n...")
                if o6 == "8":
                    print"Success you are right!\n-------------------------------------------------------------------------"
                    K+=1
                else:
                    print"Are you sure? because it's the wrong answer the right one is :\n8\n------------------------------------------------------------------------"
                    L+=1
                o7=raw_input("_who built the telescope?\n*Nutune[n]\n*George Alfury[g]\n*Hans Lippershey[h]\n...")
                if o7 == "h":
                    print"Success you are right!\n-------------------------------------------------------------------------"
                    K+=1
                else:
                    print"Are you sure? because it's the wrong answer the right one is :\nHans Lippershey\n------------------------------------------------------------------------"
                    L+=1
                o8=raw_input("_who knew that the earth is spinning around the sun?\n*Copernicus[c]\n*Shawn Mendes[s]\n*Lucuis Fox[l]...")
                if o8 == "c":
                    print"Success you are right!\n-------------------------------------------------------------------------"
                    K+=1
                else:
                    print"Are you sure? because it's the wrong answer the right one is :\nCopernicus\n------------------------------------------------------------------------"
                    L+=1
                o9=raw_input("_who knew that the earth is a sphere planet?\nEratosthenes[e]\nFibonnacci[f]\nMarkossio[m]...")
                if o9 == "e":
                    print"Success you are right!\n-------------------------------------------------------------------------"
                    K+=1
                else:
                    print"Are you sure? because it's the wrong answer the right one is :\nEratosthenes\n------------------------------------------------------------------------"
                    L+=1
                print'the number of the right answers is: ', K
                print'the number of the wrong answers is: ', L
    if Y == "G" or Y == "g":
        n = random.randint(1,100)
        x = input("choose a number from 0 to 100...")
        a = 0
        while n != x :
            if a == 9:
                print "game is over"
                print "Loser, Loser :p"
                print "number of tries: ", a+1
                print n, "is the correct number"
                raw_input()
                break
            elif x<n:
                print x, "is smaller"
                a+=1
                print "number of tries: ", a
                x = input("choose a number again...")
            elif x>n:
                print x, "is bigger"
                a+=1
                print "number of tries: ", a
                x = input("choose a number again...")
        if n == x:
            print "yes", x, "is the correct number"
            a+=1
            print "number of tries: ", a
            raw_input()
    if Y == "C" or Y == "c":
        while 1!=2:
            print "To try another operation when finished just press enter. LooooooooooooL XD"
            x=raw_input("PS: To choose the + operation : +\nto choose the - operation : -\nto choose the x operation : x\nto choose / operation : /\nto choose the ^ operation : ^\nto go back : r\n... ")
            if x == "r" or x == "R":
                break
            elif x == "+":
                print "this is a + operation"
                A = input("Please enter a valid number ")
                B = input("Please enter a valid number ")
                print A,"+", B, "=", A+B
                raw_input()
            elif x == "-":
                print"this is a - oparation"
                A1 = input("Please enter a valid number ")
                B1 = input("Please enter a valid number ")
                print A1,"-", B1, "=", A1-B1
                raw_input()
            elif x == "x":
                print "This is a x operation"
                A2 = input("Please enter a valid number ")
                B2 = input("Please enter a valid number ")
                print A2,"x", B2, "=", A2*B2
                raw_input()
            elif x == "/":
                print "This is a / operation"
                A3 = input("Please enter a valid number ")
                B3 = input("Please enter a valid number ")
                print A3,"/", B3, "=", A3/B3
                raw_input()
            elif x == "^":
                print "This is a ^ operation"
                A4 = input("Please enter a valid number ")
                B4 = input("Please enter a valid number ")
                print A4,"^", B4, "=", A4**B4
                raw_input()
            else:
                print "this doesn't existe!!!!!!!!"
                raw_input()

