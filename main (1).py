# Feud program
import random
import time
# -------------------------
# Subprograms
# -------------------------
def forage_herb():
  x = 0
  global money
  global life
  while x == 0 and money > 0:
    selectedherb = ' '
    print(' available herbs to purchase are: \n 1 COINS | dandelion, burdock, pipewort, ragwort, nettles and holly \n 2 COINS | thyme and garlic')
    herbchoice = input('what herb do you want to forage? ')
    if herbchoice in ['d','dandelion', 'dan']:
      selectedherb = 'dandelion'
    elif herbchoice in ['b','burdock', 'bur']:
      selectedherb = 'burdock'
    elif herbchoice in ['p','pipewort', 'pip']:
      selectedherb = 'pipewort'
    elif herbchoice in ['r','ragwort', 'rag']:
      selectedherb = 'ragwort'
    elif herbchoice in ['n','nettles', 'net']:
      selectedherb = 'nettles'
    elif herbchoice in ['h','holly', 'hol']:
      selectedherb = 'holly'
    elif herbchoice in ['t','thyme', 'thy']:
      selectedherb = 'thyme'
    elif herbchoice in ['g','garlic', 'gar']:
      selectedherb = 'garlic'
    else:
      selectedherb = 'default'
      
    if selectedherb in herblist:
      print('input valid, foraging plant....')
      herbs.append(selectedherb)
      print('---------')
      print(f'you succesfully bought {selectedherb}! Added to inventory')
      print('---------')
      x = 1
      money = money - 1
      if selectedherb == 'garlic' or selectedherb == 'thyme':
        money = money - 1
        if money < 0:
          print('you lost a life for getting in debt')
          life = life - 1
      forage_herb()
      
    elif herbchoice in ['quit', 'q', 'l']:
      print('quitting forage')
      x = 1
      take_action()
    else:
      print('herb foraging was unsuccesful')

def cauldron(spell):
  global money
  y = 0
  htn1 = 'n'
  htn2 = 'n'
  herbs1 = 'default'
  herbs2 = 'default'
  if spell == 'teleport':
    herbs1 = 'dandelion'
    herbs2 = 'burdock'
  elif spell == 'protect':
    herbs1 = 'pipewort'
    herbs2 = 'ragwort'
  elif spell == 'heal' and level >= 3:
    herbs1 = 'dandelion'
    herbs2 = 'pipewort'
  elif spell == 'devildrink' and level >= 2:
    herbs1 = 'nettles'
    herbs2 = 'holly'
  elif spell == 'charm' and level >= 3:
    herbs1 = 'garlic'
    herbs2 = 'thyme'
  elif spell == 'companion' and level >= 5 and money > 8:
    herbs1 = 'garlic'
    herbs2 = 'holly'
    money = money - 8
  if herbs1 in herbs:
    print(' herb1 present')
    htn1 = 'y'
  else:
    print('invalid, either not correct level or herb not present or funds not present')
    take_action()
  if herbs2 in herbs:
    print(' herb2 present')
    htn2 = 'y'
  else:
    print('invalid')
    take_action()
  if htn1 == 'y' and htn2 == 'y':
    print('---------')
    print(f'{spell} has been brewed')
    print('---------')
    herbs.remove(herbs1)
    herbs.remove(herbs2)
    inventory.append(spell)
    brew_spell()
  else:
    print('soemthing went wrong - you must not have enough resources!')

def check_level():
  global donated
  global level
  global companion
  global money
  global totalsteps
  global castle
  global DEVIL
  global donated
  if totalsteps >= 100 and level == 1:
    level = 2
    print('---------')
    print('you reached level 2')
  elif totalsteps >= 200 and level == 2:
    level = 3
    print('---------')
    print('you reached level 3')
  elif totalsteps >= 400 and level == 3:
    level = 4
    print('---------')
    print('you reached level 4')
    print('granted 3 money as a reward')
    money = money + 3
  elif totalsteps >= 600 and level == 4:
    level = 5
    print('---------')
    print('you reached level 5')
  elif totalsteps >= 800 and level == 5 and companion == True:
    level = 6
    print('---------')
    print('you reached level 6')
  elif totalsteps >= 1500 and level == 6:
    level = 7
    print('---------')
    print('you reached level 7')
  elif totalsteps >= 2000 and level == 7:
    level = 8
    print('---------')
    print('you reached level 8')
    print('---------')
  elif totalsteps >= 2400 and level == 8:
    level = 9
    print('---------')
    print('you reached level 9')
    print('---------')
  elif totalsteps >= 3000 and level == 9:
    level = 10
    print('---------')
    print('you reached level 10')
    print('---------')
    devil_curse()
  elif totalsteps >= 4000 and level == 10:
    level = 11
    print('---------')
    print('you reached level 11')
    print('---------')
    castle = True
    DEVIL = False
    castle_menu()
  elif donated >= 120 and level == 11:
    level = 12
    print('---------')
    print('you reached level 12')
    print('---------')
    #battle()
  

def brew_spell():
  z = 0
  while z == 0:
    print(f'spells available to brew in {version} are teleport, protect, heal, devildrink, charm and companion')
    print('type "r" for availble recipes')
    brewchoice = input(' what spell do you wish to brew? ')
    selectedbrew = ' '
    if brewchoice == 'r':
      print(' LEVEL 1 | dandelion + burdock = teleport')
      print(' LEVEL 1 | pipewort + ragwort = protect')
      print(' LEVEL 2 | nettles + holly = devildrink')
      print(' LEVEL 3 | dandelion + pipewort = heal')
      print(' LEVEL 3 | garlic + thyme = charm')
      print(' LEVEL 5 | garlic + holly + 8 COINS = companion')
    elif brewchoice in ['t','teleport', 'tel']:
      selectedbrew = 'teleport'
    elif brewchoice in ['p','protect', 'pro']:
      selectedbrew = 'protect'
    elif brewchoice in ['h','heal', 'he']:
      selectedbrew = 'heal'
    elif brewchoice in [ 'd','devildrink', 'dev']:
      selectedbrew = 'devildrink'
    elif brewchoice in ['c','charm', 'cha']:
      selectedbrew = 'charm'
    elif brewchoice in ['co','companion', 'com']:
      selectedbrew = 'companion'
    else:
      selectedbrew = 'default'
      if brewchoice in ['quit', 'leave', 'l', 'q']:
        print('quitting brew')
        z = 1
        take_action()
      brew_spell()

    if selectedbrew in potions:
      print('valid spell, preparing cauldron')
      cauldron(selectedbrew)
      z = 1
      print('------------')
    else:
      print('invalid spell not found')

