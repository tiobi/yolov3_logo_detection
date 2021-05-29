import pandas as pd

#프레임 데이터 로드
df = pd.read_csv('results.csv')

#라벨 별 프레임 저장 공간
totalFrame = dict()

#프레임 내 중복 카운트 방지 
frameCount = 0


for line in df.iloc:
    #프레임 카운트가 올라갈 때마다 라벨 검사 초기화
    if frameCount != line['fnumber']:
        frameCount = line['fnumber']
        countedInFrame = []
    
    #라벨이 프레임 카운트 공간에 없으면 새로 저장
    if line['label'] not in totalFrame:
        totalFrame[line['label']] = 1
        countedInFrame.append(line['label'])
    
    #라벨이 프레임 카운트 공간에 있고, 같은 프레임에 없으면 저장, 중복 방지
    else:
        if line['label'] not in countedInFrame:
            totalFrame[line['label']] += 1
            countedInFrame.append(line['label'])
            
            
# 1초 = 5프레임(5fps)이라고가정. 실험으로 fps 계산할 필요 있음.
print("Total Video Length is : ", frameCount/5, "secounds\n")
for label in totalFrame:
    print(label, " : ",totalFrame[label]/5, "seconds")
