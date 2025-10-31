# Vul hier de namen van je duo in (of enkel je eigen naam als je alleen werkt)
# Naam 1: Sofiia Shmulevych
# Naam 2: Julie Heesakkers
# Imports
import random # importeert de random module voor het gooien van een dobbelsteen
import pygame # importeert de pygame module voor het maken van een GUI
# --------------- Globale variabelen ---------------
#pion posities
pion_posities = [0, 0]
beurt = 0                #wie is er aan de beurt, 0 = speler 0, 1 = speler 1
oude_beurt = 0
winnaar = None           #Is er een winnaar?
worp = 0                 #dobbelsteen worp waarde
worp1 = 0              #eerste dobbelsteen
worp2 = 0               #tweede dobbelsteen
gans_vakjes = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59] #gans vakken
beurten_overslaan = [0, 0] #aantal beurten dat spelers moeten overslaan
som_vakjes = [15, 40]

#coordinaten van de vakjes op het bord
vakjes = [[160, 683], [286, 683], [356, 683], [415, 683], [482, 683], [545, 683],
[618, 683], [692, 683], [758, 683], [828, 643], [895, 598], [937, 549], [965, 489],
[982, 430], [982, 353], [968, 283], [944, 220], [905, 167], [833, 111], [744, 66],
[664, 62], [597, 62], [536, 62], [464, 62], [398, 62], [335, 62], [265, 66], [198, 94],
[142, 129], [104, 174], [83, 227], [65, 283], [65, 367], [83, 435], [116, 491], [160, 535],
[216, 570], [282, 587], [342, 587], [405, 587], [468, 587], [536, 587], [615, 587],
[692, 587], [755, 578], [816, 528], [863, 458], [877, 402], [874, 335], [856, 283],
[804, 202], [737, 160], [632, 157], [545, 157], [468, 157], [394, 157], [328, 157],
[265, 167], [195, 223], [167, 325], [188, 403], [221, 454], [282, 482], [413, 456]]
#tekst voor op het scherm van cpeciale regels
speciale_tekst = ""
# bord afbeelding laden
bord_afbeelding = pygame.image.load("Ganzenbord.png")

# ---------- Pygame Initialisatie ----------
#pygame initialiseren
pygame.init()
#afmeting van het spelscherm instellen
#opslaan in "screen"
WINDOW_SIZE = [1200, 800]
screen = pygame.display.set_mode(WINDOW_SIZE)
#titel van het spelscherm instellen
pygame.display.set_caption("Ganzenbord")
#deze laat ons in een oneindige loop lopen totdat er op de kruisje wordt geklint

done = False
# --------------- Functies ---------------
def beurt_doorgeven(beurt): #functie om beurt door te geven
   if beurt == 1: #als de huidige beurt 1 is
       beurt = 0 #geef de beurt aan speler 1
   else: # anders
       beurt = 1 #gef de beurt aan speler 1
   return beurt #geef de nieuwe beurt terug
def beweeg_pion(speler, aantal_stappen): #functie om een pion te verplaatsen
   global pion_posities
   turn_around = False #variabele om bij te houden of we moeten teruglopen
   for stap in range(0,aantal_stappen): #herhaal voor elk stapje dat we moeten zetten
       # als we niet op het laatstevakje zijn en niiet moeten teruglopen
       if pion_posities[speler] < len(vakjes) - 1 and not turn_around:
            pion_posities[speler] += 1 #beweeg pion 1 vakje vooruit
       else: #anders, als we moeten teruglopen
             turn_around = True #zet de variable om terugg te lopen op True
       if turn_around: #als we moeten teruglopen
           pion_posities[speler] -= 1 #beweeg pion 1 vakje terug
       update_screen("bewegend") #teken het scherm opnieuw tijdns de beweging
