"""
Day 29~33 풀콘텐츠 — PART 5: Simpack 디지털 트윈 완전 통합
"""

# ═══════════════════════════════════════════════
# Day 29: 수식 → Simpack 완전 매핑
# ═══════════════════════════════════════════════
DAY29 = {
    "day": 29,
    "part": "5",
    "part_title": "Simpack 완전 통합",
    "week": "",
    "title_ko": "수식 → Simpack 완전 매핑",
    "title_en": "Formula-to-Simpack Complete Mapping",
    "filename": "Day29_수식Simpack매핑.html",
    "hero_eq": "기호↔입력필드 1:1 테이블",
    "difficulty": "★★★☆☆",
    "num_formulas": "매핑 12항목",

    "brain_strategy": "수식의 모든 기호(m, c, k, ζ, ωₙ)가 Simpack 어디에 입력되는지 1:1 매핑 테이블을 그리면, '수식 = 시뮬레이션'이라는 확신이 생깁니다.",

    "intuition_title": "수식 기호 → Simpack GUI 필드",
    "intuition_text": "지난 28일간 배운 수식에는 질량(m), 강성(k), 감쇠(c), 고유진동수(ωₙ), 감쇠비(ζ) 등이 등장했습니다. 이 기호들이 Simpack의 어떤 요소(Element), 어떤 입력 필드에 대응하는지 명확히 정리하면 — '이론에서 시뮬레이션까지 빈틈 없는 다리'가 완성됩니다. Body → mass/inertia, Force Element → spring & damper, Joint → DOF constraint, Marker → attachment point의 4계층 구조입니다.",

    "deriv_steps": [
        {
            "step_title": "Body 요소 매핑: m, I → Simpack Body",
            "equation": "Simpack Body Element: mass = m [kg], Ixx/Iyy/Izz = Jxx/Jyy/Jzz [kg·m²]",
            "explain_meaning": "수식의 질량 m과 관성모멘트 I가 Simpack의 Body Element 속성에 직접 입력됩니다. Sprung mass → Body_Chassis, Unsprung mass → Body_Knuckle.",
            "explain_sign": "좌표계 방향: Simpack은 SAE J670(x=전방, z=하방) 또는 ISO(z=상방) 선택 가능. 부호 실수 주의.",
            "explain_prev": "Day 01 뉴턴 제2법칙 mẍ = ΣF에서 m이 바로 이 Body mass입니다."
        },
        {
            "step_title": "Force Element 매핑: k, c → Spring/Damper",
            "equation": "Spring FE: k_lin = k [N/m], preload = F₀ [N]\nDamper FE: c_lin = c [N·s/m] 또는 비선형 F-v Lookup Table",
            "explain_meaning": "수식의 강성 k와 감쇠계수 c가 Simpack의 Force Element(Spring/Damper)에 매핑됩니다. 선형이면 단일 값, 비선형이면 Lookup Table을 사용합니다.",
            "explain_sign": "F = -kx - cẋ에서 부호: Simpack은 '양의 변위 → 음의 복원력' 자동 처리. Sign Convention이 내부적으로 반영됩니다.",
            "explain_prev": "Day 16 스프링(직렬/병렬), Day 17 댐퍼(비대칭 F-v)가 여기서 실제 입력됩니다."
        },
        {
            "step_title": "Joint 매핑: DOF 정의 → Constraint",
            "equation": "Revolute Joint: 1 ROT DOF (θ)\nPrismatic Joint: 1 TRANS DOF (z)\nSpherical: 3 ROT DOF",
            "explain_meaning": "수식에서 '1-DOF 상하 운동'이라 가정한 것이 Simpack에서는 Prismatic Joint(z방향)로 구현됩니다. Multi-link 서스펜션은 적절한 Joint 조합으로 실제 운동학을 재현합니다.",
            "explain_sign": "잠김(Lock) DOF = 구속(Constraint). Day 04에서 '행렬 크기 = DOF 수'와 직결.",
            "explain_prev": "Day 03 2-DOF 모델에서 z_s, z_u 두 자유도를 정의한 것이 Joint 구성의 기본입니다."
        },
        {
            "step_title": "Marker 매핑: 부착점 → Reference Frame",
            "equation": "Marker = {Position(x,y,z), Orientation(ψ,θ,φ)} on Body",
            "explain_meaning": "수식에서 '스프링 상단/하단'이라 칭한 부착점이 Simpack에서는 Marker로 정의됩니다. Force Element는 두 Marker 사이에 연결되며, 상대 변위/속도를 자동 계산합니다.",
            "explain_sign": "Marker 방향(Orientation)이 잘못되면 힘 방향이 뒤집힙니다. 항상 로컬 z축 = 힘 작용 방향.",
            "explain_prev": "Day 18 부싱의 복소강성이 Marker 좌표계 기준 로컬 x,y,z 방향별로 입력됩니다."
        }
    ],

    "params_table": [
        {"symbol": "m_s", "name": "Sprung mass", "typical": "350~500 kg", "simpack": "Body_Chassis → mass"},
        {"symbol": "m_u", "name": "Unsprung mass", "typical": "30~50 kg", "simpack": "Body_Knuckle → mass"},
        {"symbol": "k_s", "name": "Spring rate", "typical": "15~30 N/mm", "simpack": "FE_Spring → k_lin"},
        {"symbol": "c_s", "name": "Damper coeff", "typical": "1~3 kN·s/m", "simpack": "FE_Damper → c_lin or F-v table"},
        {"symbol": "k_t", "name": "Tire stiffness", "typical": "150~250 N/mm", "simpack": "FE_Tire → k_vertical"},
        {"symbol": "F₀", "name": "Spring preload", "typical": "설계하중", "simpack": "FE_Spring → preload"}
    ],

    "simpack_connection": "이 Day의 핵심은 수식 기호 → Simpack 입력 필드의 완전한 1:1 매핑입니다. Body(mass, inertia) → Force Element(k, c) → Joint(DOF) → Marker(attachment)의 4계층이 수식 세계와 시뮬레이션 세계를 잇는 다리입니다.",

    "deep_dive_title": "실무 함정: 단위 변환 & 좌표계",
    "deep_dive_text": "가장 흔한 Simpack 실수 TOP 3: ① 단위 혼동(N/mm vs N/m — Simpack 기본은 SI 단위계), ② 좌표계 불일치(SAE vs ISO에서 z축 방향), ③ Marker 방향 오류(로컬 축 설정 실수로 힘 방향 반전). 실무에서는 반드시 단위 체크리스트와 좌표계 다이어그램을 만들어 놓고 시작합니다.",

    "quiz": [
        {"type": "qa", "q": "수식의 감쇠계수 c가 Simpack에서 어떤 Element, 어떤 필드에 입력되는지 설명하시오.", "a": "Force Element (Damper Type) → c_lin 필드에 직접 입력 (선형), 또는 비선형일 경우 F-v Lookup Table로 입력. 단위는 N·s/m."},
        {"type": "qa", "q": "Simpack에서 1-DOF 상하 운동을 구현하려면 어떤 Joint를 사용하며, 이것이 수식의 어떤 가정에 대응하는가?", "a": "Prismatic Joint (Translation z)를 사용. 이는 수식에서 ẍ 또는 z̈ 하나의 자유도만 고려한 것에 대응. 즉 '수직 병진운동만 가능' 가정."},
        {"type": "qa", "q": "Marker의 Orientation이 잘못 설정되면 시뮬레이션에 어떤 영향을 주는가?", "a": "Force Element가 참조하는 상대변위 방향이 의도와 반대가 되어, 복원력 대신 발산력이 작용하거나 감쇠가 반대 방향으로 작용. 결과적으로 비물리적 발산이 발생."}
    ],

    "next_preview": "Day 30에서는 이 매핑을 실제로 적용하여 Quarter Car 모델을 Simpack에 완전 구현하고, 이론 고유진동수와 시뮬레이션 결과를 비교 검증합니다."
}

