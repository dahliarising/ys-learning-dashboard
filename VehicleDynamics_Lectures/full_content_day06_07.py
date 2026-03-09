"""
Day 06~07 상세 콘텐츠 — curriculum_data.py에 병합용
"""

DAY06 = {
    "day": 6,
    "part": 1,
    "part_title": "1자유도 진동계 기초",
    "title_ko": "위상각 φ 유도",
    "title_en": "Phase Angle φ Derivation",
    "filename": "Day06_위상각유도.html",
    "hero_eq": "φ = arctan(2ζr / (1−r²))",
    "difficulty": "★★☆☆☆",
    "num_formulas": "3단계",
    "brain_strategy": {
        "technique": "메타포 매핑(Metaphor Mapping)",
        "pre_routine": "음악에 맞춰 박수를 치는 상황을 상상하세요. 느린 템포(r≪1)에서는 음악과 거의 동시에 칩니다. 빠른 템포(r≫1)에서는 점점 뒤처져서 결국 반 박자(π) 늦게 치게 됩니다. r=1(공진)에서는 정확히 1/4 박자(π/2) 뒤처집니다. 이것이 위상각 φ의 물리적 의미.",
    },
    "intuition": (
        "Day 05에서 진폭비 X/X_st를 배웠습니다. 그런데 진폭만으로 강제진동을 완전히 기술할 수 없습니다. "
        "'응답이 외력보다 얼마나 늦게 따라가는가' — 이것이 위상각 φ입니다. "
        "차량에서 왜 중요한가? 엔진 마운트 설계 시 진동 전달의 타이밍을 제어해야 합니다. "
        "노면 가진에 대한 차체 응답의 위상 관계는 승차감의 '찰진' 느낌을 결정합니다. "
        "φ=0이면 외력과 동시, φ=π/2이면 1/4주기 지연(공진), φ=π이면 외력과 정반대."
    ),
    "deriv_steps": [
        {
            "label": "STEP 1 — 정상상태 해의 sin·cos 분해",
            "equation": "x_p = C₁cos(ωt) + C₂sin(ωt)",
            "explain_meaning": "Day 05의 x_p(t)=X cos(ωt−φ)를 삼각함수 덧셈정리로 전개. C₁=X cosφ, C₂=X sinφ. 이렇게 분해해야 계수 비교가 가능.",
            "explain_sign": "cos(ωt−φ) = cosφ·cos(ωt) + sinφ·sin(ωt). 부호가 모두 +인 이유: cos(A−B) 공식.",
            "explain_prev": "Day 05 STEP 2에서 x_p(t)=X cos(ωt−φ)로 가정한 것을 구체적으로 풀어쓴 것.",
        },
        {
            "label": "STEP 2 — 운동방정식에 대입 후 계수 비교",
            "equation": "cos(ωt) 계수: (k−mω²)C₁ + cωC₂ = F₀\nsin(ωt) 계수: −cωC₁ + (k−mω²)C₂ = 0",
            "explain_meaning": "x_p를 mx''+cx'+kx=F₀cos(ωt)에 대입. cos(ωt)과 sin(ωt) 항을 각각 모아서 계수가 같아야 하므로 연립방정식 2개 생성.",
            "explain_sign": "x''에서 −ω² 인자, x'에서 ω 인자가 나옵니다. sin 계수 우변=0인 이유: 외력에 sin 성분이 없으므로.",
            "explain_prev": "x_p=C₁cos(ωt)+C₂sin(ωt), x_p'=ω(−C₁sin+C₂cos), x_p''=−ω²(C₁cos+C₂sin)를 대입.",
        },
        {
            "label": "STEP 3 — 위상각 φ 공식 도출",
            "equation": "tan φ = C₂/C₁ = cω/(k−mω²) = 2ζr/(1−r²)\n∴ φ = arctan(2ζr / (1−r²))",
            "explain_meaning": "STEP 2의 두 번째 식에서 C₂/C₁ = cω/(k−mω²). 이를 ζ, r로 무차원화하면 오늘의 핵심 공식. φ는 0~π 범위.",
            "explain_sign": "r<1: 분모 양수→φ<π/2. r=1: 분모=0→φ=π/2(정확히). r>1: 분모 음수→φ>π/2. arctan에서 사분면 주의!",
            "explain_prev": "c/m=2ζω_n, k/m=ω_n², ω/ω_n=r을 사용. cω/(k−mω²) = (2ζω_n·ω)/(ω_n²−ω²) = 2ζr/(1−r²).",
        },
    ],
    "params": [
        {"sym": "φ", "name_ko": "위상각", "name_en": "Phase Angle", "unit": "rad", "meaning": "외력과 응답 사이의 시간 지연을 각도로 표현", "vehicle": "가진-응답 타이밍 차이", "range": "0(r≪1) → π/2(r=1) → π(r≫1)"},
        {"sym": "r", "name_ko": "주파수비", "name_en": "Frequency Ratio", "unit": "무차원", "meaning": "가진주파수/고유주파수 = ω/ω_n (Day 05 복습)", "vehicle": "운전 조건별 진동 영역 판별", "range": "r<1 준정적, r≈1 공진, r>1 방진"},
    ],
    "simpack_mappings": [
        {
            "sym": "φ (위상각 출력)",
            "path": "Results → Frequency Response → Phase",
            "field": "Phase [deg] vs Frequency [Hz]",
            "unit": "deg (Simpack은 도 단위, rad 변환: ×π/180)",
            "warn": "Simpack FRA의 Phase Plot에서 φ=−90°(= −π/2)가 공진점입니다. 부호 관례가 교재와 다를 수 있으니 ±확인 필수."
        },
    ],
    "deep_dive_title": "Bode Plot의 두 축 — 진폭비와 위상각을 동시에 읽는 법",
    "deep_dive_content": (
        "Day 05의 진폭비와 오늘의 위상각을 하나의 그래프에 표현한 것이 Bode Plot입니다.\n\n"
        "상단: |X/X_st| vs 주파수 (보통 dB 스케일, 20log₁₀)\n"
        "하단: φ vs 주파수\n\n"
        "핵심 읽기법:\n"
        "· 진폭 피크 주파수 → 공진 주파수 ≈ ω_n\n"
        "· 같은 주파수에서 위상이 −90°를 지남 → 공진 확인\n"
        "· 피크의 날카로움 → ζ의 크기 (날카로울수록 ζ 작음)\n"
        "· −3dB 대역폭 Δω/ω_n ≈ 2ζ → ζ 추정 가능\n\n"
        "차량 NVH에서 Bode Plot은 전달함수(Transfer Function)를 시각화하는 기본 도구입니다. "
        "Day 12~13에서 전달률 개념과 함께 더 깊이 다룹니다."
    ),
    "quiz": [
        {
            "type": "fill",
            "question": "공진점(r=1)에서의 위상각 φ는?",
            "options": ["A. 0", "B. π/4 (45°)", "C. π/2 (90°)", "D. π (180°)"],
            "correct": 2,
            "feedback_correct": "정답! r=1에서 tan φ = 2ζ·1/(1−1²) = 2ζ/0 → ∞, 따라서 φ = π/2 = 90°.",
            "feedback_wrong": "오답. 정답은 C. r=1이면 분모(1−r²)=0이므로 tanφ→∞, φ=π/2(90°).",
        },
        {
            "type": "meaning",
            "question": "r≫1(고주파 가진)에서 위상각 φ가 π(180°)에 가깝다는 것은 물리적으로 무엇을 의미하는가?",
            "options": ["A. 외력과 응답이 동시", "B. 응답이 외력과 정반대 방향으로 움직임", "C. 응답이 완전히 정지", "D. 진폭이 최대"],
            "correct": 1,
            "feedback_correct": "정답! φ≈π이면 외력이 위로 갈 때 질량은 아래로. 관성이 지배하여 외력과 반대로 움직입니다.",
            "feedback_wrong": "오답. 정답은 B. 고주파에서 질량의 관성이 지배하여 외력과 180° 반대로 움직입니다.",
        },
        {
            "type": "simpack",
            "question": "Simpack FRA에서 위상각이 −90°를 지나는 주파수는 무엇을 의미하는가?",
            "options": ["A. 반공진점", "B. 공진 주파수", "C. 정적 평형점", "D. 감쇠가 0인 점"],
            "correct": 1,
            "feedback_correct": "정답! 위상이 −90°(또는 +90°, 부호 관례에 따라)를 지나는 점이 공진 주파수입니다.",
            "feedback_wrong": "오답. 정답은 B. 위상각이 ±90°를 지나는 주파수가 공진 주파수(≈ω_n)입니다.",
        },
    ],
    "next_preview_title": "Day 07 미리보기",
    "next_preview": "공진 조건 상세 분석 — 정확한 공진 주파수 ω_peak = ω_n√(1−2ζ²), Half-Power Bandwidth로 ζ 추정, 차량에서의 공진 회피 사례.",
}

