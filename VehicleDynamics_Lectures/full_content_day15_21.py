"""
Day 15~21 풀콘텐츠
Day 15: Part 2 통합 복습
Day 16~21: PART 3 서스펜션 세부 수식
"""

DAY15 = {
    "day": 15,
    "part": 2,
    "part_title": "차량 진동 모델",
    "title_ko": "Part 2 통합 복습",
    "title_en": "Part 2 Comprehensive Review",
    "filename": "Day15_Part2복습.html",
    "hero_eq": "모델 복잡도별 비교 정리",
    "difficulty": "★☆☆☆☆",
    "brain_strategy": {
        "technique": "통합 맵핑 (Integration Mapping)",
        "pre_routine": "Day 08~14 핵심 수식 카드를 책상에 펼치고, 각 카드 사이에 '화살표'로 연결 관계를 그려본다. 쿼터카 → 하프카 → 전달함수 → 노면까지 하나의 흐름이 보이면 준비 완료."
    },
    "intuition": "PART 2에서 1DOF를 2DOF·4DOF로 확장하고 전달함수·스펙트럼까지 다뤘다. 이 Day에서는 모델 복잡도별 핵심을 비교하고, 각 모델이 어떤 질문에 답하는지를 정리한다. '쿼터카로 충분한 문제'와 '하프카가 필요한 문제'를 명확히 구분할 수 있으면 실무 판단력이 올라간다.",
    "deriv_steps": [
        {
            "step_title": "Step 1: 모델 복잡도 계층 정리",
            "equation": "1DOF → 2DOF(쿼터카) → 4DOF(하프카) → Full(7DOF+)",
            "explain_meaning": "각 모델이 추가하는 자유도: 1DOF(스프렁만), 2DOF(스프렁+언스프렁), 4DOF(바운스+피치+앞뒤 언스프렁), Full(롤·요 추가).",
            "explain_sign": "모델이 복잡해질수록 커플링 현상(pitch-bounce, roll-pitch 등)을 포착할 수 있다.",
            "explain_prev": "Day 01~07(1DOF) → Day 08~11(2DOF/4DOF) → Day 12~14(주파수 영역) 순서로 학습했다."
        },
        {
            "step_title": "Step 2: 각 모델의 핵심 방정식 요약",
            "equation": "쿼터카: [M]{ẍ} + [C]{ẋ} + [K]{x} = {F},  하프카: 4×4 매트릭스",
            "explain_meaning": "쿼터카의 2×2 매트릭스(m_s, m_u)는 수직 바운스만 다루고, 하프카의 4×4는 바운스-피치 커플링을 포함한다.",
            "explain_sign": "하프카에서 비대각 항(off-diagonal)이 커플링 강도를 결정하며, a·k_f = b·k_r이면 디커플링된다.",
            "explain_prev": "Day 08(쿼터카 구성) → Day 10(하프카 구성) → Day 11(모드 해석)에서 각각 유도했다."
        },
        {
            "step_title": "Step 3: 주파수 영역 도구 정리",
            "equation": "H(s) = X(s)/F(s),  T(ω) = |X_out/X_in|,  PSD: S_a(f) = |H|² · S_z(f)",
            "explain_meaning": "전달함수 H(s)는 시스템 DNA, 전달률 T(ω)는 방진 성능, PSD 연쇄는 노면→응답 예측의 핵심이다.",
            "explain_sign": "T(ω) < 1이면 진동 격리 성공, |H|²이 크면 그 주파수에서 응답이 증폭된다.",
            "explain_prev": "Day 12(전달함수) → Day 13(전달률) → Day 14(노면 PSD·ISO 2631)에서 유도했다."
        }
    ],
    "params": [
        {"sym": "DOF", "name_ko": "자유도", "name_en": "Degree of Freedom", "unit": "—", "meaning": "모델이 표현하는 독립 운동 수", "vehicle": "쿼터카=2, 하프카=4, 풀카=7+", "range": "1~14+"},
        {"sym": "a_w", "name_ko": "가중 RMS 가속도", "name_en": "Weighted RMS Acceleration", "unit": "m/s²", "meaning": "ISO 2631 승차감 지표", "vehicle": "승차감 평가 최종 출력", "range": "0.1~1.5"}
    ],
    "simpack_mappings": [
        {"sym": "Model", "path": "Substructure > Quarter/Half/Full", "field": "DOF 선택", "unit": "—", "warn": "분석 목적에 맞는 최소 복잡도 모델을 선택해야 계산 비용을 줄일 수 있다"}
    ],
    "deep_dive_title": "실무 판단: 언제 어떤 모델을 쓸까?",
    "deep_dive_content": "순수 수직 승차감 → 쿼터카로 충분. 전후 피치 모션(브레이킹 노즈다이브, 가속 스쿼트) 분석 → 하프카 필수. 코너링 롤·요 → 풀카(7DOF+). Simpack에서도 연구 초기엔 쿼터카로 파라미터 스터디를 빠르게 돌리고, 최종 검증만 풀카로 하는 것이 효율적이다. OEM 현업에서는 '60% 쿼터카, 30% 하프카, 10% 풀카' 비율로 해석을 수행한다.",
    "quiz": [
        {"type": "fill", "q": "쿼터카 모델의 자유도 수는 ___이다.", "a": "2 (스프렁 질량 + 언스프렁 질량)"},
        {"type": "meaning", "q": "하프카에서 디커플링 조건 a·k_f = b·k_r의 물리적 의미는?", "a": "전후 스프링 강성비가 무게중심 위치비와 일치하면 바운스와 피치가 독립적으로 진동한다"},
        {"type": "simpack", "q": "Simpack에서 쿼터카 모델을 먼저 사용하는 이유는?", "a": "파라미터 수가 적어 빠른 스위프 분석이 가능하고, 수직 방향 기본 특성을 신속히 파악할 수 있다"}
    ],
    "next_preview_title": "Day 16 미리보기: 스프링 특성",
    "next_preview": "PART 3 시작! 서스펜션의 가장 기본 요소인 스프링의 직렬/병렬 합성, 비선형(progressive) 특성, 그리고 Simpack에서의 Force Element 입력법을 다룬다."
}

