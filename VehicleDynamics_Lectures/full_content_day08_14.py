"""
Day 08~14 상세 콘텐츠 — PART 2: 차량 진동 모델
"""

DAY08 = {
    "day": 8,
    "part": 2,
    "part_title": "차량 진동 모델",
    "title_ko": "쿼터카 모델 구성",
    "title_en": "Quarter-Car Model Setup",
    "filename": "Day08_쿼터카모델.html",
    "hero_eq": "[m_s  0; 0  m_u]{x''} + [c_s  −c_s; −c_s  c_s]{x'} + [k_s  −k_s; −k_s  k_s+k_t]{x} = {0; k_t·z_r}",
    "difficulty": "★★★☆☆",
    "num_formulas": "4단계",
    "brain_strategy": {
        "technique": "물리적 조립(Physical Assembly)",
        "pre_routine": "차량의 앞바퀴 한 쪽만 잘라낸 단면을 상상하세요. 위에 차체(sprung mass), 아래에 휠+너클(unsprung mass), 둘 사이에 스프링+댐퍼, 휠 아래에 타이어 스프링. 총 2개 질량, 3개 연결요소. 이것이 쿼터카입니다.",
    },
    "intuition": (
        "PART 1에서 배운 1DOF는 차량의 한 가지 모드만 설명합니다. 실제 차량은 최소 2DOF가 필요합니다: "
        "차체(sprung mass m_s)와 휠(unsprung mass m_u). 쿼터카 모델은 차량 4개 코너 중 하나를 떼어낸 가장 기본적인 차량 모델입니다. "
        "르노코리아에서 K&C 시험할 때 측정하는 바디 바운스 주파수(~1.2 Hz)와 휠 홉 주파수(~12 Hz)가 "
        "바로 이 2DOF 모델의 두 고유진동수입니다."
    ),
    "deriv_steps": [
        {
            "label": "STEP 1 — 자유물체도(FBD) 그리기",
            "equation": "m_s: 차체 질량 (위쪽)\nm_u: 비스프링 질량 (아래쪽)\nk_s, c_s: 서스펜션 스프링·댐퍼\nk_t: 타이어 강성",
            "explain_meaning": "두 질량을 수직 방향으로 배치. m_s와 m_u 사이에 k_s·c_s 병렬 연결. m_u와 노면 사이에 k_t 연결. 변위: x_s(차체), x_u(휠), z_r(노면입력).",
            "explain_sign": "x_s, x_u 모두 위쪽이 양(+). 스프링력은 상대변위(x_s−x_u)에 비례, 댐퍼력은 상대속도(x_s'−x_u')에 비례.",
            "explain_prev": "Day 01의 1질량 FBD를 2질량으로 확장. 작용·반작용 법칙으로 연결력은 두 질량에 크기 같고 방향 반대.",
        },
        {
            "label": "STEP 2 — 차체(m_s) 운동방정식",
            "equation": "m_s·x_s'' + c_s(x_s'−x_u') + k_s(x_s−x_u) = 0",
            "explain_meaning": "차체에 작용하는 힘: 서스펜션 스프링력(상대변위)과 댐퍼력(상대속도). 외력은 차체에 직접 가해지지 않으므로 우변=0.",
            "explain_sign": "x_s−x_u > 0(서스펜션 늘어남)이면 스프링이 차체를 아래로 당김. 부호가 자연스럽게 맞음.",
            "explain_prev": "Day 01의 mx''+cx'+kx=F(t) 구조. 단, x 대신 상대변위 (x_s−x_u) 사용.",
        },
        {
            "label": "STEP 3 — 휠(m_u) 운동방정식",
            "equation": "m_u·x_u'' − c_s(x_s'−x_u') − k_s(x_s−x_u) + k_t(x_u−z_r) = 0",
            "explain_meaning": "휠에는 위쪽에서 서스펜션 반력(부호 반대), 아래쪽에서 타이어 복원력이 작용. z_r은 노면 프로파일(입력).",
            "explain_sign": "서스펜션 항의 부호가 STEP 2와 반대(작용·반작용). 타이어항 k_t(x_u−z_r): 타이어가 압축되면 위로 미는 힘.",
            "explain_prev": "뉴턴 제3법칙: 차체가 받는 힘의 반작용이 휠에 작용. k_t 항은 타이어 강성(보통 k_s의 5~10배).",
        },
        {
            "label": "STEP 4 — 행렬 형태로 정리",
            "equation": "[M]{x''} + [C]{x'} + [K]{x} = {F}\n[M] = diag(m_s, m_u)\n[K] = [k_s, −k_s; −k_s, k_s+k_t]\n{F} = {0; k_t·z_r}",
            "explain_meaning": "STEP 2, 3을 행렬로 정리. [M]은 대각, [C]와 [K]는 대칭. 이 대칭성은 에너지 보존에서 기인. 외력벡터의 k_t·z_r가 노면 가진입력.",
            "explain_sign": "[K]의 비대각 원소가 −k_s: 두 질량 간 커플링. [K]가 양정치(positive definite) → 시스템 안정.",
            "explain_prev": "1DOF: 스칼라 방정식 → 2DOF: 2×2 행렬 방정식. 이 패턴은 NDOF로 일반화됩니다(Day 08 Deep Dive).",
        },
    ],
    "params": [
        {"sym": "m_s", "name_ko": "스프링상 질량", "name_en": "Sprung Mass", "unit": "kg", "meaning": "서스펜션 위의 차체 질량 (1/4 기준)", "vehicle": "차체 코너 질량", "range": "승용차: 250~400 kg (쿼터카 기준)"},
        {"sym": "m_u", "name_ko": "비스프링 질량", "name_en": "Unsprung Mass", "unit": "kg", "meaning": "서스펜션 아래의 질량 (휠+너클+브레이크)", "vehicle": "휠 어셈블리 질량", "range": "승용차: 30~50 kg"},
        {"sym": "k_s", "name_ko": "서스펜션 강성", "name_en": "Suspension Stiffness", "unit": "N/m", "meaning": "코일 스프링의 수직 방향 등가 강성", "vehicle": "스프링 레이트 (wheel rate 기준)", "range": "15,000~30,000 N/m"},
        {"sym": "k_t", "name_ko": "타이어 강성", "name_en": "Tire Stiffness", "unit": "N/m", "meaning": "타이어의 수직 강성 (공기압에 의존)", "vehicle": "타이어 수직 스프링 레이트", "range": "150,000~250,000 N/m"},
        {"sym": "c_s", "name_ko": "서스펜션 감쇠", "name_en": "Suspension Damping", "unit": "N·s/m", "meaning": "쇼크업소버의 등가 선형 감쇠계수", "vehicle": "댐퍼 감쇠력/피스톤 속도", "range": "1,000~3,000 N·s/m"},
    ],
    "simpack_mappings": [
        {
            "sym": "m_s, m_u (질량 설정)",
            "path": "Bodies → Properties → Mass / Inertia",
            "field": "Mass [kg]",
            "unit": "kg",
            "warn": "쿼터카의 m_s = 전체 차량 질량의 약 1/4. Simpack 풀카 모델에서 코너 질량 확인: 정적 평형 해석 후 각 휠의 수직하중/g."
        },
        {
            "sym": "k_s, c_s, k_t (연결요소)",
            "path": "Force Elements → Spring/Damper/Tire",
            "field": "Stiffness [N/m], Damping [N·s/m]",
            "unit": "N/m, N·s/m",
            "warn": "Simpack에서 k_s는 'wheel rate'(휠 중심 기준 등가 강성)인지 'spring rate'(스프링 자체 강성)인지 구분. 레버비(motion ratio) 변환 필요: k_wheel = k_spring × MR²."
        },
    ],
    "deep_dive_title": "쿼터카 vs 하프카 vs 풀카 — 언제 어떤 모델을 쓰는가?",
    "deep_dive_content": (
        "차량 진동 모델의 복잡도 단계:\n\n"
        "1. 쿼터카 (2DOF): 바운스만. 수직 방향 기본 특성 평가. K&C 상관성 분석에 충분.\n"
        "2. 하프카 (4DOF): 바운스 + 피치. 전후 축 분리 설계에 사용 (Day 10~11).\n"
        "3. 풀카 (7~14DOF): 바운스 + 피치 + 롤 + 4휠. 조종안정성까지 평가. Simpack 표준 모델.\n\n"
        "르노코리아 실무에서:\n"
        "· 초기 컨셉 단계: 쿼터카 → 타겟 주파수/감쇠비 설정\n"
        "· 튜닝 단계: 하프카 → 전후 밸런스(피치 자세) 최적화\n"
        "· 최종 검증: 풀카(Simpack) → 실차 상관성 확인\n\n"
        "쿼터카의 한계: 피치 모션(앞뒤 기울기), 롤 모션(좌우 기울기)을 표현 못함. "
        "하지만 수직 방향 특성의 ~80%를 설명하므로 가장 많이 쓰이는 기본 모델."
    ),
    "quiz": [
        {
            "type": "fill",
            "question": "쿼터카 모델의 강성행렬 [K]에서 (2,2) 원소는?",
            "options": ["A. k_s", "B. k_t", "C. k_s + k_t", "D. −k_s"],
            "correct": 2,
            "feedback_correct": "정답! [K]의 (2,2) 원소 = k_s + k_t. 휠에는 서스펜션과 타이어 강성이 모두 작용.",
            "feedback_wrong": "오답. 정답은 C. 휠(m_u)의 복원력은 위쪽(k_s)과 아래쪽(k_t) 모두에서 오므로 k_s+k_t.",
        },
        {
            "type": "meaning",
            "question": "승용차에서 타이어 강성 k_t가 서스펜션 강성 k_s보다 훨씬 큰 이유는?",
            "options": ["A. 타이어 공기압이 높아서", "B. 접지력 확보를 위해 타이어는 딱딱해야 하므로", "C. 제조 원가 절감", "D. NVH 성능 향상"],
            "correct": 1,
            "feedback_correct": "정답! 타이어는 노면과의 접지를 유지해야 하므로 높은 강성(k_t≈10k_s)이 필요합니다.",
            "feedback_wrong": "오답. 정답은 B. 타이어가 노면에서 뜨면 제동·조향 불능이므로 높은 강성으로 접지력 확보.",
        },
        {
            "type": "simpack",
            "question": "Simpack에서 쿼터카 모델을 만들 때 필요한 최소 Body 수는?",
            "options": ["A. 1개", "B. 2개", "C. 3개", "D. 4개"],
            "correct": 1,
            "feedback_correct": "정답! 2개: Sprung Mass(차체)와 Unsprung Mass(휠). Ground는 고정 참조 프레임.",
            "feedback_wrong": "오답. 정답은 B. 차체(m_s)와 휠(m_u) 2개의 Body가 필요합니다.",
        },
    ],
    "next_preview_title": "Day 09 미리보기",
    "next_preview": "쿼터카의 2개 고유진동수 유도 — 바디 바운스 모드(~1.2 Hz)와 휠 홉 모드(~12 Hz). 고유치 문제 det([K]−ω²[M])=0 풀기.",
}

