"""
Day 22~28 풀콘텐츠
Day 22: Part 3 복습
Day 23~27: PART 4 주파수 영역 해석
Day 28: Part 4 복습
"""

DAY22 = {
    "day": 22,
    "part": 3,
    "part_title": "서스펜션 세부 수식",
    "title_ko": "Part 3 복습",
    "title_en": "Part 3 Comprehensive Review",
    "filename": "Day22_Part3복습.html",
    "hero_eq": "부품별 수식 비교 정리",
    "difficulty": "★☆☆☆☆",
    "brain_strategy": {
        "technique": "부품 카탈로그 맵 (Component Catalog)",
        "pre_routine": "A4 용지에 쿼터카 그림을 크게 그리고, 각 부품(스프링, 댐퍼, 부싱, 타이어) 위치에 핵심 수식 한 줄씩 적는다. 전체가 한 눈에 보이면 준비 완료."
    },
    "intuition": "PART 3에서 서스펜션의 4대 구성요소(스프링, 댐퍼, 부싱, 타이어)와 언스프렁 질량, 그리고 승차감/핸들링 트레이드오프를 다뤘다. 이 Day에서는 각 부품의 핵심 수식을 비교 정리하고, Simpack 입력 시 주의점을 총정리한다.",
    "deriv_steps": [
        {
            "step_title": "Step 1: 탄성 요소 비교",
            "equation": "스프링: F=kx | 타이어: F=k_t·δ | 부싱: F=K'x+K''x(90°)",
            "explain_meaning": "세 탄성 요소의 차이: 스프링은 순수 탄성(선형/비선형), 타이어는 공압 의존 탄성, 부싱은 주파수 의존 복소 탄성이다.",
            "explain_sign": "모든 복원력의 부호는 변위 반대 방향. 부싱의 K'' 성분만 속도(90° 앞선)에 비례하여 에너지 소산.",
            "explain_prev": "Day 16(스프링) → Day 18(부싱) → Day 19(타이어)에서 각각 유도했다."
        },
        {
            "step_title": "Step 2: 감쇠 요소 비교",
            "equation": "댐퍼: F=c(v)·ẋ | 부싱: F=K''x | 타이어: c_t·ẋ (미약)",
            "explain_meaning": "주 감쇠원은 쇽업쇼버(비선형 F-v), 부 감쇠원은 부싱(히스테리시스), 타이어 감쇠는 가장 작다.",
            "explain_sign": "감쇠 기여 순서: 댐퍼(80%+) >> 부싱(10~15%) > 타이어(5% 미만).",
            "explain_prev": "Day 17(댐퍼) → Day 18(부싱 η) → Day 19(타이어 ζ_t)에서 다뤘다."
        },
        {
            "step_title": "Step 3: 설계 트레이드오프 종합",
            "equation": "승차감: ζ_opt ≈ 0.2~0.4 | 핸들링: ζ_opt ≈ 0.3~0.5 | 해법: Skyhook c(t)",
            "explain_meaning": "고정 감쇠로는 두 목표를 동시 달성 불가. 가변 감쇠(semi-active)가 유일한 물리적 해결책이다.",
            "explain_sign": "Skyhook on/off 제어의 조건: ẋ_body · (ẋ_body - ẋ_wheel) > 0이면 c_max.",
            "explain_prev": "Day 21에서 Skyhook 이론과 르노 멀티센스를 다뤘다."
        }
    ],
    "params": [
        {"sym": "k_s", "name_ko": "스프링 강성", "name_en": "Spring Rate", "unit": "N/mm", "meaning": "코일/에어 스프링", "vehicle": "Force Element", "range": "15~80"},
        {"sym": "c(v)", "name_ko": "감쇠 F-v", "name_en": "Damper F-v", "unit": "N·s/m", "meaning": "비선형 감쇠", "vehicle": "Force Element", "range": "500~6000"},
        {"sym": "K*(f)", "name_ko": "부싱 복소강성", "name_en": "Bushing K*", "unit": "N/mm", "meaning": "주파수 의존", "vehicle": "Force Element", "range": "50~5000"},
        {"sym": "k_t", "name_ko": "타이어 강성", "name_en": "Tire Stiffness", "unit": "N/mm", "meaning": "수직 방향", "vehicle": "Tire Model", "range": "150~250"}
    ],
    "simpack_mappings": [
        {"sym": "All", "path": "Force Element > 각 부품", "field": "비선형 테이블 입력", "unit": "혼합", "warn": "모든 Force Element의 단위(N/mm vs N/m)를 통일해서 관리할 것"}
    ],
    "deep_dive_title": "Simpack 모델 체크리스트: PART 3 부품 입력 순서",
    "deep_dive_content": "실무 권장 순서: (1) 타이어 모델(PAC2002) 셋업 → (2) 스프링 F-x 곡선(범프스톱 포함) → (3) 댐퍼 F-v 곡선(바운드+리바운드) → (4) 부싱 K'(f), η(f) 테이블 → (5) 질량/관성 검증(언스프렁 질량 분리) → (6) 정적 평형(static equilibrium) 확인 → (7) 고유값 해석으로 모드 검증. 각 단계에서 단위 변환 오류가 가장 흔한 실수다.",
    "quiz": [
        {"type": "fill", "q": "서스펜션 시스템에서 감쇠 기여 순서는 댐퍼(___%) >> 부싱(___%) > 타이어(___%)이다.", "a": "80%+ >> 10~15% > 5% 미만"},
        {"type": "meaning", "q": "부싱의 동적 강성이 정적 강성보다 큰 이유는?", "a": "고무의 점탄성 특성으로 주파수가 올라가면 분자 사슬의 이완(relaxation)이 따라가지 못해 강성이 증가한다"},
        {"type": "simpack", "q": "Simpack 모델링에서 가장 흔한 실수는?", "a": "단위 변환 오류 — N/mm(시험 데이터)와 N/m(SI 입력)의 혼용이 1000배 차이를 만든다"}
    ],
    "next_preview_title": "Day 23 미리보기: 푸리에 변환 원리",
    "next_preview": "PART 4 시작! 시간 영역 신호를 주파수 영역으로 변환하는 핵심 도구 — 푸리에 변환. 연속 FT → 이산 DFT → FFT 알고리즘까지."
}

