# 차량 동역학 60일 코스 — Week 6: 모드해석·Simpack

> 🎧 이 문서는 운전 중 청취용 오디오 강의 대본입니다.
> 주제: 고유치, 모드중첩, Simpack 매핑/구현

## 이번 주 강의 목차

- **Day 26**: 고유치 문제 (~6.9분)
- **Day 27**: 모드 중첩법 (~6.6분)
- **Day 28**: Part 4 복습 (~8.2분)
- **Day 29**: 수식 → Simpack 완전 매핑 (~7.9분)
- **Day 30**: Quarter Car → Simpack 구현 검증 (~6.9분)
- **합계**: 약 36분

---

## Day 26 — 고유치 문제

### 인트로

차량 동역학 60일 코스, 26일차 강의입니다.
Part 4: 주파수 해석, 오늘의 주제는 '고유치 문제' 입니다.

### 핵심 개념

왜 이 수식이 필요한가?

💡 수식 유도 읽는 법 — 각 STEP의 파란색 라벨은 "왜 이 변환을 하는가"를 설명합니다. 수식만 보지 말고 동기 화살표, 즉 변환 화살표, 즉 의미 순서로 읽으세요. 눈으로 3번 읽는 것보다 손으로 1번 쓰는 것이 기억에 4배 효과적입니다.

다자유도(MDOF) 시스템은 자유도 수만큼의 고유진동수와 모드 형상을 가진다. 고유치 문제는 &#x27;외력 없이 스스로 진동할 수 있는 주파수와 그때의 변형 패턴&#x27;을 찾는 것이다. 차체 모달 해석에서 bending, torsion 모드를 찾는 것이 바로 이 고유치 문제를 푸는 것이다.

Diagram A — 물리계 도해

[M]
질량 행렬

[K]
강성 행렬

det=0

오메가₁², 오메가₂², ... 오메가ₙ²
고유진동수
φ₁, φ₂, ... φₙ
모드 형상

det([K] − 오메가²[M]) = 0

### 수식 유도

이제 오늘의 핵심 수식을 단계별로 살펴보겠습니다.

수식 한 줄씩 유도

Step 1: 자유진동 가정

x(t)=φ⋅ei오메가t화살표, 즉[K]φ⋅ei오메가t=오메가2[M]φ⋅ei오메가t{x(t)} = {\varphi} \cdot e^{i\omegat} \rightarrow [K]{\varphi}\cdot e^{i\omegat} = \omega^2[M]{\varphi}\cdot e^{i\omegat}x(t)=φ⋅ei오메가t화살표, 즉[K]φ⋅ei오메가t=오메가2[M]φ⋅ei오메가t

이 항의 의미: 조화 자유진동 x = φ·e^{i오메가t}를 운동방정식 [M]{ẍ}+[K]{x}={0}에 대입하면, 시간 항이 소거되고 진폭 벡터 {φ}에 대한 대수 방정식이 남는다.
부호/변환 이유: ẍ = −오메가²x이므로 [M]의 부호가 뒤집혀 [K] = 오메가²[M] 형태가 된다.
이전 단계와의 연결: Day 01의 1DOF 자유진동 질량 m·ẍ + 강성 k·x = 0 화살표, 즉 오메가² = 강성 k/m의 MDOF 일반화다.
감소

Step 2: 일반화된 고유치 문제

[K−오메가2M]φ=0화살표, 즉det⁡[K−오메가2M]=0[K - \omega^2M]{\varphi} = {0} \rightarrow \det [K - \omega^2M] = 0[K−오메가2M]φ=0화살표, 즉det[K−오메가2M]=0

이 항의 의미: 비자명 해(φ ≠ 0)가 존재하려면 행렬 [K−오메가²M]의 행렬식이 0이어야 한다.
이 조건이 특성 방정식이며, n차 다항식의 근이 n개 고유진동수를 준다.
부호/변환 이유: 오메가² 0 (양수) 화살표, 즉 진동 모드.
오메가² = 0 화살표, 즉 강체 모드(구속 조건 부족).
오메가² 0 화살표, 즉 좌굴(불안정).

### 핵심 파라미터

