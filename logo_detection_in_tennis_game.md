# YOLO V3 를 이용한 스포츠 경기의 로고 노출 분석 step-by-step

## 1. Yolomark 학습 데이터 준비

![그림2](https://user-images.githubusercontent.com/63599116/119984036-e71bfe00-bffb-11eb-81d3-1bf1fe57bdad.png)

Yolomark 를 build하고 data/img 경로에 이미지 파일을 저장합니다.

![그림3](https://user-images.githubusercontent.com/63599116/119984038-e84d2b00-bffb-11eb-8d5e-9ddb18ede77e.png)
![그림4](https://user-images.githubusercontent.com/63599116/119984042-e84d2b00-bffb-11eb-9579-35098867a8d1.png)

Data 폴더 안에 있는 obj.data와 obj.names 파일을 수정합니다.
Obj.names 파일에 detection class를 전부 적고, 그 수만큼 obj.data 파일의 classes를 변경합니다.
 

## 2.	Yolomark 학습 데이터 생성

![그림5](https://user-images.githubusercontent.com/63599116/119984044-e8e5c180-bffb-11eb-9db3-299cc13e0be2.png)
![그림6](https://user-images.githubusercontent.com/63599116/119984046-e97e5800-bffb-11eb-8248-2b8076ad3447.png)

yolo_mark.cmd 를 실행해서 학습 데이터를 생성합니다. 
키보드의 숫자키로 object class를 선택하고 사진 안에 object가 있는 부분을 드래그해서 위치를 나타냅니다. 
Data/img 폴더 안에 있는 모든 이미지에 대해 같은 작업을 반복합니다. 

![그림7](https://user-images.githubusercontent.com/63599116/119984048-e97e5800-bffb-11eb-9c70-41fdb8ad5376.png)

Yolomark를 종료하면 data/img 폴더에 각 이미지와 쌍을 이루는 txt 파일이 생성됩니다. 
 
 
## 3.	Yolo v3 학습

![그림8](https://user-images.githubusercontent.com/63599116/119984050-ea16ee80-bffb-11eb-99f3-b6c81217eb5a.png)

Yolomark 단계에서 사용한 obj.data, obj.names, train.txt 파일과 data/img 폴더를 darknet/x64/data폴더로 복사합니다.
Command를 이용해서 다음 명령어를 입력하면 학습이 시작됩니다.
 '''
darknet.exe detector train data\obj.data testcfg\yolov3.cfg data\darknet53.conv.74
 '''
![그림9](https://user-images.githubusercontent.com/63599116/119984052-eaaf8500-bffb-11eb-95df-4134745ff8b7.png)

학습이 완료되면 backup 폴더에 weight 파일이 저장되있는 것을 확인할 수 있습니다.
 
 
## 4.	Object detection
# For Windows

![그림10](https://user-images.githubusercontent.com/63599116/119984054-eaaf8500-bffb-11eb-80ae-28728a7f1d2e.png)

 Windows Command에서 Darknet.exe가 있는 경로로 들어가 명령어를 입력합니다. 
 
명령어 리스트 : 

사진데이터 객체 감지: 
'''
darknet.exe detector test {weights 파일 경로} {data 파일 경로} {cfg 파일 경로} -ext_output {입력 파일}
'''
영상 데이터 객체 감지: 
'''
darknet.exe detector demo {weights 파일 경로} {data 파일 경로} {cfg 파일 경로} -ext_output {입력파일}
'''
![그림11](https://user-images.githubusercontent.com/63599116/119984057-eb481b80-bffb-11eb-82bb-37c87099a95f.png)
![그림12](https://user-images.githubusercontent.com/63599116/119984059-eb481b80-bffb-11eb-984b-138dbeda0baf.png)

명령어를 입력하면 두 화면이 나옵니다. 
 
# For Linux (windows subsystem을 이용해 terminal환경에서 ubuntu를 구동했습니다.)

![그림13](https://user-images.githubusercontent.com/63599116/119984061-ebe0b200-bffb-11eb-9e3d-a8ea197868e8.png)
Windows와 동일한 방법으로 진행합니다. 

## 5.	Detection 파일 저장
* 현재 linux에서만 가능합니다.
* 
![그림14](https://user-images.githubusercontent.com/63599116/119984063-ebe0b200-bffb-11eb-97c8-47ffc1b60996.png)

Linux command를 입력한 후 > 기호를 입력해서 standard output을 txt 파일로 저장합니다.
저장된 파일은 아래와 같습니다. 
 
![그림15](https://user-images.githubusercontent.com/63599116/119984498-6e697180-bffc-11eb-82a1-cd6dedc76e24.png)


위 파일은 git폴더 내의 result.txt 파일과 동일합니다.