DAY23 = {
    "day": 23,
    "part": 4,
    "part_title": "주파수 영역 해석",
    "title_ko": "푸리에 변환 원리",
    "title_en": "Fourier Transform Fundamentals",
    "filename": "Day23_푸리에변환.html",
    "hero_eq": "X(f) = ∫x(t)e^(−i2πft)dt",
    "difficulty": "★★★☆☆",
    "brain_strategy": {
        "technique": "프리즘 비유 (Prism Analogy)",
        "pre_routine": "백색광이 프리즘을 통과하면 무지개 색으로 분해된다. 시간 신호 x(t)가 푸리에 '프리즘'을 통과하면 주파수 성분 X(f)로 분해된다. 이 비유를 30초간 시각화한 뒤 시작."
    },
    "intuition": "모든 시간 신호는 서로 다른 주파수의 사인파들의 합으로 표현할 수 있다. 푸리에 변환은 이 '레시피'를 알아내는 도구다. 차량 진동 신호를 FFT로 분석하면 '어느 주파수에서 진동이 큰가'를 한눈에 파악할 수 있고, 이를 통해 문제 주파수를 특정하고 원인을 추적할 수 있다.",
    "deriv_steps": [
        {
            "step_title": "Step 1: 연속 푸리에 변환 (CFT)",
            "equation": "X(f) = ∫_{−∞}^{∞} x(t) · e^{−i2πft} dt",
            "explain_meaning": "시간 신호 x(t)를 주파수 f의 복소 지수함수 e^{−i2πft}와 '내적'하여, 그 주파수 성분의 크기와 위상을 추출한다.",
            "explain_sign": "지수의 마이너스(−)는 '양의 주파수 성분 추출' 관례. X(f)는 복소수: |X(f)|가 진폭, ∠X(f)가 위상.",
            "explain_prev": "Day 06의 위상각과 Day 12의 전달함수 H(s)에서 복소수를 다뤘다. 여기서 복소 지수를 본격적으로 사용한다."
        },
        {
            "step_title": "Step 2: 역 푸리에 변환 (IFT)",
            "equation": "x(t) = ∫_{−∞}^{∞} X(f) · e^{+i2πft} df",
            "explain_meaning": "주파수 영역의 성분들을 모두 합치면 원래 시간 신호를 복원할 수 있다. FT와 IFT는 완전 가역이다.",
            "explain_sign": "지수의 플러스(+)는 역변환 관례. 정보 손실 없이 시간↔주파수 완전 대응.",
            "explain_prev": "Day 12에서 라플라스 변환의 역변환을 다뤘다. 푸리에는 s = i2πf의 특수한 경우다."
        },
        {
            "step_title": "Step 3: 이산 푸리에 변환 (DFT)과 FFT",
            "equation": "X[k] = Σ_{n=0}^{N-1} x[n] · e^{−i2πkn/N},  k = 0,1,...,N-1",
            "explain_meaning": "컴퓨터에서는 연속 신호를 샘플링하여 N개의 이산 데이터를 다룬다. DFT는 N개 시간 데이터를 N개 주파수 성분으로 변환한다.",
            "explain_sign": "주파수 해상도: Δf = 1/T = f_s/N. N이 크면 해상도↑ but 계산량 O(N²). FFT 알고리즘이 O(N·log₂N)으로 단축.",
            "explain_prev": "Day 14에서 PSD를 정성적으로 사용했다. PSD 계산의 기반이 바로 이 DFT/FFT다."
        },
        {
            "step_title": "Step 4: 샘플링 정리와 에일리어싱",
            "equation": "f_s ≥ 2 · f_max  (나이퀴스트 조건)",
            "explain_meaning": "샘플링 주파수 f_s는 신호 최대 주파수의 2배 이상이어야 한다. 그렇지 않으면 고주파 성분이 저주파로 접혀 나타나는(aliasing) 오류 발생.",
            "explain_sign": "차량 진동 해석에서 관심 주파수가 0~100Hz이면 f_s ≥ 200Hz, 실무에서는 4~10배인 512~1024Hz를 사용.",
            "explain_prev": "노면 PSD(Day 14)를 측정할 때 샘플링 주파수 선정이 중요한 이유다."
        }
    ],
    "params": [
        {"sym": "f_s", "name_ko": "샘플링 주파수", "name_en": "Sampling Frequency", "unit": "Hz", "meaning": "초당 데이터 수집 횟수", "vehicle": "DAQ 시스템 설정", "range": "256~2048"},
        {"sym": "N", "name_ko": "FFT 포인트 수", "name_en": "FFT Size", "unit": "—", "meaning": "분석 데이터 길이 (2^n)", "vehicle": "2^10=1024, 2^12=4096 등", "range": "512~8192"},
        {"sym": "Δf", "name_ko": "주파수 해상도", "name_en": "Frequency Resolution", "unit": "Hz", "meaning": "Δf = f_s / N", "vehicle": "낮을수록 정밀", "range": "0.1~2"},
        {"sym": "f_max", "name_ko": "최대 분석 주파수", "name_en": "Max Analysis Frequency", "unit": "Hz", "meaning": "f_s / 2 (나이퀴스트)", "vehicle": "진동 해석 상한", "range": "100~500"}
    ],
    "simpack_mappings": [
        {"sym": "FFT", "path": "Post-Processing > FFT Analysis", "field": "FFT Size, Window", "unit": "—", "warn": "Simpack 후처리에서 FFT 수행 시 윈도우 함수(Hanning) 반드시 적용"},
        {"sym": "f_s", "path": "Solver > Output Step", "field": "Time Step [s]", "unit": "s", "warn": "출력 시간 스텝 = 1/f_s. 0.001s → 1000Hz. 적분 스텝과 출력 스텝은 다를 수 있음"}
    ],
    "deep_dive_title": "윈도우 함수: 왜 Hanning을 기본으로 쓰는가?",
    "deep_dive_content": "유한 길이 신호에 FFT를 적용하면 양 끝이 불연속이 되어 스펙트럼 누출(leakage)이 발생한다. 윈도우 함수는 양 끝을 부드럽게 0으로 만들어 이를 완화한다. Hanning(Hann) 윈도우는 주파수 해상도와 누출 억제의 균형이 좋아 범용 표준이다. Flat-top 윈도우는 진폭 정확도가 높아 캘리브레이션용, Rectangular(윈도우 없음)은 과도응답 분석에 사용한다.",
    "quiz": [
        {"type": "fill", "q": "샘플링 주파수 1024Hz, FFT 포인트 4096이면 주파수 해상도 Δf = ___Hz.", "a": "0.25 (= 1024/4096)"},
        {"type": "meaning", "q": "에일리어싱(aliasing)이란 무엇인가?", "a": "샘플링 주파수의 절반(나이퀴스트 주파수)을 초과하는 고주파 성분이 저주파로 접혀 나타나는 현상. 실제 없는 저주파 성분이 생겨 분석 결과를 왜곡한다."},
        {"type": "simpack", "q": "Simpack 후처리에서 FFT 수행 시 윈도우 함수를 적용해야 하는 이유는?", "a": "유한 길이 시뮬레이션 데이터의 양 끝 불연속으로 인한 스펙트럼 누출(leakage)을 방지하기 위함이다"}
    ],
    "next_preview_title": "Day 24 미리보기: PSD 정의와 해석",
    "next_preview": "내일은 FFT 결과를 '파워'로 변환하는 PSD(Power Spectral Density)를 정식으로 유도한다. Welch 방법과 단위(g²/Hz, (m/s²)²/Hz)까지."
}