오늘 강의에서 기억해야 할 주요 변수와 수치입니다.
수식 파라미터 완전 해부
명칭 (한/영)
물리적 의미
전형적 범위
고유진동수 / Natural Frequency
라디안 퍼 세컨드
자유진동 각주파수
모달 해석 결과
모드 형상 / Mode Shape
정규화된 변형 패턴

### 심화 학습

💡 MAC 매트릭스: 시험과 시뮬레이션을 연결하는 열쇠 — 클릭하여 펼치기
MAC(Modal Assurance Criterion)은 두 모드 벡터의 코사인 유사도다: MAC_ij = |{φ_A_i}ᵀ{φ_B_j}|² / ({φ_A_i}ᵀ{φ_A_i})({φ_B_j}ᵀ{φ_B_j}). MAC = 1이면 완전 일치, 0이면 직교. 실무에서 Simpack 모델을 실차 해머링 데이터와 비교할 때 MAC 매트릭스를 작성하여 각 모드의 일치도를 평가한다. 대각 성분이 0.9 이상이면 모델이 신뢰할 수 있다고 판단한다.
💡 s-plane 해석법 — 복소 고유치 읽기
■ 복소 고유치: s = σ ± j오메가d
σ (실수부): 감쇠율 화살표, 즉 |σ| 클수록 빨리 감쇠
오메가d (허수부): 감쇠 진동 주파수 화살표, 즉 fd = 오메가d/(2파이)

### 실차 적용 사례

🚗 레퍼런스 차량 쿼터카 고유치 (s-plane)
s = −4.12 ± j6.91
fd = 1.10 헤르츠, 제타, 즉 감쇠비 = 0.51
s = −28.5 ± j67.2
fd = 10.7 헤르츠, 제타, 즉 감쇠비 = 0.39

### 시뮬레이션 실습 가이드

Simpack 입력 매핑
Day 26 파라미터 입력 가이드
Body + Joint + Force 정의
시간영역/주파수영역 선택
Analysis Eigenvalue

### 복습 퀴즈

오늘 배운 내용을 점검해보겠습니다.

### 마무리

이상으로 26일차 '고유치 문제' 강의를 마칩니다.
다음 27일차 강의에서 이어집니다. 운전 조심하세요.

---

## Day 27 — 모드 중첩법

### 인트로

차량 동역학 60일 코스, 27일차 강의입니다.
Part 4: 주파수 해석, 오늘의 주제는 '모드 중첩법' 입니다.

### 핵심 개념

왜 이 수식이 필요한가?

💡 수식 유도 읽는 법 — 각 STEP의 파란색 라벨은 "왜 이 변환을 하는가"를 설명합니다. 수식만 보지 말고 동기 화살표, 즉 변환 화살표, 즉 의미 순서로 읽으세요. 눈으로 3번 읽는 것보다 손으로 1번 쓰는 것이 기억에 4배 효과적입니다.

MDOF 강제진동을 직접 풀려면 n×n 연립미분방정식을 풀어야 한다. 모드 중첩법은 &#x27;모드 좌표 변환&#x27;으로 이를 n개의 독립 1DOF 문제로 분해한다. 각 1DOF를 풀고 다시 합치면 원래 응답이 된다. 계산 효율이 비약적으로 좋아지고, &#x27;어떤 모드가 응답에 지배적인가&#x27;를 직관적으로 파악할 수 있다.

Diagram A — 물리계 도해

{x}
물리 좌표
N-DOF coupled

[Φ]

{η}
모드 좌표
N × 1-DOF

Σ

x(t)
응답 합성

{x} = [Φ]{η} 화살표, 즉 비연성 SDOF 합

### 수식 유도

이제 오늘의 핵심 수식을 단계별로 살펴보겠습니다.

수식 한 줄씩 유도

Step 1: 모달 좌표 변환

x=[Φ]q,[Φ]=[φ1φ2⋅⋅⋅φn]{x} = [Φ]{q}, [Φ] = [{\varphi_1} {\varphi_2} \cdot \cdot \cdot {\varphi_n}]x=[Φ]q,[Φ]=[φ1​φ2​⋅⋅⋅φn​]