DAY16 = {
    "day": 16,
    "part": 3,
    "part_title": "서스펜션 세부 수식",
    "title_ko": "스프링 특성",
    "title_en": "Spring Characteristics — Series/Parallel",
    "filename": "Day16_스프링특성.html",
    "hero_eq": "1/k_eq = 1/k₁ + 1/k₂ (직렬)",
    "difficulty": "★★☆☆☆",
    "brain_strategy": {
        "technique": "물리 직관 연결 (Physical Analogy)",
        "pre_routine": "볼펜 스프링을 두 개 꺼내서 직렬(끝과 끝 연결)과 병렬(나란히 묶기)을 직접 손으로 눌러본다. 직렬이 더 부드럽고, 병렬이 더 뻣뻣한 촉감을 기억한 뒤 시작."
    },
    "intuition": "서스펜션에서 스프링은 '에너지 저장 장치'다. 코일 스프링, 에어 스프링, 토션 바 — 형태는 달라도 F = k·x가 기본이다. 여러 스프링이 조합되면 직렬(부드러워짐)과 병렬(뻣뻣해짐)의 합성 법칙을 따른다. 현가장치에서 메인 스프링 + 범프 스톱은 직렬이 아닌 병렬이며, 이 구분이 실무 설계의 출발점이다.",
    "deriv_steps": [
        {
            "step_title": "Step 1: 병렬 스프링 합성",
            "equation": "k_eq = k₁ + k₂",
            "explain_meaning": "병렬: 두 스프링이 같은 변위 x를 공유하고 힘이 합산된다. F_total = F₁ + F₂ = k₁x + k₂x = (k₁+k₂)x.",
            "explain_sign": "합성 강성은 항상 개별 강성보다 크다 → 시스템이 더 뻣뻣해진다.",
            "explain_prev": "Day 01에서 단일 스프링 F = kx를 유도했다. 이를 두 개로 확장한다."
        },
        {
            "step_title": "Step 2: 직렬 스프링 합성",
            "equation": "1/k_eq = 1/k₁ + 1/k₂  →  k_eq = k₁k₂/(k₁+k₂)",
            "explain_meaning": "직렬: 두 스프링에 같은 힘 F가 작용하고 변위가 합산된다. x_total = x₁ + x₂ = F/k₁ + F/k₂.",
            "explain_sign": "합성 강성은 항상 개별 강성보다 작다 → 시스템이 더 부드러워진다.",
            "explain_prev": "병렬과 반대 패턴이다. 전기회로의 저항 병렬 합성(1/R = 1/R₁ + 1/R₂)과 형태가 같다."
        },
        {
            "step_title": "Step 3: 비선형 스프링 (Progressive Rate)",
            "equation": "F(x) = k₁x + k₃x³  (하드닝 스프링: k₃ > 0)",
            "explain_meaning": "코일 스프링의 피치가 변하거나 범프 스톱이 접촉하면 변위가 커질수록 강성이 증가한다.",
            "explain_sign": "k₃ > 0이면 하드닝(hardening) — 큰 입력에서 강성 증가로 바닥 침(bottoming) 방지. k₃ < 0이면 소프트닝(softening).",
            "explain_prev": "Day 05(강제진동)에서 선형 스프링만 다뤘다. 실차에서는 비선형이 필수다."
        },
        {
            "step_title": "Step 4: Wheel Rate와 Spring Rate의 관계",
            "equation": "k_wheel = k_spring · (MR)²",
            "explain_meaning": "Motion Ratio(MR)는 '스프링 변위 / 휠 변위'의 비율이다. MR < 1이면 스프링이 휠보다 적게 움직여서 휠 레이트가 스프링 레이트보다 작아진다.",
            "explain_sign": "MR² 형태인 이유: 에너지 보존 ½k_s·δ_s² = ½k_w·δ_w² → k_w = k_s·(δ_s/δ_w)² = k_s·MR².",
            "explain_prev": "Day 09에서 쿼터카 고유진동수를 구할 때 wheel rate 개념이 잠시 등장했다. 여기서 정식으로 유도한다."
        }
    ],
    "params": [
        {"sym": "k_s", "name_ko": "스프링 강성", "name_en": "Spring Rate", "unit": "N/mm", "meaning": "단위 변위당 스프링 복원력", "vehicle": "코일 스프링 제원표", "range": "15~80"},
        {"sym": "k_w", "name_ko": "휠 레이트", "name_en": "Wheel Rate", "unit": "N/mm", "meaning": "휠 센터 기준 등가 강성", "vehicle": "k_s × MR²", "range": "10~50"},
        {"sym": "MR", "name_ko": "모션 비", "name_en": "Motion Ratio", "unit": "—", "meaning": "스프링 변위 / 휠 변위", "vehicle": "기구학 해석에서 산출", "range": "0.5~1.0"},
        {"sym": "k₃", "name_ko": "3차 비선형 계수", "name_en": "Cubic Stiffness", "unit": "N/mm³", "meaning": "Progressive 특성 크기", "vehicle": "범프스톱 특성", "range": "0.001~0.1"}
    ],
    "simpack_mappings": [
        {"sym": "k_s", "path": "Force Element > Spring > Stiffness", "field": "Spring Rate [N/mm]", "unit": "N/mm", "warn": "Simpack 입력은 N/mm 단위 — SI(N/m) 변환 주의"},
        {"sym": "F(x)", "path": "Force Element > Spring > Nonlinear > F-x Curve", "field": "Force-Displacement 테이블", "unit": "N vs mm", "warn": "범프스톱 포함 시 테이블 끝점에서 강성 급증 → 적분 시간 스텝 자동 조절 확인"}
    ],
    "deep_dive_title": "에어 스프링 vs 코일 스프링: 강성 비교",
    "deep_dive_content": "에어 스프링의 강성은 압력·체적의 함수: k_air = n·P·A²/V (n=폴리트로픽 지수). 코일 스프링은 k = Gd⁴/(8D³N)으로 재질과 기하학에 의해 결정된다. 에어 스프링은 하중에 따라 압력을 조절해 차고를 일정하게 유지할 수 있어 프리미엄 차량에 사용된다. Simpack에서는 에어 스프링 전용 Force Element(압력-체적 커브)를 제공한다.",
    "quiz": [
        {"type": "fill", "q": "직렬 스프링 합성 공식: 1/k_eq = 1/k₁ + 1/k₂에서 k₁=20, k₂=30이면 k_eq = ___N/mm.", "a": "12 (= 20×30/(20+30) = 600/50)"},
        {"type": "meaning", "q": "범프스톱이 메인 스프링과 '병렬'인 이유는?", "a": "둘 다 같은 변위(휠 트래블)를 공유하고 힘이 합산되기 때문이다. 범프스톱 접촉 후 합성 강성이 급증한다."},
        {"type": "simpack", "q": "Simpack에서 비선형 스프링을 입력하는 방법은?", "a": "Force Element > Spring > Nonlinear에서 F-x 곡선을 테이블(포인트별)로 입력한다"}
    ],
    "next_preview_title": "Day 17 미리보기: 댐퍼(쇽업쇼버) 모델",
    "next_preview": "내일은 서스펜션의 에너지 소산 장치인 쇽업쇼버를 다룬다. F-v 특성 곡선, 바운드/리바운드 비대칭, Maxwell 모델까지!"
}