DAY24 = {
    "day": 24,
    "part": 4,
    "part_title": "주파수 영역 해석",
    "title_ko": "PSD 정의와 해석",
    "title_en": "Power Spectral Density — Definition & Interpretation",
    "filename": "Day24_PSD정의.html",
    "hero_eq": "S_xx(f) = |X(f)|²/T",
    "difficulty": "★★★☆☆",
    "brain_strategy": {
        "technique": "에너지 분배 사고 (Energy Distribution)",
        "pre_routine": "히스토그램을 떠올린다: X축이 주파수, Y축이 '에너지 밀도'. PSD는 '주파수별 에너지 히스토그램'이다. 막대 면적의 합이 총 에너지. 이 이미지를 5초 유지."
    },
    "intuition": "FFT의 |X(f)|²는 주파수 f에서의 '파워'이지만, 측정 시간 T에 의존한다. PSD S_xx(f) = |X(f)|²/T는 시간 정규화된 파워 밀도[단위²/Hz]로, 측정 시간에 무관한 신호 고유의 특성이다. 노면, 가속도, 하중 등의 랜덤 신호를 비교하려면 PSD가 필수다.",
    "deriv_steps": [
        {
            "step_title": "Step 1: 파시발 정리 (Parseval's Theorem)",
            "equation": "∫|x(t)|² dt = ∫|X(f)|² df",
            "explain_meaning": "시간 영역의 총 에너지와 주파수 영역의 총 에너지는 같다. 에너지는 보존된다.",
            "explain_sign": "양변 모두 양수(절댓값 제곱의 적분). 이 등식이 PSD 정의의 출발점이다.",
            "explain_prev": "Day 23의 FT/IFT 가역성에서 자연스럽게 따라오는 결과다."
        },
        {
            "step_title": "Step 2: PSD 정의",
            "equation": "S_xx(f) = lim_{T→∞} |X_T(f)|² / T  [단위²/Hz]",
            "explain_meaning": "측정 시간 T로 나눠 '밀도'로 만든다. f₁~f₂ 구간의 RMS 값은 √(∫_{f₁}^{f₂} S_xx df)로 구할 수 있다.",
            "explain_sign": "S_xx ≥ 0 항상. 단위가 [신호단위²/Hz]: 가속도면 (m/s²)²/Hz, 변위면 m²/Hz.",
            "explain_prev": "Day 14에서 노면 PSD를 S_z(n) = C·n^(-w)로 정성 소개했다. 여기서 정식 유도한다."
        },
        {
            "step_title": "Step 3: Welch 방법 (실무 표준)",
            "equation": "S_xx = (1/K) Σ_{k=1}^{K} |X_k(f)|² / (f_s · S₂)",
            "explain_meaning": "긴 데이터를 K개의 겹침(overlap) 세그먼트로 나누고, 각 세그먼트에 윈도우+FFT를 적용한 후 평균. S₂는 윈도우 보정 계수.",
            "explain_sign": "겹침률 50~75%가 표준. 평균 횟수 K가 클수록 PSD 추정의 분산이 줄어든다(통계적 안정).",
            "explain_prev": "Day 23의 FFT와 윈도우 함수를 조합하여 실무용 PSD 추정법을 완성한다."
        },
        {
            "step_title": "Step 4: RMS와 PSD의 관계",
            "equation": "x_RMS = √(∫_0^{f_max} S_xx(f) df)",
            "explain_meaning": "PSD 곡선 아래 면적의 제곱근이 RMS 값이다. 특정 주파수 대역만 적분하면 그 대역의 RMS를 구할 수 있다.",
            "explain_sign": "전체 면적 = σ² (분산). RMS는 '대역별 에너지 기여도'를 정량화하는 핵심 연산.",
            "explain_prev": "Day 14의 ISO 2631 가중 RMS 가속도 a_w는 PSD에 가중함수를 곱한 뒤 적분한 것이다."
        }
    ],
    "params": [
        {"sym": "S_xx", "name_ko": "파워스펙트럼밀도", "name_en": "PSD", "unit": "단위²/Hz", "meaning": "주파수별 에너지 밀도", "vehicle": "신호 분석 결과", "range": "—"},
        {"sym": "K", "name_ko": "평균 횟수", "name_en": "Number of Averages", "unit": "—", "meaning": "Welch 세그먼트 수", "vehicle": "통계 안정성 지표", "range": "10~100"},
        {"sym": "Overlap", "name_ko": "겹침률", "name_en": "Overlap Ratio", "unit": "%", "meaning": "세그먼트 간 겹침 비율", "vehicle": "50~75% 표준", "range": "50~75"},
        {"sym": "x_RMS", "name_ko": "RMS 값", "name_en": "Root Mean Square", "unit": "신호 단위", "meaning": "PSD 면적의 제곱근", "vehicle": "진동 크기 지표", "range": "—"}
    ],
    "simpack_mappings": [
        {"sym": "PSD", "path": "Post-Processing > Spectral Analysis > PSD", "field": "Welch Method", "unit": "단위²/Hz", "warn": "세그먼트 길이와 겹침률을 명시. 기본값이 최적이 아닐 수 있음"},
        {"sym": "RMS", "path": "Post-Processing > Statistics > RMS", "field": "RMS Value", "unit": "신호 단위", "warn": "주파수 대역 필터를 적용한 후 RMS를 구해야 의미 있는 비교가 가능"}
    ],
    "deep_dive_title": "양면 PSD vs 단면 PSD: 차이와 변환",
    "deep_dive_content": "수학적 FT는 음의 주파수를 포함하는 양면(two-sided) PSD를 생성한다. 실수 신호에서 음의 주파수 성분은 양의 주파수의 미러이므로, 실무에서는 단면(one-sided) PSD G_xx(f) = 2·S_xx(f) (f > 0)을 사용한다. Simpack을 포함한 대부분의 소프트웨어는 단면 PSD를 기본으로 출력한다. 논문이나 규격을 읽을 때 양면/단면 구분을 확인해야 2배 오류를 방지할 수 있다.",
    "quiz": [
        {"type": "fill", "q": "PSD의 단위는 [신호단위²/___]이다.", "a": "Hz"},
        {"type": "meaning", "q": "Welch 방법에서 세그먼트 수 K를 늘리면 어떤 효과가 있는가?", "a": "PSD 추정의 통계적 분산이 줄어들어 곡선이 매끄러워진다. 대신 각 세그먼트 길이가 줄어 주파수 해상도가 나빠지는 트레이드오프가 있다."},
        {"type": "simpack", "q": "Simpack PSD 분석에서 양면/단면 PSD 구분이 중요한 이유는?", "a": "단면 PSD는 양면의 2배이므로, 외부 데이터와 비교 시 구분하지 않으면 에너지가 2배 차이 나는 오류가 발생한다"}
    ],
    "next_preview_title": "Day 25 미리보기: FRF 측정과 해석",
    "next_preview": "내일은 시스템의 '지문' — 주파수응답함수(FRF)를 측정하고 해석하는 방법을 다룬다. 해머링 테스트, 코히어런스 γ²까지."
}

