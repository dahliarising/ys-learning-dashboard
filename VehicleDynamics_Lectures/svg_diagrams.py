"""
═══════════════════════════════════════════════════════
YS 진동학 마스터 — SVG 다이어그램 라이브러리
각 Day에 맞는 물리계 도해 + 응답/주파수 곡선을 생성
색상: Day01 기준 (dark theme)
═══════════════════════════════════════════════════════
"""

# 공통 색상 팔레트 (Day 01 기준)
C = {
    "bg": "#0A0C10",
    "panel": "#111520",
    "gold": "#C9A84C",
    "gold_bright": "#E8C96A",
    "green": "#4ABF8A",
    "blue": "#4A9EBF",
    "purple": "#8A6ABF",
    "orange": "#BF6A4A",
    "dim": "#7A7A8A",
    "dark": "#252A38",
    "card": "#1A1E28",
}

ARROW_DEFS = """
  <defs>
    <marker id="arrowGold" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#E8C96A"/>
    </marker>
    <marker id="arrowGreen" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#4ABF8A"/>
    </marker>
    <marker id="arrowBlue" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#4A9EBF"/>
    </marker>
    <marker id="arrowOrange" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#BF6A4A"/>
    </marker>
    <marker id="arrowPurple" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#8A6ABF"/>
    </marker>
    <marker id="arrowDim" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#7A7A8A"/>
    </marker>
  </defs>
"""

def _ground(x, y, w):
    """지면 해칭"""
    lines = [f'<rect x="{x}" y="{y}" width="{w}" height="6" rx="2" fill="{C["dark"]}"/>']
    for xi in range(int(x)+10, int(x+w), 25):
        lines.append(f'<line x1="{xi}" y1="{y+6}" x2="{xi-8}" y2="{y+14}" stroke="{C["dim"]}" stroke-width="1.2"/>')
    return "\n    ".join(lines)

def _spring(x, y1, y2, label="k", color=None):
    """스프링 지그재그"""
    c = color or C["green"]
    mid_y = (y1 + y2) / 2
    seg = (y2 - y1) / 8
    pts = f"{x},{y1} "
    for i in range(1, 7):
        offset = 15 if i % 2 == 1 else -15
        pts += f"{x+offset},{y1 + i*seg} "
    pts += f"{x},{y2}"
    return f"""<polyline points="{pts}" fill="none" stroke="{c}" stroke-width="2" stroke-linejoin="round"/>
    <text x="{x-22}" y="{mid_y+4}" font-family="JetBrains Mono" font-size="14" fill="{c}">{label}</text>"""

def _damper(x, y1, y2, label="c", color=None):
    """댐퍼 (실린더 + 피스톤)"""
    c = color or C["blue"]
    mid_y = (y1 + y2) / 2
    h = 28
    return f"""<line x1="{x}" y1="{y1}" x2="{x}" y2="{mid_y-h/2}" stroke="{c}" stroke-width="2"/>
    <rect x="{x-12}" y="{mid_y-h/2}" width="24" height="{h}" rx="2" fill="none" stroke="{c}" stroke-width="2"/>
    <line x1="{x}" y1="{mid_y-h/2}" x2="{x}" y2="{mid_y-h/2-10}" stroke="{c}" stroke-width="2"/>
    <line x1="{x-8}" y1="{mid_y-h/2-10}" x2="{x+8}" y2="{mid_y-h/2-10}" stroke="{c}" stroke-width="2.5"/>
    <line x1="{x}" y1="{mid_y-h/2-10}" x2="{x}" y2="{y2}" stroke="{c}" stroke-width="2"/>
    <text x="{x+18}" y="{mid_y+4}" font-family="JetBrains Mono" font-size="14" fill="{c}">{label}</text>"""

def _mass(x, y, w, h, label="m", color=None):
    """질량 블록"""
    c = color or C["gold"]
    return f"""<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{C["card"]}" stroke="{c}" stroke-width="2"/>
    <text x="{x+w/2}" y="{y+h/2+5}" font-family="JetBrains Mono" font-size="16" fill="{C["gold_bright"]}" text-anchor="middle">{label}</text>"""

def _arrow(x1, y1, x2, y2, label="", color="arrowGold", text_color=None):
    """화살표 + 라벨"""
    tc = text_color or C["gold_bright"]
    lx = max(x1, x2) + 8
    ly = (y1 + y2) / 2 + 4
    return f"""<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{tc}" stroke-width="2" marker-end="url(#{color})"/>
    <text x="{lx}" y="{ly}" font-family="JetBrains Mono" font-size="12" fill="{tc}">{label}</text>"""

def _axes(ox, oy, w, h, xlabel="t", ylabel="x(t)"):
    """좌표축"""
    return f"""<line x1="{ox}" y1="{oy}" x2="{ox+w}" y2="{oy}" stroke="{C["dim"]}" stroke-width="1"/>
    <line x1="{ox}" y1="{oy-h}" x2="{ox}" y2="{oy+h}" stroke="{C["dim"]}" stroke-width="1"/>
    <text x="{ox+w+5}" y="{oy+4}" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}">{xlabel}</text>
    <text x="{ox-5}" y="{oy-h-5}" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}" text-anchor="end">{ylabel}</text>"""

def _grid_bg(x, y, w, h):
    return f"""<defs><pattern id="gridP" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{C["card"]}" stroke-width="0.5"/>
    </pattern></defs>
    <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#gridP)"/>"""


# ═══════════════════════════════════════════════════
# PART 1: Day 02~07 SVG
# ═══════════════════════════════════════════════════

def svg_day02():
    """비감쇠 자유진동 — 1DOF 스프링-질량 + 정현파 응답"""
    a = f"""<svg viewBox="0 0 500 320" width="500" height="320" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    {_ground(120, 280, 260)}
    <line x1="250" y1="280" x2="250" y2="240" stroke="{C["green"]}" stroke-width="2"/>
    {_spring(250, 240, 160, "k")}
    <line x1="250" y1="160" x2="250" y2="120" stroke="{C["green"]}" stroke-width="2"/>
    {_mass(175, 80, 150, 40, "m")}
    {_arrow(360, 120, 360, 55, "x(t)", "arrowGold")}
    <text x="100" y="50" font-family="Noto Sans KR" font-size="12" fill="{C["dim"]}">비감쇠: c = 0</text>
    <text x="100" y="68" font-family="JetBrains Mono" font-size="11" fill="{C["green"]}">ωₙ = √(k/m)</text>
  </svg>"""
    b = f"""<svg viewBox="0 0 480 240" width="480" height="240" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 410, 200)}
    {_axes(50, 110, 410, 90, "t", "x(t)")}
    <path d="M50,30 Q95,30 140,110 Q185,190 230,190 Q275,190 320,110 Q365,30 410,30 Q435,30 460,110" fill="none" stroke="{C["green"]}" stroke-width="2.5"/>
    <text x="420" y="40" font-family="JetBrains Mono" font-size="10" fill="{C["green"]}">ζ=0 등폭</text>
    <line x1="50" y1="218" x2="230" y2="218" stroke="{C["purple"]}" stroke-width="1.5"/>
    <text x="140" y="232" font-family="JetBrains Mono" font-size="10" fill="{C["purple"]}" text-anchor="middle">Tₙ = 2π/ωₙ</text>
  </svg>"""
    return a, b

def svg_day03():
    """감쇠비 ζ 분류 — 3가지 응답 비교"""
    a = f"""<svg viewBox="0 0 500 320" width="500" height="320" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    {_ground(120, 280, 260)}
    {_spring(195, 280, 160, "k")}
    {_damper(305, 280, 160, "c")}
    {_mass(160, 120, 180, 40, "m")}
    {_arrow(370, 150, 370, 75, "x(t)", "arrowGold")}
    <text x="100" y="50" font-family="JetBrains Mono" font-size="12" fill="{C["gold_bright"]}">ζ = c / (2√(km))</text>
  </svg>"""
    b = f"""<svg viewBox="0 0 480 250" width="480" height="250" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 410, 210)}
    {_axes(50, 120, 410, 100, "t", "x(t)")}
    <path d="M50,30 Q73,30 95,120 Q117,210 140,210 Q163,210 186,120 Q208,30 230,30 Q253,30 276,120 Q298,210 320,210 Q343,210 365,120 Q388,30 410,30 Q433,30 456,120" fill="none" stroke="{C["green"]}" stroke-width="1.5" opacity="0.5"/>
    <text x="400" y="40" font-family="JetBrains Mono" font-size="9" fill="{C["green"]}" opacity="0.7">ζ=0</text>
    <path d="M50,30 Q80,45 110,120 Q135,180 160,175 Q185,172 210,120 Q232,82 255,85 Q278,88 300,120 Q320,143 340,141 Q360,139 380,120 Q400,108 420,110 Q440,112 460,120" fill="none" stroke="{C["gold_bright"]}" stroke-width="2.5"/>
    <text x="400" y="98" font-family="JetBrains Mono" font-size="9" fill="{C["gold_bright"]}">ζ=0.2</text>
    <path d="M50,30 C120,50 200,110 280,118 C350,120 420,120 460,120" fill="none" stroke="{C["orange"]}" stroke-width="2" stroke-dasharray="6 3"/>
    <text x="400" y="130" font-family="JetBrains Mono" font-size="9" fill="{C["orange"]}">ζ=1 임계</text>
    <path d="M50,30 C150,80 250,115 350,119 C400,120 430,120 460,120" fill="none" stroke="{C["purple"]}" stroke-width="1.5" stroke-dasharray="3 3"/>
    <text x="400" y="150" font-family="JetBrains Mono" font-size="9" fill="{C["purple"]}">ζ=2 과감쇠</text>
  </svg>"""
    return a, b

