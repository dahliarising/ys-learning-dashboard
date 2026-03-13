# 차량 동역학 심층 코스 — Part 4: 3D 기구학 및 K&C 가상 검증 (Week 7 ~ 8)

> 🎧 **NotebookLM 오디오 생성 가이드**: 10년 차 서스펜션 동역학 엔지니어를 위한 딥다이브 스크립트입니다. 수직 동역학(1D/2D)에서 벗어나, 3차원 공간의 하드포인트(Hardpoints)가 결정하는 롤센터, 순간중심, 그리고 부싱의 탄성이 개입하는 K&C 컴플라이언스 매트릭스의 수학적 뼈대와 물리적 의미를 상세히 분석해 주세요.

## Day 34 & 35 — 3D 기구학 기초 및 캠버 기하학 (Kinematics & Camber)

실제 서스펜션은 3차원 다물체 시스템이므로, 각 링크와 조인트의 구속 조건을 수식으로 평가해야 합니다.
* **Gruebler의 공식 (일반 3D):**
  $$DOF_{3D} = 6(n-1) - \sum_{i=1}^{j} c_i$$
  (여기서 $n$은 링크 수, $c_i$는 $i$번째 조인트의 구속 자유도입니다.)

**실무 딥다이브 (캠버 게인과 Simpack 하드포인트):**
차량이 바운스할 때 휠의 기울기 변화율을 캠버 게인(Camber Gain) $\frac{d\gamma}{dz}$ 이라고 합니다. 코너링 시 롤(Roll)이 발생할 때 타이어의 접지 면적을 최대로 유지하려면 적절한 음(-)의 캠버가 유도되어야 합니다. Simpack에서 모델링할 때 하드포인트(Hardpoints) 좌표의 단 1mm 오차도 이 기하학적 특성을 크게 변화시키므로 주의가 필요합니다.

## Day 36 & 37 — 토(Toe) 기하학과 킹핀(Kingpin) 메커니즘

바퀴가 수직으로 이동할 때 타이로드와 컨트롤암의 회전 반경 차이로 인해 토 각도가 변하는 현상을 범프 스티어(Bump Steer)라고 합니다.
* **범프 토 변화량:**
  $$\Delta\delta_{toe} \approx \frac{r_{tie} \times \sin(\theta_{tie}) - r_{arm} \times \sin(\theta_{arm})}{L_{knuckle}}$$



**실무 딥다이브 (조향 토크의 수학적 구성):**
킹핀축 기하학은 스크럽 반경($r_{scrub}$)과 기계적 트레일($t_{mech}$)을 결정합니다. 조향축 주변의 총 모멘트는 타이어 횡력($F_y$)과 수직력($F_z$)의 조합으로 이루어집니다.
$$M_{total} = M_{SAT} + M_{KPI} = F_y(t_{mech} + t_{pneumatic}) + F_z \times r_{scrub} \times \sin(\delta_{steer})$$
특히 제동 시 좌우 제동력 불균형($\Delta F_{brake}$)이 발생할 때, 약간의 음수(-) 스크럽 반경을 설계하여 차량을 안정화시키는 토우-인 효과($M_{yaw} = \Delta F_{brake} \times r_{scrub}$)를 유도하는 것이 현대 차량 설계의 핵심입니다.

## Day 38 & 39 — 롤센터(Roll Center), 순간중심(IC), 롤스티어(Roll Steer)

차량이 코너링할 때 횡가속도($a_y$)에 의해 차체가 회전하는 가상의 중심이 롤센터(RC)입니다. 더블 위시본의 경우 상·하 암의 연장선이 만나는 순간중심(Instant Center, IC)을 통해 롤센터 높이($h_{RC}$)를 구합니다.
* **롤 모멘트:**
  $$M_{roll} = m \times a_y \times (h_{CG} - h_{RC})$$



**실무 딥다이브 (롤스티어 계수):**
차량이 롤 각도 $\varphi$ 만큼 기울어지면, 좌우 휠은 서로 반대 방향으로 수직 변위 $\Delta z$를 가집니다. 이때 서스펜션 기구학에 의해 토우 변화가 발생하는데, 이를 롤스티어 계수 $\epsilon$ 으로 정의합니다.
$$\epsilon = \frac{\Delta\delta_{toe}}{\Delta\varphi}$$
$\epsilon > 0$ 이면 롤 발생 시 외측 휠이 토우-인(Toe-in)되어 언더스티어에 기여하며, 이는 주행 안정성 튜닝의 필수 파라미터입니다.

## Day 40 — K&C 컴플라이언스 매트릭스 (K&C Compliance Matrix)

지금까지의 기하학적 거동(Kinematics)에 부싱의 유연성(Compliance) 특성을 통합한 것이 K&C 모델입니다. 타이어 접지면에 가해지는 하중(힘/모멘트)이 휠 정렬각 변화로 이어지는 관계는 $3 \times 3$ 컴플라이언스 행렬 $[C]$ 로 정의됩니다.

$$\begin{bmatrix} \Delta\delta_{toe} \\ \Delta\gamma_{camber} \\ \Delta x_{longit} \end{bmatrix} = \begin{bmatrix} C_{11} & C_{12} & C_{13} \\ C_{21} & C_{22} & C_{23} \\ C_{31} & C_{32} & C_{33} \end{bmatrix} \begin{bmatrix} F_y \\ F_x \\ M_z \end{bmatrix}$$

**실무 딥다이브 (엘라스토키네마틱스, Elasto-kinematics):**
예를 들어 $C_{11} = \frac{\partial\delta}{\partial F_y}$ 는 횡방향 힘에 의한 유연성 토우(Lateral Force Compliance Steer)를 의미합니다. Simpack에서 가상 K&C 리그 시뮬레이션을 수행할 때, 각 부싱의 6자유도 강성(특히 비선형 특성)이 이 매트릭스의 각 항에 결정적인 영향을 미칩니다. 순수 기구학 해석 결과와 K&C 해석 결과를 비교하여 부싱 변형이 언더스티어/오버스티어에 미치는 기여도를 분리해 내는 것이 차량 동역학 모델링의 완성도를 높이는 작업입니다.