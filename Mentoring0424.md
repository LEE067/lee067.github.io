### SAP GUI

- Tcode - > S000:  기본으로 가는 티코드
- System - user profile 사용자 설정 바꿀 수 있음
  - parameters 에 parameter ID 넣어서 매개변수 값 해놓으면 사용자가 세팅해놓은 값을 자동으로 가져온다.
- SE11 에서 테이블 조회.. -> F8하면 조회..
  - setting - user parameter
    =ALV Grid 는 엑셀형식 에서 Ctrl + Y하면 영역 선택 가능(드래그)

- SE80 프로그램 개발 .. 



# MM(구매) Overview

**Material** **Management**

**Procurement	** (조달)  => 주업무..

	-  외부조달
	-  내부조달(생산)
	-  내/외부 혼용

-------



### 설계서

- FS(Functional Spec) - 설계

- TS(Technical Spec) - 개발

-----

#### 영업 - 구매 - 생산

​        		｜   

​		공급업체(벤더)

**BOM **  *Bill of Material*

Pushing  : 본사에서 정해서 대리점에 분배..

Pulling  : 대리점에서 요청하는 수만큼 본사에서..



**MTO** : Make to Order 

**MTS** : Make to Stock



# MRP (Material Resource Planning)

- MRP 자동..으로 돌려서 .. 구매팀이.. 소요량 구할 수 있다. MRP가 알아서 해준다.

- 외부조달용 - **PR(구매요청) PR에는 자재, 수량 , 납품요청일**(이 때까지 해줘~), 
  - Delivery Time 업체가 우리한테 보내주는 시간
  - GR Time : (우리한테 들어왔을 때 입고검사 / 품질검사) 내부적으로 입고 됐을 때 우리가 실질적으로 쓸 수 있는 기간  - Day based..
- PO -> GR -> IV (입고된 만큼 공급업체에게 돈 지급 / 돈을 지불해야한다는 문서 생성됨) -> FI (대금 지급 / 실제로 돈을 지불)구
- SAP는 PO, GR, IV가 구매 한 세트
- PO 에는 단가,  공급업체(벤더)가 추가적으로 있어야 한다.
- 벤더 컨택하는 것이 구매 업무..
- 구매팀 평가하는 것이 납품적기율 (얼마나 기한을 잘 맞췄나), 얼마나 단가를 맞췄나가 중요

### MM에서 기본정보(영업 - 구매 - 생산 - 기본 - 회계 )

- 자재마스터의 속성은 대략 200개 정도 ..  
  - 기본적 : (단위 , 자재명, 무게 ...등등)
- 자재마스터를 정확하게 알아야 문제없이 돌아간다 ....
- 단가도 마스터 중 하나 .. (**구매 정보 레코드**) - 어느 벤더의 어느 자재의 단가가 관리되는 것..
- 소스 리스트(구매에서의 소스는 공급업체)  - 하나의 자재를 조달할 수 있는 벤더 리스트

------------

--------

--------

# ABAP -  조해선 멘토님(Part 2)

### [[복습]]

#### Search help ? F4를 눌렀을 때(Possible entry, Input help) , 내가 입력할 수 있는 Entry 가 나오는 것

- Input help 방법 중 하나가 Search help 이다.

#### SPRO? Configuration하는 것이다. 현업이 사용할 수 있도록 .. SPRO화면에서 컨이 하는 것.

#### SAP Server ? DEV, QAS, PRD 서버가 3개 .

#### CTS 는 데이터를 이관해주는 툴이고, CTS No.단위로 서버간 이동이 이루어진다.	

#### SAP를 구현하는 방법

​	<모듈>	

1. Configuration 2. Personalization 

​	<개발>

3. Enhancement 4. Modification 5. Development

#### SAP Navigation

- /nex, /n, /o, /h - 디버깅할 때

#### Client

서버에...

- Client dependent : DATA (내가 접속한 클라이언트에서만 데이터가 보인다.)
- Client Independent  : 개발 Obj (전체에서 다 보인다. )

----

### ABAP Dictionary? - SE11 ///SE80 (ABAP Programming)

#### [구성] 

- Database object
  - Database Table(물리적으로 저장되는 공간), View(가상의 Table)
- Type Definition
  - Element, Structure, Table Type
- ABAP Tool
  - Search Help(F4), Lock Object

#### Database Object

- Table : 데이터가 실제로 저장
- View : Table 조합으로 만들어진.. 가상 테이블 / 실제 수정, 삭제 X

- Type : Char, Numc, INT ....

#### Table in ABAP Dictionary => Transparent Table (실제 데이터가 들어가있는 테이블)

- pooled / Cluster Table  (옛날 구버전... ECC or 더 과거..)  // 여러개의 테이블을 조합된 테이블이다.

#### View in ABAP Dictionary (4가지)

- Projection View 
- Database View
- **Maintenance View** // 하나의 프로그램이다라고 생각, Table 입력, 수정 , 삭제 가능
- Help View : Search Help 만들 때 사용한다.

#### Type Definition(3가지)