def kleur_vak_kiezen(i):
  kleur = (230, 230, 230)  # standaard grijs
  if i in gans_vakjes:
      kleur = (255, 255, 150)  # geel
  elif i == 19:
      kleur = (255, 180, 90)  # herberg
  elif i == 42:
      kleur = (180, 130, 255)  # doolhof
  elif i == 52:
      kleur = (255, 100, 100)  # gevangenis
  elif i == 63:
      kleur = (150, 255, 150)  # eind
  elif i == 0:
      kleur = (255, 255, 255)  # start
  elif i == 6 or i == 12:
      kleur = (0, 200, 200)  # brug
  elif i == 31:
      kleur = (120, 170, 255)  # rivier
  elif i == 8:
      kleur = (255, 215, 0)  # geluk
  elif i in som_vakjes:
      kleur = (150, 255, 255)  # som
  return kleur
def teken_gekleurde_vakjes():
  for i in range(len(vakjes)):
      kleur = kleur_vak_kiezen(i)
      x, y = vakjes[i]
      pygame.draw.circle(screen, kleur, (x, y), 10)
def update_screen(situatie): #functie om het scherm te update
   #screen.fill((255, 255, 255)) #begin met een witte achtergrond
   if beurt == 0:
      achtergrond_kleur = (220, 240, 255)
   else:
      achtergrond_kleur = (255, 230, 240)
   screen.fill(achtergrond_kleur)

   bord_rect = bord_afbeelding.get_rect() #vraagt afmeting van het bordplaatje
   screen.blit(bord_afbeelding, bord_rect) #teken het bord bij de volgende update van het scherm
   teken_gekleurde_vakjes()
   #update het scherm met pionnen
   speler0_x = vakjes[pion_posities[0]][0] # x coordinaat van speler 0
   speler0_y = vakjes[pion_posities[0]][1] # y coordinaat van speler 0
   kleur_speler0 = (255, 0, 0) # kleur van speler 0
   pygame.draw.circle(screen, kleur_speler0, (speler0_x, speler0_y), 10)
   speler1_x = vakjes[pion_posities[1]][0] +5 #x coordinaat van speler 1
   speler1_y = vakjes[pion_posities[1]][1] +5 # y coordinaat van speler 1
   kleur_speler1 = (0, 0, 255) # kleur van speler 1
   pygame.draw.circle(screen, kleur_speler1, (speler1_x, speler1_y), 10) #teken pion van speler 1
   #update de tekst
   myfont = pygame.font.SysFont(None, 30)        #maak font object aan voor tekst
   #bepaal welke beurt we moeten weergeven
   if situatie == "bewegend":        #tijdens bewegen laten we de huidige beurt zien
       beurt_display = beurt
   else:
       beurt_display = oude_beurt
   #bepalen welke beurt we moeten weergeven (huidige of vorige)
   if pion_posities == [0,0]:
       text = "Druk op spatie om speler 1 te laten beginnen"
       label = myfont.render(text, 1, (0,0,0))
       screen.blit(label, (330, 470))
   elif winnaar == None:    #tijdens het spel
       #teken laaste worp op het scherm
       text = "Speler " + str(beurt_display + 1) + " gooide " + str(worp1) + str(worp2) + "(totaal" +str(worp) + ")"
       label = myfont.render(text, 1, (0,0,0))
       screen.blit(label, (400, 470))
       #teken de laatste worp op het scherm:
       text = "Speler " + str(beurt + 1) + " is aan de beurt "
       label = myfont.render(text, 1, (0,0,0))
       screen.blit(label, (400, 495))
       #teken de regel die net is uitgevoerd op het scherm:
       label = myfont.render(speciale_tekst, 1, (0,0,0))
       screen.blit(label, (250, 260))
   else: #einde van het speel
       text="Speler " + str(winnaar + 1) + " heeft gewonnen!!!"
       label = myfont.render(text, 1, (0,0,0))
       screen.blit(label, (370, 470))
       tekst = "Druk op Backspace voor een rematch!"
       label = myfont.render(tekst, 1, (0,0,0))
       screen.blit(label, (370, 495))
   pygame.display.flip()#ververs het beeldscherm met de nieuwe graphics
   pygame.time.wait(120)#wacht 120 ms