DAY17 = {
    "day": 17,
    "part": 3,
    "part_title": "서스펜션 세부 수식",
    "title_ko": "댐퍼(쇽업쇼버) 모델",
    "title_en": "Damper Model — F-v Curve & Maxwell",
    "filename": "Day17_댐퍼모델.html",
    "hero_eq": "F = cv, Maxwell 모델",
    "difficulty": "★★★☆☆",
    "brain_strategy": {
        "technique": "대비 학습 (Contrast Learning)",
        "pre_routine": "어제 스프링(에너지 저장)과 오늘 댐퍼(에너지 소산)를 머릿속에서 대비시킨다. 스프링은 '변위에 비례하는 힘', 댐퍼는 '속도에 비례하는 힘' — 이 한 줄 차이를 3번 반복한 뒤 시작."
    },
    "intuition": "댐퍼(쇽업쇼버)는 운동 에너지를 열로 변환하는 장치다. 오일이 좁은 밸브를 통과할 때 저항이 생기고, 이 저항력이 F = c·v (감쇠력 = 감쇠계수 × 속도)다. 실제 댐퍼는 바운드(압축)와 리바운드(인장)에서 감쇠력이 다르고, 고속에서는 블로오프 밸브가 열려 감쇠력 증가가 둔화된다.",
    "deriv_steps": [
        {
            "step_title": "Step 1: 선형 점성 감쇠 모델",
            "equation": "F_d = c · ẋ",
            "explain_meaning": "감쇠력 F_d는 피스톤 속도 ẋ에 비례한다. c는 감쇠계수[N·s/m].",
            "explain_sign": "ẋ > 0(리바운드/인장)이면 F > 0(인장력), ẋ < 0(바운드/압축)이면 F < 0(압축력). 항상 운동 방향을 저항한다.",
            "explain_prev": "Day 03에서 감쇠비 ζ = c/(2√(km))를 정의했다. 여기서 c의 물리적 실체를 다룬다."
        },
        {
            "step_title": "Step 2: 바운드/리바운드 비대칭 모델",
            "equation": "F_d = c_b · ẋ  (ẋ < 0, 바운드)  |  F_d = c_r · ẋ  (ẋ > 0, 리바운드)",
            "explain_meaning": "리바운드 감쇠 c_r이 바운드 감쇠 c_b보다 2~4배 크다. 이는 범프 입력 시 빠르게 흡수(부드러운 바운드)하고, 스프링 복원 시 천천히 돌아오게(강한 리바운드) 하기 위함이다.",
            "explain_sign": "c_r/c_b ≈ 2~4. 이 비율이 승차감과 접지력의 균형을 결정한다.",
            "explain_prev": "Day 03의 감쇠비 ζ는 선형 모델 기준이었다. 비대칭 모델에서는 등가 감쇠비를 에너지 등가법으로 구한다."
        },
        {
            "step_title": "Step 3: 블로오프 밸브 (Blow-off) 효과",
            "equation": "F = c₁·ẋ (|ẋ| ≤ v_b),  F = c₁·v_b + c₂·(ẋ - v_b) (|ẋ| > v_b),  c₂ < c₁",
            "explain_meaning": "저속 구간에서는 높은 감쇠 c₁으로 제어성을 확보하고, 고속(v_b 이상)에서는 낮은 c₂로 전환되어 충격을 완화한다.",
            "explain_sign": "v_b는 블로오프 속도(0.1~0.3 m/s). 이 지점에서 F-v 기울기가 꺾인다.",
            "explain_prev": "Day 05의 강제진동에서 감쇠는 일정하다고 가정했다. 실차에서는 이 비선형이 핵심이다."
        },
        {
            "step_title": "Step 4: Maxwell 모델 (댐퍼 + 직렬 스프링)",
            "equation": "F = c · (ẋ₁ - ẋ₂),  x₁ - x₂ = F/k_rod + ∫F/c dt",
            "explain_meaning": "실제 쇽업쇼버의 로드(rod)에는 탄성이 있다. Maxwell 모델은 스프링과 댐퍼를 직렬로 연결하여 고주파에서의 댐퍼 강성 효과를 표현한다.",
            "explain_sign": "주파수가 높아지면 댐퍼 임피던스가 증가하여 마치 강체처럼 행동 → 고주파 전달 증가.",
            "explain_prev": "Day 16의 직렬 스프링 합성 개념이 여기서 '스프링 + 댐퍼 직렬'로 확장된다."
        }
    ],
    "params": [
        {"sym": "c", "name_ko": "감쇠계수", "name_en": "Damping Coefficient", "unit": "N·s/m", "meaning": "속도당 감쇠력", "vehicle": "쇽업쇼버 F-v 곡선 기울기", "range": "500~5000"},
        {"sym": "c_b", "name_ko": "바운드 감쇠", "name_en": "Bump Damping", "unit": "N·s/m", "meaning": "압축 방향 감쇠", "vehicle": "밸브 셋팅(바운드 측)", "range": "500~2000"},
        {"sym": "c_r", "name_ko": "리바운드 감쇠", "name_en": "Rebound Damping", "unit": "N·s/m", "meaning": "인장 방향 감쇠", "vehicle": "밸브 셋팅(리바운드 측)", "range": "1500~6000"},
        {"sym": "v_b", "name_ko": "블로오프 속도", "name_en": "Blow-off Velocity", "unit": "m/s", "meaning": "감쇠 기울기 전환점", "vehicle": "밸브 크랙 압력에 의존", "range": "0.1~0.3"}
    ],
    "simpack_mappings": [
        {"sym": "c(v)", "path": "Force Element > Damper > F-v Curve", "field": "Force vs Velocity 테이블", "unit": "N vs m/s", "warn": "바운드/리바운드 양쪽 데이터 모두 입력 — 1사분면+3사분면 데이터 필요"},
        {"sym": "k_rod", "path": "Force Element > Damper > Series Stiffness", "field": "Rod Stiffness [N/mm]", "unit": "N/mm", "warn": "Maxwell 모델 사용 시 활성화. 값이 너무 크면(>10⁶) 수치 강성(stiff) 문제 발생"}
    ],
    "deep_dive_title": "CDC/MR 댐퍼: 가변 감쇠 기술",
    "deep_dive_content": "CDC(Continuous Damping Control)는 솔레노이드 밸브로 오리피스 면적을 실시간 조절한다. MR(Magneto-Rheological) 댐퍼는 자기장으로 MR 유체의 점도를 변화시킨다. 둘 다 c(t)를 제어 입력으로 사용하며, Simpack에서는 Co-simulation 또는 User Subroutine으로 구현한다. Skyhook 제어: c = c_max if ẋ_body · (ẋ_body - ẋ_wheel) > 0, else c_min.",
    "quiz": [
        {"type": "fill", "q": "리바운드/바운드 감쇠비 c_r/c_b의 일반적 범위는 ___배이다.", "a": "2~4"},
        {"type": "meaning", "q": "블로오프 밸브가 열리면 왜 승차감이 좋아지는가?", "a": "고속 충격 입력에서 감쇠력 증가가 둔화되어 탑승자에게 전달되는 충격 피크가 감소한다"},
        {"type": "simpack", "q": "Simpack에서 댐퍼 F-v 곡선 입력 시 주의할 점은?", "a": "바운드(음의 속도)와 리바운드(양의 속도) 양쪽 데이터를 모두 입력해야 하며, 원점(0,0)을 반드시 포함해야 한다"}
    ],
    "next_preview_title": "Day 18 미리보기: 부싱 복소강성",
    "next_preview": "내일은 서스펜션 조인트의 숨은 주역 — 고무 부싱! 복소강성 K* = K'(1+iη)로 주파수 의존성과 손실계수를 모델링한다."
}