DAY25 = {
    "day": 25,
    "part": 4,
    "part_title": "주파수 영역 해석",
    "title_ko": "FRF 측정과 해석",
    "title_en": "FRF Measurement & Coherence γ²",
    "filename": "Day25_FRF측정.html",
    "hero_eq": "H(ω) = X(ω)/F(ω), γ²",
    "difficulty": "★★★★☆",
    "brain_strategy": {
        "technique": "블랙박스 사고 (Black Box Thinking)",
        "pre_routine": "시스템을 블랙박스로 그리고, 입력 F(ω)와 출력 X(ω)를 화살표로 표시. 박스 안의 '변환 규칙'이 FRF H(ω)다. 이 3요소 관계를 머릿속에 그린 뒤 시작."
    },
    "intuition": "FRF(Frequency Response Function)는 시스템이 각 주파수의 입력을 어떻게 '변환'하는지를 보여주는 함수다. 임팩트 해머로 차체를 때리고(입력), 가속도계로 응답을 측정하면(출력), 두 신호의 비로 FRF를 구할 수 있다. FRF의 피크가 공진 주파수이고, 코히어런스 γ²는 측정 품질의 '신뢰도 점수'다.",
    "deriv_steps": [
        {
            "step_title": "Step 1: FRF 정의 (H1 추정기)",
            "equation": "H₁(ω) = S_xf(ω) / S_ff(ω)",
            "explain_meaning": "입출력 교차 PSD(S_xf)를 입력 자기 PSD(S_ff)로 나눈다. 이 추정기는 출력 노이즈에 강건하다.",
            "explain_sign": "H₁은 복소수: |H₁|이 게인(진폭비), ∠H₁이 위상차. 입력 노이즈가 있으면 과소추정.",
            "explain_prev": "Day 12의 전달함수 H(s)를 측정 데이터로부터 추정하는 방법이다."
        },
        {
            "step_title": "Step 2: H2 추정기와 비교",
            "equation": "H₂(ω) = S_xx(ω) / S_fx(ω)",
            "explain_meaning": "출력 자기 PSD를 교차 PSD로 나눈다. 이 추정기는 입력 노이즈에 강건하다.",
            "explain_sign": "이상적 측정에서 H₁ = H₂. 차이가 크면 노이즈 또는 비선형 문제가 존재한다.",
            "explain_prev": "H₁과 H₂의 기하평균이 '진짜' FRF에 가깝다. 실무에서는 H₁을 기본으로 사용."
        },
        {
            "step_title": "Step 3: 코히어런스 함수 γ²",
            "equation": "γ²(ω) = |S_xf(ω)|² / (S_xx(ω) · S_ff(ω)),  0 ≤ γ² ≤ 1",
            "explain_meaning": "γ² = 1이면 출력이 입력으로 완전히 설명됨(선형, 노이즈 없음). γ² < 1이면 노이즈, 비선형, 또는 다른 입력원이 존재.",
            "explain_sign": "γ² < 0.9인 주파수 대역의 FRF는 신뢰도가 낮다. 해당 대역을 회색으로 표시하는 것이 관례.",
            "explain_prev": "Day 14의 ISO 2631 분석에서 '신뢰할 수 있는 주파수 범위'를 판단하는 기준이 코히어런스다."
        },
        {
            "step_title": "Step 4: 임팩트 해머 테스트 실무",
            "equation": "F(t) = 짧은 펄스 → F(ω) ≈ flat (광대역 가진)",
            "explain_meaning": "해머의 짧은 충격은 넓은 주파수 범위를 동시에 가진한다. 해머 팁 재질(고무/나일론/스틸)이 가진 주파수 범위를 결정한다.",
            "explain_sign": "부드러운 팁 → 저주파 위주, 딱딱한 팁 → 고주파까지. 더블 히팅(double hit) 주의 — 코히어런스 급락의 주범.",
            "explain_prev": "쿼터카(Day 08)의 이론적 FRF를 실제로 측정하여 비교할 수 있다."
        }
    ],
    "params": [
        {"sym": "H(ω)", "name_ko": "주파수응답함수", "name_en": "FRF", "unit": "출력단위/입력단위", "meaning": "주파수별 입출력 비", "vehicle": "가속도/힘 = (m/s²)/N", "range": "—"},
        {"sym": "γ²", "name_ko": "코히어런스", "name_en": "Coherence", "unit": "—", "meaning": "측정 신뢰도 (0~1)", "vehicle": "0.9 이상 신뢰", "range": "0~1"},
        {"sym": "S_xf", "name_ko": "교차 PSD", "name_en": "Cross PSD", "unit": "혼합 단위/Hz", "meaning": "입출력 상관 밀도", "vehicle": "FRF 계산 중간 결과", "range": "—"},
        {"sym": "n_avg", "name_ko": "평균 횟수", "name_en": "Number of Averages", "unit": "—", "meaning": "해머링 반복 횟수", "vehicle": "최소 5회, 권장 10회+", "range": "5~20"}
    ],
    "simpack_mappings": [
        {"sym": "FRF", "path": "Post-Processing > Transfer Function", "field": "Input/Output Channel", "unit": "혼합", "warn": "Simpack에서 FRF 계산 시 입출력 채널을 정확히 지정. 채널 번호 혼동 주의"},
        {"sym": "γ²", "path": "Post-Processing > Coherence", "field": "Coherence γ²", "unit": "—", "warn": "시뮬레이션 데이터는 노이즈가 없으므로 γ² ≈ 1이 정상. 1이 아니면 모델 문제"}
    ],
    "deep_dive_title": "모달 해머링 vs 가진기(Shaker) 테스트",
    "deep_dive_content": "해머 테스트: 빠르고 저비용, 광대역 가진, 이동 측정에 적합. 단점: 가진력 제어 불가, 비선형 시스템에서 진폭 의존성 평가 어려움. 가진기 테스트: 가진력 정밀 제어 가능, 스위프/랜덤/버스트 랜덤 등 다양한 가진 패턴, 비선형 평가 가능. 단점: 장비 비용↑, 셋업 시간↑. 르노코리아에서는 차체 모달(해머) → 서스펜션 튜닝(가진기) 순서가 일반적이다.",
    "quiz": [
        {"type": "fill", "q": "코히어런스 γ²의 범위는 ___≤ γ² ≤ ___이다.", "a": "0 ≤ γ² ≤ 1"},
        {"type": "meaning", "q": "H₁ 추정기와 H₂ 추정기의 차이는?", "a": "H₁ = S_xf/S_ff로 출력 노이즈에 강건하고, H₂ = S_xx/S_fx로 입력 노이즈에 강건하다. 이상적 측정에서는 동일하다."},
        {"type": "simpack", "q": "Simpack 시뮬레이션에서 FRF의 코히어런스가 1이 아닌 경우 의미하는 바는?", "a": "시뮬레이션은 노이즈가 없으므로 γ² < 1이면 모델에 비선형 요소가 있거나 분석 설정(윈도우, 평균)에 문제가 있다는 신호다"}
    ],
    "next_preview_title": "Day 26 미리보기: 고유치 문제",
    "next_preview": "내일은 다자유도 시스템의 고유진동수와 모드 형상을 구하는 일반화된 고유치 문제 [K−ω²M]{φ}={0}을 다룬다."
}