# --------------- Hoofdloop van het spel ---------------
update_screen("normaal") #update screen
while not done:
   #check
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           done = True
       elif event.type == pygame.KEYDOWN: #als er een toets is ingedruktt
           if event.key == pygame.K_SPACE and winnaar == None: # spatie ingedrukt en nog geen winnaar
               print("spatiebalk ingedrukt - hier komt de dobbelsteenworp en pion verplaatsing")
               speciale_tekst=""
               if beurten_overslaan[beurt] > 0:
                  beurten_overslaan[beurt] -= 1
                  speciale_tekst = "Speler " + str(beurt + 1) + " slaat een beurt over. Nog " + str(beurten_overslaan[beurt]) + " beurten te gaan"
                  oude_beurt = beurt
                  beurt = beurt_doorgeven(beurt)
                  update_screen("normaal")
                  continue
               worp1 = random.randint(1, 6) #gooi eerste dobbelsteen (1-6)
               worp2 = random.randint(1, 6) #gooi tweede dobbelsteen (1-6)
               worp = worp1 + worp2 #totaal
               beweeg_pion(beurt, worp) #verplaats de pion van de speler die aan de beurt is
               #dingen toevoegen extra regels en vakjes etc.
               while winnaar is None and (pion_posities[beurt] in gans_vakjes):
                   #zolang je op een gans staat, loop je nog eens dezelfde worp vooruit
                   speciale_tekst = ("Gans, speler " + str(beurt + 1) + " loop nog " + str(worp) + " vakjes")
                   beweeg_pion(beurt, worp)
                   if pion_posities[beurt] == 63:
                       break #als je tijdens gans op 63 eindigt, stop dan
               if pion_posities[beurt] == 6: #brug op vakjes 6 en 12
                   pion_posities[beurt] == 12
                   speciale_tekst = "Brug, speler " + str(beurt + 1) + " springt naar vak 12"
               elif pion_posities[beurt] == 12:
                   pion_posities[beurt] == 6
                   speciale_tekst = "Brug, speler " + str(beurt + 1) + " springt naar vak 6"
               if pion_posities[beurt] == 31: #rivier op vakje 31 (terug naar de start)
                   pion_posities[beurt] = 0
                   speciale_tekst = "Rivier, speler " + str(beurt + 1) + " gaat terug naar de start"
               if pion_posities[beurt] ==  8: #gelukvakje
                   oude_beurt = beurt #speler mag blijven gooien
                   speciale_tekst = "Geluk, speler " + str(beurt + 1) + " mag nog een keer gooien"
                   update_screen("normaal")
                   continue
               
# weer
               weer_teller += 1

if weer_teller >= random.randint(2, 4):

    weer_teller = 0

    huidig_weer = random.choice(["normaal", "zon", "regen", "storm", "mist"])

if huidig_weer == "zon":
    speciale_tekst = " Zon! Speler " + str(beurt + 1) + " mag 2 extra stappen vooruit."
    beweeg_pion(beurt, 2)
elif huidig_weer == "regen":
    speciale_tekst = " Regen! Speler " + str(beurt + 1) + " glijdt 2 vakjes achteruit."
    beweeg_pion(beurt, -2)
elif huidig_weer == "storm":
    speciale_tekst = " Storm! Speler " + str(beurt + 1) + "  blijft staan."
    pion_posities[beurt] -= worp
elif huidig_weer == "mist"
    speciale_tekst = " Mist! Speler " + str(beurt + 1) + " kan maar 1 stap vooruit."
    pion_posities[beurt] -= worp - 1

# dobbelsteenbonus
if pion_posities[beurt] == 29:  # voorbeeld vakje
    extra_worp = random.randint(1,6)
    if extra_worp <= 3:
        pion_posities[beurt] -= 1
        if pion_posities[beurt] < 0:
            pion_posities[beurt] = 0

        speciale_tekst = " Bonusdobbelsteen! Gooi " + str(extra_worp) + "  1 stap achteruit."
    else:
        pion_posities[beurt] += 1
        speciale_tekst = " Bonusdobbelsteen! Gooi " + str(extra_worp) + " 1 stap vooruit."

