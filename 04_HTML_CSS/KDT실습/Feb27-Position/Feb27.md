coding style guide html
기술 업계 독성말투

CSS Layout
Position, Floats, Flexbox, Display

## CSS Position
Normal Flow(좌측상단?)에서 요소를 끄집어내서 다른 위치로 배치하는 것
- Normal flow
CSS를 적용하지 않았을 경우에 웹페이지 요소가 기본적으로 배치되는 방향

### How?
다른 요소 위에 놓기, 화면 특정 위치에 고정시키기 등

Position 이동 방향 : 4가지 방향 + Z축 방향
Z축은 모니터(x와 y축으로 이루어진 평면)에 앞에 있는 우리 얼굴로 쏘는 방향
****
Position 유형
기본 위치
상대 위치 : relative는 집을 나간애가 아니기때문에 normal flow를 깨지 않음. 다른 상자가 위로 딸려오지 않음. 이게 절대 위치와 다른 점.
절대 위치 :부모(relative)를 찾아서 간다. normal flow를 다 깨버림. 집나간 자식. 기존 위치를 버리고 새로운 기준(새로운 부모:static이 아닌, relative인 부모)를 찾으러 간다. -> 상자가 4개에서 3개로 줄어든다.(개발자도구로 확인 가능) 
고정 위치
끈끈이