이 항의 의미: 물리 좌표 {x}를 모드 형상 매트릭스 [Φ]와 모달 좌표 {q}의 곱으로 표현한다.
q_i는 i번째 모드의 &#x27;참여 정도(진폭)&#x27;를 나타낸다.
부호/변환 이유: [Φ]는 n×n 정방 매트릭스.
각 열이 하나의 모드 형상 벡터.
이전 단계와의 연결: Day 26에서 구한 고유벡터 {φ_i}들을 열로 배열한 것이 [Φ]이다.
감소

Step 2: 디커플된 모달 방정식

질량 m~i⋅q¨i+감쇠계수 c~i⋅q˙i+강성 k~i⋅qi=f~i(t)질량 m̃_i \cdot q̈_i + 감쇠계수 c̃_i \cdot q̇_i + 강성 k̃_i \cdot q_i = f̃_i(t)질량 m~i​⋅q¨​i​+감쇠계수 c~i​⋅q˙​i​+강성 k~i​⋅qi​=f~​i​(t)

이 항의 의미: 모드 형상의 직교성 덕분에 각 모달 좌표 q_i는 독립적인 1DOF 방정식을 따른다.
질량 m̃_i = {φ_i}ᵀ[M]{φ_i}가 모달 질량이다.
부호/변환 이유: f̃_i = {φ_i}ᵀ{외력 F of t}는 모달 힘.

### 핵심 파라미터

오늘 강의에서 기억해야 할 주요 변수와 수치입니다.
수식 파라미터 완전 해부
명칭 (한/영)
물리적 의미
전형적 범위
모달 좌표 / Modal Coordinate
각 모드의 참여 진폭
모드 중첩 중간 결과
질량 m̃_i
모달 질량 / Modal Mass
{φ_i}ᵀ[M]{φ_i}

### 심화 학습

💡 Craig-Bampton 방법: 유연체 모델의 핵심 — 클릭하여 펼치기
Simpack에서 유연 차체(flex body)를 사용할 때 Craig-Bampton 방법이 적용된다. 이 방법은 (1) 경계 자유도(마운트 포인트)의 정적 모드와 (2) 고정 경계 내부의 동적 모드를 합성한다. FE 모델에서 수만 자유도를 수십 개의 모드로 축소하여 MBD 해석에 사용한다. OEM에서는 NASTRAN 화살표, 즉 Craig-Bampton 화살표, 즉 Simpack fbi 파일 workflow가 표준이다.
💡 Craig-Bampton 방법 — Simpack 유연체의 핵심
■ Craig-Bampton (CB) 축소법
구조물의 DOF를 대폭 줄이면서 동적 특성 보존
경계 DOF(인터페이스) + 내부 모드(고정경계 모드) 조합

### 실차 적용 사례

🚗 레퍼런스 차량 모드 중첩 적용
쿼터카 2DOF 모드 참여율:
1차 모드(바운스, 1.3Hz): 참여율 92% — 지배적!
2차 모드(휠홉, 11Hz): 참여율 8% — 고주파 미세 기여
화살표, 즉 승차감 분석에서 1차 모드만으로도 90%+ 정확도!

### 시뮬레이션 실습 가이드

Simpack 입력 매핑
Day 27 파라미터 입력 가이드
Body + Joint + Force 정의
시간영역/주파수영역 선택
Analysis Modal Reduction

### 복습 퀴즈

오늘 배운 내용을 점검해보겠습니다.
문제 1: 모드중첩법에서 핵심 개념 확인

### 마무리

이상으로 27일차 '모드 중첩법' 강의를 마칩니다.
다음 28일차 강의에서 이어집니다. 운전 조심하세요.

---

## Day 28 — Part 4 복습

### 인트로

차량 동역학 60일 코스, 28일차 강의입니다.
Part 4: 주파수 해석, 오늘의 주제는 'Part 4 복습' 입니다.

### 핵심 개념

왜 이 수식이 필요한가?

💡 수식 유도 읽는 법 — 각 STEP의 파란색 라벨은 "왜 이 변환을 하는가"를 설명합니다. 수식만 보지 말고 동기 화살표, 즉 변환 화살표, 즉 의미 순서로 읽으세요. 눈으로 3번 읽는 것보다 손으로 1번 쓰는 것이 기억에 4배 효과적입니다.