DAY18 = {
    "day": 18,
    "part": 3,
    "part_title": "서스펜션 세부 수식",
    "title_ko": "부싱 복소강성",
    "title_en": "Bushing Complex Stiffness K*",
    "filename": "Day18_부싱복소강성.html",
    "hero_eq": "K* = K'(1 + iη)",
    "difficulty": "★★★☆☆",
    "brain_strategy": {
        "technique": "복소수 시각화 (Complex Plane Visualization)",
        "pre_routine": "복소 평면을 그리고, 실축(탄성)과 허축(손실)을 표시한다. K'가 실축 길이, K''가 허축 길이, η = K''/K'가 기울기 각도의 탄젠트임을 떠올린 뒤 시작."
    },
    "intuition": "고무 부싱은 스프링이면서 동시에 댐퍼다. 변형하면 일부 에너지는 저장(탄성)되고 일부는 열로 소산(점성)된다. 이 두 성질을 하나로 표현하는 것이 복소강성 K* = K' + iK''이다. K'(저장강성)은 복원력, K''(손실강성)은 감쇠력을 담당한다. 주파수가 올라가면 K'도 K''도 변한다 — 이것이 '주파수 의존성'이다.",
    "deriv_steps": [
        {
            "step_title": "Step 1: 조화 가진 하의 힘-변위 관계",
            "equation": "x(t) = X₀ e^{iωt},  F(t) = K* · x(t) = (K' + iK'') X₀ e^{iωt}",
            "explain_meaning": "조화 변위 입력에 대해 힘은 변위와 같은 주파수지만 위상이 다르다. K'은 변위와 동위상 성분(in-phase), K''은 90° 앞선 성분(quadrature).",
            "explain_sign": "K'' > 0이면 힘이 변위보다 앞서고, 에너지가 소산된다(히스테리시스 루프 면적 > 0).",
            "explain_prev": "Day 06에서 위상각 φ를 배웠다. 부싱의 위상 지연은 η = tanδ로 표현된다."
        },
        {
            "step_title": "Step 2: 손실계수(Loss Factor) 정의",
            "equation": "η = K''/K' = tanδ",
            "explain_meaning": "η(에타)는 1사이클에서 소산된 에너지 / (2π × 최대 저장 에너지)의 비율이다. δ는 힘과 변위 사이의 위상차(loss angle).",
            "explain_sign": "η ≈ 0.05~0.3이 일반 고무 범위. η가 클수록 NVH(소음진동) 감쇠에 유리하지만 열 발생도 증가.",
            "explain_prev": "Day 03의 감쇠비 ζ와 관계: 1DOF에서 η ≈ 2ζ (작은 감쇠 근사)."
        },
        {
            "step_title": "Step 3: 주파수 의존성 모델",
            "equation": "K'(f) = K₀ · (1 + α · log₁₀(f/f₀)),  η(f) ≈ η₀ · (f/f₀)^β",
            "explain_meaning": "고무의 저장강성은 주파수가 10배 올라갈 때 α만큼 증가(동적 경화 효과). 손실계수도 주파수에 따라 변한다.",
            "explain_sign": "α > 0 → 주파수 증가 시 부싱이 뻣뻣해짐. β > 0이면 고주파에서 손실 증가.",
            "explain_prev": "Day 05 강제진동에서 k는 상수였다. 부싱에서는 k(ω)로 주파수 함수가 된다."
        },
        {
            "step_title": "Step 4: Kelvin-Voigt 모델과의 관계",
            "equation": "K* = k + iωc  →  K' = k, K'' = ωc  →  η = ωc/k",
            "explain_meaning": "Kelvin-Voigt(스프링 + 댐퍼 병렬) 모델에서 복소강성을 유도하면 손실강성이 주파수에 비례한다.",
            "explain_sign": "이 모델은 고주파에서 η가 무한대로 발산하는 비물리적 문제가 있다 → 실무에서는 테이블 입력이 안전.",
            "explain_prev": "Day 17의 Maxwell 모델은 직렬, Kelvin-Voigt는 병렬. 두 모델의 차이를 복소강성으로 비교할 수 있다."
        }
    ],
    "params": [
        {"sym": "K'", "name_ko": "저장강성", "name_en": "Storage Stiffness", "unit": "N/mm", "meaning": "탄성 복원력 성분", "vehicle": "부싱 동적 시험 결과", "range": "50~5000"},
        {"sym": "K''", "name_ko": "손실강성", "name_en": "Loss Stiffness", "unit": "N/mm", "meaning": "에너지 소산 성분", "vehicle": "K' × η", "range": "5~500"},
        {"sym": "η", "name_ko": "손실계수", "name_en": "Loss Factor", "unit": "—", "meaning": "감쇠 능력 지표", "vehicle": "고무 물성 시험", "range": "0.05~0.3"},
        {"sym": "δ", "name_ko": "손실각", "name_en": "Loss Angle", "unit": "deg", "meaning": "힘-변위 위상차", "vehicle": "δ = arctan(η)", "range": "3~17°"}
    ],
    "simpack_mappings": [
        {"sym": "K*(f)", "path": "Force Element > Bushing > Frequency Dependent", "field": "K'(f), η(f) 테이블", "unit": "N/mm, —", "warn": "주파수별 K'과 η 테이블을 별도로 입력. 보간 방법(선형/로그)을 확인할 것"},
        {"sym": "K_static", "path": "Force Element > Bushing > Static Stiffness", "field": "Static Rate [N/mm]", "unit": "N/mm", "warn": "동적 강성은 정적 강성의 1.2~2.0배 — 정적값만 넣으면 과소 평가"}
    ],
    "deep_dive_title": "부싱 시험법: 왜 주파수 스위프가 필요한가?",
    "deep_dive_content": "부싱 동특성 시험은 일반적으로 1~100Hz 주파수 스위프로 수행한다. 진폭은 ±0.1~±1.0mm (소진폭)와 ±3~±5mm(대진폭)를 나눠서 측정한다. 큰 이유: (1) 고무의 Payne 효과 — 진폭이 커지면 K'이 감소하고 η가 증가한다. (2) Mullins 효과 — 첫 사이클은 이후와 다르므로 컨디셔닝 사이클이 필요하다. Simpack에 입력할 때는 실차 작동 진폭에 해당하는 데이터를 선택해야 한다.",
    "quiz": [
        {"type": "fill", "q": "손실계수 η = K''/K'에서, K' = 200 N/mm이고 η = 0.15이면 K'' = ___N/mm.", "a": "30 (= 200 × 0.15)"},
        {"type": "meaning", "q": "Kelvin-Voigt 모델의 한계는 무엇인가?", "a": "η = ωc/k로 주파수에 비례하여, 고주파에서 비물리적으로 큰 손실계수를 예측한다"},
        {"type": "simpack", "q": "Simpack에서 부싱의 정적 강성만 입력하면 어떤 문제가 발생하는가?", "a": "동적 강성이 정적 강성의 1.2~2.0배이므로, 고주파 영역에서 강성을 과소평가하여 진동 전달을 과대 예측한다"}
    ],
    "next_preview_title": "Day 19 미리보기: 타이어 수직 동특성",
    "next_preview": "타이어는 '두 번째 스프링'이다. 타이어의 수직 강성 k_t, 감쇠, 그리고 접지 패치 필터 효과를 다룬다."
}