DAY09 = {
    "day": 9, "part": 2, "part_title": "차량 진동 모델",
    "title_ko": "쿼터카 고유진동수", "title_en": "Quarter-Car Natural Frequencies",
    "filename": "Day09_쿼터카고유진동수.html",
    "hero_eq": "det([K] − ω²[M]) = 0 → ω₁(바디), ω₂(휠)",
    "difficulty": "★★★☆☆", "num_formulas": "4단계",
    "brain_strategy": {
        "technique": "극단적 상상(Extreme Thinking)",
        "pre_routine": "두 극단을 상상하세요. ① k_t→∞(타이어가 강체): 사실상 1DOF, ω≈√(k_s/m_s). ② m_u→0(휠 질량 없음): 역시 1DOF. 현실은 이 두 극단 사이. 2개 고유주파수가 나타나는데, 하나는 차체가 주로 움직이고(바디 바운스), 다른 하나는 휠이 주로 움직입니다(휠 홉).",
    },
    "intuition": (
        "Day 08에서 쿼터카 행렬 방정식을 세웠습니다. 2DOF 시스템은 2개의 고유진동수를 가집니다. "
        "첫 번째(낮은 주파수): 바디 바운스 모드 — 차체가 크게, 휠은 작게 움직임. 약 1~1.5 Hz. "
        "두 번째(높은 주파수): 휠 홉 모드 — 휠이 크게, 차체는 거의 안 움직임. 약 10~15 Hz. "
        "이 두 주파수가 서스펜션 설계의 가장 기본적인 타겟 스펙입니다."
    ),
    "deriv_steps": [
        {
            "label": "STEP 1 — 고유치 문제 설정",
            "equation": "([K] − ω²[M]){φ} = {0}  →  비자명해 조건: det([K] − ω²[M]) = 0",
            "explain_meaning": "자유진동 해를 x={φ}e^(iωt)로 가정하면 행렬 고유치 문제. det=0이 ω²에 대한 특성방정식.",
            "explain_sign": "ω²이 고유값(eigenvalue), {φ}가 모드 형상(eigenvector). 2×2이므로 ω² 2개.",
            "explain_prev": "Day 02의 1DOF: ms²+k=0 → ω²=k/m. 이것의 행렬 버전.",
        },
        {
            "label": "STEP 2 — 4차 특성방정식 전개",
            "equation": "m_s·m_u·ω⁴ − [m_s(k_s+k_t) + m_u·k_s]ω² + k_s·k_t = 0",
            "explain_meaning": "det 전개 후 ω² = λ로 치환하면 λ에 대한 2차 방정식. 근의 공식으로 두 고유진동수의 제곱 λ₁, λ₂를 구함.",
            "explain_sign": "감쇠 c_s=0으로 놓고(비감쇠 고유진동수) 풀음. 두 근 모두 양수 → 안정 시스템.",
            "explain_prev": "Day 08의 [K], [M] 행렬 원소를 대입하여 det를 직접 계산.",
        },
        {
            "label": "STEP 3 — 근사 공식 (m_u ≪ m_s 조건)",
            "equation": "ω₁² ≈ k_s/m_s  (바디 바운스)\nω₂² ≈ (k_s+k_t)/m_u  (휠 홉)",
            "explain_meaning": "m_u/m_s ≈ 0.1로 작으므로 커플링이 약함. 바디 바운스는 거의 1DOF(m_s+k_s), 휠 홉도 거의 1DOF(m_u+k_s+k_t).",
            "explain_sign": "ω₂/ω₁ ≈ √((k_s+k_t)m_s/(k_s·m_u)) ≈ 8~12배. 주파수가 크게 분리되어 있음.",
            "explain_prev": "Day 02: ω_n=√(k/m). 여기서 각 모드를 '독립된 1DOF'처럼 근사한 것.",
        },
        {
            "label": "STEP 4 — 모드 형상 해석",
            "equation": "모드 1: {φ₁} ≈ {1; 1} → 차체·휠 동위상\n모드 2: {φ₂} ≈ {ε; −1} → 차체 거의 정지, 휠만 진동",
            "explain_meaning": "바디 바운스: 차체와 휠이 같은 방향으로 움직이되 차체가 더 큼. 휠 홉: 휠만 크게 진동, 차체는 거의 부동.",
            "explain_sign": "ε ≈ −k_s/(k_s+k_t−m_s·ω₂²) → 0에 가까움. 차체가 '관성 앵커' 역할.",
            "explain_prev": "각 ω²를 ([K]−ω²[M]){φ}=0에 대입하면 모드 형상. 이것이 Simpack Eigenvalue의 Mode Shape.",
        },
    ],
    "params": [
        {"sym": "ω₁", "name_ko": "바디 바운스 주파수", "name_en": "Body Bounce Frequency", "unit": "Hz", "meaning": "차체가 주로 움직이는 1차 모드", "vehicle": "승차감의 기본 주파수", "range": "f₁ = 1.0~1.5 Hz"},
        {"sym": "ω₂", "name_ko": "휠 홉 주파수", "name_en": "Wheel Hop Frequency", "unit": "Hz", "meaning": "휠이 주로 움직이는 2차 모드", "vehicle": "접지력 변동의 주 주파수", "range": "f₂ = 10~15 Hz"},
        {"sym": "{φ}", "name_ko": "모드 형상", "name_en": "Mode Shape", "unit": "무차원", "meaning": "각 모드에서 질량들의 상대적 운동 비율", "vehicle": "바운스/홉 모드 시각화", "range": "정규화된 벡터"},
    ],
    "simpack_mappings": [
        {
            "sym": "ω₁, ω₂ (Eigenvalue 출력)",
            "path": "Results → Eigenvalue Analysis → Eigenfrequencies",
            "field": "Frequency [Hz], Mode Shape",
            "unit": "Hz",
            "warn": "Simpack 풀카 모델에서는 바디 바운스 외에 피치, 롤 모드도 나타남. 모드 형상 애니메이션으로 바운스 모드를 식별하세요."
        },
    ],
    "deep_dive_title": "바디 바운스 주파수 1~1.5 Hz의 의미 — 인체 감각과의 관계",
    "deep_dive_content": (
        "왜 차량 설계자는 바디 바운스를 1~1.5 Hz로 타겟팅할까요?\n\n"
        "인체의 주파수별 민감도:\n"
        "· 0.5~1 Hz: 멀미 유발 대역 (배, 비행기 요동)\n"
        "· 1~2 Hz: 걷기 리듬과 유사 → 자연스러움\n"
        "· 4~8 Hz: 내장기관 공진 → 매우 불쾌\n"
        "· 8~20 Hz: 근골격계 공진 → 피로\n\n"
        "바디 바운스 1~1.5 Hz는 '걷기 리듬'과 비슷하여 인체에 자연스럽습니다. "
        "동시에 4~8 Hz 대역은 이미 서스펜션이 잘 걸러주는 영역(r>1)이 됩니다.\n\n"
        "휠 홉 10~15 Hz는 인체에 직접 전달되면 불쾌하지만, 차체(sprung mass)의 관성으로 "
        "크게 감쇄됩니다. 문제는 접지력 변동: 휠 홉이 심하면 타이어가 노면에서 뜨게 되어 "
        "제동·조향 성능이 저하됩니다."
    ),
    "quiz": [
        {
            "type": "fill",
            "question": "쿼터카의 바디 바운스 주파수 근사값은 ω₁ ≈ √(___/___)?",
            "options": ["A. k_t / m_s", "B. k_s / m_s", "C. k_s / m_u", "D. (k_s+k_t) / m_u"],
            "correct": 1,
            "feedback_correct": "정답! 바디 바운스 ω₁ ≈ √(k_s/m_s). Day 02의 1DOF와 같은 형태!",
            "feedback_wrong": "오답. 정답은 B. 차체 질량 m_s와 서스펜션 강성 k_s가 바디 바운스를 결정.",
        },
        {
            "type": "meaning",
            "question": "휠 홉 주파수가 바디 바운스의 약 10배인 이유는?",
            "options": ["A. 타이어 강성이 매우 높고 휠 질량이 작으므로", "B. 댐퍼가 강하므로", "C. 노면이 거칠므로", "D. 차체가 무거우므로"],
            "correct": 0,
            "feedback_correct": "정답! ω₂≈√((k_s+k_t)/m_u). k_t≈10k_s이고 m_u≈m_s/8이므로 주파수가 ~10배.",
            "feedback_wrong": "오답. 정답은 A. 높은 타이어 강성(k_t≈10k_s) + 작은 휠 질량(m_u≈m_s/8) → 높은 주파수.",
        },
        {
            "type": "simpack",
            "question": "Simpack에서 바디 바운스 모드를 식별하는 방법은?",
            "options": ["A. 가장 낮은 주파수 선택", "B. Mode Shape 애니메이션에서 차체가 주로 움직이는 모드", "C. 감쇠비가 가장 큰 모드", "D. 가장 높은 주파수 선택"],
            "correct": 1,
            "feedback_correct": "정답! Mode Shape 애니메이션을 보고 차체(sprung mass)가 주로 상하 운동하는 모드가 바디 바운스.",
            "feedback_wrong": "오답. 정답은 B. 주파수 순서만으로는 부족. 반드시 Mode Shape으로 물리적 의미 확인.",
        },
    ],
    "next_preview_title": "Day 10 미리보기",
    "next_preview": "하프카 모델 — 바운스+피치 연성. 4DOF 행렬 방정식과 피치 관성모멘트 I_y의 역할. 전후 축 스프링 배분이 피치 거동에 미치는 영향.",
}