def svg_day04():
    """부족감쇠 자유진동 — 포락선 + 감쇠진동"""
    a = None  # Day 03과 같은 물리계이므로 생략
    b = f"""<svg viewBox="0 0 480 250" width="480" height="250" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 410, 210)}
    {_axes(50, 120, 410, 100, "t", "x(t)")}
    <path d="M50,30 C150,52 250,88 350,108 C420,115 460,118 460,120" fill="none" stroke="{C["gold"]}" stroke-width="1" stroke-dasharray="5 3" opacity="0.6"/>
    <path d="M50,210 C150,188 250,152 350,132 C420,125 460,122 460,120" fill="none" stroke="{C["gold"]}" stroke-width="1" stroke-dasharray="5 3" opacity="0.6"/>
    <text x="350" y="100" font-family="JetBrains Mono" font-size="10" fill="{C["gold"]}" opacity="0.7">±Ae^(-ζωₙt)</text>
    <path d="M50,30 Q80,40 105,120 Q125,190 155,185 Q180,180 205,120 Q225,72 250,75 Q275,78 295,120 Q312,152 335,150 Q355,148 375,120 Q390,102 410,105 Q430,107 450,120" fill="none" stroke="{C["gold_bright"]}" stroke-width="2.5"/>
    <circle cx="50" cy="30" r="4" fill="{C["gold_bright"]}"/>
    <text x="58" y="24" font-family="JetBrains Mono" font-size="9" fill="{C["gold_bright"]}">x₀</text>
    <line x1="50" y1="228" x2="155" y2="228" stroke="{C["purple"]}" stroke-width="1.5"/>
    <text x="102" y="242" font-family="JetBrains Mono" font-size="10" fill="{C["purple"]}" text-anchor="middle">T_d = 2π/ω_d</text>
  </svg>"""
    return a, b

def svg_day05():
    """강제조화진동 — 주파수응답 곡선(진폭비)"""
    a = f"""<svg viewBox="0 0 500 320" width="500" height="320" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    {_ground(120, 280, 260)}
    {_spring(195, 280, 160, "k")}
    {_damper(305, 280, 160, "c")}
    {_mass(160, 120, 180, 40, "m")}
    <line x1="250" y1="80" x2="250" y2="120" stroke="{C["orange"]}" stroke-width="2.5" marker-end="url(#arrowOrange)"/>
    <text x="260" y="75" font-family="JetBrains Mono" font-size="12" fill="{C["orange"]}">F₀sin(ωt)</text>
  </svg>"""
    b = f"""<svg viewBox="0 0 480 260" width="480" height="260" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 410, 220)}
    <line x1="50" y1="230" x2="460" y2="230" stroke="{C["dim"]}" stroke-width="1"/>
    <line x1="50" y1="10" x2="50" y2="230" stroke="{C["dim"]}" stroke-width="1"/>
    <text x="460" y="248" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}">r = ω/ωₙ</text>
    <text x="15" y="15" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}">X/X_st</text>
    <line x1="50" y1="230" x2="50" y2="228" stroke="{C["dim"]}" stroke-width="1"/>
    <text x="48" y="245" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}" text-anchor="end">0</text>
    <line x1="175" y1="230" x2="175" y2="225" stroke="{C["dim"]}" stroke-width="1"/>
    <text x="175" y="245" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}" text-anchor="middle">1</text>
    <path d="M50,210 C80,210 120,205 150,150 C165,85 170,40 175,25 C180,40 185,90 200,155 C230,210 280,218 340,220 C400,222 440,224 460,225" fill="none" stroke="{C["orange"]}" stroke-width="2.5"/>
    <text x="180" y="20" font-family="JetBrains Mono" font-size="10" fill="{C["orange"]}">ζ=0.1</text>
    <path d="M50,210 C80,208 120,200 150,165 C165,125 170,90 175,70 C180,90 185,130 200,170 C230,208 280,215 340,218 C400,220 440,222 460,224" fill="none" stroke="{C["gold_bright"]}" stroke-width="2"/>
    <text x="185" y="68" font-family="JetBrains Mono" font-size="10" fill="{C["gold_bright"]}">ζ=0.3</text>
    <path d="M50,210 C80,206 120,195 150,180 C170,160 175,150 180,160 C200,185 250,208 340,216 C400,218 440,222 460,223" fill="none" stroke="{C["blue"]}" stroke-width="1.5"/>
    <text x="185" y="148" font-family="JetBrains Mono" font-size="10" fill="{C["blue"]}">ζ=0.7</text>
    <line x1="175" y1="12" x2="175" y2="230" stroke="{C["dim"]}" stroke-width="0.8" stroke-dasharray="4 3"/>
    <text x="178" y="135" font-family="Noto Sans KR" font-size="9" fill="{C["dim"]}">공진영역</text>
  </svg>"""
    return a, b

def svg_day06():
    """위상각 φ — 위상각 vs 주파수비"""
    a = None
    b = f"""<svg viewBox="0 0 480 260" width="480" height="260" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 410, 220)}
    <line x1="50" y1="230" x2="460" y2="230" stroke="{C["dim"]}" stroke-width="1"/>
    <line x1="50" y1="10" x2="50" y2="230" stroke="{C["dim"]}" stroke-width="1"/>
    <text x="460" y="248" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}">r = ω/ωₙ</text>
    <text x="15" y="15" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}">φ [°]</text>
    <text x="43" y="18" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}" text-anchor="end">0°</text>
    <text x="43" y="125" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}" text-anchor="end">90°</text>
    <text x="43" y="232" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}" text-anchor="end">180°</text>
    <line x1="175" y1="10" x2="175" y2="230" stroke="{C["dim"]}" stroke-width="0.8" stroke-dasharray="4 3"/>
    <text x="175" y="245" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}" text-anchor="middle">1</text>
    <path d="M50,15 C80,16 120,18 155,40 C165,60 172,90 175,120 C178,150 185,180 200,200 C230,220 300,228 400,230 C440,230 460,230 460,230" fill="none" stroke="{C["orange"]}" stroke-width="2.5"/>
    <text x="300" y="185" font-family="JetBrains Mono" font-size="10" fill="{C["orange"]}">ζ=0.1</text>
    <path d="M50,15 C80,18 120,30 155,65 C165,85 172,105 175,120 C178,135 185,160 200,180 C230,210 300,225 400,228 C440,229 460,230 460,230" fill="none" stroke="{C["gold_bright"]}" stroke-width="2"/>
    <text x="300" y="165" font-family="JetBrains Mono" font-size="10" fill="{C["gold_bright"]}">ζ=0.3</text>
    <text x="178" y="115" font-family="Noto Sans KR" font-size="9" fill="{C["purple"]}">r=1 → φ=90°</text>
    <circle cx="175" cy="120" r="4" fill="{C["purple"]}"/>
  </svg>"""
    return a, b

def svg_day07():
    """공진 — 진폭 발산 + 위상각 합동"""
    a = None
    b = f"""<svg viewBox="0 0 480 260" width="480" height="260" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 410, 220)}
    {_axes(50, 120, 410, 100, "t", "x(t)")}
    <path d="M50,120 Q60,105 70,120 Q80,135 90,120 Q100,100 110,120 Q120,140 130,120 Q140,95 150,120 Q160,148 170,120 Q180,88 190,120 Q200,155 210,120 Q220,80 230,120 Q240,165 250,120 Q260,70 270,120 Q280,175 290,120 Q300,58 310,120 Q320,185 330,120 Q340,48 350,120 Q360,195 370,120 Q380,38 390,120 Q400,205 410,120 Q420,28 430,120 Q440,215 450,120" fill="none" stroke="{C["orange"]}" stroke-width="2"/>
    <path d="M50,120 C100,115 150,100 200,80 C250,55 300,30 400,15" fill="none" stroke="{C["orange"]}" stroke-width="1" stroke-dasharray="4 3" opacity="0.5"/>
    <path d="M50,120 C100,125 150,140 200,160 C250,185 300,210 400,225" fill="none" stroke="{C["orange"]}" stroke-width="1" stroke-dasharray="4 3" opacity="0.5"/>
    <text x="320" y="25" font-family="JetBrains Mono" font-size="10" fill="{C["orange"]}">ζ→0 공진 발산</text>
    <text x="100" y="240" font-family="JetBrains Mono" font-size="10" fill="{C["dim"]}">ω = ωₙ (공진 조건)</text>
  </svg>"""
    return a, b

# ═══════════════════════════════════════════════════
# PART 2: Day 08~14 SVG
# ═══════════════════════════════════════════════════

def svg_day08():
    """쿼터카 2-DOF 모식도"""
    a = f"""<svg viewBox="0 0 500 420" width="500" height="420" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    <!-- Road -->
    <path d="M80,390 Q180,385 250,390 Q320,395 400,390" fill="none" stroke="{C["dim"]}" stroke-width="2"/>
    <text x="250" y="410" font-family="JetBrains Mono" font-size="11" fill="{C["dim"]}" text-anchor="middle">z_r (노면)</text>
    <!-- Tire spring -->
    {_spring(250, 380, 300, "k_t", C["purple"])}
    <!-- Unsprung mass -->
    {_mass(185, 260, 130, 35, "m_u (언스프렁)", C["blue"])}
    <!-- Suspension spring + damper -->
    {_spring(195, 250, 160, "k_s")}
    {_damper(305, 250, 160, "c_s")}
    <!-- Sprung mass -->
    {_mass(160, 120, 180, 40, "m_s (스프렁)")}
    <!-- Arrows -->
    {_arrow(380, 280, 380, 230, "z_u", "arrowBlue", C["blue"])}
    {_arrow(380, 150, 380, 80, "z_s", "arrowGold")}
  </svg>"""
    return a, None

def svg_day09():
    """쿼터카 고유진동수 — bounce vs wheel hop"""
    a = None
    b = f"""<svg viewBox="0 0 480 250" width="480" height="250" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 410, 210)}
    <line x1="50" y1="230" x2="460" y2="230" stroke="{C["dim"]}" stroke-width="1"/>
    <line x1="50" y1="10" x2="50" y2="230" stroke="{C["dim"]}" stroke-width="1"/>
    <text x="460" y="248" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}">f [Hz]</text>
    <text x="15" y="15" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}">|H(f)|</text>
    <!-- Bounce peak ~1.2 Hz -->
    <path d="M50,210 C70,208 100,200 120,100 C130,40 135,35 140,40 C145,50 155,120 180,190 C220,210 300,215 350,218 C360,200 370,160 375,130 C380,100 382,95 385,100 C388,110 392,140 400,180 C420,210 440,215 460,218" fill="none" stroke="{C["gold_bright"]}" stroke-width="2.5"/>
    <line x1="132" y1="230" x2="132" y2="35" stroke="{C["gold"]}" stroke-width="0.8" stroke-dasharray="3 3" opacity="0.4"/>
    <text x="132" y="248" font-family="JetBrains Mono" font-size="9" fill="{C["gold"]}" text-anchor="middle">~1.2 Hz</text>
    <text x="90" y="55" font-family="Noto Sans KR" font-size="10" fill="{C["gold_bright"]}">Bounce</text>
    <!-- Wheel hop peak ~11 Hz -->
    <line x1="382" y1="230" x2="382" y2="95" stroke="{C["blue"]}" stroke-width="0.8" stroke-dasharray="3 3" opacity="0.4"/>
    <text x="382" y="248" font-family="JetBrains Mono" font-size="9" fill="{C["blue"]}" text-anchor="middle">~11 Hz</text>
    <text x="400" y="85" font-family="Noto Sans KR" font-size="10" fill="{C["blue"]}">Wheel Hop</text>
  </svg>"""
    return a, b