# ═══════════════════════════════════════════════
# Day 30: Quarter Car → Simpack 구현 & 검증
# ═══════════════════════════════════════════════
DAY30 = {
    "day": 30,
    "part": "5",
    "part_title": "Simpack 완전 통합",
    "week": "",
    "title_ko": "Quarter Car → Simpack 구현 & 검증",
    "title_en": "Quarter Car Implementation & Verification",
    "filename": "Day30_QuarterCar구현.html",
    "hero_eq": "이론값 vs 시뮬레이션 비교",
    "difficulty": "★★★★☆",
    "num_formulas": "검증 5항목",

    "brain_strategy": "이론에서 구한 ωₙ, ζ 값과 Simpack 시뮬레이션에서 측정한 값을 직접 비교하면, 모델 신뢰성을 수치로 입증할 수 있습니다.",

    "intuition_title": "이론 ↔ 시뮬레이션 1:1 검증",
    "intuition_text": "Day 03에서 유도한 2-DOF Quarter Car의 고유진동수 ω₁, ω₂와 감쇠비 ζ를 이론값으로 기억하고 있습니다. 이제 Simpack에서 같은 파라미터로 모델을 만들고 고유치 해석(Eigenvalue Analysis)을 돌리면 — 이론값과 시뮬레이션 값이 일치해야 합니다. 이 일치 확인이 바로 '모델 검증(Verification)'입니다.",

    "deriv_steps": [
        {
            "step_title": "Step 1: Simpack 모델 구축 절차",
            "equation": "① Body 2개(sprung, unsprung) → ② Joint 2개(prismatic z) → ③ FE 3개(k_s, c_s, k_t) → ④ Marker 연결 → ⑤ Road input 정의",
            "explain_meaning": "Simpack에서 Quarter Car를 구현하는 5단계 순서입니다. Body → Joint → Force Element → Marker → Excitation의 순서가 가장 효율적입니다.",
            "explain_sign": "Road input은 Road Surface Element로 정의하며, step input(단턱), sine sweep, random road(ISO 8608) 등을 선택합니다.",
            "explain_prev": "Day 29에서 정리한 수식↔Simpack 매핑이 여기서 실제로 적용됩니다."
        },
        {
            "step_title": "Step 2: 이론 고유진동수 계산 (복습)",
            "equation": "det([K] - ω²[M]) = 0 → ω₁ ≈ √(k_s/m_s) ≈ 1~1.5 Hz (bounce), ω₂ ≈ √(k_t/m_u) ≈ 10~15 Hz (wheel hop)",
            "explain_meaning": "이론에서 2-DOF 시스템의 고유진동수를 구하는 방법입니다. Bounce 모드(차체)와 Wheel Hop 모드(바퀴)를 미리 계산해 놓습니다.",
            "explain_sign": "ω₁ < ω₂: 차체 진동수가 항상 바퀴 진동수보다 낮습니다. 질량비(m_s >> m_u)와 강성비(k_t >> k_s) 때문.",
            "explain_prev": "Day 03, Day 26에서 유도한 고유치 문제의 실제 적용입니다."
        },
        {
            "step_title": "Step 3: Simpack Eigenvalue Analysis 실행",
            "equation": "Simpack → Analysis → Eigenvalue → Modes Table → f₁, f₂, ζ₁, ζ₂",
            "explain_meaning": "Simpack의 Eigenvalue Analysis 기능을 실행하면 각 모드의 고유진동수(Hz), 감쇠비, 모드 형상을 자동으로 계산합니다. 결과를 이론값과 비교합니다.",
            "explain_sign": "일치 기준: 고유진동수 오차 < 1%, 감쇠비 오차 < 5%이면 모델 검증 성공.",
            "explain_prev": "Day 26 고유치 문제에서 배운 [K-ω²M]φ=0이 Simpack 내부에서 수치적으로 풀리는 것입니다."
        },
        {
            "step_title": "Step 4: 시간영역 검증 — Step Response",
            "equation": "Step input 30mm → z_s(t) 응답 → 이론: z_s(t) = A·e^(-ζωₙt)·sin(ωdt + φ) → Simpack 결과와 오버레이 비교",
            "explain_meaning": "고유치 외에 시간영역 응답도 비교합니다. 30mm step 입력에 대한 차체 변위를 이론 공식과 Simpack 결과를 동일 그래프에 겹쳐서 확인합니다.",
            "explain_sign": "감쇠 진동의 포락선(envelope) e^(-ζωₙt)이 일치하면, 시간영역에서도 모델이 검증된 것입니다.",
            "explain_prev": "Day 02 감쇠자유진동 공식이 여기서 시뮬레이션 검증 기준으로 사용됩니다."
        }
    ],

    "params_table": [
        {"symbol": "m_s", "name": "Sprung mass", "typical": "400 kg", "simpack": "Body_Sprung → mass = 400"},
        {"symbol": "m_u", "name": "Unsprung mass", "typical": "40 kg", "simpack": "Body_Unsprung → mass = 40"},
        {"symbol": "k_s", "name": "Spring rate", "typical": "22 N/mm", "simpack": "FE_Spring → k_lin = 22000 N/m"},
        {"symbol": "c_s", "name": "Damper coeff", "typical": "1500 N·s/m", "simpack": "FE_Damper → c_lin = 1500"},
        {"symbol": "k_t", "name": "Tire stiffness", "typical": "200 N/mm", "simpack": "FE_Tire → k_lin = 200000 N/m"},
        {"symbol": "f₁_theory", "name": "Bounce freq (이론)", "typical": "1.18 Hz", "simpack": "Eigenvalue에서 확인"},
        {"symbol": "f₂_theory", "name": "Wheel hop freq (이론)", "typical": "11.25 Hz", "simpack": "Eigenvalue에서 확인"}
    ],

    "simpack_connection": "Quarter Car는 Simpack 모델 검증의 '기본 벤치마크'입니다. 이론값과 정확히 일치해야 더 복잡한 Full Vehicle 모델의 기반이 됩니다.",

    "deep_dive_title": "검증 실패 시 디버깅 체크리스트",
    "deep_dive_text": "고유진동수 오차 > 5%일 때: ① 단위 확인(N/mm → N/m 변환), ② Gravity 설정 확인(Static equilibrium 선 계산), ③ Joint DOF 확인(의도치 않은 DOF 잠김), ④ Marker 위치 확인(Center of Gravity와 부착점 불일치). 감쇠비 오차가 클 때: ⑤ Damper 단위(N·s/m), ⑥ Numerical damping 설정(적분기 파라미터).",

    "quiz": [
        {"type": "qa", "q": "Simpack에서 Quarter Car Eigenvalue Analysis 결과가 이론 Bounce 주파수보다 높게 나왔다. 가능한 원인 3가지를 서술하시오.", "a": "① Spring rate 단위 오류(N/mm를 N/m으로 변환하지 않아 1000배 과대), ② Sprung mass를 과소 입력, ③ Joint에 추가 강성(friction, stiffness stop)이 설정되어 유효 강성이 증가."},
        {"type": "qa", "q": "시간영역 Step Response에서 이론과 Simpack 결과의 '포락선'이 일치하는지 확인하는 방법을 설명하시오.", "a": "응답 피크들을 연결한 포락선이 e^(-ζωₙt)를 따르는지 확인. Log decrement 방법으로 연속 피크 비에서 ζ를 역산하여 이론 ζ와 비교."},
        {"type": "qa", "q": "모델 검증(Verification)과 모델 확인(Validation)의 차이를 설명하시오.", "a": "Verification: 수식이 올바르게 구현되었는지 확인(이론 vs 시뮬레이션). Validation: 시뮬레이션이 실제 물리를 올바르게 대표하는지 확인(시뮬레이션 vs 실차 시험). V&V는 순서대로 진행."}
    ],

    "next_preview": "Day 31에서는 Verification을 넘어 Validation으로 — FRF 시뮬레이션 결과와 실차 측정 데이터의 상관성 분석을 학습합니다."
}