def move_around():
  steps = 0
  randomitem = ' error '
  global money
  global totalsteps
  global protect
  global life
  global charm 
  global hours
  global hunger
  global companion
  global find
  global companionf
  global companion_name
  chance = 0
  proceed = input('do you wish to move? y/n: ')
  
  if proceed == 'y':
    hours = hours + 1
    if companion == True:
      hunger = hunger - 1
      find = find - 1 
      if hunger == 0:
        companionf = 0
        ('--------')
        ('--------')
        ('--------')
        print('your companion has died')
        print('penatly 5 coins')
        money = money - 5
        print(f'rest in peace {companion_name}')
        print(f'you had {len(herbs)} herbs - should have looked after him ):')
        ('--------')
        ('--------')
        ('--------')
        companion = False
    print('moving a random ammount forward...')
    steps = steps + random.randint(1,20)
    totalsteps += steps
    print(f'took {steps} steps forward out of a possible 20')
    if steps in [1,2,3,4,5]:
      ranmoney = random.randint(1,3)
      money = money + ranmoney
      print('---------')
      print(f'found {ranmoney} coins')
      print('---------')
    elif steps in [6,7,8]:
      if protect > 0:
        print('---------')
        print(' you have been protected - whilst protected beggars cannot be interacted with')
        print('---------')
        protect = protect - 1
      else:
        chance = 0
        print('you stumbled upon a beggar')
        randomitem = random.choice(herblist)
        print(f' he asks if you want to purchase {randomitem} for one coin?')
        if money == 0:
          print('---------')
          print('you have no money to trade with')
          take_action()
        beggarchoice = input('y/n: ')
        if beggarchoice == 'y':
          money = money - 1
          chance = random.randint(1,2)
          if chance == 1:
            herbs.append(randomitem)
          else:
            print('---------')
            print('he attacked you and kept the money')
            print('---------')
            life = life - 1
        else: 
          print('there was no consequence')
          take_action()
    elif steps in [9,10]:
      if protect > 0:
        print('---------')
        print(' you have been protected, the monster ran away')
        print('---------')
        protect = protect - 1
      else:
        print('---------')
        print('A monster attacked you - you have lost a life')
        print('---------')
        life = life - 1
        take_action()
        
    elif steps in [13,14]:
      print('---------')
      print('you found a chest')
      print('---------')
      randomitem = random.choice(herblist)
      herbs.append(randomitem)
      print(f'you found a {randomitem}')
    elif steps in [20]:
      ranrare = ' '
      print('---------')
      ranrare = random.choice(rarelist)
      print(f'you found {ranrare}')
      rare.append(ranrare)
      print('sell me at a merchant')
      print('---------')
    elif steps in [11,12,15,16]:
        print('---------')
        print('there is a bandit')
        print('---------')
        if charm > 0:
          charm = charm - 1
          print('the bandit has been charmed,you steal an item')
          chance = random.randint(1,3)
          if chance == 1:
            money = money + 1
            print('---------')
            print('money stolen')
            print('---------')
            take_action()
          elif chance == 2:
            randomsitem = random.choice(herblist)
            print('---------')
            print(f'{randomsitem} stolen from bandit')
            print('---------')
            herbs.append(randomsitem)
            take_action()
            
          elif chance == 3:
            print('---------')
            print('he had nothing to steal')
            print('---------')
            take_action()
          else:
            print('error')
            
            
        if len(inventory) > 0:
          inventory.remove(random.choice(inventory))
          print('the bandit stole an item')
        elif money > 0:
          money = money - random.randint(1,2)
          print('the bandit stole money')
        else:
          print('---------')
          print('there is nothing to steal so he runs away')
          print('---------')
    else:
      print('---------')
      print('you found nothing')
      print('---------')
      take_action()
  else:
    take_action()

