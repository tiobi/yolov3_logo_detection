# YOLO v3를 이용한 스포츠 경기의 로고 노출 분석

## 1. YOLO v3 소개 및 학습과정

### 1. 1. Yolo 소개

YOLO: Real-Time Object Detection (pjreddie.com)
Yolo는 기존 Object Detection 모델들의 단점을 보완한 모델이다.

https://user-images.githubusercontent.com/63599116/119982142-72e05b00-bff9-11eb-9e99-7395d47ee50c.png

Selective Search에서 많은 Proposal 때문에 detection시간이 오래 걸리는 R-CNN과 다르게, Yolo는 Localization과 Classification 작업을 동시에 진행하기에 Real-time Object Detection이 가능합니다. 
 
Yolo 모델은 여러 사람에 의해 만들어진 다양한 Version이 있지만, 이하 모든 정보는 최초로 Yolo 모델을 만들어낸 사람이 마지막으로 만든 Yolo v3 를 기준으로 작성되었습니다. 이 Version 이후의 Version들은 속도와 정확성이 개선되었지만 Linux 환경에서 작동하도록 기획되었기에 Windows 환경에서 사용하기 쉽지 않습니다.  
 
또한 Yolo는 cuDNN, Visual Studio, Configuration, Environment Variable 등 다양한 환경에서 다른 설정들이 필요하기 때문에 학습과 예측의 대략적인 과정만 나타내도록 하겠습니다.


### 1. 2. YOLO 학습 데이터 생성

Yolo는 학습을 위해 여러 가지의 파일을 생성/변경해야 합니다. 그 중 학습용 이미지 파일과 그 이미지에서 Object의 Label과 Grid를 나타내는 텍스트 파일쌍을 만들어야 합니다. 

https://user-images.githubusercontent.com/63599116/119982145-74118800-bff9-11eb-8bb5-72608ca7105f.png

Yolomark git : https://github.com/AlexeyAB/Yolo_mark
1. Yolo mark프로그램 실행하면 다음과 같은 화면이 나옵니다. 
2. Object가 있는 곳을 드래그 하면 window가 생성이 됩니다. 
3. 키보드의 숫자키를 이용해서 object의 클래스별로 window를 생성합니다.
4.	Window를 생성하면 이미지와 좌표를 연결한 파일이 아래처럼 생성됩니다.

https://user-images.githubusercontent.com/63599116/119982147-74aa1e80-bff9-11eb-8788-3434c740de75.png

yolomark라는 프로그램을 사용하면 학습용 데이터를 용이하게 만들 수 있습니다. 준비한 학습용 이미지를 한 폴더에 저장하고 yolomark를 실행시켜서 나타나는 화면에 object의 label과 grid를 표기하면 학습용 이미지 파일의 이름과 같은 텍스트 파일이 만들어집니다. 

https://user-images.githubusercontent.com/63599116/119982149-74aa1e80-bff9-11eb-9272-d9ada689cc5c.png

텍스트 파일을 열어보면 5개의 숫자가 있는데 각각 
[라벨] [x좌표] [y좌표] [폭] [높이]
를 나타냅니다. 한 이미지에서 여러 Object를 표기하면 여러 줄의 데이터가 생성됩니다. 


### 1. 3. YOLO 모델 학습

Yolomark로 만들어낸 학습 데이터를 yolov3.exe가 있는 폴더의 하위폴더에 저장하고 command로 yolov3.exe를 실행하면, 문제가 없는 한 다음과 같은 화면이 나오면서 학습이 시작됩니다. 
 
1. 학습 데이터를 yolov3.exe가 있는 경로로 복사합니다.

https://user-images.githubusercontent.com/63599116/119982150-7542b500-bff9-11eb-9562-e88c1ef76935.png

왼쪽 화면에 학습되고 있는 모델의 Loss값이 그래프로 나타납니다(예시는 학습 초기이기 때문에 그래프가 나타나지 않았습니다). 오른쪽 화면에 학습의 진행 과정이 나타납니다. 
과적합이 일어나거나 정해진 Batch size만큼 학습이 진행되면 학습을 중단합니다. 
학습 가중치 파일인 .weights 파일이 생성되면 이것을 가지고 예측을 할 수 있습니다. 

https://user-images.githubusercontent.com/63599116/119982151-7542b500-bff9-11eb-852a-f22cdb162ac1.png


### 1. 4. 학습된 가중치를 이용한 오브젝트 검출

https://user-images.githubusercontent.com/63599116/119982153-75db4b80-bff9-11eb-9013-f205eb3858e1.png

Yolov3.exe를 cmd를 이용하여 실행하고 예측할 이미지를 입력하면 다음과 같은 화면이 나오며 이미지 속 Object를 검출할 수 있습니다. 

위 예시는 학습용 데이터가 부족하여 정확하게 Object를 검출하지 못했습니다. 정확한 학습이 이루어지면 Object 주변 Grid가 더 정확하게 나타납니다. 