def svg_day10():
    """하프카 — bounce + pitch 2모드"""
    a = f"""<svg viewBox="0 0 520 350" width="520" height="350" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    <!-- Beam (sprung) -->
    {_mass(80, 100, 360, 35, "m_s, I_pitch", C["gold"])}
    <!-- Front suspension -->
    {_spring(140, 140, 230, "k_f")}
    {_damper(180, 140, 230, "c_f")}
    <!-- Rear suspension -->
    {_spring(340, 140, 230, "k_r")}
    {_damper(380, 140, 230, "c_r")}
    <!-- Front unsprung -->
    {_mass(110, 235, 100, 28, "m_uf", C["blue"])}
    <!-- Rear unsprung -->
    {_mass(310, 235, 100, 28, "m_ur", C["blue"])}
    <!-- Road -->
    <path d="M60,310 Q200,305 260,310 Q320,315 460,310" fill="none" stroke="{C["dim"]}" stroke-width="2"/>
    <!-- z_s, θ arrows -->
    {_arrow(460, 130, 460, 60, "z_s", "arrowGold")}
    <path d="M260,95 A30,30 0 0,1 290,95" fill="none" stroke="{C["purple"]}" stroke-width="2" marker-end="url(#arrowPurple)"/>
    <text x="270" y="80" font-family="JetBrains Mono" font-size="12" fill="{C["purple"]}">θ</text>
    <text x="130" y="330" font-family="Noto Sans KR" font-size="10" fill="{C["dim"]}">전축</text>
    <text x="340" y="330" font-family="Noto Sans KR" font-size="10" fill="{C["dim"]}">후축</text>
  </svg>"""
    return a, None

def svg_day11():
    """하프카 모드형상 — bounce vs pitch"""
    a = None
    b = f"""<svg viewBox="0 0 480 250" width="480" height="250" xmlns="http://www.w3.org/2000/svg">
    <!-- Bounce mode -->
    <text x="120" y="20" font-family="Noto Sans KR" font-size="12" fill="{C["gold_bright"]}" text-anchor="middle">Bounce Mode</text>
    <rect x="40" y="60" width="160" height="20" rx="4" fill="{C["card"]}" stroke="{C["gold"]}" stroke-width="1.5"/>
    <line x1="40" y1="50" x2="40" y2="60" stroke="{C["gold"]}" stroke-width="1.5" stroke-dasharray="3 2"/>
    <line x1="200" y1="50" x2="200" y2="60" stroke="{C["gold"]}" stroke-width="1.5" stroke-dasharray="3 2"/>
    <rect x="40" y="30" width="160" height="20" rx="4" fill="none" stroke="{C["gold"]}" stroke-width="1" stroke-dasharray="4 3" opacity="0.4"/>
    <text x="120" y="105" font-family="JetBrains Mono" font-size="10" fill="{C["green"]}" text-anchor="middle">동위상 상하 운동</text>
    <!-- Pitch mode -->
    <text x="360" y="20" font-family="Noto Sans KR" font-size="12" fill="{C["purple"]}" text-anchor="middle">Pitch Mode</text>
    <rect x="280" y="55" width="160" height="20" rx="4" fill="{C["card"]}" stroke="{C["purple"]}" stroke-width="1.5" transform="rotate(-8,360,65)"/>
    <rect x="280" y="30" width="160" height="20" rx="4" fill="none" stroke="{C["purple"]}" stroke-width="1" stroke-dasharray="4 3" opacity="0.4"/>
    <text x="360" y="105" font-family="JetBrains Mono" font-size="10" fill="{C["purple"]}" text-anchor="middle">전후 역위상 회전</text>
    <!-- Mode shape vectors -->
    <text x="240" y="160" font-family="Noto Sans KR" font-size="11" fill="{C["dim"]}" text-anchor="middle">모드 형상 비교</text>
    <rect x="50" y="170" width="170" height="60" rx="4" fill="{C["card"]}" stroke="{C["dim"]}" stroke-width="0.5"/>
    <text x="135" y="195" font-family="JetBrains Mono" font-size="10" fill="{C["gold_bright"]}" text-anchor="middle">φ₁ = {{1, 1}} (bounce)</text>
    <text x="135" y="215" font-family="JetBrains Mono" font-size="10" fill="{C["dim"]}" text-anchor="middle">f₁ ≈ 1.0~1.5 Hz</text>
    <rect x="260" y="170" width="170" height="60" rx="4" fill="{C["card"]}" stroke="{C["dim"]}" stroke-width="0.5"/>
    <text x="345" y="195" font-family="JetBrains Mono" font-size="10" fill="{C["purple"]}" text-anchor="middle">φ₂ = {{1, -1}} (pitch)</text>
    <text x="345" y="215" font-family="JetBrains Mono" font-size="10" fill="{C["dim"]}" text-anchor="middle">f₂ ≈ 1.2~1.8 Hz</text>
  </svg>"""
    return a, b

def svg_day12():
    """전달함수 — 블록다이어그램"""
    a = f"""<svg viewBox="0 0 480 180" width="480" height="180" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    <!-- Input -->
    <text x="20" y="95" font-family="JetBrains Mono" font-size="12" fill="{C["gold_bright"]}">Z_r(s)</text>
    <line x1="70" y1="90" x2="110" y2="90" stroke="{C["gold_bright"]}" stroke-width="2" marker-end="url(#arrowGold)"/>
    <!-- System block -->
    <rect x="115" y="65" width="160" height="50" rx="8" fill="{C["card"]}" stroke="{C["gold"]}" stroke-width="2"/>
    <text x="195" y="85" font-family="JetBrains Mono" font-size="12" fill="{C["gold_bright"]}" text-anchor="middle">H(s)</text>
    <text x="195" y="103" font-family="Noto Sans KR" font-size="9" fill="{C["dim"]}" text-anchor="middle">차량 전달함수</text>
    <!-- Output -->
    <line x1="280" y1="90" x2="320" y2="90" stroke="{C["gold_bright"]}" stroke-width="2" marker-end="url(#arrowGold)"/>
    <text x="330" y="95" font-family="JetBrains Mono" font-size="12" fill="{C["gold_bright"]}">Z_s(s)</text>
    <!-- Equation -->
    <text x="195" y="155" font-family="JetBrains Mono" font-size="11" fill="{C["green"]}" text-anchor="middle">H(s) = Z_s(s) / Z_r(s)</text>
  </svg>"""
    return a, None

def svg_day13():
    """전달률 — 방진 곡선"""
    a = None
    b = f"""<svg viewBox="0 0 480 260" width="480" height="260" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 410, 220)}
    <line x1="50" y1="230" x2="460" y2="230" stroke="{C["dim"]}" stroke-width="1"/>
    <line x1="50" y1="10" x2="50" y2="230" stroke="{C["dim"]}" stroke-width="1"/>
    <text x="460" y="248" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}">r = ω/ωₙ</text>
    <text x="15" y="15" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}">TR</text>
    <!-- TR=1 line -->
    <line x1="50" y1="140" x2="460" y2="140" stroke="{C["dim"]}" stroke-width="0.8" stroke-dasharray="4 3"/>
    <text x="462" y="138" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}">TR=1</text>
    <!-- √2 line -->
    <line x1="215" y1="10" x2="215" y2="230" stroke="{C["purple"]}" stroke-width="0.8" stroke-dasharray="4 3"/>
    <text x="215" y="248" font-family="JetBrains Mono" font-size="9" fill="{C["purple"]}" text-anchor="middle">√2</text>
    <!-- Curve -->
    <path d="M50,140 C80,138 120,130 155,70 C165,35 170,25 175,30 C180,35 185,50 200,90 C220,130 240,140 260,145 C300,155 350,170 400,185 C430,192 450,195 460,198" fill="none" stroke="{C["gold_bright"]}" stroke-width="2.5"/>
    <!-- Zones -->
    <rect x="55" y="15" width="155" height="20" rx="4" fill="{C["orange"]}" opacity="0.15"/>
    <text x="130" y="30" font-family="Noto Sans KR" font-size="10" fill="{C["orange"]}" text-anchor="middle">증폭 영역</text>
    <rect x="220" y="145" width="230" height="20" rx="4" fill="{C["green"]}" opacity="0.15"/>
    <text x="335" y="160" font-family="Noto Sans KR" font-size="10" fill="{C["green"]}" text-anchor="middle">방진(절연) 영역 TR < 1</text>
  </svg>"""
    return a, b

def svg_day14():
    """노면 PSD + ISO 2631 가중"""
    a = None
    b = f"""<svg viewBox="0 0 480 260" width="480" height="260" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 410, 220)}
    <line x1="50" y1="230" x2="460" y2="230" stroke="{C["dim"]}" stroke-width="1"/>
    <line x1="50" y1="10" x2="50" y2="230" stroke="{C["dim"]}" stroke-width="1"/>
    <text x="460" y="248" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}">f [Hz]</text>
    <text x="15" y="15" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}">PSD</text>
    <!-- Road PSD (log-log straight line approximation) -->
    <path d="M80,30 L200,120 L350,190 L460,225" fill="none" stroke="{C["dim"]}" stroke-width="2"/>
    <text x="100" y="50" font-family="JetBrains Mono" font-size="10" fill="{C["dim"]}">ISO 8608 노면</text>
    <!-- Vehicle response -->
    <path d="M80,200 C100,195 130,160 150,80 C160,50 163,42 167,50 C175,80 190,150 220,190 C250,205 300,210 340,215 C380,218 430,220 460,222" fill="none" stroke="{C["gold_bright"]}" stroke-width="2.5"/>
    <text x="170" y="38" font-family="JetBrains Mono" font-size="10" fill="{C["gold_bright"]}">차체 응답 PSD</text>
    <!-- 1-80 Hz annotation -->
    <rect x="85" y="230" width="350" height="18" rx="4" fill="{C["green"]}" opacity="0.1"/>
    <text x="260" y="243" font-family="JetBrains Mono" font-size="9" fill="{C["green"]}" text-anchor="middle">ISO 2631 가중 범위: 1~80 Hz</text>
  </svg>"""
    return a, b

