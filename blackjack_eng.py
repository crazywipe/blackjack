"""
Defining lists and dictionary to hold cards value
"""
seme = ["\u2665 Hearths \u2665", "\u2666 Diamonds \u2666", "\u2663 Clubs \u2663", "\u2660 Spades \u2660"]
carta = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
valore_carta = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

"""
Card Class
"""
class Carta:
    def __init__(self, nome, seme):
        self.nome = nome
        self.seme = seme
        self.valore = valore_carta[(self.nome)]
    def __str__(self):
        return  self.nome +' of '+ self.seme

"""
Deck Class
"""
from random import shuffle
class Mazzo:
    def __init__(self):
        self.tutte_le_carte = []
        for sem in seme:
            for car in carta:
                self.tutte_le_carte.append(Carta(car, sem))
    
    """ Deck Shuffle """
    def mischia_mazzo(self):
        shuffle(self.tutte_le_carte)
    
    """ Draw a Card """
    def pesca_carta(self):
        return self.tutte_le_carte.pop(0)

"""
Player's Class
"""
class Giocatore:
    def __init__(self, name):
        self.name = name
        self.carte_possedute = []
        self.bilancio = 1000

    """
    Remove a Card
    """
    def rimuovi_carta(self):
        self.carte_possedute.clear()

    def aggiungi_carte(self, carte):
        if type(carte) == type([]):
            self.carte_possedute.extend(carte)
        else:
            self.carte_possedute.append(carte)

    """
    Print func for hand, score, bankroll
    """
    def __str__(self):
        totale = 0
        print(f'Cards of {self.name.title()} ({len(self.carte_possedute)})')
        for car in self.carte_possedute:
            print(' ', car)
            totale = totale + car.valore
        print(f'  Total Score: {totale_carte(self.carte_possedute)}')
        return f'  Bankroll: {self.bilancio}\n'

    """
    Hidden Dealer Card
    """
    def mano_coperta(self):
        print(f'Dealer Cards ({len(self.carte_possedute)})')
        print(' *Hidden Card*')
        for car in self.carte_possedute[1:]:
            print(' ', car)
        print('  Total Score: ?')
        return f'  Bankroll: {self.bilancio}'

"""
This function return the total int value of the player owned cards, with Ace check. 
"""
def totale_carte(carte):
    totale = 0
    asso = False
    for car in carte:
        if car.nome == 'Ace':
            asso = True
        totale = totale + car.valore

    if not asso:
        return totale
    
    if totale <= 21:
        return totale
        
    return totale - 10

"""Boolean check for boosted hand """
def sballato(carte):
    if totale_carte(carte) > 21:
        return True
    else:
        return False

def gioca_ancora():
    global gioco_attivo
    while True:
        rigioca = input(f' {giocatore.name.title()} Ready to play? (Press "Y" to continue or N" for the main menu) ')
        if rigioca.lower()[0] == 'y':
            gioco_attivo = True
            return True
        elif rigioca.lower()[0] == 'n':
            gioco_attivo = False
            return False
        else:
            print('Error, Please Select Y/N ')
            continue

"""
Update dealer's and player's bankroll balance 
"""
def aggiorna_bilancio(vittoria_giocatore):
    if vittoria_giocatore:
        banco.bilancio = banco.bilancio - puntata
        giocatore.bilancio = giocatore.bilancio + puntata
    else:
        banco.bilancio = banco.bilancio + puntata
        giocatore.bilancio = giocatore.bilancio - puntata

"""
Boolean check for finished chips 
"""

def chips_esaurite(chips):
    if chips == 0:
        return True
    else:
        return False