PART 4에서 배운 주파수 영역 도구들은 하나의 분석 파이프라인을 형성한다. FFT(시간화살표, 즉주파수 변환) 화살표, 즉 PSD(에너지 밀도) 화살표, 즉 FRF(시스템 특성) 화살표, 즉 고유치(고유 특성) 화살표, 즉 모드 중첩(효율적 응답 계산). 이 파이프라인은 PART 5에서 Simpack 디지털 트윈을 구축할 때 시험-해석 상관의 핵심 도구가 된다.

Diagram A — 물리계 도해

FFT
Day 23

PSD
Day 24

FRF
Day 25

고유치
Day 26

모드중첩
Day 27
PART 4 주파수 해석 파이프라인

### 수식 유도

이제 오늘의 핵심 수식을 단계별로 살펴보겠습니다.

수식 한 줄씩 유도

Step 1: 시간화살표, 즉주파수 변환 도구 체계

x(t)화살표, 즉[FFT]화살표, 즉X(f)화살표, 즉[∣⋅∣2/T]화살표, 즉Sxx(f)화살표, 즉[루트∫S df]화살표, 즉xRMSx(t) \rightarrow [FFT]\rightarrow X(f) \rightarrow [|\cdot |^2/T]\rightarrow S_xx(f) \rightarrow [루트\intSdf]\rightarrow x_RMSx(t)화살표, 즉[FFT]화살표, 즉X(f)화살표, 즉[∣⋅∣2/T]화살표, 즉Sx​x(f)화살표, 즉[루트∫S df]화살표, 즉xR​MS

이 항의 의미: 시간 신호를 FFT로 변환하고, PSD로 에너지 밀도를 구하고, 적분하면 RMS — 이것이 기본 분석 체인이다.
부호/변환 이유: 각 단계에서 정보가 추가되거나 압축된다.
FFT는 정보 보존, PSD는 위상 정보 제거(파워만 유지).
이전 단계와의 연결: Day 23(FFT) 화살표, 즉 Day 24(PSD) 순서로 학습했다.
감소

Step 2: 시스템 특성 추출 체계

FRF:H1=Sxf/Sff화살표, 즉∣H∣peaks화살표, 즉오메가n,제타, 즉 감쇠비FRF: H_1 = S_xf/S_ff \rightarrow |H| peaks \rightarrow \omega_n, \zetaFRF:H1​=Sx​f/Sf​f화살표, 즉∣H∣peaks화살표, 즉오메가n​,제타, 즉 감쇠비

이 항의 의미: 입출력 데이터에서 FRF를 구하면, 피크 주파수가 고유진동수, 반치폭이 감쇠비를 제공한다.
부호/변환 이유: 이 과정을 EMA(Experimental Modal Analysis)라 하며, 시험-해석 상관의 기준이 된다.
이전 단계와의 연결: Day 25(FRF·코히어런스) 화살표, 즉 Day 26(고유치)의 실험적 대응이다.
감소

Step 3: 응답 예측 체계

Sresponse(f)=∣H(f)∣2⋅Sinput(f)S_response(f) = |H(f)|^2 \cdot S_input(f)Sr​esponse(f)=∣H(f)∣2⋅Si​nput(f)

이 항의 의미: 입력 PSD와 FRF²의 곱으로 출력 PSD를 예측할 수 있다.

### 핵심 파라미터

오늘 강의에서 기억해야 할 주요 변수와 수치입니다.
수식 파라미터 완전 해부
명칭 (한/영)
물리적 의미
전형적 범위
Pipeline
분석 파이프라인 / Analysis Pipeline
FFT화살표, 즉PSD화살표, 즉FRF화살표, 즉모달
표준 분석 절차
실험 모달 해석 / Experimental Modal Analysis
시험에서 모드 추출

### 심화 학습

