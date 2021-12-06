import numpy as np
import random
from PIL import Image

def main_loop():
    rarity_array = []
    # asks user how many images they want to make
    while True:
        try:
            loop_counter = int(input('How many images would you like to generate?: '))
            break
        except ValueError:
            print('wrong input...')

    # main loop
    for i in range(0, loop_counter):
        


        # image data to list
        def file_to_array(): # turns image_data file into a list
            file = open('image_data.txt', 'r')
            data = [line.strip('\n')[:-1].split(',') if line[-2] == "," else line.strip('\n').split(',') for line in file.readlines()]
            file.close()

            rarity(data)
            return data



        # rarity generator
        def rarity(data): # generates rarity for image
            number = random.randint(1, 1000)
            
            if number >= 1 and number <= 500: # 50% chance of getting this rarity
                rarity = 'common'
                common(data, rarity)
                return rarity
            
            elif number >= 500 and number <= 750: # 25% chance of getting this rarity
                rarity = 'uncommon'
                uncommon(data, rarity)
                return rarity

            elif number >= 750 and number <= 850: # 10% chance of getting this rarity
                rarity = 'rare'
                rare(data, rarity)
                return rarity

            elif number >= 850 and number <= 900: # 5% chance of getting this rarity
                rarity = 'covert'
                covert(data, rarity)
                return rarity

            elif number >= 950 and number <= 960: # 1% chance of getting this rarity
                rarity = 'legendary'
                main_colors = 'red'
                legendary_r(data, rarity)
                return rarity

            elif number >= 960 and number <= 970: # 1% chance of getting this rarity
                rarity = 'legendary'
                main_colors = 'green'
                legendary_g(data, rarity)
                return rarity

            elif number >= 970 and number <= 980: # 1% chance of getting this rarity
                rarity = 'legendary'
                main_colors = 'blue'
                legendary_b(data, rarity)
                return rarity

            elif number == 999: # 0.1% chance of getting this rarity
                rarity = 'classified'
                main_colors = 'black'
                classified_blk(data, rarity)
                return rarity

            elif number == 1000: # 0.1% chance of getting this rarity
                rarity = 'classified'
                main_colors = 'white'
                classified_wht(data, rarity)
                return rarity



        # color generator
        def common(data, rarity):
            PF = [0,0,0] 
            EW = [255,255,255]
            EC = [random.randint(0, 250),random.randint(0, 250),random.randint(0, 250)]
            BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
            OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
            BG = [250,249,213]
            BK = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
            return PF, EW, EC, BC, OT, BG, BK

        def uncommon(data, rarity):
            PF = [0,0,0] 
            EW = [0,0,0]
            EC = [random.randint(0, 250),random.randint(0, 250),random.randint(0, 250)]
            BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
            OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
            BG = [250,249,213]
            BK = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
            return PF, EW, EC, BC, OT, BG, BK

        def rare(data, rarity): # later on this will get complementary colors...
            eyeWhiteColors = [255,0]
            eyeWhite = random.choice(eyeWhiteColors)
            PF = [0,0,0] 
            EW = [eyeWhite,eyeWhite,eyeWhite]
            EC = [random.randint(0, 250),random.randint(0, 250),random.randint(0, 250)]
            BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
            OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
            BG = [250,249,213]
            BK = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
            return PF, EW, EC, BC, OT, BG, BK

        def covert(data, rarity): # still need to decide how the colors will look here...
            pass

        def legendary_r(data, rarity):
            eyeWhiteColors = [255,0]
            eyeWhite = random.choice(eyeWhiteColors)
            PF = [0,0,0] 
            EW = [eyeWhite,eyeWhite,eyeWhite]
            EC = [random.randint(50, 255),0,0]
            BC = [random.randint(50, 255),0,0]
            OT = [random.randint(100, 250),0,0]
            BG = [random.randint(1, 255),0,0]
            BK = [random.randint(50, 255),0,0]

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
            return PF, EW, EC, BC, OT, BG, BK

        def legendary_g(data, rarity):
            eyeWhiteColors = [255,0]
            eyeWhite = random.choice(eyeWhiteColors)
            PF = [0,0,0] 
            EW = [eyeWhite,eyeWhite,eyeWhite]
            EC = [0,random.randint(50, 255),0]
            BC = [0,random.randint(50, 255),0]
            OT = [0,random.randint(100, 255),0]
            BG = [0,random.randint(1, 255),0]
            BK = [0,random.randint(50, 255),0]

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
            return PF, EW, EC, BC, OT, BG, BK

        def legendary_b(data, rarity):
            eyeWhiteColors = [255,0]
            eyeWhite = random.choice(eyeWhiteColors)
            PF = [0,0,0] 
            EW = [eyeWhite,eyeWhite,eyeWhite]
            EC = [0,0,random.randint(50, 255)]
            BC = [0,0,random.randint(50, 255)]
            OT = [0,0,random.randint(100, 250)]
            BG = [0,0,random.randint(1, 255)]
            BK = [0,0,random.randint(50, 255)]

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
            return PF, EW, EC, BC, OT, BG, BK

        def classified_blk(data, rarity):
            PF = [0,0,0] 
            EW = [255,255,255]
            ECr = random.randint(0, 150)
            EC = [ECr,ECr,ECr]
            BCr = random.randint(0, 150)
            BC = [BCr,BCr,BCr]
            OT = [0,0,0]
            BG = [250,249,213]
            BKr = random.randint(0,150)
            BK = [BKr,BKr,BKr]

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
            return PF, EW, EC, BC, OT, BG, BK

        def classified_wht(data, rarity):
            PF = [0,0,0] 
            EW = [255,255,255]
            ECr = random.randint(150, 255)
            EC = [ECr,ECr,ECr]
            BCr = random.randint(150, 255)
            BC = [BCr,BCr,BCr]
            OT = [255,255,255]
            BG = [28,28,28]
            BKr = random.randint(150,255)
            BK = [BKr,BKr,BKr]

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
            return PF, EW, EC, BC, OT, BG, BK



        # img generator
        def img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK):        
            RGB_data = []

            # makes a new array replacing the letters with the generated RGB colors
            for j in range(30):
                for k in range(30):
                    if data[j][k] == 'PF':
                        RGB_data.append(PF)
                    elif data[j][k] == 'EW':
                        RGB_data.append(EW)
                    elif data[j][k] == 'EC':
                        RGB_data.append(EC)
                    elif data[j][k] == 'BC':
                        RGB_data.append(BC)
                    elif data[j][k] == 'OT':
                        RGB_data.append(OT)
                    elif data[j][k] == 'BG':
                        RGB_data.append(BG)
                    elif data[j][k] == 'BK':
                        RGB_data.append(BK)

 
            # print(i+1, rarity)
            # new dimensions for image
            dimensions = 480, 480 

            # array handling with numpy
            RGB_data = np.array(RGB_data, dtype=np.uint8)
            RGB_data = RGB_data.reshape(30,30,3)
            
            # using PIL to turn the RGB values into an image
            img_data = Image.fromarray(RGB_data, 'RGB')
            img_data = img_data.resize(dimensions, resample=0)
            img_data.save(f'duck-{i+1}.png')
            # img_data.show()

            rarity_array.append(i+1)
            rarity_array.append(rarity)

        file_to_array()

    rarity_display(rarity_array)



def rarity_display(rarity_array):
    common = 0
    uncommon = 0
    rare = 0
    legendary = 0
    classified = 0

    for i in range(len(rarity_array)):
        if rarity_array[i] == 'common':
            common += 1
        elif rarity_array[i] == 'uncommon':
            uncommon += 1
        elif rarity_array[i] == 'rare':
            rare += 1
        elif rarity_array[i] == 'legendary':
            legendary += 1
        elif rarity_array[i] == 'classified':
            classified += 1

    print(f'common: {common}\nuncommon: {uncommon}\nrare: {rare}\nlegendary: {legendary}\nclassified: {classified}\n')


    
if __name__ == '__main__':
    main_loop()
    