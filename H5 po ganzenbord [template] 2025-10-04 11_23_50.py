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
worp1 = 0                #eerste dobbelsteen
worp2 = 0                #tweede dobbelsteen
gans_vakjes = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59] #gans vakken
beurten_overslaan = [0, 0] #aantal beurten dat spelers moeten overslaan
som_vakjes = [15, 40]

#weer variabelen
weer_teller = 0
huidig_weer = "normaal"

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

#tekst voor op het scherm van speciale regels
speciale_tekst = ""

# bord afbeelding laden
bord_afbeelding = pygame.image.load("Ganzenbord.png")

# ---------- Pygame Initialisatie ----------
pygame.init()
WINDOW_SIZE = [1200, 800]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Ganzenbord")
done = False

# --------------- Functies ---------------
def beurt_doorgeven(beurt): #functie om beurt door te geven
   if beurt == 1: 
       beurt = 0 
   else: 
       beurt = 1 
   return beurt 

def beweeg_pion(speler, aantal_stappen): #functie om een pion te verplaatsen
   global pion_posities
   turn_around = False 
   for stap in range(abs(aantal_stappen)): 
       if aantal_stappen > 0: # vooruit
           if pion_posities[speler] < len(vakjes) - 1 and not turn_around:
               pion_posities[speler] += 1
           else:
               turn_around = True
           if turn_around:
               pion_posities[speler] -= 1
       else: # achteruit bewegen
           if pion_posities[speler] > 0:
               pion_posities[speler] -= 1
       update_screen("bewegend") 

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
   if beurt == 0:
      achtergrond_kleur = (220, 240, 255)
   else:
      achtergrond_kleur = (255, 230, 240)
   screen.fill(achtergrond_kleur)

   bord_rect = bord_afbeelding.get_rect() 
   screen.blit(bord_afbeelding, bord_rect) 
   teken_gekleurde_vakjes()

   speler0_x = vakjes[pion_posities[0]][0]
   speler0_y = vakjes[pion_posities[0]][1]
   kleur_speler0 = (255, 0, 0)
   pygame.draw.circle(screen, kleur_speler0, (speler0_x, speler0_y), 10)

   speler1_x = vakjes[pion_posities[1]][0] + 5
   speler1_y = vakjes[pion_posities[1]][1] + 5
   kleur_speler1 = (0, 0, 255)
   pygame.draw.circle(screen, kleur_speler1, (speler1_x, speler1_y), 10)

   myfont = pygame.font.SysFont(None, 30)
   if situatie == "bewegend":        
       beurt_display = beurt
   else:
       beurt_display = oude_beurt

   if pion_posities == [0,0]:
       text = "Druk op spatie om speler 1 te laten beginnen"
       label = myfont.render(text, 1, (0,0,0))
       screen.blit(label, (330, 470))
   elif winnaar == None:
       text = f"Speler {beurt_display + 1} gooide {worp1} en {worp2} (totaal {worp})"
       label = myfont.render(text, 1, (0,0,0))
       screen.blit(label, (400, 470))
       text = "Speler " + str(beurt + 1) + " is aan de beurt "
       label = myfont.render(text, 1, (0,0,0))
       screen.blit(label, (400, 495))
       label = myfont.render(speciale_tekst, 1, (0,0,0))
       screen.blit(label, (250, 260))
   else:
       text = "Speler " + str(winnaar + 1) + " heeft gewonnen!!!"
       label = myfont.render(text, 1, (0,0,0))
       screen.blit(label, (370, 470))
       tekst = "Druk op Backspace voor een rematch!"
       label = myfont.render(tekst, 1, (0,0,0))
       screen.blit(label, (370, 495))

   pygame.display.flip()
   pygame.time.wait(120)

# --------------- Hoofdloop van het spel ---------------
update_screen("normaal")