DAY10 = {
    "day": 10, "part": 2, "part_title": "차량 진동 모델",
    "title_ko": "하프카 모델 — 바운스+피치", "title_en": "Half-Car Model — Bounce-Pitch Coupling",
    "filename": "Day10_하프카모델.html",
    "hero_eq": "m·z'' + k_f(z−aθ) + k_r(z+bθ) = 0\nI_y·θ'' − a·k_f(z−aθ) + b·k_r(z+bθ) = 0",
    "difficulty": "★★★★☆", "num_formulas": "4단계",
    "brain_strategy": {
        "technique": "신체 감각 기억(Kinesthetic Memory)",
        "pre_routine": "의자에 앉아 눈을 감고, 차가 방지턱을 넘는 상상을 하세요. 앞바퀴가 먼저 올라가면 차체가 '뒤로 기울고(피치 업)', 뒷바퀴가 넘으면 '앞으로 기울(피치 다운)'. 이 앞뒤 기울기가 피치(pitch) 모션이고, 바운스(상하)와 동시에 일어납니다.",
    },
    "intuition": (
        "쿼터카는 수직 방향만 봤습니다. 하프카는 여기에 피치(앞뒤 기울기)를 추가합니다. "
        "차량 측면에서 보면 차체 무게중심(CG)의 상하 운동(z)과 CG를 중심으로 한 회전(θ)이 커플링됩니다. "
        "커플링의 원인: 전후 축 스프링의 위치가 CG에서 떨어져 있으므로(a, b), "
        "스프링력이 동시에 수직력과 모멘트를 만듭니다."
    ),
    "deriv_steps": [
        {
            "label": "STEP 1 — 좌표계 정의",
            "equation": "z: CG의 수직 변위 (바운스)\nθ: CG 중심 피치각 (라디안)\na: CG~전축 거리, b: CG~후축 거리",
            "explain_meaning": "하프카는 2개 자유도: z(바운스)와 θ(피치). 전축 변위 = z − aθ, 후축 변위 = z + bθ (소각도 근사).",
            "explain_sign": "θ>0을 피치 업(앞이 올라감)으로 정의. 전축은 CG 앞에 있으므로 변위가 z−aθ로 줄어듦.",
            "explain_prev": "Day 08의 x_s(수직 변위 1개) → z(수직) + θ(회전) 2개로 확장.",
        },
        {
            "label": "STEP 2 — 바운스(z) 방정식",
            "equation": "m·z'' + (k_f+k_r)z + (−a·k_f+b·k_r)θ = 0",
            "explain_meaning": "전축 스프링력 k_f(z−aθ)와 후축 스프링력 k_r(z+bθ)를 합산. z'' 계수가 m, z 계수가 k_f+k_r, θ 계수가 커플링 항.",
            "explain_sign": "커플링 항 (−a·k_f+b·k_r): a·k_f = b·k_r이면 커플링=0 → 바운스와 피치가 독립(이상적)!",
            "explain_prev": "Day 08의 차체 방정식에서 단일 k_s가 k_f와 k_r로 분리되고 위치(a, b)가 추가.",
        },
        {
            "label": "STEP 3 — 피치(θ) 방정식",
            "equation": "I_y·θ'' + (−a·k_f+b·k_r)z + (a²k_f+b²k_r)θ = 0",
            "explain_meaning": "CG 중심 모멘트 평형. I_y는 피치 관성모멘트. 각 스프링력×레버암을 합산. 커플링 항이 바운스 방정식과 동일.",
            "explain_sign": "a²k_f+b²k_r: 항상 양(+). 거리의 제곱 × 강성이므로 피치 복원 모멘트. I_y가 크면 피치 주파수↓.",
            "explain_prev": "뉴턴 제2법칙의 회전 버전: Σ M = I_y·θ''. 레버 암 a, b가 모멘트를 결정.",
        },
        {
            "label": "STEP 4 — 행렬 형태와 커플링 조건",
            "equation": "[m 0; 0 I_y]{z''; θ''} + [k_f+k_r, −a·k_f+b·k_r; −a·k_f+b·k_r, a²k_f+b²k_r]{z; θ} = 0\n디커플링 조건: a·k_f = b·k_r",
            "explain_meaning": "강성행렬의 비대각 원소 = 바운스-피치 커플링. a·k_f=b·k_r이면 비대각=0 → 바운스와 피치가 완전히 독립.",
            "explain_sign": "디커플링 조건은 '전후 스프링의 모멘트가 균형'을 의미. 실제 차량은 약간의 커플링을 의도적으로 남김.",
            "explain_prev": "Day 08의 2×2 행렬과 같은 구조. 비대각 원소가 물리적 커플링을 나타냄.",
        },
    ],
    "params": [
        {"sym": "I_y", "name_ko": "피치 관성모멘트", "name_en": "Pitch Moment of Inertia", "unit": "kg·m²", "meaning": "피치축(y축) 주위의 회전 관성", "vehicle": "차체의 피치 동적 특성 결정", "range": "승용차: 1500~3000 kg·m²"},
        {"sym": "a, b", "name_ko": "CG~축 거리", "name_en": "CG to Axle Distance", "unit": "m", "meaning": "무게중심에서 전축(a)/후축(b)까지 거리", "vehicle": "축하중 배분 결정 (a:b ≈ 전축하중:후축하중 역비)", "range": "L=a+b≈2.5~2.8 m"},
    ],
    "simpack_mappings": [
        {
            "sym": "I_y (관성모멘트)",
            "path": "Bodies → Sprung Mass → Inertia",
            "field": "Iyy [kg·m²]",
            "unit": "kg·m²",
            "warn": "Simpack에서 Iyy는 차체 CG 기준. K&C 시험에서 관성모멘트를 직접 측정하기 어려우므로, 보통 CAD 데이터 또는 경험식(I_y ≈ 0.3·m·L²)으로 추정."
        },
    ],
    "deep_dive_title": "피치 센터(Pitch Center)와 flat ride 튜닝",
    "deep_dive_content": (
        "바운스-피치 커플링을 제어하는 것이 승차감 튜닝의 핵심입니다.\n\n"
        "Flat Ride 조건: 방지턱을 넘을 때 차체가 수평을 유지하며 상하로만 움직이는 것.\n"
        "이를 위한 조건: 바운스 주파수와 피치 주파수가 비슷하고(f_bounce ≈ f_pitch),\n"
        "전축 주파수가 후축보다 약간 낮아야 합니다(f_front < f_rear × 0.85~0.95).\n\n"
        "이유: 앞바퀴가 방지턱을 먼저 넘고, 차체가 축간거리(L)만큼 이동한 후 뒷바퀴가 넘음.\n"
        "앞의 진동이 시작되고 뒤의 진동이 시작될 때까지의 시간차가 있어,\n"
        "뒷축 주파수가 높으면(빠른 복귀) 두 입력이 상쇄됩니다.\n\n"
        "르노코리아 실무: K&C 바운스 시험에서 전후 축 바운스 주파수를 측정하고,\n"
        "f_r/f_f ≈ 1.1~1.2 범위인지 확인합니다."
    ),
    "quiz": [
        {
            "type": "fill",
            "question": "바운스-피치 디커플링 조건은 a·k_f = ___·___?",
            "options": ["A. a · k_r", "B. b · k_r", "C. b · k_f", "D. L · k_t"],
            "correct": 1,
            "feedback_correct": "정답! a·k_f = b·k_r이면 커플링 항이 0 → 바운스와 피치 독립.",
            "feedback_wrong": "오답. 정답은 B. 전축 모멘트(a·k_f) = 후축 모멘트(b·k_r) → 디커플링.",
        },
        {
            "type": "meaning",
            "question": "Flat ride를 위해 전축과 후축 바운스 주파수의 관계는?",
            "options": ["A. f_f = f_r", "B. f_f > f_r", "C. f_f < f_r", "D. 관계없음"],
            "correct": 2,
            "feedback_correct": "정답! 전축 주파수를 후축보다 낮게 설정(f_f < f_r)하면 flat ride 조건에 유리.",
            "feedback_wrong": "오답. 정답은 C. 전축이 먼저 가진되고 시간차 후 후축이 가진되므로, 뒤가 빠르면(f_r > f_f) 상쇄 효과.",
        },
        {
            "type": "simpack",
            "question": "Simpack에서 피치 모드를 확인할 때 어떤 좌표의 모드 형상을 봐야 하는가?",
            "options": ["A. X축 병진", "B. Y축 회전 (Ry)", "C. Z축 병진", "D. Z축 회전 (Rz)"],
            "correct": 1,
            "feedback_correct": "정답! 피치 = Y축 회전(Ry). Simpack에서 θ_y 성분이 지배적인 모드가 피치 모드.",
            "feedback_wrong": "오답. 정답은 B. 피치는 Y축(차폭 방향 축) 주위의 회전입니다.",
        },
    ],
    "next_preview_title": "Day 11 미리보기",
    "next_preview": "하프카 피치 주파수·모드 분석과 Simpack 검증. 바운스-피치 연성모드 해석, 전후 스프링 배분 최적화.",
}