# schuifvakje

if pion_posities[beurt] == 34:  # voorbeeld vakje

    ander = 1 - beurt

    effect = random.randint(1,6)

    if effect <=3:

        pion_posities[ander] -= 1
        if pion_posities[ander] < 0:
            pion_posities[ander] = 0

        speciale_tekst = " Schuif! Speler " + str(beurt+1) + " laat speler " + str(ander+1) + " 1 stap teruggaan."
    else:
        pion_posities[ander] += 1
        speciale_tekst = " Schuif! Speler " + str(beurt+1) + " laat speler " + str(ander+1) + " 1 stap vooruit gaan."
 
               #if pion_posities[beurt] in som_vakjes: #som vakje
                  # speciale_tekst = "Som vakje"
                    import random
                   getal1 = random.randint(1, 10)
                   getal2 = random.randint(1, 10)
                   antwoord = getal1 + getal2
                   vraag = "Wat is" + str(getal1) + "+" + str(getal2) + "?"
                   antwoord_speler = int(input(vraag))
                   if antwoord == antwoord_speler: #juist? dan mag je blijven staan
                       speciale_tekst = "Speler " + str(beurt + 1) + "mag blijven staan"
                   else: #onjuist? dan sla je een beurt over
                       beurten_overslaan[beurt] += 1
                       speciale_tekst = "Speler " + str(beurt + 1) + "slaat een beurt over"

               if pion_posities[beurt] == 52: #gevangenis op de vakje 52
                   beurten_overslaan[beurt] += 3
                   speciale_tekst = ("Gevangenis, speler "+str(beurt + 1) + " moet 3 beurten overslaan")
               if pion_posities[beurt] == 42: #doolhof terug
                   pion_posities[beurt] -= 3 #speler gaat 3 vakjes terug
                   if pion_posities[beurt] < 0:
                       pion_posities[beurt] = 0
                   speciale_tekst = ("Doolhof, speler " + str(beurt + 1) + " gaat 3 vakjes terug")
               if pion_posities[beurt] ==19: #herberg, dus beurt overslaan
                   beurten_overslaan[beurt] += 1
                   speciale_tekst = ("Herberg, speler " + str(beurt + 1) + " slaat een beurt over")
               ander = 1 - beurt #als je eindigt op hetzelfde vakje als de ander, sla hem terug naar de start
        
               if pion_posities[beurt] == pion_posities[ander] and winnaar is None:
                   pion_posities[ander] = 0
                   speciale_tekst = ("Speler " + str(beurt + 1) + "slaat speler " + str(ander + 1) + " terug naar de start")
               if pion_posities[beurt] == 63: #als de speler op vakje 63 komt
                   winnaar = beurt            #deze speler is de winnaar
               else:
                   if worp1 == worp2: #extra beurt bij twee gelijke dobbelstenen
                       speciale_tekst = ("Dubbel dobbelsteen, speler " + str(beurt + 1) + " mag nog een keer gooien")
                       oude_beurt = beurt #beurt blift gelijk
                   else:
                      oude_beurt = beurt #sla de huidige beurt als oude_beurt
                      beurt = beurt_doorgeven(beurt) #geef de beurt door aan de volgende speler

           elif event.key == pygame.K_BACKSPACE:
               print("Backspace ingedrukt - Reset het spel")
               pion_posities = [0, 0]                              #zet pion posities terug naar start
               beurt = 0                                           #zet de beurt terug naar speler 0            
               oude_beurt = 0                                      #zet de oude beurt terug naar speler 0
               winnaar = None                                      #zet de winnaar terug naar none
               worp = 0                                            #zet de wopr terug naar 0    
               worp1 = 0                                           #zet de eerste wopr terug naar 0
               worp2 = 0                                           #zet de tweede wopr terug naar 0
               beurten_overslaan = [0, 0]                          # zet beurten overslaan terug naar 0
           update_screen("normaal") #update screen

# --------------- Afsluiten van Pygame ---------------
pygame.quit() # sluit Pygame en het spel netjes af