# ═══════════════════════════════════════════════════
# PART 3: Day 15~21 SVG
# ═══════════════════════════════════════════════════

def svg_day15():
    """Part 2 복습 — 모델 복잡도 비교"""
    a = f"""<svg viewBox="0 0 480 200" width="480" height="200" xmlns="http://www.w3.org/2000/svg">
    <!-- QC box -->
    <rect x="20" y="30" width="120" height="80" rx="8" fill="{C["card"]}" stroke="{C["green"]}" stroke-width="1.5"/>
    <text x="80" y="60" font-family="JetBrains Mono" font-size="12" fill="{C["green"]}" text-anchor="middle">Quarter Car</text>
    <text x="80" y="80" font-family="JetBrains Mono" font-size="10" fill="{C["dim"]}" text-anchor="middle">2 DOF</text>
    <text x="80" y="95" font-family="JetBrains Mono" font-size="10" fill="{C["dim"]}" text-anchor="middle">bounce + hop</text>
    <!-- HC box -->
    <rect x="170" y="30" width="120" height="80" rx="8" fill="{C["card"]}" stroke="{C["gold"]}" stroke-width="1.5"/>
    <text x="230" y="60" font-family="JetBrains Mono" font-size="12" fill="{C["gold_bright"]}" text-anchor="middle">Half Car</text>
    <text x="230" y="80" font-family="JetBrains Mono" font-size="10" fill="{C["dim"]}" text-anchor="middle">4 DOF</text>
    <text x="230" y="95" font-family="JetBrains Mono" font-size="10" fill="{C["dim"]}" text-anchor="middle">+ pitch</text>
    <!-- FC box -->
    <rect x="320" y="30" width="140" height="80" rx="8" fill="{C["card"]}" stroke="{C["purple"]}" stroke-width="1.5"/>
    <text x="390" y="60" font-family="JetBrains Mono" font-size="12" fill="{C["purple"]}" text-anchor="middle">Full Vehicle</text>
    <text x="390" y="80" font-family="JetBrains Mono" font-size="10" fill="{C["dim"]}" text-anchor="middle">7+ DOF</text>
    <text x="390" y="95" font-family="JetBrains Mono" font-size="10" fill="{C["dim"]}" text-anchor="middle">+ roll + warp</text>
    <!-- Arrow flow -->
    <line x1="145" y1="70" x2="165" y2="70" stroke="{C["dim"]}" stroke-width="2" marker-end="url(#arrowDim)"/>
    <line x1="295" y1="70" x2="315" y2="70" stroke="{C["dim"]}" stroke-width="2" marker-end="url(#arrowDim)"/>
    {ARROW_DEFS}
    <text x="240" y="160" font-family="Noto Sans KR" font-size="11" fill="{C["dim"]}" text-anchor="middle">모델 복잡도 ────────→</text>
  </svg>"""
    return a, None

def svg_day16():
    """스프링 — 직렬/병렬 + progressive"""
    a = None
    b = f"""<svg viewBox="0 0 480 250" width="480" height="250" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 200, 210)}
    <line x1="50" y1="230" x2="260" y2="230" stroke="{C["dim"]}" stroke-width="1"/>
    <line x1="50" y1="10" x2="50" y2="230" stroke="{C["dim"]}" stroke-width="1"/>
    <text x="260" y="248" font-family="JetBrains Mono" font-size="10" fill="{C["gold_bright"]}">x [mm]</text>
    <text x="15" y="15" font-family="JetBrains Mono" font-size="10" fill="{C["gold_bright"]}">F [N]</text>
    <!-- Linear -->
    <line x1="50" y1="210" x2="240" y2="40" stroke="{C["green"]}" stroke-width="2"/>
    <text x="200" y="55" font-family="JetBrains Mono" font-size="9" fill="{C["green"]}">선형 k</text>
    <!-- Progressive -->
    <path d="M50,210 C100,200 150,170 200,100 C230,50 245,25 250,18" fill="none" stroke="{C["gold_bright"]}" stroke-width="2.5"/>
    <text x="230" y="18" font-family="JetBrains Mono" font-size="9" fill="{C["gold_bright"]}">프로그레시브</text>
    <!-- Series/Parallel diagram on right -->
    <text x="370" y="25" font-family="Noto Sans KR" font-size="11" fill="{C["dim"]}" text-anchor="middle">직렬 vs 병렬</text>
    <rect x="300" y="40" width="60" height="90" rx="4" fill="{C["card"]}" stroke="{C["green"]}" stroke-width="1"/>
    <text x="330" y="75" font-family="JetBrains Mono" font-size="9" fill="{C["green"]}" text-anchor="middle">k₁</text>
    <text x="330" y="100" font-family="JetBrains Mono" font-size="9" fill="{C["green"]}" text-anchor="middle">k₂</text>
    <text x="330" y="148" font-family="JetBrains Mono" font-size="9" fill="{C["green"]}" text-anchor="middle">직렬</text>
    <text x="330" y="165" font-family="JetBrains Mono" font-size="8" fill="{C["dim"]}" text-anchor="middle">1/k=1/k₁+1/k₂</text>
    <rect x="400" y="40" width="60" height="90" rx="4" fill="{C["card"]}" stroke="{C["gold"]}" stroke-width="1"/>
    <text x="430" y="80" font-family="JetBrains Mono" font-size="9" fill="{C["gold"]}" text-anchor="middle">k₁ ∥ k₂</text>
    <text x="430" y="148" font-family="JetBrains Mono" font-size="9" fill="{C["gold"]}" text-anchor="middle">병렬</text>
    <text x="430" y="165" font-family="JetBrains Mono" font-size="8" fill="{C["dim"]}" text-anchor="middle">k=k₁+k₂</text>
  </svg>"""
    return a, b

def svg_day17():
    """댐퍼 — F-v 곡선"""
    a = None
    b = f"""<svg viewBox="0 0 480 260" width="480" height="260" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 410, 220)}
    <line x1="240" y1="10" x2="240" y2="230" stroke="{C["dim"]}" stroke-width="1"/>
    <line x1="50" y1="120" x2="460" y2="120" stroke="{C["dim"]}" stroke-width="1"/>
    <text x="460" y="115" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}">v [m/s]</text>
    <text x="245" y="20" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}">F [N]</text>
    <text x="350" y="248" font-family="Noto Sans KR" font-size="9" fill="{C["orange"]}">Rebound (인장)</text>
    <text x="130" y="248" font-family="Noto Sans KR" font-size="9" fill="{C["blue"]}">Bound (압축)</text>
    <!-- Bound side (compression, left, softer) -->
    <path d="M240,120 C220,130 180,155 140,170 C110,180 80,185 60,188" fill="none" stroke="{C["blue"]}" stroke-width="2.5"/>
    <!-- Rebound side (extension, right, stiffer) -->
    <path d="M240,120 C260,100 300,60 340,38 C370,25 400,18 430,15" fill="none" stroke="{C["orange"]}" stroke-width="2.5"/>
    <!-- Blow-off -->
    <circle cx="340" cy="38" r="4" fill="{C["orange"]}"/>
    <text x="345" y="52" font-family="JetBrains Mono" font-size="9" fill="{C["orange"]}">Blow-off</text>
    <!-- Asymmetry label -->
    <text x="380" y="145" font-family="JetBrains Mono" font-size="10" fill="{C["dim"]}">R/C ratio ≈ 2~3</text>
  </svg>"""
    return a, b

def svg_day18():
    """부싱 — 복소강성 벡터 다이어그램"""
    a = f"""<svg viewBox="0 0 400 280" width="400" height="280" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    <!-- Axes -->
    <line x1="80" y1="220" x2="350" y2="220" stroke="{C["dim"]}" stroke-width="1"/>
    <line x1="80" y1="250" x2="80" y2="30" stroke="{C["dim"]}" stroke-width="1"/>
    <text x="350" y="240" font-family="JetBrains Mono" font-size="11" fill="{C["dim"]}">K' (Storage)</text>
    <text x="50" y="30" font-family="JetBrains Mono" font-size="11" fill="{C["dim"]}">K'' (Loss)</text>
    <!-- K* vector -->
    <line x1="80" y1="220" x2="300" y2="80" stroke="{C["gold_bright"]}" stroke-width="2.5" marker-end="url(#arrowGold)"/>
    <text x="210" y="130" font-family="JetBrains Mono" font-size="14" fill="{C["gold_bright"]}">K*</text>
    <!-- K' component -->
    <line x1="80" y1="220" x2="300" y2="220" stroke="{C["green"]}" stroke-width="1.5" stroke-dasharray="4 3"/>
    <text x="190" y="248" font-family="JetBrains Mono" font-size="11" fill="{C["green"]}" text-anchor="middle">K'</text>
    <!-- K'' component -->
    <line x1="300" y1="220" x2="300" y2="80" stroke="{C["orange"]}" stroke-width="1.5" stroke-dasharray="4 3"/>
    <text x="315" y="155" font-family="JetBrains Mono" font-size="11" fill="{C["orange"]}">K''</text>
    <!-- Angle -->
    <path d="M130,220 A50,50 0 0,0 115,195" fill="none" stroke="{C["purple"]}" stroke-width="1.5"/>
    <text x="138" y="200" font-family="JetBrains Mono" font-size="11" fill="{C["purple"]}">δ</text>
    <text x="200" y="270" font-family="JetBrains Mono" font-size="10" fill="{C["dim"]}" text-anchor="middle">tan(δ) = K''/K' = η (Loss Factor)</text>
  </svg>"""
    return a, None