def help_menu():
  helpneeded = ' '
  global version
  global lore
  print(f' 1 ( basics ) 2 ( levels ) 3 ( merchants ) L ( lore ) q ( quit ) version {version} \n 4 ( recipes ) 5 ( companions ) 6 ( moving encounters ) 7 ( spells purposes ) 8 ( casino )')
  helpneeded = input('what do you need help with? ')
  if helpneeded in ['1', 'basics', 'b']:
    print('--BASICS--')
    print('Forage: you can forage for herbs, these can be used to brew potions')
    print('each forage costs atleast 1 coin, when on forage prices will be shown')
    print('----------')
    print('Brew: you can brew potions using herbs, these can be used in multiple different ways')
    print('each potion will cost 2 herbs, when on brew type 'r' for recipes')
    print('----------')
    print('Move: you can move around the realm, this will move you a random ammount of steps')
    print('there is an element of risk, as you move randomly from 1 - 20.')
    print('moving adds to your steps total. Steps are requiered to progress the game')
    print('----------')
    print('Use: you can use potions, it will ask for which to use, if in your invetory it will cast')
    print('once a potion is used it will be removed from your inventory')
    print('----------')
    print('Inventory: you can check your inventory, this will show you what spells you have bought/crafted')
    print('Herbs: you can check your herbs, this will show you what herbs you have bought/farmed/found')
    print('----------')
    print('Quit: typing quit on the main menu will commit suicide, losing what you own')
    print('using quit at any other point will take you to main menu, backing out of an action')
    print('----------')
    print('Stats:')
    print('The stats in this game are: money, steps, protect, life, charm and hours')
    print('Money: currency in game which can be earnt and spent - getting into debt loses a life')
    print('Steps: the total ammount of steps you have taken')
    print('Protect/protection: the ammount of times you can be protected (blocks beggars and monsters)')
    print('Life: the ammount of times you can be attacked by monsters before you die')
    print('Charm: the ammount of times you can charm the bandits, stealing an item from them')
    print('Time: a 6 hour clock which keeps track of the tick you are on. Useful for companions and farming')
    print('----------')
    
  elif helpneeded in ['2', 'levels','le']:
    print('--LEVEL REQUIERMENTS--')
    print(' level 1: steps = 0 \n level 2: steps = 100 \n level 3: steps = 200 \n level 4: steps = 400 \n level 5: steps = 600 \n level 6: steps = 800 and companion alive \n level 7: steps = 1500 \n level 8: steps = 2000 \n level 9: steps = 2400 \n level 10: steps = 3000 \n level 11: steps = 4000 \n level 12: complete castle ')
    print('--LEVEL GRANTS--')
    print(' level 1: herb, recipes and and life')
    print(' level 2: devildrink unlock')
    print(' level 3: heal and charm unlock')
    print(' level 4: grants 3 coins')
    print(' level 5: unlocks companions')
    print(' level 6: unlocks bundles')
    print(' level 7: unlocks casino')
    print(' level 8: grants 8 coins')
    print(' level 9: Summon Merchant')
    print(" level 10: The Devil's Curse")
    print(' level 11: unlocks the castle')
    print(' level 12: unlocks _£%!$&8(_')
    print('----------')
  elif helpneeded in ['3', 'merchants', 'm']:
    print('--MERCHANTS--')
    print('Merchants spawn every 200 steps')
    print('Once you reach 2500 steps - you gain the ability to summon him at your will')
    print('Merchants are protecters and traders of the world. They can help with many things;)')
    print('At Merchants you may sell rare items for money - the rate is different everytime you meet him')
    print('At the Merchants you may buy a random potion (that could be above your level) for 4 coins')
    print('At the Merchants you may buy auto-farm for 10 coins which will farm the herb you choose every 6 hours')
    print('At the Merchants you may release your companion into the wild')
    print('YOU SHOULD ONLY BUY 1 OF THE SAME TYPE OF FARM')
    print('Merchants are very helpful, using a teleport potion to advance steps may be a useful tactic ;) ')
    print('----------')
  elif helpneeded in ['4', 'recipes', 'r']:
    print('--RECIPES--')
    print('--HERB PRICES--')
    print(' 1 COINS | dandelion, burdock, pipewort, ragwort, nettles and holly \n 2 COINS | thyme and garlic')
    print('--BREW RECIPES')
    print(' LEVEL 1 | dandelion + burdock = teleport')
    print(' LEVEL 1 | pipewort + ragwort = protect')
    print(' LEVEL 2 | nettles + holly = devildrink')
    print(' LEVEL 3 | dandelion + pipewort = heal')
    print(' LEVEL 3 | garlic + thyme = charm')
    print(' LEVEL 5 | garlic + holly + 8 COINS = companion')
    print('----------')
  elif helpneeded in ['5', 'companions', 'c']:
    print('--COMPANIONS--')
    print('LEVEL 5 AND UP ARE ADVISED TO OWN A COMPANION, it is not advised to own at a lower level')
    print('Companions can be spawned by brewing the potion "companion" - this potion summons one')
    print('Your companion is then named, and should be given your attention')
    print('Your companion will become hungry after 6 hours. If it is hungary feed it with a random herb')
    print('Companions eat anything, so it may even eat your garlic or thyme! So be mindful when feeding')
    print('Companions will find items every 10 hours. These items can be anything in the game - but usually spells')
    print('If your companion finds the spell "companion" it will be traded for a dandelion')
    print('Companions cost 8 money to buy, and will require feeding and if they die in your possesion')
    print('they will be hosted a funeral which will cost you 5 coins')
    print('IT IS VERY IMPORTANT TO NOTE COMPANIONS ARE EXTREMELY EXPENSIVE, SO MAKE SURE YOU HAVE THE FUNDS')
    print('if you no longer want your companion you can release him into the wild at a merchants')
    print('----------')
  elif helpneeded in ['6', 'moving encounters', 'm']:
    print('--MOVING ENCOUNTERS--')
    print('When you move, you move a random ammount of steps from 1 to 20')
    print('Steps are required to progress the game')
    print('----------')
    print('What You May Encouner;')
    print('MONSTER: monster will damage you 1 life when encountered')
    print('unless you have protection, in which case it will run away')
    print('----------')
    print('BEGGAR: beggar will give you the opportunity to purhcase any random item for 1 coin')
    print('saying no will make him leave leading to no consequence.')
    print('having protection will automatically make the choice to leave')
    print('If you agree to the deal there is a 50/50 chance you will recieve the item and a 50/50')
    print('chance you will not and he will take your money and damage you a life - its a risk')
    print('----------')
    print('BANDIT: bandit will steal money and items from you')
    print('Bandit will attempt to steal a coin from you, if you have no coins it will steal an item')
    print('If you have charm it will attempt to charm the bandit if succesful you will steal an item')
    print('If unsuccesful there will be no consequecne and you both keep items')
    print('there is a 2 in 3 chance it will be succesful. Charm is the only way to avoid bandits')
    print('----------')
    print('CHEST: finding a chest will grant you either a herb or a potion')
    print('the odds are 50/50 - there is no downside to fidning a chest (yet)')
    print('----------')
    print('RARE ITEM: there is a 1 in 20 chance you will find a rare item')
    print('rare items can be sold at merchants for varying but high prices')
    print('----------')
    print('NOTHING: yeh no, litterly nothing happens - i mean litterly.')
    print('----------')
    print('CURRENT ODDS')
    print('Odds are always a secret and depend on the version you play')
    print('----------')
  elif helpneeded in ['7', 'spells purposes', 's']:
    print('--SPELL PURPOSES--')
    print('Teleport: teleports you across the map safely anywhere between 10 and 120 steps')
    print('Protect: blocks beggars and monsters - Max of 5, potion gives 2')
    print('Heal: heals you 1 life - Max of 3')
    print('Charm: charms the bandits and takes an item potion gives 2, max of 3')
    print('Companion: summons a companion, max of 1')
    print('Devils_drink: 50/50 chance of -6 coins or +6 coins')
    print('----------')
  elif helpneeded in ['q', 'quit', 'menu']:
    take_action()
  elif helpneeded in ['casino', '8', 'ca']:
    print('--CASINO--')
    print('at level 7 you reach the ability to enter the casino')
    print('each spin of the wheel will cost you 4 coins - remember if you run out of money you will lose a life')
    print('the aim of casino is to match all 3 roles to the same number')
    print('matching 1s will grant you 3 of the same random spell')
    print('matching 2s will grant you 3 rares')
    print('matching 3s will grant you 20 coins')
    print('getting 1,2,3 in that order, grants 10 coins')
    print('getting a random mix will win you nothing')
    print('----------')
  elif helpneeded in ['L','l','lore','Lore']:
    if lore == True:
      lore = False
      print('----------')
      print('Lore turned off')
      print('----------')
    elif lore == False:
      lore = True
      print('----------')
      print('Lore turned on')
      print('----------')
    
def check_totals():
  global money
  global protect
  global totalsteps
  global hours
  global life
  global charm
  if money < 0:
    money = 0
  if life > 3:
    life = 3
  if protect > 5:
    protect = 5
  if protect < 0:
    protect = 0
  if charm > 3:
    charm = 3
  if totalsteps < 0:
    totalsteps = 0
  if hours >= 7:
    hours = 0
  
def use_item():
  randomnum = 0
  global totalsteps
  global protect
  global money
  global life
  global charm
  global companion
  if len(inventory) > 0:
   itemselected = input('which item do you wish to use: ')
   if itemselected == 'teleport' and 'teleport' in inventory:
     randomsteps = random.randint(50,120)
     totalsteps = totalsteps + randomsteps
     print(f'{itemselected} has been cast')
     print(f' you travelled {randomsteps} steps!')
     inventory.remove(itemselected)
   elif itemselected == 'protect' and 'protect' in inventory:
     protect = protect + 2
     print(f'{itemselected} has been cast')
     inventory.remove(itemselected)
   elif itemselected == 'devildrink' and 'devildrink' in inventory:
     print(f'{itemselected} has been cast')
     randomnum = random.randint(1,2)
     inventory.remove(itemselected)
     if randomnum == 1:
       print('You lost 6 coins. The Devil didnt like you')
       money = money - 6
     elif randomnum == 2:
       print('You gained 6 coins. The Devil liked you')
       money = money + 6
     else:
       print('error casting devil potion')
     
   elif itemselected == 'heal' and 'heal' in inventory:
     life += 1
     print(f'{itemselected} has been cast')
     inventory.remove(itemselected)
   elif itemselected == 'charm' and 'charm' in inventory:
     charm = charm + 2
     print(f'{itemselected} has been cast')
     inventory.remove(itemselected)
   elif itemselected == 'companion' and 'companion' in inventory:
     yesn = input('warning - you should only spawn a companion if you have a good ammount of money \n are you sure y/n:')
     if companion == True:
       print('---------')
       print('cant spawn as you already have a companion')
       take_action()
     if yesn == 'y':
      companion = True
      inventory.remove(itemselected)
      print('---------')
      print('A wild dog has been summoned \n - he will follow you and depend on you \n access the companion menu by typing c')
      print('---------')
     else:
       print('cancelled')
       take_action()
     
