# Mentoring 08/05/21 

## ABAP 

### <Table 만드는 순서>

#### ★ 속성 (유지보수 허용 체크를 했기 때문에 우리가 값을 만질 수 있다. // M.View만들때 유지보수 허용체크를 항상 해야한다.)-> field (Clinet mandt!!)-> 외래키/search help - >ref table / ref field (통화, 단위)[지정해준다.] -> Technical setting (buffer or not / Log /Table size) 

### Activated 하면 끝!

---

금액1 통화1 금액2 통화2 //필드명

​			KRW			USD  //명확하게 하기 위해서 반드시 연결고리를 해준다..

- KRW는 / 100 이 되어서 보여진다. But USD 는 그대로 보여진다.

----

### ABAP3주차 # Data

포인터..

#### 데이터 선언방법

- DATA		Data object 명  	TYPE  	Data Type
- DATA Object명 = VALUE(값)

- A = B 와 MOVE B TO A. 같은 것!

#### Data Object //Table형태와 같음 !

- Single Value 형태
  - 변수 / 필드
  - 포인터는 변수의 위치를 지목한다.
- Structure 형태 (구조체 / Work area)
  - 테이블에 있는 것을 가공하기위해 작업하는 공간
  - 구조체 필드 명시법 '-'로 표시 ex)주문내역-주문번호..
  - 변수(필드)의 집합 , single row 형태
- **★★★Table 형태(인터널테이블)중요!!★★★**
  - Work area 에 담아서 작업을 한다! (즉, 한번의 과정을 거쳐서 값을 도출한다.)
  - 인터널 테이블은 바로 값을 접근해 작업할 수가 없다. 몇 번째 행을 가져와라는 가능! 따라서 구조체에 넣어서 작업을 한다...
  - 구조체의 집합, multi rows 형태 
  - 인터널 테이블(프로그램이 종료되면 사라짐) < > 데이터베이스 테이블(냉장고에 있기 때문에 언제든지 꺼내 쓸 수 있음)
    - 인터널 테이블에서 만들어진 것을 DB 테이블에 넣으면 나중에 다시 꺼내쓸 수 있다.

### Data Type

- Data object를 정의하기 위한 하나의 템플릿이다.

- 타입을 그냥 정의하는 것이기 때문에 메모리 공간을 차지하지 않음

- Global (ABAP Dictionary에서 선언됨, 어느 프로그램이든 갖다 쓸 수 있음) / Local (해당 프로그램에서만 사용가능)

  - 프로그램 내에서 정의한 타입

    - TYPES	(Data Type명)	 TYPE	(Data type) //타입은 메모리에 올라가는 것은 아니다.

  - ABAP Dictionary에서 정의한 타입

    - element, structure, table타입 // ABAP Dictionary에 정의된 3가지 타입

    - ABAP Dictionary에서 생성한 DB Object

    - 통화(CURR, CUKY....)같은 타입들은 딕셔너리내에서 사용하기 위해 만들어진 타입

    - ```
      ABAP Program(Dic에 있는 것을 사용할 수 있음)
      	C, N, D, T, P, I
      DIC (자기가 정의한 것만 사용할 수 있음) //element, domain, table field선언할때...
      	NUMC, CHAR, CUKY, CURR, CLNT
      // 연결고리가 있는 것이 아니라 서로 다른 타입들이다.
      ```

    - View 나 Table도 타입으로 사용할 수 있다.  Classic View(P.V와 D.V 순수하게 Read목적으로 만들어진 뷰)

    - DATA    LS_ZAI     TYPE       ZAI...

    - DATA    LS_ZAI     TYPE     **table of**     ZAI //인터널 테이블 

    - == > DB Object일때 .. 

- **★★★★Data type 에 사용가능 유형★★★★**

  - ABAP Predefined Type (Built-in type) - 기본 타입

    - 문자 C(숫자가 포함되어 있으면 숫자로 인식된다, Alphanemeric Type) / N(Numeric , character 같은 수, 0~9까지숫자표현만 가능) / D(Date, 날짜 타입- 기본: YYYYMMDD) / T(Time, HHMMSS) / STRING(무한대 , 길이 제한 X)
    - 숫자 I(INTEGER, 마이너스 값 허용) / P(소수점 타입)
    - 길이지정이 가능한 타입(MAX) => C, N, P
    - 날짜 세팅을 할 수 있다. 그렇지만 DB에 들어가는 것은 동일한 포맷으로 들어간다.

  - 프로그램 내에서 내가 새로 타입을 만든 것 ABAP Predefined Type을 다시 재정의 ?

    - TYPES	 New_ZAI	 type	ZAI

    - DATA	LS_ZAI      TYPE      NEW_ZAI

      ---

    - TYPES      New_Char         type        C       length 10 

    - DATA      L_Char    TYPE      New_Char