def svg_day19():
    """타이어 수직 동특성 — 타이어 모델 + 동강성 주파수 곡선"""
    a = f"""<svg viewBox="0 0 440 320" width="440" height="320" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    <!-- Road surface -->
    {_ground(80, 280, 280)}
    <!-- Tire (circle) -->
    <ellipse cx="220" cy="240" rx="60" ry="35" fill="none" stroke="{C["gold"]}" stroke-width="2"/>
    <text x="220" y="244" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}" text-anchor="middle">Contact Patch</text>
    <!-- Tire spring + damper to wheel -->
    {_spring(180, 140, 205, "k_t", C["green"])}
    {_damper(260, 140, 205, "c_t", C["blue"])}
    <!-- Wheel center mass -->
    {_mass(190, 120, 60, 20, "m_w", C["gold_bright"])}
    <!-- Enveloping filter annotation -->
    <rect x="310" y="170" width="120" height="50" rx="6" fill="{C["card"]}" stroke="{C["purple"]}" stroke-width="1"/>
    <text x="370" y="190" font-family="JetBrains Mono" font-size="9" fill="{C["purple"]}" text-anchor="middle">Enveloping</text>
    <text x="370" y="206" font-family="JetBrains Mono" font-size="9" fill="{C["purple"]}" text-anchor="middle">Filter</text>
    <!-- Labels -->
    <text x="220" y="30" font-family="Noto Sans KR" font-size="13" fill="{C["gold_bright"]}" text-anchor="middle">타이어 수직 동특성 모델</text>
    <text x="220" y="310" font-family="JetBrains Mono" font-size="10" fill="{C["dim"]}" text-anchor="middle">k_t ≈ 200 kN/m · c_t ≈ 200 N·s/m</text>
  </svg>"""
    b = f"""<svg viewBox="0 0 480 260" width="480" height="260" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 410, 220)}
    {_axes(50, 230, 410, 220, "f [Hz]", "|k*| [kN/m]")}
    <!-- Dynamic stiffness curve (increases with frequency) -->
    <path d="M80,200 C120,195 160,185 200,170 C240,150 280,125 320,100 C360,80 400,65 440,55" fill="none" stroke="{C["gold_bright"]}" stroke-width="2.5"/>
    <text x="350" y="45" font-family="JetBrains Mono" font-size="10" fill="{C["gold_bright"]}">|k*(f)|</text>
    <!-- Loss angle curve -->
    <path d="M80,180 C120,170 160,160 200,155 C240,160 280,170 320,175 C360,178 400,180 440,181" fill="none" stroke="{C["orange"]}" stroke-width="2" stroke-dasharray="6 3"/>
    <text x="350" y="195" font-family="JetBrains Mono" font-size="10" fill="{C["orange"]}">tan(δ)</text>
    <!-- Frequency zones -->
    <text x="120" y="248" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}" text-anchor="middle">1</text>
    <text x="260" y="248" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}" text-anchor="middle">30</text>
    <text x="420" y="248" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}" text-anchor="middle">100</text>
  </svg>"""
    return a, b

def svg_day20():
    """Tire Hop — 질량비 영향 + Hop 주파수 곡선"""
    a = f"""<svg viewBox="0 0 440 300" width="440" height="300" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    <!-- Ground -->
    {_ground(80, 260, 280)}
    <!-- Tire spring -->
    {_spring(170, 200, 255, "k_t", C["green"])}
    <!-- Unsprung mass -->
    {_mass(150, 170, 80, 30, "m_u", C["orange"])}
    <!-- Suspension spring + damper -->
    {_spring(150, 90, 170, "k_s", C["green"])}
    {_damper(240, 90, 170, "c_s", C["blue"])}
    <!-- Sprung mass -->
    {_mass(130, 60, 120, 30, "m_s", C["gold_bright"])}
    <!-- Hop mode arrow -->
    <line x1="320" y1="185" x2="320" y2="145" stroke="{C["orange"]}" stroke-width="2" marker-end="url(#arrowOrange)"/>
    <line x1="320" y1="185" x2="320" y2="225" stroke="{C["orange"]}" stroke-width="2" marker-end="url(#arrowOrange)"/>
    <text x="345" y="190" font-family="JetBrains Mono" font-size="10" fill="{C["orange"]}">Tire Hop</text>
    <text x="345" y="205" font-family="JetBrains Mono" font-size="10" fill="{C["orange"]}">~12 Hz</text>
    <!-- Title -->
    <text x="220" y="25" font-family="Noto Sans KR" font-size="13" fill="{C["gold_bright"]}" text-anchor="middle">Tire Hop 모드 (언스프렁 질량)</text>
  </svg>"""
    b = f"""<svg viewBox="0 0 480 260" width="480" height="260" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 410, 220)}
    {_axes(50, 230, 410, 220, "m_u/m_s", "f_hop [Hz]")}
    <!-- Hop frequency vs mass ratio -->
    <path d="M80,40 C120,60 160,80 200,100 C240,120 280,140 320,160 C360,175 400,188 440,198" fill="none" stroke="{C["orange"]}" stroke-width="2.5"/>
    <text x="300" y="130" font-family="JetBrains Mono" font-size="10" fill="{C["orange"]}">f_hop = √(k_t/m_u)/2π</text>
    <!-- Optimal zone -->
    <rect x="100" y="50" width="80" height="100" rx="4" fill="{C["green"]}" opacity="0.08"/>
    <text x="140" y="170" font-family="JetBrains Mono" font-size="9" fill="{C["green"]}" text-anchor="middle">최적 영역</text>
    <text x="140" y="185" font-family="JetBrains Mono" font-size="9" fill="{C["green"]}" text-anchor="middle">μ ≈ 0.1~0.15</text>
  </svg>"""
    return a, b

def svg_day21():
    """Skyhook 제어 개념도"""
    a = f"""<svg viewBox="0 0 480 350" width="480" height="350" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    <!-- Sky (reference) -->
    <line x1="60" y1="30" x2="420" y2="30" stroke="{C["purple"]}" stroke-width="1.5" stroke-dasharray="6 3"/>
    <text x="240" y="22" font-family="JetBrains Mono" font-size="11" fill="{C["purple"]}" text-anchor="middle">가상의 하늘 (관성 기준)</text>
    <!-- Skyhook damper -->
    {_damper(240, 30, 120, "c_sky", C["purple"])}
    <!-- Sprung mass -->
    {_mass(160, 120, 160, 40, "m_s")}
    <!-- Suspension -->
    {_spring(195, 165, 250, "k_s")}
    {_damper(305, 165, 250, "c_s")}
    <!-- Unsprung mass -->
    {_mass(170, 255, 140, 30, "m_u", C["blue"])}
    <!-- Road -->
    <path d="M100,330 Q240,325 380,330" fill="none" stroke="{C["dim"]}" stroke-width="2"/>
    <text x="240" y="345" font-family="JetBrains Mono" font-size="10" fill="{C["dim"]}" text-anchor="middle">노면 z_r</text>
    <!-- Concept label -->
    <text x="400" y="80" font-family="Noto Sans KR" font-size="10" fill="{C["purple"]}">하늘에 댐퍼를</text>
    <text x="400" y="95" font-family="Noto Sans KR" font-size="10" fill="{C["purple"]}">걸 수 있다면?</text>
  </svg>"""
    return a, None


# ═══════════════════════════════════════════════════
# PART 4: Day 22~28 SVG
# ═══════════════════════════════════════════════════

def svg_day22():
    return svg_day15()  # PART 3 복습도 같은 패턴

def svg_day23():
    """푸리에 변환 — 시간→주파수 분해"""
    a = None
    b = f"""<svg viewBox="0 0 480 250" width="480" height="250" xmlns="http://www.w3.org/2000/svg">
    <!-- Time domain -->
    <rect x="20" y="10" width="200" height="100" rx="6" fill="{C["card"]}" stroke="{C["dim"]}" stroke-width="0.5"/>
    <text x="120" y="28" font-family="Noto Sans KR" font-size="10" fill="{C["dim"]}" text-anchor="middle">시간 영역</text>
    <path d="M40,70 Q55,40 70,70 Q80,90 90,70 Q100,45 115,70 Q125,85 135,70 Q148,50 160,70 Q168,82 175,70 Q185,55 200,70" fill="none" stroke="{C["gold_bright"]}" stroke-width="2"/>
    <text x="120" y="100" font-family="JetBrains Mono" font-size="10" fill="{C["gold_bright"]}" text-anchor="middle">x(t)</text>
    <!-- Arrow -->
    <text x="255" y="55" font-family="JetBrains Mono" font-size="24" fill="{C["green"]}" text-anchor="middle">→</text>
    <text x="255" y="75" font-family="JetBrains Mono" font-size="10" fill="{C["green"]}" text-anchor="middle">FFT</text>
    <!-- Frequency domain -->
    <rect x="290" y="10" width="170" height="100" rx="6" fill="{C["card"]}" stroke="{C["dim"]}" stroke-width="0.5"/>
    <text x="375" y="28" font-family="Noto Sans KR" font-size="10" fill="{C["dim"]}" text-anchor="middle">주파수 영역</text>
    <line x1="310" y1="95" x2="440" y2="95" stroke="{C["dim"]}" stroke-width="0.8"/>
    <rect x="325" y="50" width="15" height="45" rx="2" fill="{C["gold_bright"]}"/>
    <rect x="355" y="65" width="15" height="30" rx="2" fill="{C["green"]}"/>
    <rect x="385" y="78" width="15" height="17" rx="2" fill="{C["blue"]}"/>
    <rect x="415" y="85" width="15" height="10" rx="2" fill="{C["purple"]}"/>
    <text x="375" y="108" font-family="JetBrains Mono" font-size="10" fill="{C["gold_bright"]}" text-anchor="middle">|X(f)|</text>
    <!-- Nyquist -->
    <text x="240" y="170" font-family="JetBrains Mono" font-size="11" fill="{C["orange"]}" text-anchor="middle">Nyquist: f_s > 2·f_max (앨리어싱 방지)</text>
    <!-- Sine decomposition -->
    <text x="240" y="200" font-family="Noto Sans KR" font-size="10" fill="{C["dim"]}" text-anchor="middle">복잡한 신호 = 사인파들의 합</text>
    <path d="M60,230 Q100,215 140,230 Q180,245 220,230" fill="none" stroke="{C["gold_bright"]}" stroke-width="1.5"/>
    <text x="145" y="222" font-family="JetBrains Mono" font-size="8" fill="{C["gold_bright"]}">f₁</text>
    <text x="240" y="230" font-family="JetBrains Mono" font-size="14" fill="{C["dim"]}">+</text>
    <path d="M260,230 Q280,220 300,230 Q320,240 340,230" fill="none" stroke="{C["green"]}" stroke-width="1.5"/>
    <text x="305" y="222" font-family="JetBrains Mono" font-size="8" fill="{C["green"]}">f₂</text>
    <text x="355" y="230" font-family="JetBrains Mono" font-size="14" fill="{C["dim"]}">+</text>
    <path d="M370,230 Q378,225 386,230 Q394,235 402,230" fill="none" stroke="{C["blue"]}" stroke-width="1.5"/>
    <text x="390" y="222" font-family="JetBrains Mono" font-size="8" fill="{C["blue"]}">f₃</text>
    <text x="420" y="230" font-family="JetBrains Mono" font-size="14" fill="{C["dim"]}">+ ···</text>
  </svg>"""
    return a, b