DAY26 = {
    "day": 26,
    "part": 4,
    "part_title": "주파수 영역 해석",
    "title_ko": "고유치 문제",
    "title_en": "Generalized Eigenvalue Problem",
    "filename": "Day26_고유치문제.html",
    "hero_eq": "[K − ω²M]{φ} = {0}",
    "difficulty": "★★★★☆",
    "brain_strategy": {
        "technique": "기타줄 비유 (Guitar String Analogy)",
        "pre_routine": "기타줄의 각 프렛 위치에서 고유의 음(진동수)과 모양(모드)이 있듯이, 차량 구조물도 고유진동수와 모드 형상을 가진다. '차량 = 거대한 악기'를 5초 상상."
    },
    "intuition": "다자유도(MDOF) 시스템은 자유도 수만큼의 고유진동수와 모드 형상을 가진다. 고유치 문제는 '외력 없이 스스로 진동할 수 있는 주파수와 그때의 변형 패턴'을 찾는 것이다. 차체 모달 해석에서 bending, torsion 모드를 찾는 것이 바로 이 고유치 문제를 푸는 것이다.",
    "deriv_steps": [
        {
            "step_title": "Step 1: 자유진동 가정",
            "equation": "{x(t)} = {φ} · e^{iωt}  →  [K]{φ}·e^{iωt} = ω²[M]{φ}·e^{iωt}",
            "explain_meaning": "조화 자유진동 x = φ·e^{iωt}를 운동방정식 [M]{ẍ}+[K]{x}={0}에 대입하면, 시간 항이 소거되고 진폭 벡터 {φ}에 대한 대수 방정식이 남는다.",
            "explain_sign": "ẍ = −ω²x이므로 [M]의 부호가 뒤집혀 [K] = ω²[M] 형태가 된다.",
            "explain_prev": "Day 01의 1DOF 자유진동 m·ẍ + k·x = 0 → ω² = k/m의 MDOF 일반화다."
        },
        {
            "step_title": "Step 2: 일반화된 고유치 문제",
            "equation": "[K − ω²M]{φ} = {0}  →  det[K − ω²M] = 0",
            "explain_meaning": "비자명 해(φ ≠ 0)가 존재하려면 행렬 [K−ω²M]의 행렬식이 0이어야 한다. 이 조건이 특성 방정식이며, n차 다항식의 근이 n개 고유진동수를 준다.",
            "explain_sign": "ω² > 0 (양수) → 진동 모드. ω² = 0 → 강체 모드(구속 조건 부족). ω² < 0 → 좌굴(불안정).",
            "explain_prev": "Day 09에서 쿼터카(2×2)의 특성 방정식을 풀었다. 여기서 n×n으로 일반화한다."
        },
        {
            "step_title": "Step 3: 모드 형상 벡터의 직교성",
            "equation": "{φ_i}ᵀ [M] {φ_j} = 0  (i ≠ j)",
            "explain_meaning": "서로 다른 모드 형상은 질량 매트릭스에 대해 직교한다. 이 성질이 모드 중첩법의 기반이다.",
            "explain_sign": "직교성 = '모드 간 에너지가 섞이지 않는다'. 각 모드를 독립적으로 분석할 수 있다.",
            "explain_prev": "Day 10의 하프카에서 바운스/피치 모드가 특정 조건에서 디커플링(직교)되는 것을 보았다."
        },
        {
            "step_title": "Step 4: 감쇠 시스템의 복소 고유치",
            "equation": "λ = −σ ± iω_d,  σ = ζω_n,  ω_d = ω_n√(1−ζ²)",
            "explain_meaning": "감쇠가 있으면 고유치가 복소수가 된다. 실수부 σ는 감쇠율(exponential decay), 허수부 ω_d는 감쇠 고유진동수.",
            "explain_sign": "σ > 0이면 안정(진동 감쇠), σ < 0이면 불안정(진동 성장). 차량에서 σ < 0은 shimmy, flutter 등의 자려진동.",
            "explain_prev": "Day 04(부족감쇠 자유진동)에서 1DOF의 λ = −ζω_n ± iω_d를 유도했다. MDOF로 확장."
        }
    ],
    "params": [
        {"sym": "ω_n", "name_ko": "고유진동수", "name_en": "Natural Frequency", "unit": "rad/s", "meaning": "자유진동 각주파수", "vehicle": "모달 해석 결과", "range": "—"},
        {"sym": "{φ}", "name_ko": "모드 형상", "name_en": "Mode Shape", "unit": "—", "meaning": "정규화된 변형 패턴", "vehicle": "각 절점의 상대 변위", "range": "—"},
        {"sym": "ζ", "name_ko": "모달 감쇠비", "name_en": "Modal Damping Ratio", "unit": "—", "meaning": "각 모드의 감쇠 정도", "vehicle": "반치폭법/로그감쇠율", "range": "0.01~0.10"},
        {"sym": "MAC", "name_ko": "모달 확인 기준", "name_en": "Modal Assurance Criterion", "unit": "—", "meaning": "두 모드 벡터의 유사도", "vehicle": "시험-해석 상관", "range": "0~1 (0.9+ 양호)"}
    ],
    "simpack_mappings": [
        {"sym": "ω_n, {φ}", "path": "Analysis > Eigenvalue", "field": "Eigenfrequencies, Mode Shapes", "unit": "Hz, —", "warn": "감쇠 포함 시 Complex Eigenvalue 선택. 실수 모드만 보면 감쇠 효과를 놓친다"},
        {"sym": "MAC", "path": "Post-Processing > MAC Matrix", "field": "Test vs FE Modes", "unit": "—", "warn": "MAC > 0.9: 동일 모드 판정. 0.7~0.9: 유사하지만 확인 필요. < 0.7: 다른 모드"}
    ],
    "deep_dive_title": "MAC 매트릭스: 시험과 시뮬레이션을 연결하는 열쇠",
    "deep_dive_content": "MAC(Modal Assurance Criterion)은 두 모드 벡터의 코사인 유사도다: MAC_ij = |{φ_A_i}ᵀ{φ_B_j}|² / ({φ_A_i}ᵀ{φ_A_i})({φ_B_j}ᵀ{φ_B_j}). MAC = 1이면 완전 일치, 0이면 직교. 실무에서 Simpack 모델을 실차 해머링 데이터와 비교할 때 MAC 매트릭스를 작성하여 각 모드의 일치도를 평가한다. 대각 성분이 0.9 이상이면 모델이 신뢰할 수 있다고 판단한다.",
    "quiz": [
        {"type": "fill", "q": "n자유도 시스템의 고유치 문제에서 구해지는 고유진동수의 개수는 ___개이다.", "a": "n"},
        {"type": "meaning", "q": "모드 형상의 직교성이 왜 중요한가?", "a": "직교성 덕분에 각 모드를 독립적인 1DOF 시스템으로 분리하여 분석할 수 있다(모드 중첩법의 기반)"},
        {"type": "simpack", "q": "Simpack 고유값 해석에서 Real Eigenvalue와 Complex Eigenvalue의 차이는?", "a": "Real은 비감쇠 고유진동수만, Complex는 감쇠 포함 복소 고유값(감쇠율 σ + 감쇠 고유진동수 ω_d)을 모두 제공한다"}
    ],
    "next_preview_title": "Day 27 미리보기: 모드 중첩법",
    "next_preview": "내일은 고유치 문제의 결과를 활용하여 강제진동 응답을 효율적으로 구하는 모드 중첩법(Modal Superposition)을 다룬다."
}