def buy_merchant():
  global forsale
  global money
  global ammountbought
  print(f'You can purchace {forsale} for only 4 coins!')
  merchantchoice = input('purchace? y/n: ')
  if merchantchoice == 'y' and money >=  4 and ammountbought <= 3:
    money = money - 4
    ammountbought = ammountbought + 1
    inventory.append(forsale)
    print('---------')
    print(f'you have purchased {forsale} for 4 coins!')
    print('you can buy up to 3')
    print('---------')
  else:
    print('---------')
    print('insufficient funds, bought too many or cancelled purchase')
    print('---------')
  merchant()
  
def sell_merchant():
  rate = 0
  sum = 0
  global money
  rate = random.randint(4,10)
  print('---------')
  print(f'I will buy all your rare items for the rate of {rate} each, today!')
  print('---------')
  accept = input('accept rate y/n: ')
  if accept == 'y' and len(rare) > 0:
    sum = len(rare) 
    owed = sum * rate
    money = money + owed
    print('---------')
    print(f'payed {owed} for {sum} items')
    print('---------')
    i = 0
    for i in range(sum):
      i += 1
      rare.remove(rare[0])
    merchant()
  else:
    print('---------')
    print('no rare items or cancelled sale')
    print('---------')
    merchant()

def auto_merchant():
  auto = ''
  global dandelion
  global burdock
  global ragwort
  global pipewort
  global money
  global companion
  
  if money < 10:
    print('---------')
    print('insufficient funds')
    print('---------')
    merchant()
  print('Costs 10 coins')
  print(' d (dandelion) b (burdock) r (ragwort) p (pipewort) l (leave) ')
  print(' buying a farm again will spend your money and gain you nothing ')
  auto = input(' which automation would you like to buy? ')
  if auto == 'd':
    print('---------')
    print('dandelion farm activated - every 6 hours = 1 dandelion')
    print('---------')
    money = money - 10
    dandelion = True
    merchant()
  elif auto == 'b':
    print('---------')
    print('burdock farm activated - every 6 hours = 1 burdock')
    print('---------')
    burdock = True
    money = money - 10
    merchant()
  elif auto == 'r':
    print('---------')
    print(f'ragwort farm activated - every 6 hours = 1 ragwort')
    print('---------')
    money = money - 10
    ragwort = True
    merchant()
  elif auto == 'p':
    print('---------')
    print(f'pipewort farm activated - every 6 hours = 1 pipewort') 
    print('---------')
    money = money - 10
    pipewort = True
    merchant()
  elif auto == 'l':
    merchant()
  else: 
    ('error, retype')
    auto_merchant()
  
  merchant()

def meet_merchant():
  global forsale
  global ammountbought
  ammountbought = 0
  forsale = random.choice(potions)
  print('(your last action was saved)')
  print('---------')
  print('You stumbled upon a merchant')
  print('---------')
  merchant()

def devil_curse():
  global DEVIL
  global Merchmax
  global companion
  global money
  global life
  print('---------')
  print('---------')
  print('---------')
  print('---------')
  print('---------')
  print('---------')
  print('𖤐𖤐𖤐𖤐⸸ - YOU HAVE BEEN CURSED - ⸸𖤐𖤐𖤐𖤐')
  time.sleep(1)
  print('𖤐𖤐𖤐𖤐⸸ - THE END IS NEAR - ⸸𖤐𖤐𖤐𖤐')
  time.sleep(1)
  print('𖤐𖤐𖤐𖤐⸸ - YOU MUST TRAVEL THE PATH ALONE - ⸸𖤐𖤐𖤐𖤐')
  time.sleep(1)
  print('𖤐𖤐𖤐𖤐⸸ - AND SHALL SUFFER - ⸸𖤐𖤐𖤐𖤐')
  time.sleep(1)
  print('𖤐𖤐𖤐𖤐⸸ - EVERY 100 steps = -1 LIFE - ⸸𖤐𖤐𖤐𖤐')
  time.sleep(1)
  print('𖤐𖤐𖤐𖤐⸸ - THE MERCHANT HAS BEEN EXECUTED ⸸𖤐𖤐𖤐𖤐')
  time.sleep(1)
  print('𖤐𖤐𖤐𖤐⸸ - YOUR COMPANION MURDERED - ⸸𖤐𖤐𖤐𖤐')
  time.sleep(1)
  print('𖤐𖤐𖤐𖤐⸸ - BUNDLES BANNED - ⸸𖤐𖤐𖤐𖤐')
  time.sleep(1)
  print('𖤐𖤐𖤐𖤐⸸ - TELEPORT BANNED - ⸸𖤐𖤐𖤐𖤐')
  time.sleep(1)
  print('𖤐𖤐𖤐𖤐⸸ - INVENTORY - ⸸𖤐𖤐𖤐𖤐')
  time.sleep(1)
  print('𖤐𖤐𖤐𖤐⸸ - HERBS - ⸸𖤐𖤐𖤐𖤐')
  time.sleep(1)
  print('𖤐𖤐𖤐𖤐⸸ - MONEY - ⸸𖤐𖤐𖤐𖤐')
  time.sleep(1.5)
  print('𖤐𖤐𖤐𖤐⸸ - RESET - ⸸𖤐𖤐𖤐𖤐')
  time.sleep(2)
  print('𖤐𖤐𖤐𖤐⸸ - okay - i am not that mean (granted 10 coins) - ⸸𖤐𖤐𖤐𖤐')
  time.sleep(1)
  print('---------')
  print('---------')
  print('---------')
  print('---------')
  print('---------')
  print('---------')
  money = 10
  life = 3
  inventory = []
  herbs = []
  DEVIL = True
  Merchmax = False
  companion = False