💡 Python 한 줄 코드: scipy.signal로 PSD/FRF 구하기 — 클릭하여 펼치기
from scipy.signal import welch, csd; f, Sxx = welch(x, fs=1024, nperseg=2048); f, Sxf = csd(x, force, fs=1024, nperseg=2048); f, Sff = welch(force, fs=1024, nperseg=2048); H1 = Sxf / Sff; gamma2 = np.abs(Sxf)**2 / (Sxx * Sff). 이 5줄이면 PSD, FRF, 코히어런스를 모두 구할 수 있다. Simpack 출력을 CSV로 내보내서 이 코드로 검증하는 습관을 기르자.
💡 주파수 영역 해석 워크플로 — 한눈에 보기
1️⃣ 시간 데이터 x(t) 화살표, 즉 FFT 화살표, 즉 X(f): 스펙트럼
2️⃣ X(f) 화살표, 즉 PSD: S_xx(f) = |X(f)|²/T: 에너지 밀도
3️⃣ 입출력 비교 화살표, 즉 FRF: H(f) = Y(f)/X(f): 시스템 특성

### 실차 적용 사례

🚗 레퍼런스 차량 주파수 영역 해석 체인
S_road(f) [ISO B] × |H_seat(f)|² 화살표, 즉 S_seat(f) 화살표, 즉 a_w = 루트∫W²·S df
이 체인으로 설계 변경 전후 승차감을 빠르게 예측 가능!

### 시뮬레이션 실습 가이드

Simpack 입력 매핑
Day 28 파라미터 입력 가이드
Body + Joint + Force 정의
시간영역/주파수영역 선택
Post-Processing Full Pipeline

### 복습 퀴즈

오늘 배운 내용을 점검해보겠습니다.
문제 1: Part4복습에서 핵심 개념 확인

### 마무리

이상으로 28일차 'Part 4 복습' 강의를 마칩니다.
다음 29일차 강의에서 이어집니다. 운전 조심하세요.

---

## Day 29 — 수식 → Simpack 완전 매핑

### 인트로

차량 동역학 60일 코스, 29일차 강의입니다.
Part 5: Simpack 실습, 오늘의 주제는 '수식 → Simpack 완전 매핑' 입니다.

### 핵심 개념

왜 이 수식이 필요한가?

💡 수식 유도 읽는 법 — 각 STEP의 파란색 라벨은 "왜 이 변환을 하는가"를 설명합니다. 수식만 보지 말고 동기 화살표, 즉 변환 화살표, 즉 의미 순서로 읽으세요. 눈으로 3번 읽는 것보다 손으로 1번 쓰는 것이 기억에 4배 효과적입니다.

지난 28일간 배운 수식에는 질량(질량 m), 강성(강성 k), 감쇠(감쇠계수 c), 고유진동수(오메가ₙ), 감쇠비(제타, 즉 감쇠비) 등이 등장했습니다. 이 기호들이 Simpack의 어떤 요소(Element), 어떤 입력 필드에 대응하는지 명확히 정리하면 — &#x27;이론에서 시뮬레이션까지 빈틈 없는 다리&#x27;가 완성됩니다. Body 화살표, 즉 mass/inertia, Force Element 화살표, 즉 spring damper, Joint 화살표, 즉 DOF constraint, Marker 화살표, 즉 attachment point의 4계층 구조입니다.

Diagram A — 물리계 도해

Body (질량 m, I)

Force Element (강성 k, 감쇠계수 c)

Joint (DOF)

Marker (x,y,z,ψ,θ,φ)

Simpack GUI
mass = 400 킬로그램
k_lin = 22000 N/질량 m
Prismatic (z)
Position + Orient

### 수식 유도

이제 오늘의 핵심 수식을 단계별로 살펴보겠습니다.

수식 한 줄씩 유도

Body 요소 매핑: 질량 m, I 화살표, 즉 Simpack Body

SimpackBodyElement:mass=질량 m[킬로그램],Ixx/Iyy/Izz=Jxx/Jyy/Jzz[킬로그램⋅m2]Simpack Body Element: mass = 질량 m [킬로그램], Ixx/Iyy/Izz = Jxx/Jyy/Jzz [킬로그램\cdot 질량 m^2]SimpackBodyElement:mass=질량 m[킬로그램],Ixx/Iyy/Izz=Jxx/Jyy/Jzz[킬로그램⋅m2]