---

### 실습 (se80)

Local Object로 바꿔준다. -> ZAI218R01 (Program 이름)

Type => I / M / 1 Executable program (90%이상)

Save(저장)  +	Check(저울모양) 	=>	Activate	=> 실행 (F8)

'*나 "로  ' 주석 // 전체 라인시 -> * // 중간부터 주석 큰 따옴표

DATA :	LV_CHAR 	TYPE 	C		length	5,

​				LV_NUMC	TYPE	N		length	3.

​						,

​						. => 이런 방식으로 선언

#### LV_CHAR => Naming Rule

- L: 지역변수

- G: 전역변수
- V: 변수
- S: 구조
- T: 인터벌 테이블

DATA: LV_CHAR TYPE C LENGTH 5,
    LV_NUMC TYPE N LENGTH 3.

 LV_CHAR: 'ABCD'.
 MOVE 3 TO LV_NUMC.
 WRITE: LV_CHAR, LV_NUMC.		=> ABCD	003 출력! 

같은 3이지만 '3'으로 해주면 문자로 인식하고, 3으로 쓰면 숫자로 인식

---

# FI Module #1

#### 물류(MM)에서의 흐름 (물류 쪽은 수량과 단가로 / 회계 쪽은 금액들로) =>> 완전한 통합!

1. PR

2. PO => 자재 마스터 * 수량

3. GR(Goods Received) : 입고

4. IV(Invoice)
5. 지급

##### CTS(Correction & Transport System)  왜 이것이  중요한가?

- DEV(개발 수행->단위 테스트->통합테스트) ==> QA:품질관리 (사용사가 직접 테스트) ==>PRD
  - 이렇게 옆으로 넘기는 항목들을 CTS라고 한다!

##### Office 도구와의 호환성 (PDF와도 .. 호환이 된다)

---

##### Process => AS-IS processs, 현행 프로세스 분석 - 담당현업 PI(System and 업무 => Activity)

##### =(SAP)=> 개선사항 도출 => To-Be Process //Process 적 관점

---

### <기준정보>

- FI (계정 마스터, 자산 마스터)
- CO (Profit Center, Cost Center) 
- MM (원부자재 마스터, Vendor 마스터)
- SD (고객 마스터, 가격 마스터)
- PP (제품/반제품 마스터, BOM/ROUTING, W/C:Work Center)
- QM (품질 특성)

---

#### <회계 영역> - 물류/회계 통합 프로세스!

- 보조원장
  - 총계정원장 관리(GL) : 계정과목(COA),  기간, 금액 => 재무제표 (BS, PL, Cash Flow)

    - 재무제표를 만드는 기준이 총계정원장 관리이다 !
    - 조직에 대한 정보도 포함되어 있음. 

  - 매입채무 (AP) : Vendor에 대한 정보 (공급업체에게 줘야하기 때문에), 금액, 지급일자

  - 매출채권 (AR)  : Customer, 수금예정일, 금액

    < SD 모듈을 통해 발생되는 프로세스 >

    - Sales Order => X

    - 출고 =>  매출원가 / 제품

    - Billing => 매출채권 / 제품매출

      ​									부가세

    - 수금 => 현금 / 매출채권

      ===> 모든 계정들은 총계정원장으로...

  - 자산관리 (AA):

    <구매쪽이랑 비슷 - 자산구매>

    - 고정자산(자산 마스터-> 감가상각=국가/세무회계 마다 다를 수 있다, 내용연수, 자산 내용) 

      부가세									/	 미지급금

  - 세무관리 (TX): 부가세 ..

  - 현금관리 (TR) : 현금에 대한 내용들, 계좌(은행, 지점, 계좌번호)

<MM에서 회계적으로 처리되는 것 => 재고자산 (GL Account)>

3. (4/15) GR => 재고자산 / **GR-IR** (결산을 위한 계정, **임시 계정** => 결산 시에 잔액이 있으면 안된다)

4. (5/15) IV => GR - IR / 매입채무

   ​					부가세

   <#case1>

   ​	(4/30 결산) => GR-IR / 미확정 채무  // 확정 채무로 부채로 인식한다.

   ​	(5/1 역분개) 미확정 채무 / GR - IR

   <#case2> 송장처리 먼저 -> IV하는 경우

   ​	(4/30 결산) => 미착 재고자산(자산이 아직 도착하지 않았기 때문에) / GR-IR

   ​	(5/1 역분개) => GR-IR / 미착재고

5.  (지급처리) 매입채무 / 현금	 

----

COA (계정과목표, Chart Of Account) - 자산, 부채-자본, 비용, 수익

- 한 회사에서 사용할 수 있는 COA는 1개 !

Auto Posting (자동전표)