DAY27 = {
    "day": 27,
    "part": 4,
    "part_title": "주파수 영역 해석",
    "title_ko": "모드 중첩법",
    "title_en": "Modal Superposition Method",
    "filename": "Day27_모드중첩법.html",
    "hero_eq": "모달좌표 변환 → 응답 재구성",
    "difficulty": "★★★★☆",
    "brain_strategy": {
        "technique": "오케스트라 비유 (Orchestra Analogy)",
        "pre_routine": "오케스트라의 각 악기(모드)가 독립적으로 연주하고, 지휘자(중첩)가 이를 합치면 하나의 곡(응답)이 된다. '분해 → 독립 풀기 → 재합성' 3단계를 기억."
    },
    "intuition": "MDOF 강제진동을 직접 풀려면 n×n 연립미분방정식을 풀어야 한다. 모드 중첩법은 '모드 좌표 변환'으로 이를 n개의 독립 1DOF 문제로 분해한다. 각 1DOF를 풀고 다시 합치면 원래 응답이 된다. 계산 효율이 비약적으로 좋아지고, '어떤 모드가 응답에 지배적인가'를 직관적으로 파악할 수 있다.",
    "deriv_steps": [
        {
            "step_title": "Step 1: 모달 좌표 변환",
            "equation": "{x} = [Φ]{q},  [Φ] = [{φ₁} {φ₂} ··· {φ_n}]",
            "explain_meaning": "물리 좌표 {x}를 모드 형상 매트릭스 [Φ]와 모달 좌표 {q}의 곱으로 표현한다. q_i는 i번째 모드의 '참여 정도(진폭)'를 나타낸다.",
            "explain_sign": "[Φ]는 n×n 정방 매트릭스. 각 열이 하나의 모드 형상 벡터.",
            "explain_prev": "Day 26에서 구한 고유벡터 {φ_i}들을 열로 배열한 것이 [Φ]이다."
        },
        {
            "step_title": "Step 2: 디커플된 모달 방정식",
            "equation": "m̃_i · q̈_i + c̃_i · q̇_i + k̃_i · q_i = f̃_i(t)",
            "explain_meaning": "모드 형상의 직교성 덕분에 각 모달 좌표 q_i는 독립적인 1DOF 방정식을 따른다. m̃_i = {φ_i}ᵀ[M]{φ_i}가 모달 질량이다.",
            "explain_sign": "f̃_i = {φ_i}ᵀ{F(t)}는 모달 힘. 물리 외력을 모드 공간으로 투영한 것이다.",
            "explain_prev": "Day 26의 직교성 조건이 여기서 결정적 역할을 한다. 직교성이 없으면 디커플링 불가."
        },
        {
            "step_title": "Step 3: 모달 응답 → 물리 응답 재구성",
            "equation": "{x(t)} = Σ_{i=1}^{n} {φ_i} · q_i(t)  ≈ Σ_{i=1}^{m} {φ_i} · q_i(t),  m << n",
            "explain_meaning": "각 모달 응답 q_i(t)에 해당 모드 형상 φ_i를 곱하고 합산하면 물리 응답이 된다. 핵심: 하위 m개 모드만으로도 충분히 정확한 근사가 가능(모드 절단).",
            "explain_sign": "m/n의 비가 모드 절단 비율. 차량에서 0~50Hz 범위의 모드만 사용하면 대부분의 승차감 분석이 가능.",
            "explain_prev": "Day 08~11의 쿼터카/하프카 응답을 모드 중첩으로 해석하면 각 모드의 기여도를 분리할 수 있다."
        },
        {
            "step_title": "Step 4: 모달 참여 계수",
            "equation": "Γ_i = {φ_i}ᵀ [M] {1} / m̃_i",
            "explain_meaning": "모달 참여 계수는 '이 모드가 전체 응답에 얼마나 기여하는가'의 지표다. {1}은 단위 벡터(균일 가진 방향).",
            "explain_sign": "Γ_i가 큰 모드가 응답을 지배한다. 차량에서 바디 바운스 모드의 Γ가 가장 크다.",
            "explain_prev": "Day 15 복습에서 '어떤 모드가 중요한가?'라는 질문의 정량적 답이 바로 이 참여 계수다."
        }
    ],
    "params": [
        {"sym": "{q}", "name_ko": "모달 좌표", "name_en": "Modal Coordinate", "unit": "—", "meaning": "각 모드의 참여 진폭", "vehicle": "모드 중첩 중간 결과", "range": "—"},
        {"sym": "m̃_i", "name_ko": "모달 질량", "name_en": "Modal Mass", "unit": "kg", "meaning": "{φ_i}ᵀ[M]{φ_i}", "vehicle": "모드별 유효 질량", "range": "—"},
        {"sym": "Γ_i", "name_ko": "모달 참여 계수", "name_en": "Modal Participation Factor", "unit": "—", "meaning": "모드별 응답 기여도", "vehicle": "설계 우선순위 결정", "range": "0~1"},
        {"sym": "m", "name_ko": "사용 모드 수", "name_en": "Number of Retained Modes", "unit": "—", "meaning": "모드 절단 수", "vehicle": "정확도-효율 트레이드오프", "range": "5~50"}
    ],
    "simpack_mappings": [
        {"sym": "Modal", "path": "Analysis > Modal Reduction", "field": "Number of Modes", "unit": "—", "warn": "모드 수가 너무 적으면 고주파 응답 누락, 너무 많으면 계산 시간 증가"},
        {"sym": "Γ_i", "path": "Analysis > Eigenvalue > Modal Participation", "field": "Participation Factors", "unit": "—", "warn": "수직(Z) 방향 참여 계수가 큰 모드에 집중. 회전 방향도 확인할 것"}
    ],
    "deep_dive_title": "Craig-Bampton 방법: 유연체 모델의 핵심",
    "deep_dive_content": "Simpack에서 유연 차체(flex body)를 사용할 때 Craig-Bampton 방법이 적용된다. 이 방법은 (1) 경계 자유도(마운트 포인트)의 정적 모드와 (2) 고정 경계 내부의 동적 모드를 합성한다. FE 모델에서 수만 자유도를 수십 개의 모드로 축소하여 MBD 해석에 사용한다. 르노에서는 NASTRAN → Craig-Bampton → Simpack fbi 파일 workflow가 표준이다.",
    "quiz": [
        {"type": "fill", "q": "모드 중첩법에서 물리좌표와 모달좌표의 관계는 {x} = [___]{q}이다.", "a": "Φ (모드 형상 매트릭스)"},
        {"type": "meaning", "q": "모드 절단(mode truncation)이 가능한 이유는?", "a": "고주파 모드의 응답 기여도(모달 참여 계수)가 작고, 하위 소수의 모드가 전체 응답의 90%+ 를 차지하기 때문이다"},
        {"type": "simpack", "q": "Simpack에서 Craig-Bampton 유연체를 사용하는 이유는?", "a": "FE 모델의 수만 자유도를 수십 개의 모달 좌표로 축소하여, 정확도를 유지하면서 MBD 해석 시간을 대폭 단축한다"}
    ],
    "next_preview_title": "Day 28 미리보기: Part 4 복습",
    "next_preview": "PART 4 총정리! FFT → PSD → FRF → 고유치 → 모드 중첩까지, 주파수 영역 해석 전체 흐름을 하나의 파이프라인으로 연결한다."
}