def svg_day24():
    """PSD 정의 — 시간→주파수 변환 + PSD 곡선"""
    a = f"""<svg viewBox="0 0 480 180" width="480" height="180" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    <!-- Time domain box -->
    <rect x="20" y="40" width="160" height="80" rx="8" fill="{C["card"]}" stroke="{C["green"]}" stroke-width="1.5"/>
    <text x="100" y="65" font-family="JetBrains Mono" font-size="11" fill="{C["green"]}" text-anchor="middle">x(t)</text>
    <text x="100" y="85" font-family="Noto Sans KR" font-size="9" fill="{C["dim"]}" text-anchor="middle">시간 영역 신호</text>
    <text x="100" y="105" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}" text-anchor="middle">σ², R_xx(τ)</text>
    <!-- Arrow with FFT label -->
    <line x1="185" y1="80" x2="275" y2="80" stroke="{C["gold_bright"]}" stroke-width="2" marker-end="url(#arrowGold)"/>
    <text x="230" y="72" font-family="JetBrains Mono" font-size="10" fill="{C["gold_bright"]}" text-anchor="middle">FFT</text>
    <text x="230" y="100" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}" text-anchor="middle">Wiener–Khinchin</text>
    <!-- Frequency domain box -->
    <rect x="280" y="40" width="180" height="80" rx="8" fill="{C["card"]}" stroke="{C["gold"]}" stroke-width="1.5"/>
    <text x="370" y="65" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}" text-anchor="middle">S_xx(f)</text>
    <text x="370" y="85" font-family="Noto Sans KR" font-size="9" fill="{C["dim"]}" text-anchor="middle">파워 스펙트럼 밀도</text>
    <text x="370" y="105" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}" text-anchor="middle">[단위²/Hz]</text>
    <!-- Bottom equation -->
    <text x="240" y="160" font-family="JetBrains Mono" font-size="11" fill="{C["green"]}" text-anchor="middle">σ² = ∫ S_xx(f) df — 면적 = 총 에너지</text>
  </svg>"""
    b = f"""<svg viewBox="0 0 480 260" width="480" height="260" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 410, 220)}
    {_axes(50, 230, 410, 220, "f [Hz] (log)", "S_xx [log]")}
    <!-- PSD curve (log-log, decreasing) -->
    <path d="M80,30 C120,60 160,100 200,130 C240,155 280,175 320,190 C360,200 400,208 440,213" fill="none" stroke="{C["gold_bright"]}" stroke-width="2.5"/>
    <!-- Shaded area under curve -->
    <path d="M80,30 C120,60 160,100 200,130 C240,155 280,175 320,190 C360,200 400,208 440,213 L440,230 L80,230 Z" fill="{C["gold"]}" opacity="0.08"/>
    <text x="260" y="210" font-family="JetBrains Mono" font-size="10" fill="{C["gold"]}" text-anchor="middle">σ² = 면적</text>
    <!-- Slope annotation -->
    <text x="120" y="60" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}">-2n slope</text>
  </svg>"""
    return a, b

def svg_day25():
    """FRF 측정 — 측정 셋업 + FRF 곡선"""
    a = f"""<svg viewBox="0 0 480 200" width="480" height="200" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    <!-- Impact hammer -->
    <rect x="30" y="60" width="20" height="80" rx="3" fill="{C["card"]}" stroke="{C["orange"]}" stroke-width="1.5"/>
    <text x="40" y="55" font-family="JetBrains Mono" font-size="9" fill="{C["orange"]}" text-anchor="middle">해머</text>
    <line x1="55" y1="100" x2="90" y2="100" stroke="{C["orange"]}" stroke-width="2" marker-end="url(#arrowOrange)"/>
    <text x="72" y="92" font-family="JetBrains Mono" font-size="9" fill="{C["orange"]}" text-anchor="middle">F(t)</text>
    <!-- Structure (DUT) -->
    <rect x="95" y="50" width="120" height="100" rx="8" fill="{C["card"]}" stroke="{C["gold"]}" stroke-width="2"/>
    <text x="155" y="90" font-family="Noto Sans KR" font-size="11" fill="{C["gold_bright"]}" text-anchor="middle">시험체</text>
    <text x="155" y="110" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}" text-anchor="middle">(DUT)</text>
    <!-- Accelerometer -->
    <line x1="220" y1="100" x2="260" y2="100" stroke="{C["green"]}" stroke-width="2" marker-end="url(#arrowGreen)"/>
    <text x="240" y="92" font-family="JetBrains Mono" font-size="9" fill="{C["green"]}" text-anchor="middle">a(t)</text>
    <rect x="265" y="80" width="50" height="40" rx="4" fill="{C["card"]}" stroke="{C["green"]}" stroke-width="1.5"/>
    <text x="290" y="104" font-family="JetBrains Mono" font-size="8" fill="{C["green"]}" text-anchor="middle">가속도계</text>
    <!-- DAQ -->
    <line x1="320" y1="100" x2="350" y2="100" stroke="{C["dim"]}" stroke-width="1.5" marker-end="url(#arrowDim)"/>
    <rect x="355" y="60" width="100" height="80" rx="6" fill="{C["card"]}" stroke="{C["blue"]}" stroke-width="1.5"/>
    <text x="405" y="90" font-family="JetBrains Mono" font-size="10" fill="{C["blue"]}" text-anchor="middle">DAQ</text>
    <text x="405" y="108" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}" text-anchor="middle">FFT → H(f)</text>
    <!-- Bottom equation -->
    <text x="240" y="185" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}" text-anchor="middle">H(f) = S_xy(f) / S_xx(f) — H₁ estimator</text>
  </svg>"""
    b = f"""<svg viewBox="0 0 480 260" width="480" height="260" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 410, 220)}
    {_axes(50, 230, 410, 220, "f [Hz]", "|H(f)| [dB]")}
    <!-- FRF magnitude curve with two peaks -->
    <path d="M80,200 C100,195 130,180 150,140 C160,80 162,55 165,55 C168,55 172,80 180,140 C200,185 230,195 260,180 C280,140 290,80 293,60 C296,80 300,110 310,150 C330,190 380,205 430,210 C445,212 455,213 460,213" fill="none" stroke="{C["gold_bright"]}" stroke-width="2.5"/>
    <!-- Peak labels -->
    <text x="165" y="42" font-family="JetBrains Mono" font-size="9" fill="{C["green"]}" text-anchor="middle">f₁ bounce</text>
    <text x="293" y="47" font-family="JetBrains Mono" font-size="9" fill="{C["orange"]}" text-anchor="middle">f₂ hop</text>
    <!-- Coherence -->
    <path d="M80,30 C120,28 160,25 200,28 C240,30 280,32 320,30 C360,28 400,30 440,35" fill="none" stroke="{C["green"]}" stroke-width="1.5" stroke-dasharray="5 3"/>
    <text x="420" y="25" font-family="JetBrains Mono" font-size="9" fill="{C["green"]}">γ² ≈ 1</text>
  </svg>"""
    return a, b

def svg_day26():
    """고유치 — det[K-ω²M]=0 시각화"""
    a = f"""<svg viewBox="0 0 480 200" width="480" height="200" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    <!-- M matrix -->
    <rect x="30" y="50" width="90" height="70" rx="6" fill="{C["card"]}" stroke="{C["blue"]}" stroke-width="1.5"/>
    <text x="75" y="75" font-family="JetBrains Mono" font-size="14" fill="{C["blue"]}" text-anchor="middle">[M]</text>
    <text x="75" y="100" font-family="Noto Sans KR" font-size="9" fill="{C["dim"]}" text-anchor="middle">질량 행렬</text>
    <!-- K matrix -->
    <rect x="150" y="50" width="90" height="70" rx="6" fill="{C["card"]}" stroke="{C["green"]}" stroke-width="1.5"/>
    <text x="195" y="75" font-family="JetBrains Mono" font-size="14" fill="{C["green"]}" text-anchor="middle">[K]</text>
    <text x="195" y="100" font-family="Noto Sans KR" font-size="9" fill="{C["dim"]}" text-anchor="middle">강성 행렬</text>
    <!-- Arrow to eigenvalue -->
    <line x1="245" y1="85" x2="285" y2="85" stroke="{C["gold_bright"]}" stroke-width="2" marker-end="url(#arrowGold)"/>
    <text x="265" y="75" font-family="JetBrains Mono" font-size="9" fill="{C["gold_bright"]}" text-anchor="middle">det=0</text>
    <!-- Result: eigenvalues -->
    <rect x="290" y="40" width="170" height="90" rx="8" fill="{C["card"]}" stroke="{C["gold"]}" stroke-width="2"/>
    <text x="375" y="65" font-family="JetBrains Mono" font-size="12" fill="{C["gold_bright"]}" text-anchor="middle">ω₁², ω₂², ... ωₙ²</text>
    <text x="375" y="85" font-family="Noto Sans KR" font-size="10" fill="{C["dim"]}" text-anchor="middle">고유진동수</text>
    <text x="375" y="105" font-family="JetBrains Mono" font-size="10" fill="{C["purple"]}" text-anchor="middle">φ₁, φ₂, ... φₙ</text>
    <text x="375" y="120" font-family="Noto Sans KR" font-size="9" fill="{C["dim"]}" text-anchor="middle">모드 형상</text>
    <!-- Bottom equation -->
    <text x="240" y="175" font-family="JetBrains Mono" font-size="12" fill="{C["gold"]}" text-anchor="middle">det([K] − ω²[M]) = 0</text>
  </svg>"""
    b = f"""<svg viewBox="0 0 480 260" width="480" height="260" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 410, 220)}
    {_axes(50, 230, 410, 220, "ω²", "det([K]-ω²[M])")}
    <!-- Det curve crossing zero twice -->
    <path d="M80,60 C120,80 150,120 180,180 C195,220 200,230 210,220 C230,180 250,120 280,100 C300,110 330,160 350,220 C360,230 365,230 370,220 C380,180 400,120 440,60" fill="none" stroke="{C["gold_bright"]}" stroke-width="2.5"/>
    <!-- Zero line -->
    <line x1="50" y1="170" x2="460" y2="170" stroke="{C["dim"]}" stroke-width="0.8" stroke-dasharray="4 3"/>
    <!-- Zero crossings -->
    <circle cx="195" cy="170" r="6" fill="none" stroke="{C["green"]}" stroke-width="2"/>
    <text x="195" y="195" font-family="JetBrains Mono" font-size="10" fill="{C["green"]}" text-anchor="middle">ω₁²</text>
    <circle cx="358" cy="170" r="6" fill="none" stroke="{C["orange"]}" stroke-width="2"/>
    <text x="358" y="195" font-family="JetBrains Mono" font-size="10" fill="{C["orange"]}" text-anchor="middle">ω₂²</text>
  </svg>"""
    return a, b