DAY11 = {
    "day": 11, "part": 2, "part_title": "차량 진동 모델",
    "title_ko": "하프카 모드 해석·Simpack 검증",
    "title_en": "Half-Car Modal Analysis & Simpack Validation",
    "filename": "Day11_하프카모드해석.html",
    "hero_eq": "f_bounce ≈ (1/2π)√((k_f+k_r)/m)\nf_pitch ≈ (1/2π)√((a²k_f+b²k_r)/I_y)",
    "difficulty": "★★★☆☆", "num_formulas": "3단계",
    "brain_strategy": {
        "technique": "시뮬레이션 검증 사이클(Sim-Verify Loop)",
        "pre_routine": "Day 10의 수식으로 계산한 값과 Simpack 결과를 나란히 적어보세요. 차이가 5% 이내면 OK, 10% 이상이면 모델 파라미터를 재확인. 이 '수식↔시뮬레이션 교차검증'이 디지털 트윈의 핵심 루틴입니다.",
    },
    "intuition": (
        "Day 10에서 하프카 행렬을 세웠으니, 오늘은 고유진동수·모드형상을 구하고 Simpack으로 검증합니다. "
        "실무 워크플로우: ① 수식 계산(Excel/Python) → ② Simpack 모델링 → ③ 교차 검증 → ④ 파라미터 조정. "
        "이 Day가 PART 2의 핵심 실습 Day입니다."
    ),
    "deriv_steps": [
        {
            "label": "STEP 1 — 디커플링 근사 (바운스 주파수)",
            "equation": "f_bounce ≈ (1/2π)√((k_f+k_r)/m)",
            "explain_meaning": "커플링이 약할 때(a·k_f ≈ b·k_r) 바운스는 총 스프링 강성을 총 질량으로 나눈 1DOF와 유사.",
            "explain_sign": "k_f+k_r: 전후 스프링의 병렬 합. m = 차체 전체 질량 (하프카이므로 좌우 합산).",
            "explain_prev": "Day 09의 쿼터카 ω₁≈√(k_s/m_s)와 같은 구조. k_s → k_f+k_r, m_s → m.",
        },
        {
            "label": "STEP 2 — 디커플링 근사 (피치 주파수)",
            "equation": "f_pitch ≈ (1/2π)√((a²k_f+b²k_r)/I_y)",
            "explain_meaning": "피치 복원 모멘트(a²k_f+b²k_r)를 피치 관성모멘트(I_y)로 나눈 것. 회전 자유도의 '스프링-질량'이 a²k+I_y.",
            "explain_sign": "a², b² 제곱이 붙는 이유: 모멘트 = 힘 × 레버암, 강성모멘트 = 강성 × 레버암².",
            "explain_prev": "Day 10 STEP 3의 피치 방정식에서 커플링 항을 무시(z=0)하면 이 근사식.",
        },
        {
            "label": "STEP 3 — Simpack 교차 검증 절차",
            "equation": "오차 = |f_수식 − f_Simpack| / f_Simpack × 100%\n허용 범위: < 5% (선형 모델)",
            "explain_meaning": "수식 결과와 Simpack Eigenvalue 결과를 비교. 5% 이내면 모델 정합성 확인. 차이가 크면 파라미터(특히 motion ratio, 부시 강성) 확인.",
            "explain_sign": "Simpack은 비선형 요소를 선형화하여 고유치를 구하므로, 선형 수식과의 차이는 비선형성 정도를 나타냄.",
            "explain_prev": "이 검증 루틴이 디지털 트윈 구축의 기본. Day 30~33에서 전체 모델 검증에 동일한 방법 사용.",
        },
    ],
    "params": [
        {"sym": "f_bounce", "name_ko": "바운스 주파수", "name_en": "Bounce Frequency", "unit": "Hz", "meaning": "차체 상하 운동의 고유주파수", "vehicle": "승차감 기본 지표", "range": "1.0~1.5 Hz"},
        {"sym": "f_pitch", "name_ko": "피치 주파수", "name_en": "Pitch Frequency", "unit": "Hz", "meaning": "차체 전후 기울기의 고유주파수", "vehicle": "피치 자세 제어 지표", "range": "1.2~1.8 Hz (f_pitch ≥ f_bounce)"},
    ],
    "simpack_mappings": [
        {
            "sym": "f_bounce, f_pitch (모드 식별)",
            "path": "Results → Eigenvalue Analysis → Mode Shapes",
            "field": "Z Translation(바운스) vs Ry Rotation(피치) 성분 비교",
            "unit": "Hz",
            "warn": "풀카 모델에서는 바운스와 피치가 연성되어 나타남. 모드 형상의 Z 성분과 Ry 성분 비율로 식별. 순수 바운스/피치가 아닌 연성모드일 수 있음."
        },
    ],
    "deep_dive_title": "Motion Ratio — 스프링 레이트 ≠ 휠 레이트",
    "deep_dive_content": (
        "수식에서 k_f, k_r은 '휠 레이트(wheel rate)'입니다. 실제 스프링 레이트와 다릅니다!\n\n"
        "관계식: k_wheel = k_spring × MR²\n"
        "여기서 MR = Motion Ratio = 스프링 변위 / 휠 변위\n\n"
        "맥퍼슨 스트럿: MR ≈ 0.9~1.0 (거의 1:1)\n"
        "더블 위시본: MR ≈ 0.6~0.8 (레버비 존재)\n"
        "멀티링크: MR ≈ 0.5~0.9 (설계에 따라 다양)\n\n"
        "르노코리아 실무:\n"
        "K&C 시험에서 측정하는 것은 wheel rate. 스프링 업체에 발주할 때는 spring rate.\n"
        "MR은 서스펜션 기구학(Kinematics)에서 결정되며, Simpack K&C 해석으로 구합니다.\n"
        "Day 16~17에서 서스펜션 기구학과 motion ratio를 상세히 다룹니다."
    ),
    "quiz": [
        {
            "type": "fill",
            "question": "피치 주파수 근사식에서 분모에 들어가는 것은?",
            "options": ["A. m (차체 질량)", "B. I_y (피치 관성모멘트)", "C. I_z (요 관성모멘트)", "D. m × L²"],
            "correct": 1,
            "feedback_correct": "정답! f_pitch ≈ (1/2π)√((a²k_f+b²k_r)/I_y). 피치 관성모멘트가 분모.",
            "feedback_wrong": "오답. 정답은 B. 피치 운동의 '질량' 역할을 하는 것이 I_y(피치 관성모멘트).",
        },
        {
            "type": "meaning",
            "question": "wheel rate와 spring rate의 관계에서 Motion Ratio(MR)의 역할은?",
            "options": ["A. k_wheel = k_spring + MR", "B. k_wheel = k_spring × MR²", "C. k_wheel = k_spring / MR", "D. k_wheel = k_spring × MR"],
            "correct": 1,
            "feedback_correct": "정답! k_wheel = k_spring × MR². MR이 제곱으로 들어가는 것이 핵심(에너지 등가 원리).",
            "feedback_wrong": "오답. 정답은 B. 에너지 보존: ½k_w·x² = ½k_s·(MR·x)² → k_w = k_s·MR².",
        },
        {
            "type": "simpack",
            "question": "수식과 Simpack 고유치 결과의 허용 오차 범위는?",
            "options": ["A. < 1%", "B. < 5%", "C. < 20%", "D. < 50%"],
            "correct": 1,
            "feedback_correct": "정답! 선형 모델 기준 5% 이내가 일반적. 비선형 요소가 많으면 10%까지도 허용.",
            "feedback_wrong": "오답. 정답은 B. 5% 이내. 이보다 크면 파라미터 오류(MR, 부시 강성 등)를 의심.",
        },
    ],
    "next_preview_title": "Day 12 미리보기",
    "next_preview": "전달함수(Transfer Function) H(s) 유도. 라플라스 변환으로 운동방정식을 주파수 영역으로 변환. 입력(노면)→출력(차체 가속도) 관계.",
}