DAY28 = {
    "day": 28,
    "part": 4,
    "part_title": "주파수 영역 해석",
    "title_ko": "Part 4 복습",
    "title_en": "Part 4 Comprehensive Review",
    "filename": "Day28_Part4복습.html",
    "hero_eq": "주파수 영역 전체 흐름 정리",
    "difficulty": "★★☆☆☆",
    "brain_strategy": {
        "technique": "파이프라인 사고 (Pipeline Thinking)",
        "pre_routine": "시간 신호 x(t) → [FFT] → X(f) → [|·|²/T] → PSD → [입출력비] → FRF → [det=0] → 고유치 → [Φ·q] → 응답. 이 파이프라인을 한 줄로 적은 뒤 시작."
    },
    "intuition": "PART 4에서 배운 주파수 영역 도구들은 하나의 분석 파이프라인을 형성한다. FFT(시간→주파수 변환) → PSD(에너지 밀도) → FRF(시스템 특성) → 고유치(고유 특성) → 모드 중첩(효율적 응답 계산). 이 파이프라인은 PART 5에서 Simpack 디지털 트윈을 구축할 때 시험-해석 상관의 핵심 도구가 된다.",
    "deriv_steps": [
        {
            "step_title": "Step 1: 시간→주파수 변환 도구 체계",
            "equation": "x(t) →[FFT]→ X(f) →[|·|²/T]→ S_xx(f) →[√∫Sdf]→ x_RMS",
            "explain_meaning": "시간 신호를 FFT로 변환하고, PSD로 에너지 밀도를 구하고, 적분하면 RMS — 이것이 기본 분석 체인이다.",
            "explain_sign": "각 단계에서 정보가 추가되거나 압축된다. FFT는 정보 보존, PSD는 위상 정보 제거(파워만 유지).",
            "explain_prev": "Day 23(FFT) → Day 24(PSD) 순서로 학습했다."
        },
        {
            "step_title": "Step 2: 시스템 특성 추출 체계",
            "equation": "FRF: H₁ = S_xf/S_ff → |H| peaks → ω_n, ζ",
            "explain_meaning": "입출력 데이터에서 FRF를 구하면, 피크 주파수가 고유진동수, 반치폭이 감쇠비를 제공한다.",
            "explain_sign": "이 과정을 EMA(Experimental Modal Analysis)라 하며, 시험-해석 상관의 기준이 된다.",
            "explain_prev": "Day 25(FRF·코히어런스) → Day 26(고유치)의 실험적 대응이다."
        },
        {
            "step_title": "Step 3: 응답 예측 체계",
            "equation": "S_response(f) = |H(f)|² · S_input(f)",
            "explain_meaning": "입력 PSD와 FRF²의 곱으로 출력 PSD를 예측할 수 있다. 이것이 주파수 영역 응답 예측의 핵심이다.",
            "explain_sign": "선형 시스템에서만 성립. 비선형이면 시간 영역 적분이 필수.",
            "explain_prev": "Day 14에서 노면 PSD → 가속도 PSD 변환을 소개했다. 여기서 일반화한다."
        }
    ],
    "params": [
        {"sym": "Pipeline", "name_ko": "분석 파이프라인", "name_en": "Analysis Pipeline", "unit": "—", "meaning": "FFT→PSD→FRF→모달", "vehicle": "표준 분석 절차", "range": "—"},
        {"sym": "EMA", "name_ko": "실험 모달 해석", "name_en": "Experimental Modal Analysis", "unit": "—", "meaning": "시험에서 모드 추출", "vehicle": "해머링/가진기 시험", "range": "—"}
    ],
    "simpack_mappings": [
        {"sym": "All", "path": "Post-Processing > Full Pipeline", "field": "FFT→PSD→FRF→Modal", "unit": "—", "warn": "Simpack 결과를 Matlab/Python에서 후처리하는 것이 더 유연한 경우가 많다"}
    ],
    "deep_dive_title": "Python 한 줄 코드: scipy.signal로 PSD/FRF 구하기",
    "deep_dive_content": "from scipy.signal import welch, csd; f, Sxx = welch(x, fs=1024, nperseg=2048); f, Sxf = csd(x, force, fs=1024, nperseg=2048); f, Sff = welch(force, fs=1024, nperseg=2048); H1 = Sxf / Sff; gamma2 = np.abs(Sxf)**2 / (Sxx * Sff). 이 5줄이면 PSD, FRF, 코히어런스를 모두 구할 수 있다. Simpack 출력을 CSV로 내보내서 이 코드로 검증하는 습관을 기르자.",
    "quiz": [
        {"type": "fill", "q": "주파수 영역 응답 예측: S_response = |___|² · S_input.", "a": "H(f) (주파수응답함수)"},
        {"type": "meaning", "q": "EMA(실험 모달 해석)에서 반치폭법으로 감쇠비를 구하는 원리는?", "a": "FRF 피크의 −3dB(반치폭) 주파수 폭 Δf와 공진 주파수 f_n의 비로 감쇠비를 구한다: ζ ≈ Δf/(2f_n)"},
        {"type": "simpack", "q": "Simpack 시뮬레이션 결과를 Python으로 후처리하는 것이 유리한 경우는?", "a": "커스텀 PSD 파라미터(겹침률, 윈도우), 다채널 FRF 비교, MAC 매트릭스 등 Simpack 기본 후처리가 제공하지 않는 고급 분석이 필요할 때"}
    ],
    "next_preview_title": "Day 29 미리보기: Simpack 풀카 모델 구축",
    "next_preview": "PART 5 시작! 드디어 Simpack으로 풀카(Full Vehicle) 모델을 구축한다. 지금까지 배운 모든 이론이 하나의 디지털 트윈으로 통합된다."
}