# ═══════════════════════════════════════════════
# Day 31: FRF 시뮬레이션 vs 실측 상관성
# ═══════════════════════════════════════════════
DAY31 = {
    "day": 31,
    "part": "5",
    "part_title": "Simpack 완전 통합",
    "week": "",
    "title_ko": "FRF 시뮬레이션 vs 실측 상관성",
    "title_en": "FRF Simulation vs Test Correlation",
    "filename": "Day31_FRF상관성.html",
    "hero_eq": "Correlation Analysis",
    "difficulty": "★★★★☆",
    "num_formulas": "상관성 4지표",

    "brain_strategy": "시뮬레이션과 실측 FRF를 겹쳐보면 '어디가 맞고 어디가 틀린지' 눈에 보입니다. FRAC, MAC, 주파수 오차, 진폭 오차 — 4가지 정량 지표로 모델 품질을 숫자로 평가합니다.",

    "intuition_title": "시뮬레이션 ↔ 실차 시험 비교",
    "intuition_text": "Day 25에서 배운 FRF(주파수응답함수)를 시뮬레이션으로도 구할 수 있고, 실차 시험으로도 구할 수 있습니다. 두 FRF를 동일 그래프에 겹치면 — 공진 주파수, 피크 진폭, 반공진 위치에서 차이가 나타납니다. 이 차이를 정량화하고 줄여나가는 과정이 '모델 상관성 분석(Correlation)'이며, 디지털 트윈의 신뢰도를 결정합니다.",

    "deriv_steps": [
        {
            "step_title": "Step 1: Simpack FRF 추출",
            "equation": "Simpack → Analysis → Frequency Response → H(f) = Z_out(f) / Z_in(f)",
            "explain_meaning": "Simpack에서 FRF를 구하는 방법: Sine Sweep 또는 Random 입력을 가하고, 입력/출력의 FFT 비율로 FRF를 계산합니다. Virtual Sensor로 원하는 위치의 응답을 추출합니다.",
            "explain_sign": "입력: 노면 변위 z_r(t), 출력: 차체 가속도 z̈_s(t) → 전달함수 H(f) = Z̈_s(f)/Z_r(f).",
            "explain_prev": "Day 25의 H₁ 추정자 개념이 시뮬레이션에서도 동일하게 적용됩니다."
        },
        {
            "step_title": "Step 2: FRAC — 주파수응답 상관지표",
            "equation": "FRAC(f) = |H_sim(f)·H*_test(f)|² / (|H_sim(f)|²·|H_test(f)|²)",
            "explain_meaning": "FRAC(Frequency Response Assurance Criterion)은 각 주파수에서 시뮬레이션과 실측 FRF의 유사도를 0~1로 평가합니다. 1에 가까울수록 일치.",
            "explain_sign": "FRAC은 크기만 비교하고 위상은 고려하지 않습니다. 위상까지 포함하면 Complex FRAC 사용.",
            "explain_prev": "Day 25 Coherence γ²의 개념과 유사하지만, FRAC은 '두 FRF 간' 상관도입니다."
        },
        {
            "step_title": "Step 3: 주파수/진폭 오차 정량화",
            "equation": "Δf = (f_sim - f_test)/f_test × 100 [%]\nΔA = (|H_sim(f_peak)| - |H_test(f_peak)|)/|H_test(f_peak)| × 100 [%]",
            "explain_meaning": "공진 주파수 오차 Δf와 공진 진폭 오차 ΔA를 백분율로 계산합니다. 업계 기준: Δf < 5%, ΔA < 20%이면 양호.",
            "explain_sign": "양(+): 시뮬레이션이 과대 예측, 음(-): 과소 예측. 부호가 파라미터 조정 방향을 알려줍니다.",
            "explain_prev": "Day 24 PSD에서 배운 주파수 영역 비교 방법론의 확장입니다."
        },
        {
            "step_title": "Step 4: 모델 업데이트(Model Updating)",
            "equation": "min‖H_sim(p) - H_test‖² → 최적 파라미터 p* = [k_s*, c_s*, m_u*, ...]",
            "explain_meaning": "FRF 차이를 최소화하도록 모델 파라미터를 최적화합니다. 목적함수 = 시뮬레이션 FRF와 실측 FRF의 차이 제곱합. 설계변수 = 불확실성이 큰 파라미터(부싱 강성, 감쇠 등).",
            "explain_sign": "최적화 알고리즘: Gradient-based(Sensitivity) 또는 Population-based(GA, PSO). Simpack에서 SoS(Simpack Optimization Server) 사용.",
            "explain_prev": "이것이 Day 33 디지털 트윈의 핵심 — 실차 데이터로 모델을 지속 교정하는 과정입니다."
        }
    ],

    "params_table": [
        {"symbol": "FRAC", "name": "주파수응답 상관지표", "typical": "> 0.9 양호", "simpack": "Post-processing 계산"},
        {"symbol": "Δf", "name": "공진 주파수 오차", "typical": "< 5%", "simpack": "FRF 피크 비교"},
        {"symbol": "ΔA", "name": "공진 진폭 오차", "typical": "< 20%", "simpack": "FRF 피크 비교"},
        {"symbol": "MAC", "name": "Modal Assurance Criterion", "typical": "> 0.9", "simpack": "Mode shape 비교"},
        {"symbol": "p*", "name": "최적 파라미터", "typical": "반복 최적화", "simpack": "SoS 또는 외부 Optimizer"}
    ],

    "simpack_connection": "Simpack의 FRF 해석과 Model Updating 기능이 실차 데이터와의 상관성을 정량 평가하고 개선하는 핵심 도구입니다. SoS(Simpack Optimization Server)로 자동 파라미터 최적화가 가능합니다.",

    "deep_dive_title": "실무 상관성 분석 워크플로우",
    "deep_dive_text": "르노 실무 순서: ① 실차 계측(가속도계 4ch + 변위계 2ch) → ② 시험 FRF 추출(Welch PSD + H₁ estimator) → ③ Simpack FRF 추출(동일 입출력점) → ④ 오버레이 비교(Bounce/Pitch/Wheel Hop 영역) → ⑤ 감도분석(어떤 파라미터가 영향 큰지) → ⑥ Model Updating → ⑦ 검증 완료 판정. 통상 2~3회 반복으로 수렴.",

    "quiz": [
        {"type": "qa", "q": "FRAC과 MAC의 차이를 설명하시오.", "a": "FRAC은 두 FRF(주파수응답함수) 간의 유사도를 주파수별로 비교. MAC은 두 모드 형상(mode shape) 벡터 간의 유사도를 비교. FRAC은 전달함수 기반, MAC은 고유벡터 기반."},
        {"type": "qa", "q": "시뮬레이션 Bounce 주파수가 실측보다 10% 높게 나왔다. 어떤 파라미터를 어떻게 조정해야 하는가?", "a": "f_bounce ∝ √(k_s/m_s)이므로: ① k_s를 낮추거나(스프링 강성 과대 입력), ② m_s를 높이거나(차체 질량 과소 입력). 부싱 강성이 직렬로 작용하여 유효 강성을 높이는 경우도 확인."},
        {"type": "qa", "q": "Model Updating에서 '설계변수' 선정 기준은 무엇인가?", "a": "① 불확실성이 큰 파라미터(부싱 강성, 댐퍼 특성 등 비선형/노화 영향), ② 감도가 높은 파라미터(목적함수에 미치는 영향이 큰 것), ③ 물리적 범위 내에서 조정 가능한 파라미터. 측정으로 정확히 알 수 있는 질량은 보통 고정."}
    ],

    "next_preview": "Day 32에서는 MATLAB/Simulink와 Simpack을 연결하는 Co-Simulation 기법을 배워, 제어 로직과 플랜트 모델을 동시에 시뮬레이션합니다."
}