def svg_day27():
    """모드 중첩법 — 물리좌표→모드좌표 변환"""
    a = f"""<svg viewBox="0 0 480 200" width="480" height="200" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    <!-- Physical coordinates -->
    <rect x="20" y="50" width="120" height="80" rx="8" fill="{C["card"]}" stroke="{C["blue"]}" stroke-width="1.5"/>
    <text x="80" y="78" font-family="JetBrains Mono" font-size="12" fill="{C["blue"]}" text-anchor="middle">{{x}}</text>
    <text x="80" y="98" font-family="Noto Sans KR" font-size="9" fill="{C["dim"]}" text-anchor="middle">물리 좌표</text>
    <text x="80" y="115" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}" text-anchor="middle">N-DOF coupled</text>
    <!-- Phi transform -->
    <line x1="145" y1="90" x2="195" y2="90" stroke="{C["gold_bright"]}" stroke-width="2" marker-end="url(#arrowGold)"/>
    <text x="170" y="80" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}" text-anchor="middle">[Φ]</text>
    <!-- Modal coordinates -->
    <rect x="200" y="50" width="120" height="80" rx="8" fill="{C["card"]}" stroke="{C["green"]}" stroke-width="1.5"/>
    <text x="260" y="78" font-family="JetBrains Mono" font-size="12" fill="{C["green"]}" text-anchor="middle">{{η}}</text>
    <text x="260" y="98" font-family="Noto Sans KR" font-size="9" fill="{C["dim"]}" text-anchor="middle">모드 좌표</text>
    <text x="260" y="115" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}" text-anchor="middle">N × 1-DOF</text>
    <!-- Sum back -->
    <line x1="325" y1="90" x2="365" y2="90" stroke="{C["gold_bright"]}" stroke-width="2" marker-end="url(#arrowGold)"/>
    <text x="345" y="80" font-family="JetBrains Mono" font-size="10" fill="{C["gold_bright"]}" text-anchor="middle">Σ</text>
    <!-- Result -->
    <rect x="370" y="50" width="100" height="80" rx="8" fill="{C["card"]}" stroke="{C["purple"]}" stroke-width="1.5"/>
    <text x="420" y="78" font-family="JetBrains Mono" font-size="12" fill="{C["purple"]}" text-anchor="middle">x(t)</text>
    <text x="420" y="98" font-family="Noto Sans KR" font-size="9" fill="{C["dim"]}" text-anchor="middle">응답 합성</text>
    <!-- Equation -->
    <text x="240" y="175" font-family="JetBrains Mono" font-size="11" fill="{C["gold"]}" text-anchor="middle">{{x}} = [Φ]{{η}} → 비연성 SDOF 합</text>
  </svg>"""
    return a, None

def svg_day28():
    """Part 4 복습 — 주파수 해석 파이프라인"""
    a = f"""<svg viewBox="0 0 480 160" width="480" height="160" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    <!-- Pipeline: FFT → PSD → FRF → Eigenvalue → Mode Superposition -->
    <rect x="10" y="40" width="75" height="50" rx="6" fill="{C["card"]}" stroke="{C["green"]}" stroke-width="1.5"/>
    <text x="47" y="60" font-family="JetBrains Mono" font-size="9" fill="{C["green"]}" text-anchor="middle">FFT</text>
    <text x="47" y="78" font-family="JetBrains Mono" font-size="8" fill="{C["dim"]}" text-anchor="middle">Day 23</text>
    <line x1="90" y1="65" x2="100" y2="65" stroke="{C["dim"]}" stroke-width="1.5" marker-end="url(#arrowDim)"/>
    <rect x="105" y="40" width="75" height="50" rx="6" fill="{C["card"]}" stroke="{C["gold"]}" stroke-width="1.5"/>
    <text x="142" y="60" font-family="JetBrains Mono" font-size="9" fill="{C["gold_bright"]}" text-anchor="middle">PSD</text>
    <text x="142" y="78" font-family="JetBrains Mono" font-size="8" fill="{C["dim"]}" text-anchor="middle">Day 24</text>
    <line x1="185" y1="65" x2="195" y2="65" stroke="{C["dim"]}" stroke-width="1.5" marker-end="url(#arrowDim)"/>
    <rect x="200" y="40" width="75" height="50" rx="6" fill="{C["card"]}" stroke="{C["blue"]}" stroke-width="1.5"/>
    <text x="237" y="60" font-family="JetBrains Mono" font-size="9" fill="{C["blue"]}" text-anchor="middle">FRF</text>
    <text x="237" y="78" font-family="JetBrains Mono" font-size="8" fill="{C["dim"]}" text-anchor="middle">Day 25</text>
    <line x1="280" y1="65" x2="290" y2="65" stroke="{C["dim"]}" stroke-width="1.5" marker-end="url(#arrowDim)"/>
    <rect x="295" y="40" width="75" height="50" rx="6" fill="{C["card"]}" stroke="{C["purple"]}" stroke-width="1.5"/>
    <text x="332" y="60" font-family="JetBrains Mono" font-size="9" fill="{C["purple"]}" text-anchor="middle">고유치</text>
    <text x="332" y="78" font-family="JetBrains Mono" font-size="8" fill="{C["dim"]}" text-anchor="middle">Day 26</text>
    <line x1="375" y1="65" x2="385" y2="65" stroke="{C["dim"]}" stroke-width="1.5" marker-end="url(#arrowDim)"/>
    <rect x="390" y="40" width="80" height="50" rx="6" fill="{C["card"]}" stroke="{C["orange"]}" stroke-width="1.5"/>
    <text x="430" y="60" font-family="JetBrains Mono" font-size="9" fill="{C["orange"]}" text-anchor="middle">모드중첩</text>
    <text x="430" y="78" font-family="JetBrains Mono" font-size="8" fill="{C["dim"]}" text-anchor="middle">Day 27</text>
    <text x="240" y="130" font-family="Noto Sans KR" font-size="11" fill="{C["gold_bright"]}" text-anchor="middle">PART 4 주파수 해석 파이프라인</text>
  </svg>"""
    return a, None

# ═══════════════════════════════════════════════════
# PART 5: Day 29~33 SVG
# ═══════════════════════════════════════════════════

def svg_day29():
    """수식→Simpack 매핑 — 4계층"""
    a = f"""<svg viewBox="0 0 480 250" width="480" height="250" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    <!-- 4 layers -->
    <rect x="30" y="15" width="200" height="45" rx="8" fill="{C["card"]}" stroke="{C["gold"]}" stroke-width="1.5"/>
    <text x="130" y="43" font-family="JetBrains Mono" font-size="12" fill="{C["gold_bright"]}" text-anchor="middle">Body (m, I)</text>
    <rect x="30" y="75" width="200" height="45" rx="8" fill="{C["card"]}" stroke="{C["green"]}" stroke-width="1.5"/>
    <text x="130" y="103" font-family="JetBrains Mono" font-size="12" fill="{C["green"]}" text-anchor="middle">Force Element (k, c)</text>
    <rect x="30" y="135" width="200" height="45" rx="8" fill="{C["card"]}" stroke="{C["blue"]}" stroke-width="1.5"/>
    <text x="130" y="163" font-family="JetBrains Mono" font-size="12" fill="{C["blue"]}" text-anchor="middle">Joint (DOF)</text>
    <rect x="30" y="195" width="200" height="45" rx="8" fill="{C["card"]}" stroke="{C["purple"]}" stroke-width="1.5"/>
    <text x="130" y="223" font-family="JetBrains Mono" font-size="12" fill="{C["purple"]}" text-anchor="middle">Marker (x,y,z,ψ,θ,φ)</text>
    <!-- Right side: Simpack GUI -->
    <rect x="280" y="15" width="180" height="225" rx="10" fill="{C["card"]}" stroke="{C["dim"]}" stroke-width="1"/>
    <text x="370" y="40" font-family="Noto Sans KR" font-size="12" fill="{C["dim"]}" text-anchor="middle">Simpack GUI</text>
    <text x="370" y="70" font-family="JetBrains Mono" font-size="10" fill="{C["gold_bright"]}" text-anchor="middle">mass = 400 kg</text>
    <text x="370" y="105" font-family="JetBrains Mono" font-size="10" fill="{C["green"]}" text-anchor="middle">k_lin = 22000 N/m</text>
    <text x="370" y="165" font-family="JetBrains Mono" font-size="10" fill="{C["blue"]}" text-anchor="middle">Prismatic (z)</text>
    <text x="370" y="225" font-family="JetBrains Mono" font-size="10" fill="{C["purple"]}" text-anchor="middle">Position + Orient</text>
    <!-- Arrows -->
    <line x1="235" y1="37" x2="275" y2="55" stroke="{C["gold"]}" stroke-width="1.5" marker-end="url(#arrowGold)"/>
    <line x1="235" y1="97" x2="275" y2="97" stroke="{C["green"]}" stroke-width="1.5" marker-end="url(#arrowGreen)"/>
    <line x1="235" y1="157" x2="275" y2="157" stroke="{C["blue"]}" stroke-width="1.5" marker-end="url(#arrowBlue)"/>
    <line x1="235" y1="217" x2="275" y2="217" stroke="{C["purple"]}" stroke-width="1.5" marker-end="url(#arrowPurple)"/>
  </svg>"""
    return a, None

