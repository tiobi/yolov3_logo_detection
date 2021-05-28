import pandas as pd


PATH = ''
FNAME = 'result.txt'
frameNumber = 0
result_file = open(PATH+FNAME, 'r')

df = pd.DataFrame(
    columns = ['fnumber', 
               'label', 
               'accuracy', 
               'left x', 
               'top y', 
               'width', 
               'height'])

initDetection = False
for line in result_file:
    if "Enter Image Path" in line:
        frameNumber += 1
        initDetection = True

    else:
        if initDetection == False:
            continue
        else:
            lineSplit = line.split()
            label, accuracy = lineSplit[0].replace(':', ''), lineSplit[1].replace('%', '')
            left_x, top_y = lineSplit[3], lineSplit[5]
            width, height = lineSplit[7], lineSplit[9].replace(')', '')
            df = df.append({
                'fnumber': frameNumber,
                'label':label,
                'accuracy':accuracy,
                'left x':left_x,
                'top y':top_y,
                'width':width,
                'height':height}, 
                ignore_index = True)
            
df.to_csv("results.csv", mode = 'w', index = False)