# ═══════════════════════════════════════════════
# Day 32: MATLAB/Simulink Co-Simulation
# ═══════════════════════════════════════════════
DAY32 = {
    "day": 32,
    "part": "5",
    "part_title": "Simpack 완전 통합",
    "week": "",
    "title_ko": "MATLAB/Simulink Co-Simulation",
    "title_en": "MATLAB/Simulink Co-Simulation Integration",
    "filename": "Day32_CoSimulation.html",
    "hero_eq": "상태공간 모델 연결",
    "difficulty": "★★★★☆",
    "num_formulas": "연동 4단계",

    "brain_strategy": "Simpack = 기구학/동역학 플랜트 모델, Simulink = 제어 알고리즘. 두 소프트웨어가 매 시간스텝마다 데이터를 주고받는 Co-Simulation이 현대 MBD의 핵심입니다.",

    "intuition_title": "플랜트 모델 + 제어 모델 = Co-Simulation",
    "intuition_text": "자동차의 물리적 거동(서스펜션 운동, 차체 진동)은 Simpack이 잘 계산합니다. 하지만 반능동 댐퍼(CDC)나 에어 서스펜션처럼 제어 로직이 필요한 시스템은 Simulink가 전문입니다. Co-Simulation은 두 소프트웨어를 매 통신 스텝마다 연결하여, 물리 + 제어를 동시에 시뮬레이션하는 기법입니다.",

    "deriv_steps": [
        {
            "step_title": "Step 1: Co-Simulation 아키텍처",
            "equation": "Simpack(Plant) ←→ Simulink(Controller)\n매 Δt_comm 마다: Simpack → 센서값 → Simulink → 제어명령 → Simpack",
            "explain_meaning": "통신 주기 Δt_comm마다 데이터를 교환합니다. Simpack은 현재 상태(변위, 속도, 가속도)를 Simulink에 전달하고, Simulink는 제어 명령(댐퍼력, 에어스프링 압력)을 Simpack에 전달합니다.",
            "explain_sign": "Δt_comm은 두 소프트웨어의 내부 적분 스텝보다 크거나 같아야 합니다. 너무 크면 안정성 문제, 너무 작으면 계산 시간 증가.",
            "explain_prev": "Day 21 Skyhook 제어에서 '이상적 제어력'을 수식으로 유도했는데, 이것이 Simulink 제어 블록으로 구현됩니다."
        },
        {
            "step_title": "Step 2: Simpack↔Simulink 인터페이스 설정",
            "equation": "Simpack: CoSim Interface → Input/Output Channels 정의\nSimulink: S-Function 또는 FMI(FMU) 블록",
            "explain_meaning": "Simpack에서 CoSimulation Interface를 활성화하고 입출력 채널을 정의합니다. Simulink에서는 S-Function 또는 FMU(Functional Mock-up Unit) 블록으로 Simpack 모델을 불러옵니다.",
            "explain_sign": "FMI 2.0 표준: 소프트웨어 독립적 인터페이스. Simpack FMU 내보내기 → Simulink에서 FMU Import. 가장 범용적 방법.",
            "explain_prev": "Day 05 상태공간 모델 ẋ=Ax+Bu, y=Cx+Du가 Co-Sim의 입출력 구조와 동일합니다."
        },
        {
            "step_title": "Step 3: 상태공간 연결 구조",
            "equation": "Simpack output: y = [z_s, ż_s, z_u, ż_u, z̈_s] (센서값)\nSimulink output: u = [F_damper, P_air] (제어명령)\n연결: ẋ_plant = f(x, u), y = g(x)",
            "explain_meaning": "Simpack이 플랜트의 상태를 출력하면, Simulink가 제어 법칙에 따라 액추에이터 명령을 계산하고, 이 명령이 다시 Simpack에 적용됩니다. 폐루프(Closed-loop) 시뮬레이션이 완성됩니다.",
            "explain_sign": "인과성(Causality): 센서→제어기→액추에이터→플랜트→센서의 순환. 시간 지연(1 step delay) 고려 필요.",
            "explain_prev": "Day 05에서 배운 상태공간 모형이 여기서 Simpack 플랜트 모델 전체를 표현합니다."
        },
        {
            "step_title": "Step 4: Co-Simulation 실행 & 검증",
            "equation": "Passive Damper 결과 vs CDC Co-Sim 결과 비교\n평가지표: RMS z̈_s (승차감), Dynamic Load Variation (안전성)",
            "explain_meaning": "제어 없는(Passive) 결과와 제어 있는(Co-Sim) 결과를 비교하여 제어 효과를 정량 평가합니다. 승차감(RMS 가속도 감소율)과 안전성(동적 하중 변동 감소율)이 핵심 지표입니다.",
            "explain_sign": "좋은 제어기 = RMS z̈_s 감소 + Dynamic Load Variation 미증가. 트레이드오프 개선이 최종 목표.",
            "explain_prev": "Day 21의 승차감 vs 조종안정성 트레이드오프가 Co-Sim으로 정량 평가됩니다."
        }
    ],

    "params_table": [
        {"symbol": "Δt_comm", "name": "통신 주기", "typical": "0.5~2 ms", "simpack": "CoSim Interface → Communication Step"},
        {"symbol": "y", "name": "센서 출력", "typical": "z_s, ż_s, z̈_s 등", "simpack": "Output Channels"},
        {"symbol": "u", "name": "제어 입력", "typical": "F_damper [N]", "simpack": "Input Channels"},
        {"symbol": "FMI", "name": "인터페이스 표준", "typical": "FMI 2.0", "simpack": "Export → FMU"},
        {"symbol": "RMS z̈_s", "name": "승차감 지표", "typical": "< 0.5 m/s²", "simpack": "Post-processing 계산"}
    ],

    "simpack_connection": "Simpack의 CoSimulation Interface와 FMU Export 기능이 MATLAB/Simulink와의 실시간 연동을 가능하게 합니다. CDC, 에어서스펜션, ADAS 등 제어 시스템 개발의 핵심 플랫폼입니다.",

    "deep_dive_title": "FMI 2.0 vs 직접 인터페이스",
    "deep_dive_text": "두 가지 연결 방법: ① FMI/FMU 방식 — 표준 기반으로 범용성이 높고 소프트웨어 독립적. Simpack을 FMU로 내보내면 Simulink, Adams, GT-SUITE 등 어디서나 사용 가능. ② 직접 인터페이스(Simpack-Simulink Direct) — 데이터 교환 효율이 더 높고 디버깅이 쉽지만 두 소프트웨어 버전 호환성 문제. 르노에서는 FMI 방식을 표준으로 사용하며, 이는 AUTOSAR 플랫폼과의 연계에도 유리합니다.",

    "quiz": [
        {"type": "qa", "q": "Co-Simulation에서 통신 주기(Δt_comm)를 너무 크게 설정하면 어떤 문제가 발생하는가?", "a": "제어기가 플랜트 상태 변화를 늦게 인식하여 제어 지연 발생, 심하면 수치 불안정(발산). 특히 고주파 Wheel Hop(10~15Hz) 제어 시 Δt_comm < T_hop/10 = 약 7ms 이하 필요."},
        {"type": "qa", "q": "Simpack FMU를 Simulink에서 사용하는 절차를 설명하시오.", "a": "① Simpack에서 CoSim Interface 설정 (입출력 채널 정의) → ② File → Export → FMU (FMI 2.0 Co-Simulation) → ③ Simulink에서 FMU Import 블록 배치 → ④ 입출력 포트 연결 → ⑤ Simulation Parameters에서 Fixed-step solver + 동일 Δt 설정."},
        {"type": "qa", "q": "Passive 서스펜션 대비 CDC(Continuously Damping Control)의 성능 이점을 정량적으로 어떻게 평가하는가?", "a": "동일 노면 입력에서: ① RMS z̈_s 감소율(승차감 개선 %), ② Peak z̈_s 감소율(충격 개선), ③ Dynamic Tire Load Variation 증감(안전성), ④ Suspension Travel RMS(패키징). 4개 지표를 레이더 차트로 비교."}
    ],

    "next_preview": "Day 33에서는 전체 33일의 학습을 총정리하며, 수식 → 시뮬레이션 → 실차 검증 → 디지털 트윈의 End-to-End 워크플로우를 완성합니다."
}

