__author__ = "Ahmet Onder Onlu"

import random

# Sabit olarak kalacak ve programa 
# dinamiklik sağlayacak değerlerin belirlenmesi.
MAX_LINES = 3
MAX_BET = 100
MİN_BET = 1

ROWS = 3
COLS = 3

# Seçilecek sembollerin sayılarının belirlenmesi.
symbol_counts = {
    "A" : 3,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_values = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def control_winning(columns,lines,bet,values):
    winnings = 0
    winnings_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
        
            if symbol != symbol_to_check:
                break
        
        else:
            winnings += values[symbol]*bet
            winnings_line.append(line+1)
    
    return winnings , winnings_line

#Basılacak slot machine için yaptığımız sözlükten 
# import ettiğimiz random fonksiyonu ile rastgele seçim.
def get_slot_machine_spin(rows,cols,symbols):
    all_symbol = []
    for symbol , symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbol[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

#Bir üstteki fonksiyonda hazırladığımız 3*3'lük
#matrisini transpozunu alıp ekrana basım zamanı.
def print_slot_machine(columns):
    
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            
            if i != (len(columns[0])-1):
                print(column[row], end="|")   
            
            else: 
                print(column[row], end="")   
        
        print()
            
# Depozito miktarının yani yatırılacak
#paranın kullanıcıdan alınması.
def deposit():
    
    while True:
        amount = input("what would like to deposit ? ")
        if amount.isdigit():
            amount = int(amount)
            
            if amount > 0:
               break
             
            else:
                print("Amount must be greater than 0.")
                
        else:
            print("Please enter a number")
    return amount

#Min ve max satırların arasından seçim yapılması.
def get_number_of_lines():
    
    while True:
        lines = input("Please, enter number of lines between 1 - " + str(MAX_LINES) + "? " )
        if lines.isdigit():
            lines = int(lines)
            
            if 1 <= lines <= 3:
               break
             
            else:
                print("Lines must be between 1 - "+ str(MAX_LINES) +"  ?")
                
        else:
            print("Please enter a number")
    return lines

#Her satıra yatırılacak miktarın girilmesi.
def get_bet():
    
    while True:
        amount = input("what would like to bet on each lines ? ")
        if amount.isdigit():
            amount = int(amount)
            
            if 1 <= amount <= 100 :
               break
             
            else:
                print(f"Amount must be between ${MİN_BET} - ${MAX_BET}")     
                           
        else:
            print("Please enter a number")
            
    return amount



# Elindeki bütçen ile oyunu oynayıp oynayamama 
# durumunu kontrol edip yönlendiren fonksiyon.
def spin(balance):
    while True:
        
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You don't have enough to bet that amount , you have totally : ${balance}")
            
            while True :
                flag = input("Would you like to add money to your amount (y-n) ? ")
                
                if flag == "y" :
                    while True:
                        extra = (input('How much do you want to add ? '))
                        if extra.isdigit() :
                            balance = balance + int(extra)
                            break
                        else :
                            print("You must enter a value! ")
                    break
                elif flag == "n":
                    break
                
                else:
                    print("Please, Enter a valid option")
                    continue
            
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines on total : {total_bet} .")
    
    slots = get_slot_machine_spin(ROWS,COLS,symbol_counts)
    print_slot_machine(slots)
    winnings , winning_lines = control_winning(slots,lines,bet,symbol_values)
    print(f"You won ${winnings}. ")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet

#Oyun da döngüselliği sağlayan ve tüm yapıyı
#çalıştırabilen ana fonksiyonumuz
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        track = input("Press enter to play the slot machine(q to quit) ")
    
        if track == "q":
            break
        balance += spin(balance)
        
    print(f"You left with totally ${balance}.")
    
main()