DAY12 = {
    "day": 12, "part": 2, "part_title": "차량 진동 모델",
    "title_ko": "전달함수 유도", "title_en": "Transfer Function H(s) Derivation",
    "filename": "Day12_전달함수유도.html",
    "hero_eq": "H(s) = X_s(s)/Z_r(s) = (c_s·s + k_s) / (m_s·s² + c_s·s + k_s)",
    "difficulty": "★★★☆☆", "num_formulas": "3단계",
    "brain_strategy": {
        "technique": "블랙박스 사고(Black-Box Thinking)",
        "pre_routine": "서스펜션을 하나의 '상자'로 생각하세요. 입력: 노면 요철 z_r(t). 출력: 차체 움직임 x_s(t). 전달함수 H(s)는 이 상자의 '성격표'입니다. 어떤 주파수의 입력이 얼마나 증폭/감쇠되어 나오는지를 완전히 기술합니다.",
    },
    "intuition": (
        "Day 05~06에서 '진폭비와 위상각'을 배웠는데, 이를 일반화한 것이 전달함수입니다. "
        "라플라스 변환(s=σ+jω)을 사용하면 미분방정식이 대수 방정식이 되어 다루기 쉬워집니다. "
        "차량 NVH에서 전달함수는 '노면→차체' 경로의 진동 특성을 완전히 기술하는 도구입니다. "
        "Simpack의 FRA(Frequency Response Analysis)가 바로 전달함수를 수치적으로 구하는 것."
    ),
    "deriv_steps": [
        {
            "label": "STEP 1 — 라플라스 변환 적용",
            "equation": "m_s·s²X_s + c_s·s(X_s−X_u) + k_s(X_s−X_u) = 0",
            "explain_meaning": "시간 미분 x'' → s²X(s), x' → sX(s). 초기조건=0 가정(정상상태 분석). 대문자 X_s(s), X_u(s)는 라플라스 변환된 변위.",
            "explain_sign": "s는 복소 주파수. s=jω를 대입하면 Day 05의 주파수 응답과 동일. 라플라스는 더 일반적.",
            "explain_prev": "Day 08의 시간영역 방정식을 주파수(s)영역으로 변환한 것.",
        },
        {
            "label": "STEP 2 — 단순화: 타이어 강체 가정",
            "equation": "X_u ≈ Z_r (k_t → ∞ 근사)\n→ m_s·s²X_s + c_s·s(X_s−Z_r) + k_s(X_s−Z_r) = 0",
            "explain_meaning": "타이어가 매우 딱딱하면(k_t≫k_s) 휠이 노면을 그대로 추종. 쿼터카가 1DOF로 축소. 기본 전달함수 유도에 적합.",
            "explain_sign": "이 근사는 바디 바운스 주파수 영역(~1 Hz)에서 유효. 휠 홉 영역(~12 Hz)에서는 부정확.",
            "explain_prev": "Day 09의 m_u→0 극한과 동일한 단순화. 2DOF→1DOF 축소.",
        },
        {
            "label": "STEP 3 — 전달함수 도출",
            "equation": "H(s) = X_s/Z_r = (c_s·s + k_s) / (m_s·s² + c_s·s + k_s)",
            "explain_meaning": "X_s에 대해 정리하면 전달함수. 분자: 입력(노면)이 스프링·댐퍼를 통해 전달. 분모: 시스템 동특성(관성+감쇠+강성).",
            "explain_sign": "s=jω 대입: |H(jω)| = Day 05의 진폭비와 관계. 분모=0이 되는 s값이 극점(pole) → 고유진동수 결정.",
            "explain_prev": "Day 05의 X/X_st를 전달함수 형태로 다시 표현한 것. s 도메인이 더 범용적.",
        },
    ],
    "params": [
        {"sym": "H(s)", "name_ko": "전달함수", "name_en": "Transfer Function", "unit": "무차원", "meaning": "입력 대비 출력의 주파수별 이득(gain)과 위상", "vehicle": "노면→차체 진동 전달 특성", "range": "|H|<1이면 방진, |H|>1이면 증폭"},
        {"sym": "s", "name_ko": "라플라스 변수", "name_en": "Laplace Variable", "unit": "rad/s", "meaning": "복소 주파수 s=σ+jω. jω는 순수 진동, σ는 감쇠/성장", "vehicle": "주파수 영역 해석의 기본 변수", "range": "s=jω (주파수 응답 해석 시)"},
    ],
    "simpack_mappings": [
        {
            "sym": "H(jω) (FRA 출력)",
            "path": "Analysis → Frequency Response Analysis → Setup",
            "field": "Input: Road Excitation, Output: Body CG Acceleration",
            "unit": "m/s² per m (가속도 전달함수일 때)",
            "warn": "Simpack FRA 설정 시 Input과 Output을 명확히 정의. 변위 전달함수 vs 가속도 전달함수 구분. 가속도 = s²×변위이므로 H_acc = s²·H_disp."
        },
    ],
    "deep_dive_title": "극점과 영점 — 전달함수의 DNA를 읽는 법",
    "deep_dive_content": (
        "전달함수 H(s)의 본질은 분모=0의 근(극점, poles)과 분자=0의 근(영점, zeros)으로 결정됩니다.\n\n"
        "극점(Poles): 분모 m_s·s²+c_s·s+k_s=0의 근\n"
        "→ s = −ζω_n ± jω_d (Day 04와 동일!)\n"
        "→ 극점의 실수부 = 감쇠, 허수부 = 진동 주파수\n\n"
        "영점(Zeros): 분자 c_s·s+k_s=0의 근\n"
        "→ s = −k_s/c_s\n"
        "→ 이 주파수에서 전달이 0 (완전 차단)\n\n"
        "Bode Plot 읽기:\n"
        "· 극점 주파수 근처: 공진 피크\n"
        "· 영점 주파수 근처: 반공진(dip)\n"
        "· 고주파(ω≫ω_n): s² 지배 → −40 dB/decade 감쇠\n\n"
        "Day 13에서 이를 '전달률(Transmissibility)' 개념으로 발전시킵니다."
    ),
    "quiz": [
        {
            "type": "fill",
            "question": "전달함수의 극점은 분___=0의 근이고, 영점은 분___=0의 근이다?",
            "options": ["A. 모/자", "B. 자/모", "C. 모/모", "D. 자/자"],
            "correct": 0,
            "feedback_correct": "정답! 극점=분모=0, 영점=분자=0. 극점이 시스템의 고유 동특성을 결정.",
            "feedback_wrong": "오답. 정답은 A. Poles=분모의 근, Zeros=분자의 근.",
        },
        {
            "type": "meaning",
            "question": "전달함수 H(jω)의 절대값 |H|<1이 의미하는 것은?",
            "options": ["A. 입력보다 출력이 큼 (증폭)", "B. 입력보다 출력이 작음 (방진)", "C. 시스템 불안정", "D. 공진 발생"],
            "correct": 1,
            "feedback_correct": "정답! |H|<1이면 노면 입력이 감쇠되어 차체에 도달. 방진(isolation) 영역.",
            "feedback_wrong": "오답. 정답은 B. |H|<1 = 입력 감쇠 = 방진 효과.",
        },
        {
            "type": "simpack",
            "question": "Simpack FRA에서 전달함수를 구할 때 반드시 정의해야 하는 두 가지는?",
            "options": ["A. 질량과 강성", "B. Input 위치/방향과 Output 위치/물리량", "C. 시간 범위와 시간 간격", "D. 초기속도와 초기변위"],
            "correct": 1,
            "feedback_correct": "정답! FRA에서는 가진 입력(어디에, 어떤 방향)과 응답 출력(어디에서, 무엇을)을 명확히 정의해야 합니다.",
            "feedback_wrong": "오답. 정답은 B. Input(가진점/방향)과 Output(측정점/물리량)이 전달함수의 정의.",
        },
    ],
    "next_preview_title": "Day 13 미리보기",
    "next_preview": "전달률(Transmissibility) T(ω) 유도와 방진 설계 원리. √2 교차점의 의미와 서스펜션 설계에의 적용.",
}