mk1 = 0
mk2 = 0
mk3 = 0
mk4 = 0
mk5 = 0
mk6 = 0
mk7 = 0
mk8 = 0
mk9 = 0
mk10 = 0
mk11 = 0
mk12 = 0
mk13 = 0
def merchant():
  global success
  global money
  global Merchmax
  global auto
  global lore
  global companion
  global companion_name
  global mk1
  global mk2
  global mk3
  global mk4
  global mk5
  global mk6
  global mk7
  global mk8
  global mk9
  global mk10
  global mk11
  global mk12
  global mk13

  if merch == 2 and lore == True and mk1 == 0:
    mk1 = 1
    print('-')
    print("Why hello there!  \n I’m the Importer, the only merchant you will encounter in this realm. \n You may wonder where you are, well it’s lucky you met me, I can help. You’ve just entered Mallowkeep, a town filled with dark forests and dangerous alleyways. But don’t worry! It’s one of the few cities in this realm where you are safe from… \n Well nevermind about that, I don’t want you to panic. \n You will find me at the entrance to every town, which is, if I’m right, which is not very often, around 200 steps apart. Don’t question how I’m there before you. Just don’t, even I don’t understand. \n I wish you luck on your journey my benevolent friend! Beware beggars, there’s a chance you may gain money, but don’t gamble your life away. \n From now on, courage will be your best defence against the hardships ahead. \n Stay strong. ")
    proceed = input('proceed ')
  if merch == 3 and lore == True and mk2 == 0:
    mk2 = 1
    print('-')
    print("Oh! Its you! I didn’t expect to see you so soon! Well, anyway I’m relieved to see you, I was worried you were dead, and that would be no good. There’s no use in a dead customer. Just ask me if you need anything. \n It’s good you’re here, I heard that Genesis was looking for you in Mallowkeep. I’ll tell you more about Genesis next time I see you! \n Anyway, you’ve entered Grafenberg! This is a town crammed with wealth and opportunities, don’t waste your chance! \n How’s your head, any head-aches? \n Just ignore that, I’m just concerned for your health, I don’t want my number one customer dying on their journey! \n Oh, It seems I must go, I do have other customers you know! If you need me, remember you will meet me only 200 steps away. \n Good luck, brave traveller, remember to protect your rare items as I can give you a hefty price for them next time you see me. Goodbye!")
    proceed = input('proceed: ')
  if merch == 4 and lore == True and mk3 == 0:
    mk3 = 1
    print('-')
    print("How are you so speedy? Why you remind me of one of the pets that I used to have, a beautiful creature ,it was a mesmerising emerald colour with long striding legs and wide paws, it was fascinating to watch because it seemed as though it moved at the speed of light. Oh how I miss it - it was stolen from me in an act of revenge. \n Anyway, that’s not important! How are you, I do hope you’re well. It seems you’ve been busy whilst we were apart. \n While you’re here I may as well tell you more about Genesis. They seem to have a deal with a Devil, or so I’ve heard from the rumours of the realm; they’ve gained more control of the people, life has become a living hell. \n I was worried that they’d found you, God knows what torture you would have experienced, it’s lucky you have me, your amazing merchant. \n I must go now, so I’ll leave you with a warning: this town, Crosshills, is barren and dark, I suggest you move through here quickly, don’t get caught up in frolicking! \n Farewell! ")
    proceed = input('proceed: ')
  if merch == 5 and lore == True and mk4 == 0:
    mk4 = 1
    print('-')
    print("You again?! Now that is really unexpected, but a good surprise. I heard you had a tiring journey through Crosshills, but I can swear to you that Magon is a lot nicer! \n Have you experienced any more headaches? No, very good! \n You must persevere and work harder! This journey is not for the weak. \n I know it must be tempting to try a Devil’s Drink but I really can’t advise you to, remember he is not on your side, at the moment he’s hunting for you alongside Genesis. \n Did you know, the drink was initially created to tempt apostles and religious zealots, so that the Devil could use their sin of gambling as a tool of bargaining. It was basically blackmail, so I’d stay away from it if I was you! \n I know I may seem like a ranting fool to you, but I only want the best for you, if anything I’m like your guardian angel. \n It’s time for you to journey onwards, if you need help, you can always ask, don’t feel cowardly for needing guidance. \n I’ll meet you in the next town’s alehouse, it’s warm and welcoming there! \n Goodbye!")
    proceed = input('proceed: ')
  if merch == 6 and lore == True and mk5 == 0:
    mk5 = 1
    print('-')
    print("Oh, it’s you! \n I don’t really have much to say today, but I do think you should try some of this beer, it’s very strong but very filling. \n You seem tired, maybe brew some teleport spells? \n I’ll see you in Verdrana, stay safe!")
    time.sleep(2)
    print("You try some...")
    time.sleep(3)
    print("He was right, the old man, that was the best beer you ever tasted")
    proceed = input('proceed: ')
  if merch == 7 and lore == True and mk6 == 0:
    mk6 = 1
    print('-')
    print("Hello again traveller, I’m sorry I was so intoxicated when we last spoke. \n There was a bit too much ragwort in my mug of ale. Ragwort was only discovered to have alcoholic properties quite recently, almost got banned because the Genesis had some… unfortunate experiences with alcohol. But luckily I didn’t! \n Now, there are some casinos further ahead. I beg you not to go inside, even if you don’t get found by Genesis and the Devil, then you might lose all your hard-earned money. \n Who will buy from me then? Oh don’t worry I’m just joking, I have come to see you as a friend even though our conversations are rather… one sided. \n Speaking of friendship, have you been having any hallucinations or head-aches. No? Thank God. \n Goodbye then, have fun walking through Verdrana, remember to stay away from those damn casinos, and if you do go in, please don’t mention me!")
    proceed = input('proceed: ')
  if merch == 8 and lore == True and mk7 == 0:
    mk7 = 1
    print('-')
    print("Why hello again, I’ve heard that you have stumbled across some casinos (well hopefully anyway), I really hope you didn’t lose anything. \n I feel obligated to tell you now for my reasons to detest those casinos. Before, I mentioned my furry friend, oh how I loved it. \n Before I was a merchant I became addicted to gambling, my whole world became slot machines and poker, but I quickly lost money. The further I got in debt, the more the Devil wanted me to pay him back. \n Now my pet was worth a lot of money, and I refused to sell it, until one night the Devil stole my friend as payment for my debts. God knows what happened to it. \n And that’s the reason I was so concerned about you being near a casino, it’s not safe. \n But since then I have hidden away from the Devil, I cannot lose anything again, and that is why you couldn’t tell them about me either. \n I really do need to get along, sadly I have more customers to get to, I will see you in Ancead, the next town along.")
    proceed = input('proceed: ')
  if merch == 9 and lore == True and mk8 == 0:
    mk8 = 1
    print('-')
    print("Hello, hello! It’s me! I thought I should tell you how I became a merchant, since you seemed bored and it’s an interesting story. \n So, as I told you last time, I gambled away my happiness, and I became a coward, slept in alleyways, and became a beggar. \n Until, one day a kind traveller, much like you, stumbled across me and we traded some ragweed. They seemed to be part of the alcohol business too, so I felt obliged to form a relationship with them where I would find them ragweed for a decent price. \n They basically took me under their wing from then on, and I realised that I could make a business out of trades, and so I became the Importer. \n I think that is why I have taken a liking to you, my dear friend. Oh my, look at the time, the sun has almost set, I need to get a room in the open house . \n You could come if you want, but you don’t seem like the type of person to waste time with sleep and laziness. \n Goodbye!")
    proceed = input('proceed: ')
  if merch == 10 and lore == True and mk9 == 0:
    mk9 = 1
    print('-')
    print("Welcome! Welcome! My brave friend, it is a delight to see you again! \n How’s your journey been, I’ve been waiting ages for you to arrive in Earthholt. This is one of my favourites place you know, I grew up here with just my father, he was a man who wouldn’t accept failure, which is why I was casted out of his home when I started to drown in debt. \n This was a few years before the Genesis grew stronger. \n Oh of course I don’t hate him, I completely understand why he did it, but I do wish he would see me again. \n Well, no time for sob stories, right now, it’s important you keep moving forward, I heard Genesis and the Devil are hunting around for someone at the casinos just a bit back down the road. \n You really must tell me if you have any headaches. \n If you need anything from me, I’ll be waiting eagerly for you at the entrance to Catabria, it’s a cosy little town not far along. \n Don’t die!")
    proceed = input('proceed: ')
  if merch == 11 and lore == True and mk10 == 0:
    mk10 = 1
    print('-')
    print("Oh my god, it’s you again! Amazing, you really are determined to survive. \n This is Catabria, a pleasant old village, you’ll really enjoy it here \n I think you really ought to know more about the Genesis, since it seems to be hunting you. Not that it is hunting you, it could be hunting anyone, just to be careful. \n The Genesis seems to have advanced skills in brewing, it seems they have a massive farm of herbs, and most of the realm’s ragwort is grown in their farm. Almost nobody knows how they cultivated it so much, but they can control us all so much more when they have control of popular herbs. \n Since it seems they are stuck in time, but gaining knowledge and power, they seem to be unstoppable. \n Can I be honest with you? I think you are fierce enough to defeat the Devil and the Genesis, I see in you a courageous and fearless soul. \n I really do hope the best for you, my sweet friend, and I hope one day I can freely travel the realm with you! \n But, you really must carry on forward, goodbye!")
    proceed = input('proceed: ')
  if merch == 12 and lore == True and mk11 == 0:
    mk11 = 1
    print('-')
    print('The Merchant Did not say anything to me today')
    proceed = input('proceed: ')
  if merch == 13 and lore == True and mk12 == 0:
    mk12 = 1
    print('-')
    print("Hello again! Sorry I was quiet last time, i’m fine i assure you! \n Anyway my friend now have you been? Any hallucinations? Any headaches? \n Nevermind my stupid questions, I’ve decided that you need me much more now than ever, so here’s a potion so that you can summon me anytime you want, of course I will still be waiting at the next town for you, but this will be so fun! \n I would join you for travelling but I can’t wrack up my debt again, I must keep my business in control. \n Now, I’m a bit worried about your safety, you see someone has been following me since the last town, and I fear they know that I’ve become friends with you. \n You really must be careful. \n It’s a beautiful day today, it seems you will have a good journey. \n See you soon!")
    proceed = input('proceed: ')
  if merch == 14 and lore == True and mk13 == 0:
    mk13 = 1
    print('-')
    print("Oh thank God it’s you, we really must meet in quiet places from now on, I fear the Devil and Genesis know I am helping. \n They don’t agree with me selling spells and farms for decent prices, because they like to keep control of the farms. Becoming friends with you is even worse to them. \n I’m sure someone is after me, I keep hearing someone walking close behind me, yet every time I turn around there is nothing. Then, whilst I was waiting for you, a beggar ran up to me and tried to stab me, then a piano fell off a rooftop not far from where I was standing. \n Well if you move quickly, we can meet 2 towns along at midnight, I heard that there’s carved stone pillars in Unterbay that, at a certain time, the stars through the pillars form a doorway. \n They call it the Doorway To The Stars - I really think we should see it together \n Well then, you must get along with your journey!")
    proceed = input('proceed: ')   
  if merch == 13:
    Merchmax = True
  merchyn = ' '
  merchoice = ''
  print(f'money : {money}')
  print(f' hey {name} what can i do for you?')
  if companion == True:
    print(' c ( release companion )')
  merchoice = input(' b (purchase spell) a (auto-farm) s (sell item) l (leave) ')
  if merchoice == 'c':
    if companion == True:
      print('--------')
      print(f'you released {companion_name} into the wild')
      print('--------')
      companion = False
    else:
      print('You do not own a companion, craft one at level 5')
  if merchoice in ['l','leave']:
    take_action()
  elif merchoice in ['b','purchase herb']:
    buy_merchant()
  elif merchoice in ['s','sell item']:
    sell_merchant()
  elif merchoice in ['a','auto-farm']:
    auto_merchant()
    