DAY19 = {
    "day": 19,
    "part": 3,
    "part_title": "서스펜션 세부 수식",
    "title_ko": "타이어 수직 동특성",
    "title_en": "Tire Vertical Dynamics",
    "filename": "Day19_타이어수직동특성.html",
    "hero_eq": "f_t = (1/2π)√(k_t/m_u)",
    "difficulty": "★★★☆☆",
    "brain_strategy": {
        "technique": "스케일 사고 (Scale Thinking)",
        "pre_routine": "타이어를 손으로 눌러본 경험을 떠올린다. 서스펜션 스프링보다 10배 뻣뻣한 느낌 — k_t ≈ 200 N/mm vs k_s ≈ 20 N/mm. 이 '10배' 스케일 차이가 two-mass 시스템의 두 고유진동수를 분리시킨다."
    },
    "intuition": "쿼터카 모델에서 타이어는 '노면과 언스프렁 질량 사이의 스프링'이다. 타이어 강성 k_t는 공기압, 하중, 속도에 따라 변하고, 접지 패치(contact patch)의 유한 길이가 고주파 노면 입력을 필터링한다. 타이어 hop 주파수(~12Hz)는 서스펜션 바운스(~1.2Hz)보다 10배 높아서 두 모드가 자연스럽게 분리된다.",
    "deriv_steps": [
        {
            "step_title": "Step 1: 타이어 수직 강성 기본 모델",
            "equation": "F_t = k_t · (z_road - z_u)",
            "explain_meaning": "타이어 수직력은 노면 변위 z_road와 언스프렁 질량 변위 z_u의 차이에 비례한다.",
            "explain_sign": "z_road > z_u (범프)이면 F_t > 0 (위쪽 힘). 타이어가 노면에서 떨어지면(z_u - z_road > δ_static) 인장력 불가 → F_t = 0 (리프트오프).",
            "explain_prev": "Day 08 쿼터카 모델에서 k_t를 사용했다. 여기서는 k_t의 물리적 의미와 측정법을 다룬다."
        },
        {
            "step_title": "Step 2: 공기압과 강성의 관계",
            "equation": "k_t ≈ k₀ + α_p · (P - P₀)",
            "explain_meaning": "타이어 강성은 기준 공기압 P₀에서의 강성 k₀에 압력 감도 α_p를 더한 선형 근사로 표현된다.",
            "explain_sign": "α_p > 0: 공기압 증가 → 강성 증가 → 승차감 악화, 접지력 향상. 일반적으로 α_p ≈ 3~5 N/mm/bar.",
            "explain_prev": "Day 16에서 스프링 강성의 비선형을 다뤘다. 타이어도 비선형이지만 작동 범위에서 선형 근사가 유효하다."
        },
        {
            "step_title": "Step 3: 접지 패치 필터 효과",
            "equation": "H_cp(f) = sin(πfL/V) / (πfL/V)",
            "explain_meaning": "접지 패치 길이 L이 유한하므로, 노면 요철 중 파장이 L보다 짧은 성분은 평균화되어 감쇠된다. 이것이 sinc 함수 형태의 저역통과 필터(LPF)다.",
            "explain_sign": "f·L/V > 1이면 H_cp → 0: 차속 V가 빠르거나 패치 L이 작으면 필터 차단주파수가 올라가서 고주파 노면 입력이 더 많이 전달된다.",
            "explain_prev": "Day 14에서 노면 PSD를 다뤘다. 접지 패치 필터는 PSD가 타이어에 입력되기 전에 적용되는 물리적 LPF다."
        },
        {
            "step_title": "Step 4: 타이어 감쇠와 등가 감쇠비",
            "equation": "c_t ≈ 0.01 ~ 0.05 × 2√(k_t · m_u)",
            "explain_meaning": "타이어 감쇠는 고무 히스테리시스에 의한 것으로, 쇽업쇼버에 비해 매우 작다(ζ_t ≈ 1~5%).",
            "explain_sign": "ζ_t가 작으므로 타이어 hop 모드는 감쇠가 부족 — 이것이 'shimmy', 'wheel hop' 등의 원인이 된다.",
            "explain_prev": "Day 03의 감쇠비 ζ 정의를 타이어에 적용한다. Day 18의 고무 손실계수 η와도 연결: ζ_t ≈ η_tire/2."
        }
    ],
    "params": [
        {"sym": "k_t", "name_ko": "타이어 수직강성", "name_en": "Tire Vertical Stiffness", "unit": "N/mm", "meaning": "타이어의 수직 스프링 상수", "vehicle": "타이어 제원표 / 시험", "range": "150~250"},
        {"sym": "c_t", "name_ko": "타이어 감쇠", "name_en": "Tire Damping", "unit": "N·s/m", "meaning": "타이어 고무의 에너지 소산", "vehicle": "손실계수로부터 환산", "range": "50~500"},
        {"sym": "L", "name_ko": "접지 패치 길이", "name_en": "Contact Patch Length", "unit": "mm", "meaning": "타이어-노면 접촉 영역 길이", "vehicle": "하중·공기압에 의존", "range": "100~200"},
        {"sym": "P", "name_ko": "공기압", "name_en": "Inflation Pressure", "unit": "bar", "meaning": "타이어 내부 압력", "vehicle": "차량 권장값", "range": "2.0~3.0"}
    ],
    "simpack_mappings": [
        {"sym": "k_t", "path": "Tire > Vertical > Stiffness", "field": "Radial Stiffness [N/mm]", "unit": "N/mm", "warn": "Simpack 타이어 모델(PAC2002 등)에서는 수직 강성이 하중 의존 — Fz-deflection 곡선 확인"},
        {"sym": "c_t", "path": "Tire > Vertical > Damping", "field": "Radial Damping [N·s/m]", "unit": "N·s/m", "warn": "타이어 감쇠를 0으로 놓으면 wheel hop 공진이 과대평가됨"}
    ],
    "deep_dive_title": "런플랫 타이어의 동특성 변화",
    "deep_dive_content": "런플랫(Run-flat) 타이어는 사이드월이 보강되어 공기압 0에서도 주행 가능하다. 대가: k_t가 일반 타이어보다 20~40% 높고, 타이어 질량도 10~20% 증가한다. 이는 (1) 바디 바운스 주파수 상승 → 승차감 악화, (2) 언스프렁 질량 증가 → 접지력 저하로 이어진다. BMW가 런플랫 + 전자제어 댐퍼(EDC)를 세트로 적용하는 이유가 여기에 있다.",
    "quiz": [
        {"type": "fill", "q": "일반 승용차 타이어의 수직 강성 범위는 약 ___~___N/mm이다.", "a": "150~250"},
        {"type": "meaning", "q": "접지 패치 필터가 sinc 함수 형태인 이유는?", "a": "유한 길이 L의 접지 패치가 노면 프로파일을 이동평균하는 효과이며, 이동평균의 주파수 응답이 sinc 함수이기 때문이다"},
        {"type": "simpack", "q": "Simpack 타이어 모델에서 수직 감쇠를 0으로 설정하면 어떤 문제가 발생하는가?", "a": "wheel hop 공진(~12Hz) 피크가 과대평가되어 비현실적으로 큰 언스프렁 질량 진동이 나타난다"}
    ],
    "next_preview_title": "Day 20 미리보기: 언스프렁 질량 & Tire Hop",
    "next_preview": "내일은 '언스프렁 질량'의 정의와 최적화, 그리고 tire hop 주파수 설계 가이드라인을 다룬다."
}