while not done:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           done = True
       elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_SPACE and winnaar == None:
               print("spatiebalk ingedrukt - hier komt de dobbelsteenworp en pion verplaatsing")
               speciale_tekst = ""
               if beurten_overslaan[beurt] > 0:
                  beurten_overslaan[beurt] -= 1
                  speciale_tekst = "Speler " + str(beurt + 1) + " slaat een beurt over. Nog " + str(beurten_overslaan[beurt]) + " beurten te gaan"
                  oude_beurt = beurt
                  beurt = beurt_doorgeven(beurt)
                  update_screen("normaal")
                  continue

               worp1 = random.randint(1, 6)
               worp2 = random.randint(1, 6)
               worp = worp1 + worp2
               beweeg_pion(beurt, worp)

               #gansvakjes
               while winnaar is None and (pion_posities[beurt] in gans_vakjes):
                   speciale_tekst = ("Gans, speler " + str(beurt + 1) + " loopt nog " + str(worp) + " vakjes")
                   beweeg_pion(beurt, worp)
                   if pion_posities[beurt] == 63:
                       break

               #brug
               if pion_posities[beurt] == 6:
                   pion_posities[beurt] = 12
                   speciale_tekst = "Brug, speler " + str(beurt + 1) + " springt naar vak 12"
               elif pion_posities[beurt] == 12:
                   pion_posities[beurt] = 6
                   speciale_tekst = "Brug, speler " + str(beurt + 1) + " springt naar vak 6"

               #rivier
               if pion_posities[beurt] == 31:
                   pion_posities[beurt] = 0
                   speciale_tekst = "Rivier, speler " + str(beurt + 1) + " gaat terug naar de start"

               #gelukvakje
               if pion_posities[beurt] == 8:
                   oude_beurt = beurt
                   speciale_tekst = "Geluk, speler " + str(beurt + 1) + " mag nog een keer gooien"
                   update_screen("normaal")
                   continue

               #weer toevoeging
               weer_teller += 1
               if weer_teller >= random.randint(2, 4):
                   weer_teller = 0
                   huidig_weer = random.choice(["normaal", "zon", "regen", "storm", "mist"])

               if huidig_weer == "zon":
                   speciale_tekst = "Zon, speler " + str(beurt + 1) + " mag 2 extra stappen vooruit."
                   beweeg_pion(beurt, 2)
               elif huidig_weer == "regen":
                   speciale_tekst = "Regen, speler " + str(beurt + 1) + " glijdt 2 vakjes achteruit."
                   beweeg_pion(beurt, -2)
               elif huidig_weer == "storm":
                   speciale_tekst = "Storm, speler " + str(beurt + 1) + " blijft staan."
               elif huidig_weer == "mist":
                   speciale_tekst = "Mist, speler " + str(beurt + 1) + " kan maar 1 stap vooruit."
                   beweeg_pion(beurt, 1)

               #dobbelsteenbonus
               if pion_posities[beurt] == 29:
                   extra_worp = random.randint(1, 6)
                   if extra_worp <= 3:
                       pion_posities[beurt] -= 1
                       if pion_posities[beurt] < 0:
                           pion_posities[beurt] = 0
                       speciale_tekst = "Bonusdobbelsteen! Gooi " + str(extra_worp) + ": 1 stap achteruit."
                   else:
                       pion_posities[beurt] += 1
                       speciale_tekst = "Bonusdobbelsteen! Gooi " + str(extra_worp) + ": 1 stap vooruit."

               #schuifvakje
               if pion_posities[beurt] == 34:
                   ander = 1 - beurt
                   effect = random.randint(1, 6)
                   if effect <= 3:
                       pion_posities[ander] -= 1
                       if pion_posities[ander] < 0:
                           pion_posities[ander] = 0
                       speciale_tekst = "Schuif! Speler " + str(beurt + 1) + " laat speler " + str(ander + 1) + " 1 stap teruggaan."
                   else:
                       pion_posities[ander] += 1
                       speciale_tekst = "Schuif! Speler " + str(beurt + 1) + " laat speler " + str(ander + 1) + " 1 stap vooruit gaan."

               #som vakje
               if pion_posities[beurt] in som_vakjes:
                   getal1 = random.randint(1, 10)
                   getal2 = random.randint(1, 10)
                   antwoord = getal1 + getal2
                   gok = random.randint(1, 20)
                   if gok == antwoord:
                       speciale_tekst = "Som goed! Speler " + str(beurt + 1) + " mag blijven staan."
                   else:
                       beurten_overslaan[beurt] += 1
                       speciale_tekst = "Som fout! Speler " + str(beurt + 1) + " slaat een beurt over."

               #gevangenis
               if pion_posities[beurt] == 52:
                   beurten_overslaan[beurt] += 3
                   speciale_tekst = "Gevangenis, speler " + str(beurt + 1) + " moet 3 beurten overslaan"

               #doolhof
               if pion_posities[beurt] == 42:
                   pion_posities[beurt] -= 3
                   if pion_posities[beurt] < 0:
                       pion_posities[beurt] = 0
                   speciale_tekst = "Doolhof, speler " + str(beurt + 1) + " gaat 3 vakjes terug"

               #herberg
               if pion_posities[beurt] == 19:
                   beurten_overslaan[beurt] += 1
                   speciale_tekst = "Herberg, speler " + str(beurt + 1) + " slaat een beurt over"

               #botsing
               ander = 1 - beurt
               if pion_posities[beurt] == pion_posities[ander] and winnaar is None:
                   pion_posities[ander] = 0
                   speciale_tekst = "Speler " + str(beurt + 1) + " slaat speler " + str(ander + 1) + " terug naar de start"

               #winnaar
               if pion_posities[beurt] == 63:
                   winnaar = beurt
               else:
                   if worp1 == worp2:
                       speciale_tekst = "Dubbel dobbelsteen! Speler " + str(beurt + 1) + " mag nog een keer gooien"
                       oude_beurt = beurt
                   else:
                       oude_beurt = beurt
                       beurt = beurt_doorgeven(beurt)

           elif event.key == pygame.K_BACKSPACE:
               print("Backspace ingedrukt - Reset het spel")
               pion_posities = [0, 0]
               beurt = 0
               oude_beurt = 0
               winnaar = None
               worp = 0
               worp1 = 0
               worp2 = 0
               beurten_overslaan = [0, 0]

           update_screen("normaal")

# --------------- Afsluiten van Pygame ---------------
pygame.quit()