def svg_day30():
    """V&V — 이론 vs 시뮬레이션"""
    a = None
    b = f"""<svg viewBox="0 0 480 220" width="480" height="220" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 410, 180)}
    {_axes(50, 100, 410, 80, "t", "z_s(t)")}
    <!-- Theory (dashed gold) -->
    <path d="M50,30 Q80,42 105,100 Q125,155 150,150 Q175,146 200,100 Q220,65 245,68 Q268,70 290,100 Q308,122 330,120 Q352,118 372,100 Q388,88 408,90 Q428,92 448,100" fill="none" stroke="{C["gold"]}" stroke-width="1.5" stroke-dasharray="6 3"/>
    <text x="380" y="35" font-family="JetBrains Mono" font-size="10" fill="{C["gold"]}">이론 (해석해)</text>
    <!-- Simpack (solid green) -->
    <path d="M50,30 Q80,44 105,100 Q126,156 150,150 Q176,147 200,100 Q221,64 245,67 Q269,70 290,100 Q309,123 330,121 Q353,119 372,100 Q389,87 408,89 Q429,91 448,100" fill="none" stroke="{C["green"]}" stroke-width="2.5"/>
    <text x="380" y="50" font-family="JetBrains Mono" font-size="10" fill="{C["green"]}">Simpack 결과</text>
    <!-- Match annotation -->
    <text x="260" y="200" font-family="JetBrains Mono" font-size="11" fill="{C["gold_bright"]}" text-anchor="middle">✅ Δf < 1%, Δζ < 5% → Verification 완료</text>
  </svg>"""
    return a, b

def svg_day31():
    """FRF 상관성 — 시뮬레이션 vs 실측 오버레이"""
    a = None
    b = f"""<svg viewBox="0 0 480 260" width="480" height="260" xmlns="http://www.w3.org/2000/svg">
    {_grid_bg(50, 10, 410, 220)}
    {_axes(50, 230, 410, 220, "f [Hz]", "|H(f)| [dB]")}
    <!-- Simulation curve -->
    <path d="M80,200 C100,195 130,180 150,130 C160,70 163,45 166,45 C169,45 173,70 183,140 C200,190 240,195 270,175 C285,130 290,75 293,55 C296,75 300,110 310,155 C340,195 400,210 440,213" fill="none" stroke="{C["gold_bright"]}" stroke-width="2.5"/>
    <text x="420" y="203" font-family="JetBrains Mono" font-size="9" fill="{C["gold_bright"]}">SIM</text>
    <!-- Measured curve (slightly offset) -->
    <path d="M80,195 C100,190 130,175 150,135 C160,78 163,55 167,52 C171,55 175,80 185,145 C200,185 240,190 270,170 C285,135 290,82 294,65 C298,82 302,115 312,155 C340,190 400,205 440,208" fill="none" stroke="{C["green"]}" stroke-width="2" stroke-dasharray="6 3"/>
    <text x="420" y="220" font-family="JetBrains Mono" font-size="9" fill="{C["green"]}">TEST</text>
    <!-- FRAC annotation -->
    <rect x="340" y="30" width="110" height="45" rx="6" fill="{C["card"]}" stroke="{C["purple"]}" stroke-width="1"/>
    <text x="395" y="48" font-family="JetBrains Mono" font-size="10" fill="{C["purple"]}" text-anchor="middle">FRAC = 0.92</text>
    <text x="395" y="66" font-family="JetBrains Mono" font-size="9" fill="{C["dim"]}" text-anchor="middle">MAC > 0.95</text>
  </svg>"""
    return a, b

def svg_day32():
    """Co-Sim 블록다이어그램"""
    a = f"""<svg viewBox="0 0 480 200" width="480" height="200" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    <!-- Simpack block -->
    <rect x="30" y="50" width="160" height="70" rx="10" fill="{C["card"]}" stroke="{C["green"]}" stroke-width="2"/>
    <text x="110" y="78" font-family="JetBrains Mono" font-size="13" fill="{C["green"]}" text-anchor="middle">Simpack</text>
    <text x="110" y="98" font-family="Noto Sans KR" font-size="10" fill="{C["dim"]}" text-anchor="middle">Plant Model</text>
    <!-- Simulink block -->
    <rect x="290" y="50" width="160" height="70" rx="10" fill="{C["card"]}" stroke="{C["orange"]}" stroke-width="2"/>
    <text x="370" y="78" font-family="JetBrains Mono" font-size="13" fill="{C["orange"]}" text-anchor="middle">Simulink</text>
    <text x="370" y="98" font-family="Noto Sans KR" font-size="10" fill="{C["dim"]}" text-anchor="middle">Controller</text>
    <!-- Arrows -->
    <line x1="195" y1="70" x2="285" y2="70" stroke="{C["gold_bright"]}" stroke-width="2" marker-end="url(#arrowGold)"/>
    <text x="240" y="62" font-family="JetBrains Mono" font-size="9" fill="{C["gold_bright"]}" text-anchor="middle">센서값 (z, ż, z̈)</text>
    <line x1="285" y1="105" x2="195" y2="105" stroke="{C["purple"]}" stroke-width="2" marker-end="url(#arrowPurple)"/>
    <text x="240" y="125" font-family="JetBrains Mono" font-size="9" fill="{C["purple"]}" text-anchor="middle">제어명령 (F_damper)</text>
    <!-- Communication step -->
    <text x="240" y="170" font-family="JetBrains Mono" font-size="10" fill="{C["dim"]}" text-anchor="middle">Δt_comm = 1 ms (FMI 2.0)</text>
  </svg>"""
    return a, None

def svg_day33():
    """디지털 트윈 파이프라인"""
    a = f"""<svg viewBox="0 0 480 180" width="480" height="180" xmlns="http://www.w3.org/2000/svg">
    {ARROW_DEFS}
    <!-- Pipeline stages -->
    <rect x="10" y="40" width="75" height="50" rx="6" fill="{C["card"]}" stroke="{C["green"]}" stroke-width="1.5"/>
    <text x="47" y="60" font-family="JetBrains Mono" font-size="9" fill="{C["green"]}" text-anchor="middle">PART 1</text>
    <text x="47" y="78" font-family="Noto Sans KR" font-size="8" fill="{C["dim"]}" text-anchor="middle">수학 기초</text>
    <line x1="90" y1="65" x2="100" y2="65" stroke="{C["dim"]}" stroke-width="1.5" marker-end="url(#arrowDim)"/>
    <rect x="105" y="40" width="75" height="50" rx="6" fill="{C["card"]}" stroke="{C["gold"]}" stroke-width="1.5"/>
    <text x="142" y="60" font-family="JetBrains Mono" font-size="9" fill="{C["gold_bright"]}" text-anchor="middle">PART 2</text>
    <text x="142" y="78" font-family="Noto Sans KR" font-size="8" fill="{C["dim"]}" text-anchor="middle">차량 모델</text>
    <line x1="185" y1="65" x2="195" y2="65" stroke="{C["dim"]}" stroke-width="1.5" marker-end="url(#arrowDim)"/>
    <rect x="200" y="40" width="75" height="50" rx="6" fill="{C["card"]}" stroke="{C["blue"]}" stroke-width="1.5"/>
    <text x="237" y="60" font-family="JetBrains Mono" font-size="9" fill="{C["blue"]}" text-anchor="middle">PART 3</text>
    <text x="237" y="78" font-family="Noto Sans KR" font-size="8" fill="{C["dim"]}" text-anchor="middle">부품 특성</text>
    <line x1="280" y1="65" x2="290" y2="65" stroke="{C["dim"]}" stroke-width="1.5" marker-end="url(#arrowDim)"/>
    <rect x="295" y="40" width="75" height="50" rx="6" fill="{C["card"]}" stroke="{C["purple"]}" stroke-width="1.5"/>
    <text x="332" y="60" font-family="JetBrains Mono" font-size="9" fill="{C["purple"]}" text-anchor="middle">PART 4</text>
    <text x="332" y="78" font-family="Noto Sans KR" font-size="8" fill="{C["dim"]}" text-anchor="middle">주파수 해석</text>
    <line x1="375" y1="65" x2="385" y2="65" stroke="{C["dim"]}" stroke-width="1.5" marker-end="url(#arrowDim)"/>
    <rect x="390" y="40" width="75" height="50" rx="6" fill="{C["card"]}" stroke="{C["orange"]}" stroke-width="1.5"/>
    <text x="427" y="60" font-family="JetBrains Mono" font-size="9" fill="{C["orange"]}" text-anchor="middle">PART 5</text>
    <text x="427" y="78" font-family="Noto Sans KR" font-size="8" fill="{C["dim"]}" text-anchor="middle">디지털 트윈</text>
    <!-- Bottom label -->
    <text x="240" y="130" font-family="Noto Sans KR" font-size="12" fill="{C["gold_bright"]}" text-anchor="middle">수식 → 시뮬레이션 → 검증 → 예측 → 최적화</text>
    <text x="240" y="155" font-family="JetBrains Mono" font-size="11" fill="{C["gold"]}" text-anchor="middle">🎯 End-to-End Digital Twin Pipeline</text>
  </svg>"""
    return a, None


# ═══════════════════════════════════════════════════
# 메인 디스패처
# ═══════════════════════════════════════════════════
SVG_MAP = {
    2: svg_day02, 3: svg_day03, 4: svg_day04, 5: svg_day05,
    6: svg_day06, 7: svg_day07,
    8: svg_day08, 9: svg_day09, 10: svg_day10, 11: svg_day11,
    12: svg_day12, 13: svg_day13, 14: svg_day14,
    15: svg_day15, 16: svg_day16, 17: svg_day17, 18: svg_day18,
    19: svg_day19, 20: svg_day20, 21: svg_day21,
    22: svg_day22, 23: svg_day23, 24: svg_day24, 25: svg_day25,
    26: svg_day26, 27: svg_day27, 28: svg_day28,
    29: svg_day29, 30: svg_day30, 31: svg_day31, 32: svg_day32,
    33: svg_day33,
}

def get_svgs(day_num):
    """Day 번호에 해당하는 (diagram_a, diagram_b) 반환. 없으면 (None, None)"""
    fn = SVG_MAP.get(day_num)
    if fn:
        return fn()
    return None, None