DAY20 = {
    "day": 20,
    "part": 3,
    "part_title": "서스펜션 세부 수식",
    "title_ko": "언스프렁 질량 & Tire Hop",
    "title_en": "Unsprung Mass & Tire Hop Frequency",
    "filename": "Day20_TireHop.html",
    "hero_eq": "f_hop = (1/2π)√((k_s+k_t)/m_u)",
    "difficulty": "★★★☆☆",
    "brain_strategy": {
        "technique": "극단값 사고 (Extreme Value Thinking)",
        "pre_routine": "m_u → 0이면? 타이어가 노면을 완벽히 추종(이상적). m_u → ∞이면? 휠이 관성으로 뜨고 접지력 상실. 이 두 극단을 5초씩 상상한 뒤 시작."
    },
    "intuition": "언스프렁 질량(unsprung mass)은 '스프링 아래의 모든 것' — 휠, 타이어, 브레이크, 너클, 로어암 일부 등이다. 이 질량이 작을수록 타이어가 노면을 잘 추종하여 접지력이 좋아진다. tire hop 주파수는 언스프렁 질량과 타이어+스프링 강성의 함수이며, 보통 10~15Hz 범위다. 이 주파수가 바디 바운스(1~2Hz)와 충분히 분리되어야 좋은 승차감을 얻는다.",
    "deriv_steps": [
        {
            "step_title": "Step 1: 언스프렁 질량 구성",
            "equation": "m_u = m_wheel + m_tire + m_brake + m_knuckle + f_arm · m_arm",
            "explain_meaning": "서스펜션 암(arm)은 한쪽이 차체에, 한쪽이 너클에 연결되므로 전체 질량의 일부(f_arm ≈ 1/3~1/2)만 언스프렁에 기여한다.",
            "explain_sign": "모든 항이 양수. 일반 승용차에서 m_u ≈ 30~50 kg/코너.",
            "explain_prev": "Day 08 쿼터카에서 m_u를 사용했지만 구성을 다루지 않았다. 여기서 분해한다."
        },
        {
            "step_title": "Step 2: Tire Hop 고유진동수 유도",
            "equation": "f_hop = (1/2π) √((k_s + k_t) / m_u)",
            "explain_meaning": "언스프렁 질량은 위에서 서스펜션 스프링 k_s, 아래에서 타이어 스프링 k_t로 지지된다. 바디 질량이 충분히 커서 고정점(anti-node)으로 근사하면 두 스프링이 병렬이 된다.",
            "explain_sign": "k_t >> k_s이므로 f_hop ≈ (1/2π)√(k_t/m_u)로 근사 가능. k_t가 지배적이다.",
            "explain_prev": "Day 09에서 쿼터카 2개 고유진동수를 구했다. 여기서는 wheel hop 모드에 집중한다."
        },
        {
            "step_title": "Step 3: 스프렁/언스프렁 질량비의 영향",
            "equation": "μ = m_u / m_s",
            "explain_meaning": "질량비 μ가 작을수록(언스프렁이 가벼울수록) (1) tire hop 주파수와 body bounce 주파수의 분리가 커지고, (2) 접지력 변동이 감소한다.",
            "explain_sign": "이상적 μ < 0.15. 일반 승용차 μ ≈ 0.10~0.15, SUV ≈ 0.15~0.25.",
            "explain_prev": "Day 09에서 두 고유진동수 비가 √(k_t/k_s) · √(1+μ) 형태임을 보였다."
        },
        {
            "step_title": "Step 4: 접지력 변동과 언스프렁 질량",
            "equation": "ΔF_z / F_z_static ∝ m_u / k_t",
            "explain_meaning": "동적 접지력 변동(ΔF_z)은 언스프렁 질량에 비례하고 타이어 강성에 반비례한다. 접지력 변동이 크면 타이어 그립이 불안정해진다.",
            "explain_sign": "m_u 감소 → ΔF_z 감소 → 안정적 접지. 알루미늄 휠이 스틸 휠보다 좋은 이유.",
            "explain_prev": "Day 14의 ISO 2631 승차감 지표와 별개로, 접지력 변동은 조종안정성 지표다."
        }
    ],
    "params": [
        {"sym": "m_u", "name_ko": "언스프렁 질량", "name_en": "Unsprung Mass", "unit": "kg", "meaning": "스프링 아래 총 질량", "vehicle": "휠+타이어+브레이크+너클+암 일부", "range": "30~55"},
        {"sym": "μ", "name_ko": "질량비", "name_en": "Mass Ratio (unsprung/sprung)", "unit": "—", "meaning": "언스프렁/스프렁 비", "vehicle": "경량화 지표", "range": "0.08~0.25"},
        {"sym": "f_hop", "name_ko": "타이어 홉 주파수", "name_en": "Tire Hop Frequency", "unit": "Hz", "meaning": "언스프렁 질량의 공진", "vehicle": "일반 승용차", "range": "10~15"},
        {"sym": "ΔF_z", "name_ko": "접지력 변동", "name_en": "Dynamic Load Variation", "unit": "N", "meaning": "정적 대비 동적 접지력 변화", "vehicle": "주행 시 타이어 하중 변동", "range": "50~500"}
    ],
    "simpack_mappings": [
        {"sym": "m_u", "path": "Body > Unsprung > Mass", "field": "Mass [kg]", "unit": "kg", "warn": "암(control arm)의 관성 분배를 정확히 모델링 — Simpack에서는 각 바디별 질량/관성을 입력"},
        {"sym": "f_hop", "path": "Analysis > Eigenvalue", "field": "Wheel Hop Mode [Hz]", "unit": "Hz", "warn": "고유값 해석 후 모드 형상(mode shape)에서 언스프렁 질량의 수직 운동이 지배적인 모드를 확인"}
    ],
    "deep_dive_title": "경량 휠의 효과: 알루미늄 vs 탄소섬유",
    "deep_dive_content": "언스프렁 질량 1kg 감소는 스프렁 질량 4~15kg 감소와 동등한 승차감/접지력 개선 효과가 있다(차속·노면 의존). 알루미늄 휠은 스틸 대비 2~4kg 경량, 탄소섬유(CFRP) 휠은 추가 3~5kg 경량이다. 포르쉐 918, BMW M 시리즈에서 CFRP 휠을 옵션으로 제공하는 이유다. 다만 비용이 10배 이상이므로, 르노코리아 양산에서는 알루미늄 단조 휠이 현실적 선택이다.",
    "quiz": [
        {"type": "fill", "q": "일반 승용차의 언스프렁 질량은 코너당 약 ___~___kg이다.", "a": "30~55"},
        {"type": "meaning", "q": "질량비 μ = m_u/m_s가 작을수록 좋은 이유 2가지는?", "a": "(1) 바디 바운스와 tire hop 주파수 분리가 커져 모드 커플링 감소, (2) 접지력 변동이 줄어 그립 안정성 향상"},
        {"type": "simpack", "q": "Simpack 고유값 해석에서 tire hop 모드를 식별하는 방법은?", "a": "모드 형상에서 언스프렁 질량의 수직 변위가 지배적이고 스프렁 질량은 거의 정지해 있는 10~15Hz 모드를 찾는다"}
    ],
    "next_preview_title": "Day 21 미리보기: 승차감 vs 조종안정성 트레이드오프",
    "next_preview": "PART 3 마지막! 서스펜션 설계의 근본 딜레마 — 부드러운 승차감과 날카로운 핸들링을 동시에 달성하는 방법. Skyhook 이론과 최적 감쇠비를 다룬다."
}