- **Element** : Single value / 변수 / Table -Field
- **Structure** : Multi Value / 구조체/ Single value 의 집합  
  - /// element 와 structure는 Table 과 View 를 정의할 때 사용
- Table Type : ABAP Program - Internal Table

#### ABAP Tool

- Search Help : 항상 테이블이나 뷰(Help View) 기준으로 만든다.

- Lock Object : 테이블의 락을 제어 / 테이블 수정 제어 , Function으로 Lock 을 제어한다. 

  => Lock obj = Function // Lock /unlock(Enqueue / Dequeue)  .... data가 수정될 때 p1이 수정하면 다른사람이 수정하지 못하도록 락해주는것...

  - Function : 기능 구현/ 모듈화

#### Table 생성 (이론)

1. Delivery and Maintenance : Maintenance View를 만드려면 유지보수 허용이 돼있어야함

2. Fields : Client Filed 를 반드시 넣어줘야한다! / Key Field 반드시 정의 / Initial value ? /각 필드의 타입 정의  

   ​	=> Direct :  ABAP Dictionary Predefined type (CHAR, NUMC, DATS, TIMS, INT1 , 2, 3....)

   ​	=> **element** 를 연결해서  (Type 정의할 수 있음 ) -> ABAP Dictionary Predefined type 

   ​																					  -> **Domain** (에 있는 데이터 타입 선언가능)

#### Element 의미론적 속성

#### Domain 기술적 속성 - 기술적 셋팅을 할 수 있는...

- 둘다 데이터 타입 정의 가능
- 도메인에다가 입력할 수 있는 값들을 정할 수 있어서 그 정해진 값만 넣을 수 있음 // Fixed value, Value Range // Conversion Routine, 대소문자 구분 설정 // 금액에 마이너스 값을 설정하겠냐 안하겠냐 속성도 ..
  - Conversion Routine? A -> B로 바꿔 ..  //Ex. "ALPHA" 100이 들어오면 앞에 00100으로 보여주고, 00100으로 DB에 들어오면 100으로 컨버젼............. //  컨버젼 루틴의 룰에의해서 바뀌어지는...
- Table의 필드는 테이블에 종속적이지만 엘레멘트와 도메인은 독립적이다.
  - 예를 들어 T1의 Field 5 / T2의 Field 7을 동일한 element로 다양한 필드의 타입정의 할 수 있다.

- Domain이 필드를 정의하기 위한 가장 작은 단위 -> element -> Field
  - 도메인을 char 5 에서 char 7로 바꾸면 그 도메인을 참조하는 엘리먼트도 Char 7로 바뀌고 그 엘리먼트를 참조하는 Field들도 다 바뀐다.....

#### Entry Check (외래키)

- 연결고리를 지어주는 것... 우리가 바라보는 테이블 : "Check Table" , 우리가 사용하는 테이블 : "Foreign Table"
- Search Help(해당 필드에 설정을 하는 것) 를 달 수 있다.
  - Table1 -> Field A -> element(Type을 정의 한 것) - >이 ele은 Domain을 이용해서 type을 정의 
  - 가장 테이블에 근접한(가장 상위에 있는) S.H를 바라본다.

#### Currency / Quantity

- CHAR(**CURR** : 금액, **QUAN**: 수량) => 반드시!! Reference Table/Reference Fields : NUMC(**CUKY**: 통화키, **UNIT**: 단위) //항상 세트로 움직여야 한다.

#### Technical Setting

- Buffer ? (캐시메모리 같은 것...)
  
  - SAP 서버가 있고 가장 하위에 DB/  SAP에 Buffer , SAP GUI, => 3tier 구조
  
  - 프로그램 실행 (GUI) => SQL돌아서 DB로 => 다시 GUI에,,,
  
  - 비슷한 실행 결과가 버퍼에 있으면 바로 가져올 수 있다. 디비에서 찾는 것보다  훨씬 빠르게 ..
  
    

#### Table Naming Rule 

- ZAI2_ _ (ID번호)T (Table) / R(Report)/ E(Element) / D (Domin) 01, 02....

#### Field 

- MANDT , CLNT(CHAR 3) 
  - TABLE이름은 똑같으면 안되지만 FIELD이름은 같아도 된다.

#### Field Label : 숏이냐 미디엄ㅇ이냐 롱이냐 .. 동적효과 => 엘레먼트에 의미부여

#### Data type : domain (기술적 속성 부여)/ Built - in type

#### Domain -> Definition

	-  CASE - SENSITIVE ; 대소문자 구분할거냐 .. // CHAR로 데이터 타입을 하면..
	-  Sign :  금액에 마이너스 값을 넣을 것이냐... //CURR 데이터 타입을 하면

- NUMC
  - Value Range => interval : 이 범위값만 넣을 수 있음
  - fixed value고정값

#### Table -> field -> element -> domain 이 순으로 만들고 Activated 는 역순으로.. w

- Active 가 나오면 완전 무결한 상태

#### 마지막에 Define Technical Settings을 한다. // Data class와 size category

#### 