# ═══════════════════════════════════════════════
# Day 33: 디지털 트윈 완성 워크플로우
# ═══════════════════════════════════════════════
DAY33 = {
    "day": 33,
    "part": "5",
    "part_title": "Simpack 완전 통합",
    "week": "",
    "title_ko": "디지털 트윈 완성 워크플로우",
    "title_en": "Digital Twin — End-to-End Workflow",
    "filename": "Day33_디지털트윈완성.html",
    "hero_eq": "End-to-End Pipeline 총정리",
    "difficulty": "★★★☆☆",
    "num_formulas": "총정리 5단계",

    "brain_strategy": "33일간의 여정을 하나의 파이프라인으로 연결하세요: 수학 기초 → 진동 이론 → 구성요소 → 주파수 해석 → Simpack 통합. 이것이 디지털 트윈의 전체 그림입니다.",

    "intuition_title": "33일 여정의 총정리 — 디지털 트윈 완성",
    "intuition_text": "Day 01의 뉴턴 법칙에서 시작하여 Day 33에 도달했습니다. 단순한 1-DOF 스프링-질량 시스템부터 Full Vehicle 디지털 트윈까지, 모든 과정은 하나의 일관된 논리로 연결됩니다: '물리 현상을 수식으로 → 수식을 코드/시뮬레이션으로 → 시뮬레이션을 실차 데이터로 검증 → 검증된 모델로 예측 및 최적화'. 이것이 디지털 트윈의 본질입니다.",

    "deriv_steps": [
        {
            "step_title": "Pipeline Stage 1: 수학 기초 (Day 01~07)",
            "equation": "PART 1: mẍ + cẋ + kx = F(t) → 자유진동, 강제진동, 2-DOF, 행렬법, 상태공간",
            "explain_meaning": "모든 진동 해석의 기초: 뉴턴 법칙 → ODE → 해석해. 1-DOF에서 N-DOF까지 확장하는 행렬법과 상태공간 표현이 핵심. 이 수학이 없으면 시뮬레이션 결과를 해석할 수 없습니다.",
            "explain_sign": "핵심 산출물: ωₙ, ζ, 전달함수 H(s), 상태공간 [A,B,C,D]",
            "explain_prev": "33일 커리큘럼의 '뿌리'이자 '언어'입니다."
        },
        {
            "step_title": "Pipeline Stage 2: 서스펜션 이론 (Day 08~14)",
            "equation": "PART 2: Quarter/Half/Full Car 모델 → 승차감/조종안정성 평가지표",
            "explain_meaning": "수학 기초를 차량에 적용: Quarter Car(bounce, wheel hop) → Half Car(pitch) → Full Car(roll). ISO 2631 승차감 평가, 동적 하중 변동 분석. Simpack 모델 복잡도의 단계적 확장.",
            "explain_sign": "핵심 산출물: 차량 고유진동수, 모드 형상, 승차감/조종성 평가 지표",
            "explain_prev": "PART 1의 수학을 차량이라는 '시스템'에 적용한 것입니다."
        },
        {
            "step_title": "Pipeline Stage 3: 구성요소 (Day 15~21)",
            "equation": "PART 3: 스프링, 댐퍼, 부싱, 타이어 → 비선형, 주파수의존성, 트레이드오프",
            "explain_meaning": "실제 부품의 물리적 특성: 스프링의 비선형(progressive), 댐퍼의 비대칭(bound/rebound), 부싱의 주파수의존성(loss factor), 타이어의 수직 동특성. 이 실제 특성이 Simpack Force Element에 입력됩니다.",
            "explain_sign": "핵심 산출물: 각 부품의 특성 파라미터, Simpack Force Element 입력 데이터",
            "explain_prev": "PART 2의 '이상적 모델'에 '실제 부품 특성'을 부여한 것입니다."
        },
        {
            "step_title": "Pipeline Stage 4: 주파수 해석 (Day 22~28)",
            "equation": "PART 4: FFT, PSD, FRF, 고유치, 모드 중첩법 → 주파수 영역 분석 도구",
            "explain_meaning": "시간영역과 주파수영역을 자유자재로 오가는 해석 도구: FFT로 신호 분해, PSD로 에너지 분포, FRF로 시스템 특성 파악, 고유치/모드 해석으로 구조 동특성 이해.",
            "explain_sign": "핵심 산출물: 시험/시뮬레이션 데이터의 주파수 영역 분석 능력",
            "explain_prev": "PART 1~3에서 만든 모델을 '검증'하고 '진단'하는 도구입니다."
        },
        {
            "step_title": "Pipeline Stage 5: Simpack 통합 (Day 29~33)",
            "equation": "PART 5: 수식→Simpack 매핑, 모델 구축, V&V, Co-Simulation → 디지털 트윈",
            "explain_meaning": "모든 것을 통합: 수식 기호 → Simpack Element 매핑(Day 29) → 모델 구축 & 검증(Day 30) → 실차 상관성(Day 31) → Co-Simulation(Day 32) → 디지털 트윈 완성(Day 33). 이 5단계가 디지털 트윈 워크플로우의 전부입니다.",
            "explain_sign": "핵심 산출물: 실차와 상관이 검증된, 제어 로직까지 포함한 디지털 트윈 모델",
            "explain_prev": "PART 1~4의 모든 지식이 여기서 하나로 수렴합니다."
        }
    ],

    "params_table": [
        {"symbol": "PART 1", "name": "수학 기초", "typical": "Day 01~07", "simpack": "이론 기반 (수식 이해)"},
        {"symbol": "PART 2", "name": "서스펜션 이론", "typical": "Day 08~14", "simpack": "QC/HC/FC 모델 구조"},
        {"symbol": "PART 3", "name": "구성요소", "typical": "Day 15~21", "simpack": "Force Element 입력 데이터"},
        {"symbol": "PART 4", "name": "주파수 해석", "typical": "Day 22~28", "simpack": "V&V 분석 도구"},
        {"symbol": "PART 5", "name": "Simpack 통합", "typical": "Day 29~33", "simpack": "디지털 트윈 완성"}
    ],

    "simpack_connection": "33일의 학습이 하나의 디지털 트윈으로 수렴합니다. 수식(PART 1) → 모델 구조(PART 2) → 부품 데이터(PART 3) → 검증 도구(PART 4) → Simpack 통합(PART 5). 이 End-to-End 파이프라인이 디지털 트윈 엔지니어의 핵심 역량입니다.",

    "deep_dive_title": "디지털 트윈의 미래 — AI + MBD",
    "deep_dive_text": "디지털 트윈의 다음 단계: ① Physics-Informed Neural Networks(PINN) — 물리법칙을 학습한 신경망으로 실시간 예측, ② Surrogate Model — Simpack 대신 ML 모델로 1000배 빠른 최적화, ③ Online Model Updating — 실시간 센서 데이터로 모델 자동 교정, ④ Predictive Maintenance — 진동 패턴 변화로 부품 열화 예측. 오스트랄로님의 서스펜션 10년 경험 + 이 33일의 체계적 학습 + AI/ML 역량이 합쳐지면, 차세대 디지털 트윈 엔지니어로서의 경쟁력이 완성됩니다.",

    "quiz": [
        {"type": "qa", "q": "디지털 트윈의 5단계 파이프라인(PART 1~5)을 한 문장씩으로 요약하시오.", "a": "PART 1: 진동의 수학적 기초(ODE, 행렬법, 상태공간). PART 2: 차량 진동 모델(QC→HC→FC 확장). PART 3: 실제 부품 특성(비선형, 주파수의존성). PART 4: 주파수 영역 분석 도구(FFT, PSD, FRF, 모드 해석). PART 5: Simpack 통합(매핑, V&V, Co-Sim, 디지털 트윈)."},
        {"type": "qa", "q": "Verification과 Validation의 차이, 그리고 디지털 트윈에서 각각의 역할을 설명하시오.", "a": "Verification(검증): 수식이 코드/시뮬레이션에 올바르게 구현되었는가 → 이론값 vs 시뮬레이션. Validation(확인): 모델이 실제 물리를 대표하는가 → 시뮬레이션 vs 실차 시험. 디지털 트윈은 V&V를 반복하여 모델 신뢰도를 지속적으로 높입니다."},
        {"type": "qa", "q": "Physics-Informed Neural Network(PINN)이 기존 MBD 시뮬레이션 대비 갖는 장점과 한계를 서술하시오.", "a": "장점: ① 실시간 예측(수천배 빠름), ② 데이터+물리 하이브리드 학습으로 외삽 안정성, ③ 미분방정식 직접 학습으로 부분 데이터로도 학습 가능. 한계: ① 복잡한 비선형 접촉/마찰에 약함, ② 학습 데이터 범위 밖 정확도 불확실, ③ 모델 해석성(Interpretability) 부족."}
    ],

    "next_preview": "축하합니다! 33일의 여정을 완주하셨습니다. 수학 기초부터 디지털 트윈까지, 차량 진동학의 전체 파이프라인을 체계적으로 학습하셨습니다. 이제 실무에서 이 지식을 적용하며 진정한 디지털 트윈 엔지니어로 성장하세요."
}