"""
Takes a correct player bet, if player bankroll > 500: maximum bet allowed is 10% of the bankroll. Else no betting limit. """
def bet(giocatore_chips, banco_chips):
    while True:
        try:
            if giocatore_chips > 500:
                print(f'\nBankroll Player: {giocatore_chips}\nBankroll Dealer: {banco_chips}\nMax Bet: {giocatore_chips // 10}')
                x = int(input('Please, Insert a bet '))
            else:
                print(f'\nBankroll Player: {giocatore_chips}\nBankroll Dealer: {banco_chips}\nMax Bet: {giocatore_chips}\n***Super Bet***')
                x = int(input('Insert a bet '))
        except ValueError:
            print('Sorry, please insert a number')
        else:
            if x > giocatore_chips or x > banco_chips:
                print('\nSorry, the bet is incorrect, Please choose a correct bet...')
            elif x > (giocatore_chips // 10) and (giocatore_chips > 500):
                print(f'\nPlease, max bet allowed: {giocatore.bilancio //10} chips')
            else:
                return x
                break
"""
Draw a card
"""
def pesca():
    while not sballato(giocatore.carte_possedute):
        tira_carta = input(f' \n{giocatore.name.title()}, hit another card? (Y/N) ')
        if tira_carta.lower()[0] == 'y':
            giocatore.aggiungi_carte(mazzo_carte.pesca_carta())
            print('\nI*** Player Draw a Card ***\n')
            print(giocatore)
            print(banco.mano_coperta())
        elif tira_carta.lower()[0] == 'n':
            break
        else:
            print('Please Insert Y/N')


"""
MAIN 
"""
GIOCO_ATTIVO = True

while True:

    gioca = input('***Wellcome to BlackJack by Fabio Rocco***\nAre you ready to start? (Y/N) ')

    if gioca.lower()[0] == 'y':
        GIOCO_ATTIVO = True
    else:
        print('Thanks for playing, Shutting down.')
        break

    """
    Defining player, dealer and deck 
    """
    nome_giocatore = input('Please, insert your name ')
    giocatore = Giocatore(nome_giocatore)
    banco = Giocatore('Dealer')
    mazzo_carte = Mazzo()
    print(f'\n ***GAMES RULES***\n\n{giocatore.name.title()} This are the games rules:\n\n1)Player and Dealer has 1000 chips each (maximum bet is 10 per cent of the owned chips)\n2)Player will be first to talk and he will decide if hit or stand, trying to reach the score of 21 without busting.\n Aces value can be 1 or 11.\n3)If the player decide to stand on a legit hand, it will be the dealer turn to hit a card or stand\n until his score will be at least on par. Pot split in case of draw.\nSpecial Rule: ***Superbet***  For a more fun game, if player chips are < 500,\nit will be possible to go "all in" and bet all the chips on one hand!')

    while GIOCO_ATTIVO:

        """
        Player's and Dealer's cards assignament
        """
        mazzo_carte = Mazzo()
        mazzo_carte.mischia_mazzo()
        giocatore.rimuovi_carta()
        banco.rimuovi_carta()

        if gioca_ancora():
            print('\nGame started, Good Luck!')
            puntata = bet(giocatore.bilancio, banco.bilancio)
            print(f'\n***In this game you are betting {puntata} euro***')

            giocatore.aggiungi_carte(mazzo_carte.pesca_carta())
            giocatore.aggiungi_carte(mazzo_carte.pesca_carta())
            print('+++Dealer gives cards+++: \n')
            print(giocatore)

            banco.aggiungi_carte(mazzo_carte.pesca_carta())
            banco.aggiungi_carte(mazzo_carte.pesca_carta())
            print(banco.mano_coperta())
        else:
            break

        TURNO_BANCO = False
        TURNO_GIOCATORE = True

        """
        Player's Turn
        """
        while TURNO_GIOCATORE:

            pesca()

            if sballato(giocatore.carte_possedute):
                print(f'\n{giocatore.name.title()} Boosted! You lost {puntata} euro')
                aggiorna_bilancio(vittoria_giocatore=False)
                break

            else:
                TURNO_GIOCATORE = False
                TURNO_BANCO = True

        """
        Dealer's Turn 
        """
        while TURNO_BANCO:

            if totale_carte(banco.carte_possedute) > totale_carte(giocatore.carte_possedute):
                print(f'Dealer Won, You lost {puntata} euro\n')
                print(banco)
                aggiorna_bilancio(vittoria_giocatore=False)
                TURNO_BANCO = False
                break

            elif totale_carte(giocatore.carte_possedute) == totale_carte(banco.carte_possedute):
                print(banco)
                print('Game Over, Draw')
                TURNO_BANCO = False
                break

            elif totale_carte(banco.carte_possedute) < totale_carte(giocatore.carte_possedute):
                banco.aggiungi_carte(mazzo_carte.pesca_carta())
                print('\n ***Dealer Hits*** \n ')
                print(giocatore)
                print(banco)
                break
                if sballato(banco.carte_possedute):
                    print(f'Dealer Boosted, You Wonn {puntata} euro!')
                    aggiorna_bilancio(vittoria_giocatore=True)
                    TURNO_BANCO = False
                    break
                elif totale_carte(giocatore.carte_possedute) == totale_carte(banco.carte_possedute):
                    print('Game Over, Draw')
                    TURNO_BANCO = False
                    break
                else:
                    continue

        """
        Check for player's and dealer's chips running out 
        """
        if chips_esaurite(giocatore.bilancio) == True:
            print('\nNo chips left, Dealer Won!\n Thanks for playing, if you wish you can play again.')
            break
        elif chips_esaurite(banco.bilancio) == True:
            print('\nDealer runs out of chips, You Won!\nThanks for playing, if you want you can play again.')
            break
        else:
            pass