def check_merchant():
  global merch
  global totalsteps
  global ammountbought
  if totalsteps > 200 and merch == 1:
    merch = 2
    ammountbought = 0
    meet_merchant()
  if totalsteps > 400 and merch == 2:
    merch = 3
    ammountbought = 0
    meet_merchant()
  if totalsteps > 600 and merch == 3:
    merch = 4
    ammountbought = 0
    meet_merchant()
  if totalsteps > 800 and merch == 4:
    merch = 5
    ammountbought = 0
    meet_merchant()
  if totalsteps > 1000 and merch == 5:
    merch = 6
    ammountbought = 0
    meet_merchant()
  if totalsteps > 1200 and merch == 6:
    merch = 7
    ammountbought = 0
    meet_merchant()
  if totalsteps > 1400 and merch == 7:
    merch = 8
    ammountbought = 0
    meet_merchant()
  if totalsteps > 1600 and merch == 8:
    merch = 9
    ammountbought = 0
    meet_merchant()
  if totalsteps > 1800 and merch == 9:
    merch = 10
    ammountbought = 0
    meet_merchant()
  if totalsteps > 2000 and merch == 10:
    merch = 11
    meet_merchant()
  if totalsteps > 2200 and merch == 11:
    merch = 12
    ammountbought = 0
    meet_merchant()
  if totalsteps >= 2400 and merch == 12:
    merch = 13
    ammountbought = 0
    meet_merchant()
  if totalsteps >= 2600 and merch == 13:
    merch = 14
    ammountbought = 0
    meet_merchant

def companion_menu():
  global companionf
  global hunger
  global companion
  global find
  global money
  global companion_name
  global happy
  randominteract = 0
  if companionf == 0:
    companion_name = ' '
    print('*bark bark*')
    companion_name = input('What shall we name your companion? ')
    print(f' the name {companion_name} has been chosen! What an excellent name!' )
    hunger = 6
    find = 10
    companionf = 1
    happy = 6
    take_action()
  if find == 0:
    find = 10
    happy = happy - 3
    print(f'{companion_name} found something!')
    randomfind = random.choice(potions)
    print(f'companion found {randomfind}')
    inventory.append(randomfind)
    if randomfind == 'companion':
      print(f'{companion_name} cannot find companion - has been replaced with herb garlic')
      inventory.remove('companion')
      herbs.append('garlic')
    companion_menu()
    
    inventory.append(randomfind)
  print('---------')
  print(f" {companion_name}'s hunger: {hunger} happiness: {happy} hours til companion finds an item: {find}")
  companion_choice = input('feed (f) play (p) leave (l) ')
  if companion_choice == 'f' and hunger > 0:
    choice = input('DO you wish to feed your companion a random herb? y/n:')
    if choice == 'y' and len(herbs) > 0:
      herbs.remove(random.choice(herbs))
      hunger = 6
      print('---------')
      print('fed a random herb - companions hunger 6')
      print('---------')
    else:
      print('---------')
      print('cancelled due to no herbs or closed purchase')
      print('---------')
  elif companion_choice == 'p':
    randominteract = random.randint(1,9)
    print('---------')
    if randominteract == 1:
      print(f'{companion_name} jumps at you, barking and licking you. They are clearly having a good time')
    elif randominteract == 2:
      print(f'{companion_name} runs in between your legs, as you turn around he suddenly jumps onto you and licks you.')
    elif randominteract == 3:
      print(f'{companion_name} tries to jump at you and misses, falling head first into the mud. He shakes it off and barks')
    elif randominteract == 4:
      print(f'{companion_name} enjoys it as you stroke their skin. He cuddles around your leg and you enjoy the closeness')
    elif randominteract == 5:
      print(f'{companion_name} does you proud. Just as a bandit is about to hit you. They risk their life and save you')
    elif randominteract == 6:
      print(f'You and {companion_name} play with a ball together. They kick the ball between your legs and you fall over')
    elif randominteract == 7:
      print(f'You give {companion_name} a bath. They are so happy they jump up and down in the water')
    elif randominteract == 8:
      print(f'{companion_name} uses their paws and writes " I love you " in the mud. They come over and cuddle your leg')
    elif randominteract == 9:
      print(f'{companion_name} and you share a ragwort bear. Both drunk you fall over into each other and embrace')
    print('---------')
    happy = 6
    time.sleep(2)
    print(f'played with {companion_name} \n companions happiness increased')
    print('---------')
  elif companion_choice =='l':
    print('exited')
    take_action()
    
  
  