이 항의 의미: 수식의 질량 m과 관성모멘트 I가 Simpack의 Body Element 속성에 직접 입력됩니다.
Sprung mass 화살표, 즉 Body_Chassis, Unsprung mass 화살표, 즉 Body_Knuckle.
부호/변환 이유: 좌표계 방향: Simpack은 SAE J670(x=전방, z=하방) 또는 ISO(z=상방) 선택 가능.
부호 실수 주의.
이전 단계와의 연결: Day 01 뉴턴 제2법칙 mẍ = ΣF에서 m이 바로 이 Body mass입니다.
감소

Force Element 매핑: 강성 k, 감쇠계수 c 화살표, 즉 Spring/Damper

SpringFE:klin=강성 k[N/질량 m],preload=F0[N]DamperFE:clin=감쇠계수 c[N⋅s/질량 m]또는 비선형F−vLookupTableSpring FE: k_lin = 강성 k [N/질량 m], preload = F_0 [N]
Damper FE: c_lin = 감쇠계수 c [N\cdot s/질량 m] \text{또는 비선형} F-v Lookup TableSpringFE:kl​in=강성 k[N/질량 m],preload=F0​[N]DamperFE:cl​in=감쇠계수 c[N⋅s/질량 m]또는 비선형F−vLookupTable

이 항의 의미: 수식의 강성 k와 감쇠계수 c가 Simpack의 Force Element(Spring/Damper)에 매핑됩니다.
선형이면 단일 값, 비선형이면 Lookup Table을 사용합니다.
부호/변환 이유: F = -kx - cẋ에서 부호: Simpack은 &#x27;양의 변위 화살표, 즉 음의 복원력&#x27; 자동 처리.

### 핵심 파라미터

오늘 강의에서 기억해야 할 주요 변수와 수치입니다.
수식 파라미터 완전 해부
스프렁 매스
350-500
언스프렁 매스
휠+너클 질량
스프링 강성
서스펜션 스프링
N/질량 m
15,000-30,000
댐퍼 감쇠력

### 심화 학습

💡 실무 함정: 단위 변환 좌표계 — 클릭하여 펼치기
상세 콘텐츠가 여기에 추가됩니다.
💡 Simpack 좌표계 규약 — 흔한 실수 방지
■ Simpack 전역 좌표계
X = 전방(주행방향), Y = 좌측, Z = 상방 (ISO 기준)
■ 흔한 실수 #1: Marker 방향 오류

### 실차 적용 사례

🚗 레퍼런스 차량 수식화살표, 즉Simpack 매핑 테이블
mₛ 화살표, 즉 Body > Mass = 340 킬로그램
kₛ 화살표, 즉 Force Element > Spring > Stiffness = 22 N/밀리미터
감쇠계수 c 화살표, 즉 Force Element > Damper > F-v Table
kₜ 화살표, 즉 Tire > Vertical Stiffness = 220 N/밀리미터

### 시뮬레이션 실습 가이드

Simpack 입력 매핑
Simpack 파라미터 매핑
Sprung Mass 화살표, 즉 Body.mass
Unsprung Mass 화살표, 즉 Wheel.mass
Spring 화살표, 즉 Force Element

### 복습 퀴즈

오늘 배운 내용을 점검해보겠습니다.
문제 1: 수식Simpack매핑에서 핵심 개념 확인

### 마무리

이상으로 29일차 '수식 → Simpack 완전 매핑' 강의를 마칩니다.
다음 30일차 강의에서 이어집니다. 운전 조심하세요.

---

## Day 30 — Quarter Car → Simpack 구현 검증

### 인트로

차량 동역학 60일 코스, 30일차 강의입니다.
Part 5: Simpack 실습, 오늘의 주제는 'Quarter Car → Simpack 구현 검증' 입니다.

### 핵심 개념

왜 이 수식이 필요한가?

💡 수식 유도 읽는 법 — 각 STEP의 파란색 라벨은 "왜 이 변환을 하는가"를 설명합니다. 수식만 보지 말고 동기 화살표, 즉 변환 화살표, 즉 의미 순서로 읽으세요. 눈으로 3번 읽는 것보다 손으로 1번 쓰는 것이 기억에 4배 효과적입니다.