DAY13 = {
    "day": 13, "part": 2, "part_title": "차량 진동 모델",
    "title_ko": "전달률과 방진 설계", "title_en": "Transmissibility & Vibration Isolation Design",
    "filename": "Day13_전달률방진설계.html",
    "hero_eq": "T(ω) = √((1+(2ζr)²) / ((1−r²)²+(2ζr)²))",
    "difficulty": "★★★☆☆", "num_formulas": "3단계",
    "brain_strategy": {
        "technique": "핵심 숫자 기억법(Magic Number)",
        "pre_routine": "r = √2 ≈ 1.414를 기억하세요. 이 주파수비를 경계로: r<√2이면 전달률 T>1(진동 증폭), r>√2이면 T<1(방진). 서스펜션 설계의 황금률: 고유주파수를 낮춰서 대부분의 노면 가진이 r>√2 영역에 오게 만드는 것.",
    },
    "intuition": (
        "Day 12의 전달함수에서 '노면 변위 입력 대비 차체 변위 출력'의 크기가 전달률 T(ω)입니다. "
        "Day 05의 진폭비 X/X_st와 비슷하지만 결정적 차이: 전달률은 '기초 가진(base excitation)' 문제. "
        "r=√2가 마법의 숫자: 이 점에서 모든 감쇠비의 전달률 곡선이 T=1로 교차합니다. "
        "r>√2 영역에서만 진정한 방진이 일어납니다."
    ),
    "deriv_steps": [
        {
            "label": "STEP 1 — 기초 가진 모델 설정",
            "equation": "mx'' + c(x'−z_r') + k(x−z_r) = 0",
            "explain_meaning": "노면 z_r(t)가 기초(base)로 작용. 상대변위(x−z_r)에 스프링력, 상대속도(x'−z_r')에 댐퍼력. Day 08 차체 방정식과 동일 구조.",
            "explain_sign": "우변=0: 외력이 아닌 기초 운동으로 전달. 외력 가진(Day 05)과 구분되는 '기초 가진' 문제.",
            "explain_prev": "Day 08 STEP 2: m_s·x_s'' + c_s(x_s'−x_u') + k_s(x_s−x_u) = 0에서 x_u → z_r로 치환.",
        },
        {
            "label": "STEP 2 — 전달률 공식 유도",
            "equation": "T(ω) = |X/Z_r| = √((k²+(cω)²) / ((k−mω²)²+(cω)²))\n= √((1+(2ζr)²) / ((1−r²)²+(2ζr)²))",
            "explain_meaning": "x=Xe^(jωt), z_r=Z_r·e^(jωt) 대입 후 |X/Z_r| 계산. 분자에 (2ζr)²이 추가된 것이 Day 05 진폭비와의 차이.",
            "explain_sign": "분자의 (2ζr)²: 댐퍼를 통한 전달 경로. 고주파에서 댐퍼가 오히려 진동을 전달하는 원인.",
            "explain_prev": "Day 05: X/X_st = 1/√((1−r²)²+(2ζr)²). 전달률은 분자에 √(1+(2ζr)²)가 곱해진 형태.",
        },
        {
            "label": "STEP 3 — √2 교차점과 방진 조건",
            "equation": "r = √2에서 T = 1 (모든 ζ에 대해)\nr > √2: T < 1 (방진 영역)\nr < √2: T > 1 (증폭 영역)",
            "explain_meaning": "T=1 조건을 풀면 분자=분모, 정리하면 r²=2 → r=√2. 이 점에서 감쇠비에 무관하게 T=1.",
            "explain_sign": "놀라운 사실: r>√2 영역에서 감쇠를 늘리면(ζ↑) 오히려 T가 증가! 댐퍼가 진동을 전달하는 통로가 되기 때문.",
            "explain_prev": "Day 05의 공진 피크와 달리, 전달률은 고주파에서 '감쇠의 역효과'가 존재.",
        },
    ],
    "params": [
        {"sym": "T(ω)", "name_ko": "전달률", "name_en": "Transmissibility", "unit": "무차원", "meaning": "기초 입력 대비 응답의 비. T<1이면 방진", "vehicle": "서스펜션의 진동 절연 성능", "range": "공진 시 ~1/(2ζ), 고주파에서 <1"},
        {"sym": "r=√2", "name_ko": "교차 주파수비", "name_en": "Crossover Frequency Ratio", "unit": "무차원", "meaning": "T=1인 경계점. 이 위가 방진 영역", "vehicle": "방진 설계의 기준점", "range": "r=√2 ≈ 1.414"},
    ],
    "simpack_mappings": [
        {
            "sym": "T(ω) (전달률 출력)",
            "path": "Results → FRA → Transmissibility",
            "field": "Output Amplitude / Input Amplitude vs Frequency",
            "unit": "무차원 or dB",
            "warn": "Simpack에서 전달률을 구하려면 FRA Input을 노면 변위(또는 속도), Output을 차체 변위(또는 가속도)로 설정. 가속도 전달률은 ω² 인자가 추가로 곱해짐에 주의."
        },
    ],
    "deep_dive_title": "방진의 딜레마 — 감쇠가 많으면 공진은 줄지만 고주파 방진이 나빠진다",
    "deep_dive_content": (
        "전달률 그래프에서 발견되는 서스펜션 설계의 근본적 딜레마:\n\n"
        "감쇠 증가(ζ↑)의 효과:\n"
        "✓ 공진 피크 감소 (좋음) — 방지턱 넘을 때 출렁임 감소\n"
        "✗ 고주파 방진 악화 (나쁨) — 미세 요철의 진동이 더 전달됨\n\n"
        "감쇠 감소(ζ↓)의 효과:\n"
        "✗ 공진 피크 증가 (나쁨) — 큰 요철에서 심하게 출렁\n"
        "✓ 고주파 방진 개선 (좋음) — 부드러운 주행감\n\n"
        "해결책:\n"
        "1. 가변 감쇠 서스펜션(CDC): 주파수/상황에 따라 ζ 자동 조절\n"
        "2. 비선형 감쇠: 바운드(압축)와 리바운드(신장) 감쇠비를 다르게\n"
        "3. 부시 댐핑: 서스펜션 부시의 고주파 감쇠 최적화\n\n"
        "르노코리아에서 CDC 쇼크를 사용한다면, 이 딜레마를 시스템적으로 해결하는 것."
    ),
    "quiz": [
        {
            "type": "fill",
            "question": "전달률 T=1이 되는 주파수비 r은?",
            "options": ["A. 1", "B. √2 ≈ 1.414", "C. 2", "D. π"],
            "correct": 1,
            "feedback_correct": "정답! r=√2에서 모든 감쇠비에 대해 T=1. 이 위가 방진 영역.",
            "feedback_wrong": "오답. 정답은 B. r=√2 ≈ 1.414가 전달률 교차점.",
        },
        {
            "type": "meaning",
            "question": "r>√2 영역에서 감쇠를 늘리면 전달률은 어떻게 되는가?",
            "options": ["A. 감소 (더 좋은 방진)", "B. 증가 (방진 악화)", "C. 변화 없음", "D. 진동 정지"],
            "correct": 1,
            "feedback_correct": "정답! 고주파에서 감쇠↑ → T↑. 댐퍼가 진동 전달 통로가 되어 오히려 방진이 나빠짐.",
            "feedback_wrong": "오답. 정답은 B. 이것이 방진의 딜레마: 감쇠는 공진을 줄이지만 고주파 방진을 악화시킴.",
        },
        {
            "type": "simpack",
            "question": "Simpack FRA에서 전달률이 1보다 작은 영역은 어떤 의미인가?",
            "options": ["A. 시스템 불안정", "B. 공진 발생", "C. 서스펜션이 진동을 효과적으로 절연", "D. 감쇠 부족"],
            "correct": 2,
            "feedback_correct": "정답! T<1 = 서스펜션이 노면 진동을 걸러내는 방진 영역. 이 영역이 넓을수록 좋은 서스펜션.",
            "feedback_wrong": "오답. 정답은 C. T<1은 입력보다 출력이 작은 '방진(isolation)' 영역.",
        },
    ],
    "next_preview_title": "Day 14 미리보기",
    "next_preview": "노면 가진 스펙트럼 — 실제 도로 프로파일의 PSD(Power Spectral Density)와 ISO 8608 분류. 노면 입력을 쿼터카에 적용하여 승차감 지표(ISO 2631) 계산.",
}

