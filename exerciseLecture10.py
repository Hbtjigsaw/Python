#This program is going to present translations of colors from portuguese to english 
run = True
colors = {"azul":"blue","amarelo":"yellow","laranja":"orange","vermelho":"red","branco":"white","preto":"black","cinza":"gray","verde":"green"}
print("This program is going to present translations of colors from portuguese to english\n")
while run != False:
    translation = input("input a color in portuguese to verify it's translation to english: ").lower()

    if translation in colors:
        print("The translation to the color",translation,"is:",colors[translation])
    else:
        YN = input("That color is currently not present in the dictionary, would you like to add it? (Y/N): ").lower()
        if YN == "y" or YN == "yes":
            newColor = input("Please enter the translation to the color: ")
            colors[translation] = newColor 
            print("adding color and translation...")
        else:
            run = False
            print("exiting...")
    