Day 03에서 유도한 2-DOF Quarter Car의 고유진동수 오메가₁, 오메가₂와 감쇠비 제타, 즉 감쇠비를 이론값으로 기억하고 있습니다. 이제 Simpack에서 같은 파라미터로 모델을 만들고 고유치 해석(Eigenvalue Analysis)을 돌리면 — 이론값과 시뮬레이션 값이 일치해야 합니다. 이 일치 확인이 바로 &#x27;모델 검증(Verification)&#x27;입니다.

### 수식 유도

이제 오늘의 핵심 수식을 단계별로 살펴보겠습니다.

수식 한 줄씩 유도

Step 1: Simpack 모델 구축 절차

①Body2개(sprung,unsprung)화살표, 즉②Joint2개(prismaticz)화살표, 즉③FE3개(ks,cs,kt)화살표, 즉④Marker연결화살표, 즉⑤Roadinput정의① Body 2\text{개}(sprung, unsprung) \rightarrow ② Joint 2\text{개}(prismatic z) \rightarrow ③ FE 3\text{개}(k_s, c_s, k_t) \rightarrow ④ Marker \text{연결} \rightarrow ⑤ Road input \text{정의}①Body2개(sprung,unsprung)화살표, 즉②Joint2개(prismaticz)화살표, 즉③FE3개(ks​,cs​,kt​)화살표, 즉④Marker연결화살표, 즉⑤Roadinput정의

이 항의 의미: Simpack에서 Quarter Car를 구현하는 5단계 순서입니다.
Body 화살표, 즉 Joint 화살표, 즉 Force Element 화살표, 즉 Marker 화살표, 즉 Excitation의 순서가 가장 효율적입니다.
부호/변환 이유: Road input은 Road Surface Element로 정의하며, step input(단턱), sine sweep, random road(ISO 8608) 등을 선택합니다.
이전 단계와의 연결: Day 29에서 정리한 수식↔Simpack 매핑이 여기서 실제로 적용됩니다.
감소

Step 2: 이론 고유진동수 계산 (복습)

det⁡([K]−오메가2[M])=0화살표, 즉오메가1약ks/ms약1 1.
5Hz(bounce),오메가2약kt/mu약10 15Hz(wheelhop)\det ([K] - \omega^2[M]) = 0 \rightarrow \omega_1 \approx \sqrt{k_s/m_s} \approx 1~1.
5 헤르츠 (bounce), \omega_2 \approx \sqrt{k_t/m_u} \approx 10~15 헤르츠 (wheel hop)det([K]−오메가2[M])=0화살표, 즉오메가1​약ks​/ms​
​약1 1.
5Hz(bounce),오메가2​약kt​/mu​
​약10 15Hz(wheelhop)

이 항의 의미: 이론에서 2-DOF 시스템의 고유진동수를 구하는 방법입니다.

### 핵심 파라미터

오늘 강의에서 기억해야 할 주요 변수와 수치입니다.
수식 파라미터 완전 해부
스프렁 고유진동수
차체 바운스
1.0-1.5
언스프렁 고유진동수
제타, 즉 감쇠비
진동 감쇠 정도
0.2-0.4
m_u/m_s
0.08-0.15

### 심화 학습

💡 검증 실패 시 디버깅 체크리스트 — 클릭하여 펼치기
상세 콘텐츠가 여기에 추가됩니다.
💡 모델 검증 체크리스트 — 5단계
■ 1단계: Static Equilibrium
스프링 힘 = 중력? 변위가 이론값(mg/강성 k)과 일치?
■ 2단계: Eigenvalue

### 실차 적용 사례

🚗 레퍼런스 차량 쿼터카 Simpack 검증 결과
f_bounce = 1.28 헤르츠
f_hop = 11.1 헤르츠
f_bounce = 1.30 헤르츠
f_hop = 11.3 헤르츠

### 시뮬레이션 실습 가이드

Simpack 입력 매핑
Simpack 파라미터 매핑
Quarter Car Model 화살표, 즉 Subsystem
Road Input 화살표, 즉 Excitation
Sensor 화살표, 즉 Output

### 복습 퀴즈

오늘 배운 내용을 점검해보겠습니다.
문제 1: QuarterCar구현에서 핵심 개념 확인

### 마무리

이상으로 30일차 'Quarter Car → Simpack 구현 검증' 강의를 마칩니다.
다음 31일차 강의에서 이어집니다. 운전 조심하세요.

---