DAY07 = {
    "day": 7,
    "part": 1,
    "part_title": "1자유도 진동계 기초",
    "title_ko": "공진 조건 분석",
    "title_en": "Resonance Condition Analysis",
    "filename": "Day07_공진조건분석.html",
    "hero_eq": "ω_peak = ω_n√(1−2ζ²)",
    "difficulty": "★★☆☆☆",
    "num_formulas": "2단계",
    "brain_strategy": {
        "technique": "스토리텔링 기억법(Narrative Memory)",
        "pre_routine": "2010년 러시아 볼고그라드 다리가 바람에 의해 공진하여 출렁인 영상을 떠올리세요. 다리의 고유주파수와 바람 가진 주파수가 일치하면 작은 힘으로도 거대한 진폭이 발생합니다. 오늘은 '정확히 어떤 주파수에서 진폭이 최대인가'와 '공진 대역폭은 얼마나 넓은가'를 수식으로 정의합니다.",
    },
    "intuition": (
        "Day 05~06에서 진폭비와 위상각을 배웠습니다. r=1에서 공진이 일어난다고 했지만, "
        "엄밀히 말하면 진폭비가 최대가 되는 주파수는 r=1이 아니라 약간 아래입니다! "
        "감쇠가 있으면 피크가 왼쪽(저주파)으로 살짝 이동하는데, 그 정확한 위치가 ω_peak = ω_n√(1−2ζ²)입니다. "
        "실무에서 더 중요한 것은 '공진 대역폭(Bandwidth)'. Half-Power Bandwidth Δω = 2ζω_n으로 ζ를 추정할 수 있습니다. "
        "PART 1의 마지막 Day로서, 1DOF 진동계의 전체 그림을 완성합니다."
    ),
    "deriv_steps": [
        {
            "label": "STEP 1 — 진폭비의 극대 조건",
            "equation": "d(X/X_st)/dr = 0  →  ω_peak = ω_n√(1−2ζ²)",
            "explain_meaning": "Day 05의 진폭비 X/X_st = 1/√((1−r²)²+(2ζr)²)를 r에 대해 미분하고 0으로 놓으면 피크 주파수를 구할 수 있음.",
            "explain_sign": "1−2ζ² > 0이려면 ζ < 1/√2 ≈ 0.707. 이보다 ζ가 크면 피크가 사라짐(단조감소). 승용차 ζ=0.2~0.4이므로 항상 피크 존재.",
            "explain_prev": "Day 05의 진폭비 공식을 분모 제곱의 r에 대한 미분으로 최솟값을 구하면 r_peak² = 1−2ζ².",
        },
        {
            "label": "STEP 2 — Half-Power Bandwidth와 ζ 추정",
            "equation": "Δω / ω_n ≈ 2ζ  (ζ가 작을 때)",
            "explain_meaning": "진폭비가 피크의 1/√2배(= −3dB)가 되는 두 주파수의 차이가 Half-Power Bandwidth Δω. 이 값을 ω_n으로 나누면 약 2ζ.",
            "explain_sign": "1/√2 ≈ 0.707, 즉 에너지가 피크의 절반(half power)이 되는 점. ζ가 작을수록 대역폭이 좁아(날카로운 공진).",
            "explain_prev": "Day 05의 진폭비 = 피크/√2 조건을 풀면 두 근 r₁, r₂를 얻고, r₂−r₁ ≈ 2ζ (1차 근사).",
        },
    ],
    "params": [
        {"sym": "ω_peak", "name_ko": "피크 주파수", "name_en": "Peak Frequency", "unit": "rad/s", "meaning": "진폭비가 최대가 되는 정확한 가진 주파수", "vehicle": "공진 회피 설계의 기준점", "range": "ω_n√(1−2ζ²), ζ=0.3이면 ω_peak≈0.91ω_n"},
        {"sym": "Δω", "name_ko": "반치대역폭", "name_en": "Half-Power Bandwidth", "unit": "rad/s", "meaning": "공진 피크의 −3dB 폭. 공진 날카로움의 척도", "vehicle": "NVH 문제의 주파수 범위 평가", "range": "Δω ≈ 2ζω_n"},
        {"sym": "Q", "name_ko": "품질계수", "name_en": "Quality Factor", "unit": "무차원", "meaning": "Q = 1/(2ζ) = ω_n/Δω. 공진 피크의 날카로움", "vehicle": "공진 심각도 평가", "range": "승용차: Q≈1.25~2.5 (ζ=0.2~0.4)"},
    ],
    "simpack_mappings": [
        {
            "sym": "ω_peak, Δω (FRA 출력)",
            "path": "Results → Frequency Response Analysis → Bode Plot",
            "field": "Peak Frequency [Hz], −3dB Bandwidth [Hz]",
            "unit": "Hz",
            "warn": "Simpack FRA 결과에서 진폭 피크를 찾고 −3dB 점 두 개를 읽어 Δf = f₂−f₁ 계산. 이론값 2ζf_n과 비교. 비선형 댐퍼를 사용하면 이론값과 차이가 날 수 있음."
        },
    ],
    "deep_dive_title": "PART 1 총정리 — 1DOF 진동계의 7가지 핵심 수식 체계",
    "deep_dive_content": (
        "7일간 배운 1DOF 진동계의 핵심 수식을 체계적으로 정리합니다.\n\n"
        "▸ 운동방정식: mx'' + cx' + kx = F(t) [Day 01]\n"
        "▸ 고유진동수: ω_n = √(k/m) [Day 02]\n"
        "▸ 감쇠비: ζ = c/(2mω_n) [Day 03]\n"
        "▸ 감쇠고유진동수: ω_d = ω_n√(1−ζ²) [Day 04]\n"
        "▸ 진폭비: X/X_st = 1/√((1−r²)²+(2ζr)²) [Day 05]\n"
        "▸ 위상각: φ = arctan(2ζr/(1−r²)) [Day 06]\n"
        "▸ 피크 주파수: ω_peak = ω_n√(1−2ζ²) [Day 07]\n\n"
        "이 7개 수식으로 1DOF 시스템의 모든 선형 거동을 기술할 수 있습니다. "
        "PART 2(Day 08~)에서는 이를 2DOF로 확장하여 실제 차량 모델(바운스+피치, 스프링상+스프링하)을 구축합니다.\n\n"
        "Simpack 관점: Bodies(m) + Spring(k) + Damper(c) + Excitation(F) = 1DOF 모델 완성. "
        "PART 2에서 Bodies가 2개로 늘어나고, Joint 자유도 설정이 추가됩니다."
    ),
    "quiz": [
        {
            "type": "fill",
            "question": "감쇠가 있는 시스템의 정확한 피크 주파수는 ω_peak = ω_n√(1 − ___ζ²)?",
            "options": ["A. 1", "B. 2", "C. 3", "D. 4"],
            "correct": 1,
            "feedback_correct": "정답! ω_peak = ω_n√(1−2ζ²). 계수 2가 핵심.",
            "feedback_wrong": "오답. 정답은 B. ω_peak = ω_n√(1−2ζ²). Day 04의 ω_d=ω_n√(1−ζ²)와 구분!",
        },
        {
            "type": "meaning",
            "question": "Half-Power Bandwidth Δω ≈ 2ζω_n에서 ζ가 작을수록 어떻게 되는가?",
            "options": ["A. 대역폭이 넓어진다", "B. 대역폭이 좁아지고 공진이 날카로워진다", "C. 피크가 사라진다", "D. 주파수가 높아진다"],
            "correct": 1,
            "feedback_correct": "정답! ζ↓ → Δω↓ → 날카로운 공진 피크. Q=1/(2ζ)가 커져서 공진이 심각해집니다.",
            "feedback_wrong": "오답. 정답은 B. 감쇠가 작으면 공진 대역이 좁고 날카로워집니다.",
        },
        {
            "type": "simpack",
            "question": "Simpack FRA에서 −3dB 대역폭을 측정하여 ζ를 추정하는 방법은?",
            "options": ["A. ζ = Δf/(2f_n)", "B. ζ = Δf·f_n", "C. ζ = f_n/Δf", "D. ζ = 2Δf/f_n"],
            "correct": 0,
            "feedback_correct": "정답! Δω/(2ω_n) ≈ ζ, 즉 Δf/(2f_n) ≈ ζ. (Δω=2πΔf, ω_n=2πf_n이므로 2π 상쇄)",
            "feedback_wrong": "오답. 정답은 A. Δω≈2ζω_n → ζ≈Δω/(2ω_n) = Δf/(2f_n).",
        },
    ],
    "next_preview_title": "Day 08 미리보기 — PART 2 시작!",
    "next_preview": "2DOF 시스템으로 확장! 쿼터카 모델(스프링상+스프링하 질량) 구성과 2×2 행렬 운동방정식 유도. 실제 차량 파라미터(sprung mass, unsprung mass, tire stiffness) 입력.",
}