def check_alive():
  global life
  if life <= 0:
    print('------')
    print('------')
    print('------')
    print('------')
    print('------')
    print('you have died')
    print(f'rest in peace {name}')
    print('------')
    print('------')
    print('------')
    print('------')
    print(f'you finished the game with {money} money and {totalsteps} steps and {len(inventory)} items in inventory ')
    print(f'LEVEL REACHED: {level}')
    print('thanks for playing my little game - more to come later')
    print(f'you played version {version}')
    exit()
    
def check_auto():
  global dandelion
  global burdock
  global ragwort
  global pipewort
  global hours

  if dandelion == True:
    if hours == 6:
      hours = 0
      herbs.append('dandelion')
      print('autofarmed dandelion')
  if burdock == True:
    if hours == 6:
      hours = 0
      herbs.append('burdock')
      print('autofarmed burdock')
  if ragwort == True:
    if hours == 6:
      hours = 0
      herbs.append('ragwort')
      print('autofarmed ragwort')
  if pipewort == True:
    if hours == 6:
      hours = 0
      herbs.append('pipewort')
      print('autofarmed pipewort')

def get_bundles():
  global level
  global money
  print('---------')
  print(' 1 | buy 3 teleports - 10 coins')
  print(' 2 | buy 3 protects - 10 coins')
  print(' 3 | buy 3 heals - 12 coins')
  print(' 4 | buy 3 devildrink - 9 coins')
  print(' 5 | buy one of all herbs - 13 coins')
  print(' 6 | buy 3 charms - 13 coins')
  print(' q | exit')
  print('---------')
  chosenbundle = input('choose bundle number: ')
  if chosenbundle in ['1', 'teleports'] and money >= 10:
    inventory.append('teleport')
    inventory.append('teleport')
    inventory.append('teleport')
    print('bought 3 teleports')
    money = money - 10
  elif chosenbundle in ['2', 'protects'] and money >= 10:
    inventory.append('protect')
    inventory.append('protect')
    inventory.append('protect')
    print('bought 3 protects')
    money = money - 10
  elif chosenbundle in ['3', 'heals'] and money >= 12:
    inventory.append('heal')
    inventory.append('heal')
    inventory.append('heal')
    print('bought 3 heals')
    money = money - 12
  elif chosenbundle in ['4', 'devildrink'] and money >= 9:
    inventory.append('devildrink')
    inventory.append('devildrink')
    inventory.append('devildrink')
    print('bought 3 devil drinks')
    money = money - 9
  elif chosenbundle in ['5', 'herbs'] and money >= 13:
    herbs.append(herblist)
    print('bought 1 of each herb')
    money = money - 13
  elif chosenbundle in ['6', 'charm'] and money >= 13:
    inventory.append('charm')
    inventory.append('charm')
    inventory.append('charm')
    print('bought 3 charms')
    money = money - 13
  elif chosenbundle in ['q','exit']:
    print('quiting bundles')
    take_action()
  else:
    print('not enough money or invalid bundle')

def check_curse():
  global DEVIL
  global life
  global ch
  if DEVIL == True:
    i = 0
    while i < len(inventory):
      if 'teleport' in inventory:
        inventory.remove('teleport')
        i = i + 1
    if totalsteps >= 3100 and totalsteps < 3200 and ch == 1:
      life = life - 1
      ch = 2
    elif totalsteps >= 3200 and totalsteps < 3300 and ch == 2:
      life = life - 1
      ch = 3
    elif totalsteps >= 3300 and totalsteps < 3400 and ch == 3:
      life = life - 1
      ch = 4
    elif totalsteps >= 3400 and totalsteps < 3500 and ch == 4:
      life = life - 1
      ch = 5
    elif totalsteps >= 3500 and totalsteps < 3600 and ch == 5:
      life = life - 1
      ch = 6
    elif totalsteps >= 3600 and totalsteps < 3700 and ch == 6:
      life = life - 1
      ch = 7
    elif totalsteps >= 3700 and totalsteps < 3800 and ch == 7:
      life = life - 1
      ch = 8
    elif totalsteps >= 3800 and totalsteps < 3900 and ch == 8:
      life = life - 1
      ch = 9
    elif totalsteps >= 3900 and totalsteps < 4000 and ch == 9:
      life = life - 1
      ch = 10

donated = 0
def castle_menu():
  global money
  global castlem
  global name
  global rare
  global donated
  global herbs
  global inventory
  if castlem == False and lore == True:
    donated = 0
    castlem = True
    print('---------')
    print(f'𖤐𖤐𖤐𖤐⸸ - I SHALL BE BACK - I AM NOT DONE WITH YOU {name} ⸸𖤐𖤐𖤐𖤐')
    time.sleep(1)
    print('curse lifted')
    time.sleep(1)
    print('Your are left infornt of a castle. Gray bricks. No windows. No Flags.')
    time.sleep(2)
    print(' As you enter the castle you notice a letter, left outside')
    time.sleep(2)
    print('odd it it is familiar writing')
    time.sleep(2)
    print(' you approach and pick it up')
    time.sleep(1)
    print('---------')
    print("My dear traveller, \n If you receive this letter then I must be dead, which is… unfortunate. \n I hope this letter find you well and alive, and I hope your journey is going well. I think it is time I explained everything to you. \n You are Genesis. Well, not current you, past you. You see, the kind traveller who helped me when I was a beggar, was a much younger version of you. \n As younger you grew your ragwort empire, you became power-hungry and an alcoholic. One day you tried to overpower the wrong wizard,\n and part of you became stuck, and the other part of you lost your memory. \n That is why I have, well had, constantly asked you about any headaches or hallucinations, I was worried you would remember the past you. \n Now, onto Genesis, or past you. They’re stuck at the same age with the same mindset, able to move forward in time, but unable to develop any new feelings or thoughts, like sympathy. \n I’m not sure when the Devil joined a pact with Genesis, but both gained immeasurable power. \n So now you know, I understand if you hate me now for hiding the truth, but I’ve watched you develop patience and kindness, and I didn’t want you to return to your old ways. \n I’m rushing writing this letter because I know the Devil is after me for helping you, I don’t know how long I have left. \n Carry on, courageous traveller. Don’t give up. I believe in you. \n Kind regards, \n Your merchant, The Importer.")
    done = input('press any key to continue: ')
    print('Letter Read - he left me 10 coins (all he had)')
    print('---------')
    time.sleep(2)
    print('You must get revenge. Begin prepartions')
    money = money + 10
  print(' Donate current items to prepare for the revenge ')
  print(' Will donate all you have except 10 coins ')
  print(' each herb worth 1 coin. each spell worth 3 coins. each rare worth 5 coins.')
  print(f' REQUIRED COINS DONATED: {donated} 120')
  print(' Q to leave ')
  donateq = input('press D to donate: ')
  if donateq in ['d','D', 'donate'] and money >=11:
    donatedmoney = money
    donatedmoney = donatedmoney - 10
    money = 10
    donatedherbs = 1 * len(herbs)
    herbs = []
    donateditems = 3 * len(inventory)
    inventory = []
    donatedrares = 5 * len(rare)
    rare = []
    donated = donatedmoney + donatedherbs + donateditems + donatedrares
    print('---------')
    print(f'donated {donatedmoney} money. donated {donatedherbs} worth. donated {donateditems} worth. donated {donatedrares} worth')
    print('---------')
  else:
    print('unable to donate')
    
    