DAY14 = {
    "day": 14, "part": 2, "part_title": "차량 진동 모델",
    "title_ko": "노면 스펙트럼·승차감 지표", "title_en": "Road Spectrum (PSD) & Ride Comfort Index (ISO 2631)",
    "filename": "Day14_노면스펙트럼승차감.html",
    "hero_eq": "S_z(n) = S_z(n₀)·(n/n₀)^(−w),  a_w = √(∫W²(f)·S_a(f)df)",
    "difficulty": "★★★★☆", "num_formulas": "4단계",
    "brain_strategy": {
        "technique": "현실-수식 연결(Real-World Anchoring)",
        "pre_routine": "오늘 출근길에 지나온 도로를 떠올리세요. 고속도로 = 매끈(ISO A-B등급), 도심 도로 = 약간 거친(ISO C-D), 비포장 = 매우 거친(ISO E-F). 이 '거칠기'를 숫자로 표현하는 것이 노면 PSD. 이 PSD를 쿼터카에 통과시키면 차체 가속도의 PSD가 나오고, ISO 2631로 승차감 점수가 됩니다.",
    },
    "intuition": (
        "지금까지 깔끔한 cos(ωt) 입력만 다뤘지만, 실제 노면은 무수히 많은 주파수가 섞인 랜덤 입력입니다. "
        "이를 다루는 도구가 PSD(Power Spectral Density, 파워스펙트럼밀도). "
        "노면 PSD는 ISO 8608로 표준화되어 있고, 이를 전달함수에 통과시키면 차체 응답 PSD를 얻습니다. "
        "최종적으로 ISO 2631 가중함수를 적용하면 승차감 지표 a_w(weighted RMS acceleration)를 계산할 수 있습니다."
    ),
    "deriv_steps": [
        {
            "label": "STEP 1 — 노면 PSD 모델 (ISO 8608)",
            "equation": "S_z(n) = S_z(n₀) × (n/n₀)^(−w)\nn₀ = 0.1 cycle/m,  w ≈ 2",
            "explain_meaning": "n은 공간주파수(cycle/m), S_z(n₀)는 기준 공간주파수에서의 PSD 값. 도로 등급(A~H)에 따라 S_z(n₀) 값이 다름.",
            "explain_sign": "지수 −w ≈ −2: 저주파(긴 파장)가 에너지의 대부분. 고주파(짧은 파장)는 에너지가 작음. 이것이 노면의 기본 특성.",
            "explain_prev": "공간주파수 n → 시간주파수 f = n × V (V=차속). 속도가 빠를수록 같은 요철이 높은 주파수 가진이 됨.",
        },
        {
            "label": "STEP 2 — 응답 PSD 계산",
            "equation": "S_a(f) = |H_acc(j2πf)|² × S_z_input(f)",
            "explain_meaning": "시스템의 출력 PSD = |전달함수|² × 입력 PSD. H_acc는 가속도 전달함수(= (j2πf)²·H(j2πf)). Day 12의 전달함수를 활용.",
            "explain_sign": "제곱 |H|²: PSD는 에너지 밀도이므로 진폭이 아닌 파워(진폭²)로 전달.",
            "explain_prev": "Day 12: H(s) = (c_s·s+k_s)/(m_s·s²+c_s·s+k_s). 여기에 s=j2πf, ×s²(가속도).",
        },
        {
            "label": "STEP 3 — ISO 2631 가중 RMS 가속도",
            "equation": "a_w = √(∫₀^∞ W²(f) · S_a(f) df)",
            "explain_meaning": "W(f)는 ISO 2631의 주파수 가중함수. 인체가 민감한 4~8 Hz 대역에 가중치를 크게 부여. a_w가 승차감의 최종 숫자.",
            "explain_sign": "적분 → 전 주파수 대역의 에너지를 합산. 루트 → RMS(Root Mean Square). a_w < 0.315 m/s²이면 '쾌적'.",
            "explain_prev": "Day 13의 전달률로 방진 성능을 평가했다면, 여기서는 실제 도로에서의 승차감 점수를 계산.",
        },
        {
            "label": "STEP 4 — 승차감 등급 판정 (ISO 2631)",
            "equation": "a_w < 0.315: 쾌적\n0.315~0.63: 약간 불쾌\n0.63~1.0: 불쾌\n> 1.0: 매우 불쾌",
            "explain_meaning": "a_w 값으로 승차감을 객관적으로 등급화. 서스펜션 튜닝의 최종 목표: 타겟 도로에서 a_w를 허용 범위 이내로.",
            "explain_sign": "단위 m/s². 중력가속도 g ≈ 9.81 m/s² 대비 ~3%~10% 수준이 체감 영역.",
            "explain_prev": "이 지표가 K&C 시험, 실차 주행 평가, Simpack 가상 시험의 공통 평가 척도.",
        },
    ],
    "params": [
        {"sym": "S_z(n₀)", "name_ko": "노면 PSD 기준값", "name_en": "Road PSD Reference", "unit": "m³/cycle", "meaning": "n₀=0.1 cycle/m에서의 PSD. 도로 등급 결정", "vehicle": "ISO 8608 A~H 등급", "range": "A: 1×10⁻⁶, C: 16×10⁻⁶, E: 256×10⁻⁶"},
        {"sym": "a_w", "name_ko": "가중 RMS 가속도", "name_en": "Weighted RMS Acceleration", "unit": "m/s²", "meaning": "ISO 2631 승차감 최종 지표", "vehicle": "승차감 타겟 스펙", "range": "< 0.315(쾌적), 0.315~0.63(약간 불쾌)"},
        {"sym": "W(f)", "name_ko": "ISO 2631 가중함수", "name_en": "ISO 2631 Weighting Function", "unit": "무차원", "meaning": "인체 주파수별 민감도 가중치", "vehicle": "4~8 Hz 피크", "range": "W_k(수직), W_d(수평)"},
    ],
    "simpack_mappings": [
        {
            "sym": "노면 입력 (Road Profile)",
            "path": "Excitations → Road → ISO 8608 / Measured Profile",
            "field": "Road Class, Vehicle Speed [km/h]",
            "unit": "m, km/h",
            "warn": "Simpack에서 ISO 8608 노면을 생성하거나 실측 데이터(.rdf)를 입력. 차속에 따라 시간 영역 가진이 달라짐. 동일 노면이라도 속도↑ → 가진 주파수↑."
        },
        {
            "sym": "a_w (승차감 출력)",
            "path": "Results → Post-Processing → ISO 2631 Filter",
            "field": "Weighted RMS Acceleration [m/s²]",
            "unit": "m/s²",
            "warn": "Simpack 후처리에서 ISO 2631 가중 필터를 적용하여 a_w 계산 가능. 센서 위치(CG, 시트, 스티어링 휠)에 따라 값이 다름. 실차 비교 시 센서 위치 일치 필수."
        },
    ],
    "deep_dive_title": "PART 2 총정리 — 쿼터카→하프카→전달함수→승차감 평가 체계",
    "deep_dive_content": (
        "7일간의 PART 2 학습 체계:\n\n"
        "Day 08-09: 쿼터카 2DOF → 바디 바운스/휠 홉 주파수\n"
        "Day 10-11: 하프카 4DOF → 바운스/피치 연성, flat ride\n"
        "Day 12: 전달함수 H(s) → 입출력 관계의 주파수 영역 표현\n"
        "Day 13: 전달률 T(ω) → 방진 설계, √2 교차점\n"
        "Day 14: 노면 PSD + ISO 2631 → 승차감 최종 평가\n\n"
        "이 체계가 서스펜션 엔지니어의 핵심 워크플로우:\n"
        "1. 차량 파라미터 설정 → 2. 모델 구축(쿼터카/하프카) → 3. 고유진동수 확인\n"
        "4. 전달함수/전달률 분석 → 5. 실제 노면 가진 적용 → 6. 승차감 지표 평가\n\n"
        "PART 3(Day 15~)에서는 서스펜션 하드웨어 구성요소(스프링, 댐퍼, 부시, 스태빌라이저)의 "
        "비선형 특성과 모델링을 배웁니다."
    ),
    "quiz": [
        {
            "type": "fill",
            "question": "노면 PSD의 공간주파수 n을 시간주파수 f로 변환하는 식은 f = n × ___?",
            "options": ["A. ω_n", "B. V (차속)", "C. 2π", "D. k/m"],
            "correct": 1,
            "feedback_correct": "정답! f = n × V. 차속이 빠를수록 같은 요철이 높은 시간주파수로 변환.",
            "feedback_wrong": "오답. 정답은 B. 공간주파수 × 차속 = 시간주파수. f[Hz] = n[cycle/m] × V[m/s].",
        },
        {
            "type": "meaning",
            "question": "ISO 2631에서 a_w = 0.5 m/s²의 승차감 등급은?",
            "options": ["A. 쾌적", "B. 약간 불쾌", "C. 불쾌", "D. 매우 불쾌"],
            "correct": 1,
            "feedback_correct": "정답! 0.315 < 0.5 < 0.63이므로 '약간 불쾌' 등급.",
            "feedback_wrong": "오답. 정답은 B. a_w=0.5는 0.315~0.63 범위 → '약간 불쾌'.",
        },
        {
            "type": "simpack",
            "question": "Simpack에서 노면 가진을 설정할 때 반드시 함께 지정해야 하는 파라미터는?",
            "options": ["A. 온도", "B. 차량 속도", "C. 풍속", "D. 노면 마찰계수"],
            "correct": 1,
            "feedback_correct": "정답! 차속이 공간주파수→시간주파수 변환을 결정. 동일 노면도 속도에 따라 가진이 다름.",
            "feedback_wrong": "오답. 정답은 B. 노면 공간 프로파일이 같아도 차속에 따라 시간 가진이 달라짐.",
        },
    ],
    "next_preview_title": "Day 15 미리보기 — PART 3 시작!",
    "next_preview": "서스펜션 스프링 모델링 — 선형 스프링 vs 비선형(progressive) 스프링. 스프링 특성 곡선 F-δ와 Simpack Force Element 설정.",
}