DAY21 = {
    "day": 21,
    "part": 3,
    "part_title": "서스펜션 세부 수식",
    "title_ko": "승차감 vs 조종안정성 트레이드오프",
    "title_en": "Ride vs Handling Trade-off & Skyhook",
    "filename": "Day21_승차감트레이드오프.html",
    "hero_eq": "ζ_opt, Skyhook 원리",
    "difficulty": "★★★★☆",
    "brain_strategy": {
        "technique": "트레이드오프 맵 (Trade-off Mapping)",
        "pre_routine": "A4 용지에 X축=승차감(좋음←→나쁨), Y축=핸들링(좋음←→나쁨)을 그린다. 소프트 서스펜션은 좌하, 하드 서스펜션은 우상에 위치. '좌상(both good)'으로 가려면 어떤 기술이 필요할까? 이 질문을 품고 시작."
    },
    "intuition": "서스펜션 설계의 근본 딜레마: 스프링을 부드럽게 하면 승차감은 좋지만 롤이 커지고 응답이 느려진다. 감쇠를 높이면 과도응답은 빠르지만 고주파 진동이 탑승자에게 전달된다. 이 트레이드오프를 극복하는 열쇠가 '가변 감쇠(semi-active)' 기술이며, 그 이론적 기반이 Skyhook 댐퍼다.",
    "deriv_steps": [
        {
            "step_title": "Step 1: 승차감 관점 최적 감쇠비",
            "equation": "ζ_ride_opt ≈ 0.2 ~ 0.4",
            "explain_meaning": "바디 가속도(승차감 지표)를 최소화하는 감쇠비는 약 0.2~0.4이다. 이보다 크면 고주파 진동이 증가하고, 작으면 공진 피크가 커진다.",
            "explain_sign": "ζ < 0.2: 공진 피크 과대 → '뱃멀미'. ζ > 0.4: 고주파 전달 증가 → '거칠음(harshness)'.",
            "explain_prev": "Day 03(감쇠비 ζ)와 Day 13(전달률)을 종합한 결론이다."
        },
        {
            "step_title": "Step 2: 접지력 관점 최적 감쇠비",
            "equation": "ζ_handling_opt ≈ 0.3 ~ 0.5",
            "explain_meaning": "동적 접지력 변동(ΔF_z)을 최소화하는 감쇠비는 승차감 최적보다 약간 높다. 접지력이 안정적이어야 코너링 그립이 일정하다.",
            "explain_sign": "ζ_handling > ζ_ride → 항상 약간의 트레이드오프가 존재한다.",
            "explain_prev": "Day 20에서 접지력 변동 ΔF_z를 정의했다. 여기서 감쇠와의 관계를 다룬다."
        },
        {
            "step_title": "Step 3: Skyhook 댐퍼 이론",
            "equation": "F_sky = c_sky · ẋ_body  (가상의 하늘에 고정된 댐퍼)",
            "explain_meaning": "Skyhook은 '바디 절대 속도'에 비례하는 감쇠력을 발생시키는 가상 댐퍼다. 바디 운동만 억제하고 노면 추종에는 간섭하지 않아 이론적 최적 성능을 제공한다.",
            "explain_sign": "물리적으로 '하늘에 고정된 점'은 불가능하지만, 센서(가속도계)와 가변 댐퍼로 근사 구현할 수 있다.",
            "explain_prev": "Day 17의 CDC/MR 댐퍼 Deep Dive에서 Skyhook 제어를 언급했다. 여기서 수학적으로 유도한다."
        },
        {
            "step_title": "Step 4: Skyhook On/Off 제어 논리",
            "equation": "c = c_max  if  ẋ_body · (ẋ_body - ẋ_wheel) > 0,  else  c = c_min",
            "explain_meaning": "바디 속도와 상대 속도의 부호가 같으면(바디가 위로 가면서 늘어나거나, 아래로 가면서 압축) 감쇠를 최대로 하여 바디 운동을 억제한다.",
            "explain_sign": "부호가 다르면 감쇠를 최소로 하여 에너지 전달을 차단. 이 단순한 on/off 논리가 연속 가변보다 구현이 쉽고 성능도 80%+에 도달한다.",
            "explain_prev": "Day 17의 비대칭 감쇠(바운드/리바운드)를 '시간에 따라 전환'하는 개념으로 확장한 것이다."
        },
        {
            "step_title": "Step 5: PART 3 통합 정리",
            "equation": "서스펜션 = 스프링(k) + 댐퍼(c) + 부싱(K*) + 타이어(k_t) + 기구학(MR)",
            "explain_meaning": "PART 3에서 다룬 모든 구성요소가 하나의 시스템으로 통합된다. 각 요소의 파라미터가 승차감과 핸들링에 미치는 영향을 종합적으로 이해해야 최적 설계가 가능하다.",
            "explain_sign": "모든 파라미터는 상호 연결: k_s↑ → f_body↑ → 핸들링↑, 승차감↓. c↑ → 과도응답↑, harshness↑.",
            "explain_prev": "Day 16(스프링) → Day 17(댐퍼) → Day 18(부싱) → Day 19(타이어) → Day 20(언스프렁) → Day 21(종합)."
        }
    ],
    "params": [
        {"sym": "ζ_ride", "name_ko": "승차감 최적 감쇠비", "name_en": "Ride Comfort Optimal ζ", "unit": "—", "meaning": "바디 가속도 최소화 감쇠비", "vehicle": "서스펜션 튜닝 타깃", "range": "0.2~0.4"},
        {"sym": "ζ_handling", "name_ko": "핸들링 최적 감쇠비", "name_en": "Handling Optimal ζ", "unit": "—", "meaning": "접지력 변동 최소화 감쇠비", "vehicle": "서스펜션 튜닝 타깃", "range": "0.3~0.5"},
        {"sym": "c_sky", "name_ko": "스카이훅 감쇠계수", "name_en": "Skyhook Damping", "unit": "N·s/m", "meaning": "바디 절대속도 기반 감쇠", "vehicle": "제어 알고리즘 게인", "range": "1000~8000"},
        {"sym": "c_max/c_min", "name_ko": "감쇠 가변 비", "name_en": "Damping Ratio Range", "unit": "—", "meaning": "가변 댐퍼 최대/최소 비", "vehicle": "CDC/MR 댐퍼 사양", "range": "3~10"}
    ],
    "simpack_mappings": [
        {"sym": "Skyhook", "path": "Control > Skyhook > Gain", "field": "c_sky [N·s/m]", "unit": "N·s/m", "warn": "Co-simulation 또는 User Routine으로 구현. 센서 딜레이(~10ms) 반영 필수"},
        {"sym": "c_range", "path": "Force Element > Semi-Active Damper", "field": "Min/Max Damping", "unit": "N·s/m", "warn": "c_min > 0이어야 수치 안정성 보장. c_min = 0은 불가"}
    ],
    "deep_dive_title": "르노 멀티센스(Multi-Sense)와 Skyhook",
    "deep_dive_content": "르노의 멀티센스 시스템은 Comfort/Sport/개인설정 모드에서 댐퍼 감쇠, 스티어링 어시스트, 엔진 맵을 종합 제어한다. 댐퍼 부분은 CDC(연속 가변 댐퍼)로, 내부적으로 Modified Skyhook + Groundhook 혼합 알고리즘을 사용한다. Groundhook: F_gh = c_gh · ẋ_wheel은 접지력 최적화를 위한 보완 제어다. Simpack에서 이를 구현하려면 Matlab/Simulink Co-simulation이 필요하며, PART 5에서 상세히 다룬다.",
    "quiz": [
        {"type": "fill", "q": "승차감 최적 감쇠비 범위는 ζ ≈ ___~___이다.", "a": "0.2~0.4"},
        {"type": "meaning", "q": "Skyhook On/Off 제어에서 c = c_min이 되는 조건의 물리적 의미는?", "a": "바디 속도와 상대속도의 부호가 반대 — 즉 바디가 위로 가는데 상대적으로 압축되는 상황. 이때 감쇠를 줄여 노면 입력 에너지가 바디로 전달되는 것을 차단한다."},
        {"type": "simpack", "q": "Simpack에서 semi-active 댐퍼의 c_min을 0으로 설정하면 안 되는 이유는?", "a": "감쇠가 0이면 수치 적분 시 무감쇠 공진이 발생하여 발산 위험이 있다. 최소 잔류 감쇠가 필요하다."}
    ],
    "next_preview_title": "Day 22 미리보기: FFT 기초",
    "next_preview": "PART 4 시작! 시간 영역에서 주파수 영역으로 넘어가는 핵심 도구 — Fast Fourier Transform. 샘플링 정리부터 윈도우 함수까지."
}