def take_action():
  global life
  global companion
  global Merchmax
  global level
  global cheat
  global hunger
  global DEVIL
  global castle
  i = 0
  while i == 0:
    check_merchant()
    check_level()
    check_alive()
    check_totals()
    check_auto()
    check_curse()
    print('----------')
    if DEVIL == True:
      print('𖤐𖤐𖤐𖤐⸸ - CURSED - ⸸𖤐𖤐𖤐𖤐')
      
    if cheat == True:
      print('used custom stats')
    print(f'herbs: {herbs} inventory: {inventory} rares: {rare}')
    print(f'life: {life} money: {money} charm: {charm} totalsteps: {totalsteps} level: {level} protection: {protect} hours: {hours} ')
    print('----------')
    if companion == True:
      print(' c ( companion ) ')
      if hunger == 1:
        print('feed your companion, it will die soon')
    if Merchmax == True:
      print(' s ( summon merchant ) ')
    if level >= 6 and DEVIL == False and castle == False:
      print(' bu ( bundles )')
    if level >= 7:
      print(' ca ( casino )')
    if castle == True:
      print(' d/cas ( castle )')
    action = str(input('take action : f ( forage ) b ( brew )  m ( move ) u ( use ) h ( help ): '))
      
    # if action == 'f' or 'b' or 'c' or 'forage' or 'brew' or 'cast':
    #   print('input valid, proceed')
    if action in [ 'f','forage']:
      forage_herb()
    elif action in ['b', 'brew']:
      brew_spell()
    elif action in ['m', 'move']:
      move_around()
    elif action in ['h', 'help']:
      help_menu()
    elif action in ['bu', 'bundles'] and level >= 6 and DEVIL == False and castle == False:
      get_bundles()
    elif action in ['ca', 'casino'] and level >= 7:
      play_casino()
    elif action in ['c', 'companion'] and companion == True:
      companion_menu()
    elif action in ['s', 'merchant', 'summon merchant']  and Merchmax == True:
      meet_merchant()
    elif action in ['d', 'cas', 'castle'] and castle == True:
      castle_menu()
      
    elif action == 'quit':
      sure = input('are you sure you wish to quit? y/n: ')
      if sure == 'y':
        print('commiting suicide.....')
        life = 0
      else:
        take_action()
    elif action in ['u', 'use']:
      use_item()
    else:
      print('Not valid, retry')


# CASINO 

def play_casino():
  global money
  global name
  global totalsteps
  global life
  roll1 = 0
  roll2 = 0
  roll3 = 0
  wins = 0
  print(f'Welcome to the realm royale casino {name}')
  print(f'you have {wins} wins')
  print(f' money: {money} - cost of roll: 4 coins')
  if DEVIL == True:
    print('DEVIL DEAL match 3,2,1 - for -1 life and + 50 coins')
  play = input('do you wish to play? y/n: ')
  if play == 'y' and money >= 4:
    money = money - 4
    print('-----------------rolling-----------------')
    time.sleep(2)
    roll1 = random.randint(1,3)
    print('-----------------------------------------')
    print(f'--------------------{roll1}--------------------')
    print('-----------------------------------------')
    time.sleep(2)
    roll2 = random.randint(1,3)
    print(f'--------------------{roll2}--------------------')
    print('-----------------------------------------')
    time.sleep(3)
    roll3 = random.randint(1,3)
    print(f'--------------------{roll3}--------------------')
    print('-----------------------------------------')
    if roll1 == roll2 and roll2 == roll3 and roll3 == 1:
      rewardspell = random.choice(potions)
      inventory.append(rewardspell)
      inventory.append(rewardspell)
      inventory.append(rewardspell)
      wins = wins + 1
      print(f'matched 1s - granted 3 {rewardspell} spells')
      take_action()
    elif roll1 == roll2 and roll2 == roll3 and roll3 == 2:
      print('matched 2s - granted 3 rares')
      rare.append('gold')
      rare.append('medal')
      rare.append('gold')
      wins = wins + 1
    elif roll1 == roll2 and roll2 == roll3 and roll3 == 3:
      print('matched 3s - granted 20 coins')
      money = money + 20
      wins = wins + 1
    elif roll1 == 1 and roll2 == 2 and roll3 == 3:
      print('matched 1,2,3 - granted 10 coins')
      money = money + 10
      wins = wins + 1
    elif roll1 == 3 and roll2 == 2 and roll3 == 1 and DEVIL == True:
      life = life - 1
      money = money + 50
    else:
      print('You lost. Try again?')
      again = input('y/n: ')
      if again == 'y':
        play_casino()
      else:
        take_action()
  else:
    print('cancelled or not enough money')











 # -------------------------
# Main program
# -------------------------
#reset all numbers at start of game
dandelion = False
burdock = False
ragwort = False
pipewort = False
companion = False

herbs = []
inventory = []
rare = []
success = 1
merch = 1
steps = 0
money = 1
totalsteps = 0
level = 1
protect = 0
hunger = 1
ch = 1
find = 0
life = 3
hours = 0
Merchmax = False
DEVIL = False
cheat = False
lore = True
castle = False
castlem = False
charm = 0
ammountbought = 0
forsale = ' '
version = 'v2'
companion_name = ' '
companionf = 0
potions = ['teleport', 'charm', 'heal', 'devildrink', 'protect', 'companion']
herblist = ['dandelion', 'burdock', 'ragwort', 'pipewort', 'holly', 'nettles', 'garlic', 'thyme']
print('Welcome to spellbinder VERSION 2')
print('Game created By Jack Fear \nLore created by Daisy Nelson \nTesters: George Pickles, Andy Fear, Tim Basharan \nSpeed Record Holder: Jacobe Giron')
rarelist = ['gold','trophy','medal']
print(f'Version: {version}')
print('toggle lore off in help')
print('---------------------------------------------------------------')
print('type "custom" to put in custom stats (cheating) ')
name = input('what is your name? ')

if name =='custom':
  cheat = True
  money = int(input('money: '))
  life = int(input('life: '))
  totalsteps = int(input('totalsteps: '))
  protect = int(input('protect: '))
  charm = int(input('charm: '))
  compyn = input('companion? y/n: ')
  if compyn == 'y':
    companion = True
    level = 5
  else:
    companion = False
  name = str(input('name: '))

  
while True:
  take_action()
