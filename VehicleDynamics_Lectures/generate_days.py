#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════
YS 진동학 마스터 — Day HTML 자동 생성 파이프라인
═══════════════════════════════════════════════════════
사용법:
  python3 generate_days.py          → Day 02 ~ Day 33 스켈레톤 생성
  python3 generate_days.py --day 2  → Day 02만 생성
  python3 generate_days.py --range 2 5  → Day 02~05 생성
  python3 generate_days.py --full 2 → Day 02 상세 콘텐츠 생성 (curriculum_data에 상세 데이터 필요)

Day 01은 이미 수동으로 완성되어 있으므로 건너뜁니다.
상세 콘텐츠가 curriculum_data에 정의된 Day는 풀버전 생성,
없으면 스켈레톤(구조 + 빈 콘텐츠 슬롯) 생성.
═══════════════════════════════════════════════════════
"""

import os
import sys
import html as html_module
from curriculum_data import CURRICULUM, TOTAL_DAYS
from svg_diagrams import get_svgs

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ─── CSS (Day01과 동일) ───
CSS = """
:root{--bg:#0A0C10;--surface:#12151C;--surface2:#1A1E28;--border:#252A38;--gold:#C9A84C;--gold-light:#E8C96A;--blue:#4A9EBF;--green:#4ABF8A;--purple:#8A6ABF;--orange:#BF6A4A;--text:#D8D3C8;--text-dim:#7A7A8A;--text-bright:#F0EBE0}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:'Noto Sans KR',sans-serif;font-weight:300;line-height:1.8;-webkit-font-smoothing:antialiased}
::-webkit-scrollbar{width:6px}::-webkit-scrollbar-track{background:var(--bg)}::-webkit-scrollbar-thumb{background:var(--gold);border-radius:3px}
.sticky-header{position:sticky;top:0;z-index:100;background:rgba(10,12,16,0.92);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);padding:10px 0}
.header-inner{max-width:960px;margin:0 auto;padding:0 24px;display:flex;justify-content:space-between;align-items:center}
.header-brand{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:16px;color:var(--gold)}
.header-progress-wrap{display:flex;align-items:center;gap:10px;font-size:12px;color:var(--text-dim)}
.header-progress-bar{width:120px;height:4px;background:var(--surface2);border-radius:2px;overflow:hidden}
.header-progress-fill{height:100%;background:linear-gradient(90deg,var(--gold),var(--gold-light));border-radius:2px}
.container{max-width:960px;margin:0 auto;padding:0 24px 80px}
.series-info{text-align:center;padding:16px 0 0;font-size:13px;color:var(--text-dim);letter-spacing:.5px}
.hero{text-align:center;padding:60px 0 48px;animation:fadeUp .8s ease both}
.hero-day{font-family:'JetBrains Mono',monospace;font-size:14px;color:var(--gold);letter-spacing:3px;text-transform:uppercase;margin-bottom:12px}
.hero-title{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:42px;color:var(--text-bright);line-height:1.2;margin-bottom:6px}
.hero-title-en{font-family:'Cormorant Garamond',serif;font-weight:300;font-size:20px;color:var(--text-dim);margin-bottom:32px}
.hero-equation{display:inline-block;background:#0D1017;border:1px solid var(--border);border-radius:12px;padding:20px 40px;margin-bottom:32px}
.hero-equation code{font-family:'JetBrains Mono',monospace;font-size:28px;font-weight:500;color:var(--gold-light);letter-spacing:1px}
.gauge-wrap{display:flex;justify-content:center;margin-bottom:28px}
.gauge-svg{width:100px;height:100px}
.gauge-bg{fill:none;stroke:var(--surface2);stroke-width:6}
.gauge-fill{fill:none;stroke:var(--gold);stroke-width:6;stroke-linecap:round;stroke-dasharray:251;transition:stroke-dashoffset 1s ease}
.gauge-text{font-family:'JetBrains Mono',monospace;font-size:16px;fill:var(--gold-light);text-anchor:middle}
.gauge-label{font-size:9px;fill:var(--text-dim);text-anchor:middle}
.meta-badges{display:flex;flex-wrap:wrap;justify-content:center;gap:12px}
.meta-badge{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:8px 16px;font-size:13px;color:var(--text-dim)}
.meta-badge span{color:var(--text-bright);font-weight:400}
.section{margin-top:56px;animation:fadeUp .6s ease both}
.section-label{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--gold);letter-spacing:2px;text-transform:uppercase;margin-bottom:8px}
.section-title{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:28px;color:var(--text-bright);margin-bottom:20px}
.brain-box{background:linear-gradient(135deg,rgba(138,106,191,.1),rgba(138,106,191,.04));border:1px solid rgba(138,106,191,.3);border-radius:16px;padding:28px 32px}
.brain-box h3{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:20px;color:var(--purple);margin-bottom:16px}
.brain-box p,.brain-box li{font-size:14px;color:var(--text);margin-bottom:8px}
.brain-box ul{padding-left:20px}
.brain-box li::marker{color:var(--purple)}
.time-split{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:16px}
.time-block{background:rgba(138,106,191,.08);border:1px solid rgba(138,106,191,.2);border-radius:8px;padding:10px;text-align:center;font-size:12px}
.time-block .t-range{color:var(--purple);font-weight:700;font-size:13px;display:block;margin-bottom:2px}
.time-block .t-desc{color:var(--text-dim)}
.intuition-card{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:28px 32px}
.intuition-card p{font-size:15px;margin-bottom:12px}
.highlight{color:var(--gold-light);font-weight:400}
.deriv-card{background:var(--surface);border-left:3px solid var(--gold);border-radius:0 12px 12px 0;padding:24px 28px;margin-bottom:20px}
.deriv-step-num{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--gold);letter-spacing:2px;text-transform:uppercase;margin-bottom:12px}
.deriv-equation{background:#0D1017;border-radius:8px;padding:16px 20px;margin-bottom:16px;overflow-x:auto}
.deriv-equation code{font-family:'JetBrains Mono',monospace;font-size:20px;font-weight:500;color:var(--gold-light);white-space:nowrap}
.deriv-explain{font-size:14px;color:var(--text)}
.deriv-explain .label{color:var(--blue);font-weight:400}
.deriv-explain p{margin-bottom:8px}
.arrow-connector{text-align:center;color:var(--gold);font-size:24px;margin:-8px 0 12px;opacity:.5}
.checkpoint{background:rgba(74,191,138,.08);border:1px solid rgba(74,191,138,.25);border-radius:10px;padding:14px 20px;margin:24px 0;font-size:14px;color:var(--green)}
.param-table-wrap{overflow-x:auto;border-radius:12px;border:1px solid var(--border)}
table.param-table{width:100%;border-collapse:collapse;font-size:13px}
table.param-table th{background:var(--surface2);color:var(--gold);font-family:'JetBrains Mono',monospace;font-weight:500;padding:12px 14px;text-align:left;border-bottom:1px solid var(--border);font-size:11px;letter-spacing:1px;text-transform:uppercase}
table.param-table td{padding:12px 14px;border-bottom:1px solid var(--border);vertical-align:top}
table.param-table tr:last-child td{border-bottom:none}
.sym{font-family:'JetBrains Mono',monospace;color:var(--gold-light);font-size:15px}
.simpack-module{background:var(--surface);border:1px solid rgba(74,158,191,.3);border-radius:16px;overflow:hidden}
.simpack-header{background:linear-gradient(135deg,rgba(74,158,191,.15),rgba(74,158,191,.05));padding:16px 28px;border-bottom:1px solid rgba(74,158,191,.2);display:flex;align-items:center;gap:10px}
.simpack-badge{background:var(--blue);color:#fff;font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:500;padding:3px 10px;border-radius:4px;letter-spacing:1px}
.simpack-header span{color:var(--blue);font-weight:400;font-size:15px}
.simpack-body{padding:24px 28px}
.simpack-row{background:var(--surface2);border-radius:10px;padding:16px 20px;margin-bottom:12px}
.simpack-row .sp-sym{font-family:'JetBrains Mono',monospace;color:var(--gold-light);font-size:16px;font-weight:500}
.simpack-row .sp-path{font-family:'JetBrains Mono',monospace;color:var(--blue);font-size:12px;margin:6px 0}
.simpack-row .sp-detail{font-size:13px;color:var(--text-dim)}
.sp-warn{background:rgba(191,106,74,.1);border:1px solid rgba(191,106,74,.3);border-radius:8px;padding:10px 14px;margin-top:8px;font-size:12px;color:var(--orange)}
.accordion{border:1px solid var(--border);border-radius:12px;overflow:hidden}
.accordion-toggle{width:100%;background:var(--surface);border:none;padding:18px 24px;cursor:pointer;display:flex;justify-content:space-between;align-items:center;color:var(--text-bright);font-family:'Noto Sans KR',sans-serif;font-size:15px;font-weight:400}
.accordion-toggle:hover{background:var(--surface2)}
.accordion-arrow{color:var(--gold);font-size:18px;transition:transform .3s}
.accordion-content{max-height:0;overflow:hidden;transition:max-height .4s ease;background:var(--surface)}
.accordion-content.open{max-height:2000px}
.accordion-inner{padding:0 24px 24px}
.accordion-inner p{font-size:14px;margin-bottom:10px}
.accordion-inner .deriv-equation{margin-top:12px}
.quiz-card{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:24px 28px;margin-bottom:16px}
.quiz-num{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--gold);letter-spacing:2px;margin-bottom:10px}
.quiz-q{font-size:15px;color:var(--text-bright);margin-bottom:16px;font-weight:400}
.quiz-options{display:grid;gap:8px}
.quiz-opt{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:12px 16px;cursor:pointer;font-size:14px;color:var(--text);transition:all .2s}
.quiz-opt:hover{border-color:var(--gold);color:var(--text-bright)}
.quiz-opt.correct{background:rgba(74,191,138,.12);border-color:var(--green);color:var(--green)}
.quiz-opt.wrong{background:rgba(191,74,74,.12);border-color:#bf4a4a;color:#bf4a4a}
.quiz-opt.disabled{pointer-events:none;opacity:.7}
.quiz-feedback{margin-top:10px;padding:10px 14px;border-radius:8px;font-size:13px;display:none}
.quiz-feedback.show{display:block}
.quiz-feedback.correct-fb{background:rgba(74,191,138,.08);color:var(--green)}
.quiz-feedback.wrong-fb{background:rgba(191,74,74,.08);color:#bf4a4a}
.sr-track{display:flex;gap:12px;flex-wrap:wrap;margin:16px 0}
.sr-dot{width:52px;height:52px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:10px;font-family:'JetBrains Mono',monospace}
.sr-dot.today{background:var(--gold);color:var(--bg);font-weight:700}
.sr-dot.future{background:var(--surface2);border:1px solid var(--border);color:var(--text-dim)}
.sr-dot .sr-label{font-size:8px}
.next-preview{background:linear-gradient(135deg,rgba(201,168,76,.08),rgba(201,168,76,.02));border:1px solid rgba(201,168,76,.2);border-radius:12px;padding:20px 24px;margin-top:24px}
.next-preview h4{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:18px;color:var(--gold);margin-bottom:8px}
.next-preview p{font-size:14px;color:var(--text-dim)}
.footer{text-align:center;padding:40px 0 20px;font-size:12px;color:var(--text-dim);border-top:1px solid var(--border);margin-top:60px}
.placeholder-box{background:var(--surface);border:2px dashed var(--border);border-radius:16px;padding:40px;text-align:center;color:var(--text-dim);font-size:14px;margin:20px 0}
.placeholder-box .ph-icon{font-size:36px;margin-bottom:12px;display:block}
.nav-links{display:flex;justify-content:space-between;margin-top:40px;font-size:14px}
.nav-links a{color:var(--gold);text-decoration:none;padding:8px 16px;border:1px solid var(--border);border-radius:8px;transition:all .2s}
.nav-links a:hover{border-color:var(--gold);background:rgba(201,168,76,.06)}
.diagram-wrap{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px;margin:20px 0;text-align:center;overflow-x:auto}
.diagram-wrap svg{max-width:100%;height:auto}
.diagram-label{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--gold);letter-spacing:2px;text-transform:uppercase;margin-bottom:12px;text-align:center}
@keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}
@media(max-width:640px){.hero-title{font-size:28px}.hero-equation code{font-size:18px}.container{padding:0 16px 60px}.time-split{grid-template-columns:repeat(2,1fr)}.deriv-equation code{font-size:16px}}
"""

def esc(text):
    """HTML escape"""
    return html_module.escape(str(text))


def get_day_data(day_num):
    """커리큘럼 데이터에서 해당 Day 정보 가져오기"""
    for d in CURRICULUM:
        if d["day"] == day_num:
            return d
    return None


def has_full_content(data):
    """상세 콘텐츠가 정의되어 있는지 확인"""
    return "deriv_steps" in data and len(data.get("deriv_steps", [])) > 0


def build_deriv_section(data):
    """수식 유도 카드 HTML 생성"""
    if not has_full_content(data):
        return '<div class="placeholder-box"><span class="ph-icon">📐</span>수식 유도 콘텐츠가 여기에 들어갑니다.<br>generate_days.py --full {day} 또는 Claude에게 상세 생성 요청</div>'.format(day=data["day"])

    cards = []
    for i, step in enumerate(data["deriv_steps"]):
        card = f"""
    <div class="deriv-card">
      <div class="deriv-step-num">{esc(step.get('label', step.get('step_title', f'Step {i+1}')))}</div>
      <div class="deriv-equation"><code>{esc(step['equation'])}</code></div>
      <div class="deriv-explain">
        <p><span class="label">이 항의 의미:</span> {esc(step['explain_meaning'])}</p>
        <p><span class="label">부호/변환 이유:</span> {esc(step['explain_sign'])}</p>
        <p><span class="label">이전 단계와의 연결:</span> {esc(step['explain_prev'])}</p>
      </div>
    </div>"""
        cards.append(card)
        if i < len(data["deriv_steps"]) - 1:
            cards.append('    <div class="arrow-connector">↓</div>')
    return "\n".join(cards)


def build_param_table(data):
    """파라미터 테이블 HTML 생성"""
    if "params" not in data:
        return '<div class="placeholder-box"><span class="ph-icon">📋</span>파라미터 해부 테이블이 여기에 들어갑니다.</div>'

    rows = []
    for p in data["params"]:
        rows.append(f"""
        <tr>
          <td><span class="sym">{esc(p['sym'])}</span></td>
          <td>{esc(p['name_ko'])} / {esc(p['name_en'])}</td>
          <td>{esc(p['unit'])}</td>
          <td>{esc(p['meaning'])}</td>
          <td>{esc(p['vehicle'])}</td>
          <td>{esc(p['range'])}</td>
        </tr>""")

    return f"""
    <div class="param-table-wrap">
      <table class="param-table">
        <thead><tr>
          <th>기호</th><th>명칭 (한/영)</th><th>단위</th><th>물리적 의미</th><th>차량 부품</th><th>전형적 범위</th>
        </tr></thead>
        <tbody>{"".join(rows)}
        </tbody>
      </table>
    </div>"""


def build_simpack_section(data):
    """Simpack 매핑 섹션 HTML 생성"""
    if "simpack_mappings" not in data:
        return '<div class="placeholder-box"><span class="ph-icon">🔧</span>Simpack 매핑 모듈이 여기에 들어갑니다.</div>'

    rows = []
    for sm in data["simpack_mappings"]:
        rows.append(f"""
      <div class="simpack-row">
        <div class="sp-sym">{esc(sm['sym'])}</div>
        <div class="sp-path">{esc(sm['path'])}</div>
        <div class="sp-detail"><strong>필드:</strong> {esc(sm['field'])}<br><strong>단위:</strong> {esc(sm['unit'])}</div>
        <div class="sp-warn">⚠ {esc(sm['warn'])}</div>
      </div>""")

    return f"""
    <div class="simpack-module">
      <div class="simpack-header">
        <span class="simpack-badge">SIMPACK</span>
        <span>Day {data['day']} 파라미터 입력 가이드</span>
      </div>
      <div class="simpack-body">{"".join(rows)}
      </div>
    </div>"""


def build_quiz_section(data):
    """퀴즈 섹션 HTML 생성 — 두 가지 형식 지원
    형식 A (구): question/options/correct/feedback_correct/feedback_wrong
    형식 B (신): q/a (서술형 — 정답 표시/숨기기 토글)
    """
    if "quiz" not in data:
        return '<div class="placeholder-box"><span class="ph-icon">❓</span>퀴즈 3문제가 여기에 들어갑니다.</div>'

    cards = []
    type_labels = {"fill": "수식 빈칸 채우기", "meaning": "물리적 의미 연결", "simpack": "Simpack 적용"}
    for i, q in enumerate(data["quiz"]):
        qid = f"q{i+1}"

        if "options" in q:
            # 형식 A: 객관식
            opts = []
            for j, opt in enumerate(q["options"]):
                is_correct = "true" if j == q["correct"] else "false"
                opts.append(f'      <div class="quiz-opt" onclick="checkAnswer(\'{qid}\',this,{is_correct})">{esc(opt)}</div>')

            cards.append(f"""
    <div class="quiz-card">
      <div class="quiz-num">QUESTION {i+1:02d} — {type_labels.get(q['type'], q['type'])}</div>
      <p class="quiz-q">{esc(q['question'])}</p>
      <div class="quiz-options" id="{qid}">
{chr(10).join(opts)}
      </div>
      <div class="quiz-feedback" id="{qid}-fb"></div>
    </div>""")
        else:
            # 형식 B: 서술형 (q/a)
            answer_escaped = esc(q['a']).replace("'", "\\'")
            cards.append(f"""
    <div class="quiz-card">
      <div class="quiz-num">QUESTION {i+1:02d} — {type_labels.get(q['type'], q['type'])}</div>
      <p class="quiz-q">{esc(q['q'])}</p>
      <div style="margin-top:12px">
        <button class="quiz-opt" style="background:var(--gold);color:var(--bg);border-color:var(--gold);font-weight:700;text-align:center" onclick="toggleAnswer('{qid}')">정답 확인</button>
      </div>
      <div class="quiz-feedback correct-fb" id="{qid}-fb" style="display:none;margin-top:10px">
        ✅ {esc(q['a'])}
      </div>
    </div>""")
    return "\n".join(cards)


def build_deep_dive(data):
    """Deep Dive 아코디언 HTML 생성"""
    title = data.get("deep_dive_title", f"Day {data['day']} 심화 주제")
    content = data.get("deep_dive_content", "상세 콘텐츠가 여기에 추가됩니다.")

    paragraphs = content.split("\n\n")
    content_html = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        content_html.append(f"        <p>{esc(p)}</p>")

    return f"""
    <div class="accordion">
      <button class="accordion-toggle" onclick="toggleAccordion(this)">
        <span>💡 {esc(title)} — 클릭하여 펼치기</span>
        <span class="accordion-arrow">▼</span>
      </button>
      <div class="accordion-content">
        <div class="accordion-inner">
{chr(10).join(content_html)}
        </div>
      </div>
    </div>"""


def generate_day_html(day_num):
    """단일 Day HTML 파일 생성"""
    data = get_day_data(day_num)
    if not data:
        print(f"  ⚠ Day {day_num} 데이터 없음, 건너뜀")
        return None

    pct = round(day_num / TOTAL_DAYS * 100)
    gauge_offset = 251 - (251 * pct / 100)
    progress_width = f"{pct}%"

    # Prev/Next navigation
    prev_data = get_day_data(day_num - 1) if day_num > 1 else None
    next_data = get_day_data(day_num + 1) if day_num < TOTAL_DAYS else None
    prev_link = f'<a href="{prev_data["filename"]}">← Day {day_num-1}: {prev_data["title_ko"]}</a>' if prev_data else '<span></span>'
    next_link = f'<a href="{next_data["filename"]}">Day {day_num+1}: {next_data["title_ko"]} →</a>' if next_data else '<span></span>'

    # Next preview
    next_preview_html = ""
    if next_data:
        np_title = data.get("next_preview_title", f"Day {day_num+1} 미리보기")
        np_body = data.get("next_preview", f"<strong>{next_data['title_ko']}</strong> ({next_data['title_en']})")
        next_preview_html = f"""
    <div class="next-preview">
      <h4>→ {esc(np_title)}</h4>
      <p>{np_body}</p>
    </div>"""

    # Brain strategy — dict 형식(pre_routine/technique) 또는 문자열 형식 모두 지원
    brain_content = ""
    if "brain_strategy" in data:
        bs = data["brain_strategy"]
        if isinstance(bs, dict):
            brain_content = f"""
        <p><strong style="color:var(--purple);">수식 보기 전 30초 루틴</strong> — {esc(bs['pre_routine'])}</p>
        <p><strong style="color:var(--purple);">오늘의 학습 기법:</strong> {esc(bs['technique'])}</p>"""
        else:
            brain_content = f"""
        <p><strong style="color:var(--purple);">오늘의 학습 전략</strong> — {esc(str(bs))}</p>"""
    else:
        brain_content = f"""
        <p><strong style="color:var(--purple);">수식 보기 전 30초 루틴</strong> — 눈을 감고, 오늘 다룰 물리 현상을 차량 위에서 실제로 느끼는 장면을 상상하세요.</p>"""

    # Intuition — 'intuition' 키 또는 'intuition_text' 키 모두 지원
    intuition_html = ""
    intuition_raw = data.get("intuition", data.get("intuition_text", ""))
    if intuition_raw:
        intuition_html = f'<p>{esc(str(intuition_raw))}</p>'
    else:
        intuition_html = '<div class="placeholder-box"><span class="ph-icon">🚗</span>물리적 직관 설명이 여기에 들어갑니다.<br>엔지니어 언어로 "왜 이 수식이 필요한가"를 서술합니다.</div>'

    # SVG 다이어그램 가져오기
    svg_a, svg_b = get_svgs(day_num)
    diagram_a_html = ""
    if svg_a:
        diagram_a_html = f"""
  <div class="diagram-wrap">
    <div class="diagram-label">Diagram A — 물리계 도해</div>
    {svg_a}
  </div>"""

    diagram_b_html = ""
    if svg_b:
        diagram_b_html = f"""
  <div class="diagram-wrap">
    <div class="diagram-label">Diagram B — 응답 곡선</div>
    {svg_b}
  </div>"""
    else:
        diagram_b_html = f"""<div class="placeholder-box">
    <span class="ph-icon">📈</span>
    Day {day_num:02d} 전용 SVG 다이어그램이 여기에 들어갑니다.<br>
    시간축/주파수축 응답 곡선, 위상 플롯, 또는 Bode 선도 등
  </div>"""

    # Quiz feedback JS data
    quiz_fb_js = ""
    if "quiz" in data:
        for i, q in enumerate(data["quiz"]):
            if "options" not in q:
                continue  # 서술형 퀴즈는 toggleAnswer로 처리
            qid = f"q{i+1}"
            fc = esc(q.get("feedback_correct", "정답!")).replace("'", "\\'")
            fw = esc(q.get("feedback_wrong", "다시 생각해보세요.")).replace("'", "\\'")
            quiz_fb_js += f"""
    if(qId==='{qid}'){{
      if(isCorrect) fb.textContent='{fc}';
      else fb.textContent='{fw}';
    }}"""

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Day {day_num:02d} — {esc(data['title_ko'])} | YS 진동학 마스터</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;600;700&family=Noto+Sans+KR:wght@300;400;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<!-- ① STICKY HEADER -->
<header class="sticky-header">
  <div class="header-inner">
    <div class="header-brand"><a href="index.html" style="color:inherit;text-decoration:none;">YS · 진동학 마스터</a> / Day {day_num:02d}</div>
    <div class="header-progress-wrap">
      <span>{day_num} / {TOTAL_DAYS}</span>
      <div class="header-progress-bar"><div class="header-progress-fill" style="width:{progress_width}"></div></div>
      <span>{pct}%</span>
    </div>
  </div>
</header>

<div class="container">

<div class="series-info">이 시리즈 예상 총 Day: {TOTAL_DAYS}일 &nbsp;|&nbsp; PART {data['part']} — {esc(data['part_title'])}</div>

<!-- ② HERO -->
<section class="hero">
  <div class="hero-day">— DAY {day_num:02d} —</div>
  <h1 class="hero-title">{esc(data['title_ko'])}</h1>
  <p class="hero-title-en">{esc(data['title_en'])}</p>
  <div class="hero-equation"><code>{esc(data['hero_eq'])}</code></div>
  <div class="gauge-wrap">
    <svg class="gauge-svg" viewBox="0 0 100 100">
      <circle class="gauge-bg" cx="50" cy="50" r="40"/>
      <circle class="gauge-fill" cx="50" cy="50" r="40" transform="rotate(-90 50 50)" style="stroke-dashoffset:{gauge_offset:.0f}"/>
      <text class="gauge-text" x="50" y="48">{pct}%</text>
      <text class="gauge-label" x="50" y="62">DAY {day_num}/{TOTAL_DAYS}</text>
    </svg>
  </div>
  <div class="meta-badges">
    <div class="meta-badge">⏱ 포모도로 <span>25분</span></div>
    <div class="meta-badge">📐 수식 <span>{esc(data.get('num_formulas', f"{len(data.get('deriv_steps',[]))}단계"))}</span></div>
    <div class="meta-badge">⭐ 난이도 <span>{esc(data['difficulty'])}</span></div>
    <div class="meta-badge">🔁 복습 <span>D+1, D+3, D+7</span></div>
  </div>
</section>

<!-- ③ 뇌과학 학습 전략 -->
<section class="section">
  <div class="section-label">Learning Strategy</div>
  <div class="brain-box">
    <h3>🧠 뇌과학 기반 수식 학습 전략</h3>
    {brain_content}
    <div class="time-split">
      <div class="time-block"><span class="t-range">0~5분</span><span class="t-desc">물리적 직관</span></div>
      <div class="time-block"><span class="t-range">5~18분</span><span class="t-desc">수식 유도</span></div>
      <div class="time-block"><span class="t-range">18~23분</span><span class="t-desc">Simpack 매핑</span></div>
      <div class="time-block"><span class="t-range">23~25분</span><span class="t-desc">퀴즈 복습</span></div>
    </div>
  </div>
</section>

<!-- ④ 물리적 직관 -->
<section class="section">
  <div class="section-label">Step 1 — Physical Intuition</div>
  <h2 class="section-title">왜 이 수식이 필요한가?</h2>
  <div class="intuition-card">
    {intuition_html}
  </div>
  {diagram_a_html}
</section>

<!-- ⑤ 수식 단계별 풀이 -->
<section class="section">
  <div class="section-label">Step 2 — Derivation</div>
  <h2 class="section-title">수식 한 줄씩 유도</h2>
  {build_deriv_section(data)}
</section>

<!-- ⑥ 파라미터 테이블 -->
<section class="section">
  <div class="section-label">Step 3 — Parameter Mapping</div>
  <h2 class="section-title">수식 파라미터 완전 해부</h2>
  {build_param_table(data)}
</section>

<!-- ⑦ SVG 다이어그램 B -->
<section class="section">
  <div class="section-label">Response Visualization</div>
  <h2 class="section-title">응답 곡선 / 주요 그래프</h2>
  {diagram_b_html}
</section>

<!-- ⑧ Simpack 매핑 -->
<section class="section">
  <div class="section-label">Step 4 — Simpack Mapping</div>
  <h2 class="section-title">Simpack 입력 매핑</h2>
  {build_simpack_section(data)}
</section>

<!-- ⑨ Deep Dive -->
<section class="section">
  <div class="section-label">Deep Dive</div>
  <h2 class="section-title">심화 학습</h2>
  {build_deep_dive(data)}
</section>

<!-- ⑩ 퀴즈 -->
<section class="section">
  <div class="section-label">Quiz</div>
  <h2 class="section-title">즉시 복습 퀴즈</h2>
  {build_quiz_section(data)}
</section>

<!-- ⑪ 간격 반복 + 내일 예고 -->
<section class="section">
  <div class="section-label">Spaced Repetition</div>
  <h2 class="section-title">간격 반복 스케줄</h2>
  <div class="sr-track">
    <div class="sr-dot today"><span>D+0</span><span class="sr-label">오늘</span></div>
    <div class="sr-dot future"><span>D+1</span><span class="sr-label">내일</span></div>
    <div class="sr-dot future"><span>D+3</span><span class="sr-label">3일후</span></div>
    <div class="sr-dot future"><span>D+7</span><span class="sr-label">7일후</span></div>
    <div class="sr-dot future"><span>D+14</span><span class="sr-label">14일후</span></div>
  </div>
  {next_preview_html}
</section>

<!-- Navigation -->
<div class="nav-links">
  {prev_link}
  <a href="index.html">📋 목차</a>
  {next_link}
</div>

<div class="footer">
  YS · Vehicle Dynamics Study Series — Day {day_num:02d} of {TOTAL_DAYS}<br>
  Designed for 25-min Pomodoro sessions · Renault Korea Suspension Engineer
</div>

</div>

<script>
function toggleAccordion(btn){{
  const c=btn.nextElementSibling;const a=btn.querySelector('.accordion-arrow');
  c.classList.toggle('open');a.style.transform=c.classList.contains('open')?'rotate(180deg)':'rotate(0deg)';
}}
function toggleAnswer(qId){{
  const fb=document.getElementById(qId+'-fb');
  if(fb.style.display==='none'){{fb.style.display='block';}}else{{fb.style.display='none';}}
}}
function checkAnswer(qId,el,isCorrect){{
  const opts=document.querySelectorAll('#'+qId+' .quiz-opt');
  const fb=document.getElementById(qId+'-fb');
  opts.forEach(o=>{{
    o.classList.add('disabled');
    if(o===el) o.classList.add(isCorrect?'correct':'wrong');
    if(!isCorrect&&o.getAttribute('onclick')&&o.getAttribute('onclick').includes('true')) o.classList.add('correct');
  }});
  fb.classList.add('show');
  fb.classList.add(isCorrect?'correct-fb':'wrong-fb');
  {quiz_fb_js}
}}
const obs=new IntersectionObserver(e=>{{e.forEach(x=>{{if(x.isIntersecting){{x.target.style.opacity='1';x.target.style.transform='translateY(0)'}}}});}},{{threshold:.1}});
document.querySelectorAll('.section').forEach(s=>{{s.style.opacity='0';s.style.transform='translateY(24px)';s.style.transition='opacity .6s ease, transform .6s ease';obs.observe(s);}});
</script>
</body>
</html>"""
    return html


def main():
    args = sys.argv[1:]

    if "--day" in args:
        idx = args.index("--day")
        day_num = int(args[idx + 1])
        days_to_gen = [day_num]
    elif "--range" in args:
        idx = args.index("--range")
        start = int(args[idx + 1])
        end = int(args[idx + 2])
        days_to_gen = list(range(start, end + 1))
    else:
        # Default: generate all except Day 01 (already done manually)
        days_to_gen = list(range(2, TOTAL_DAYS + 1))

    print(f"═══ YS 진동학 마스터 — HTML 생성기 ═══")
    print(f"생성 대상: Day {days_to_gen[0]:02d} ~ Day {days_to_gen[-1]:02d} ({len(days_to_gen)}개)")
    print(f"출력 디렉토리: {OUTPUT_DIR}")
    print()

    generated = 0
    full = 0
    skeleton = 0

    for day_num in days_to_gen:
        data = get_day_data(day_num)
        if not data:
            print(f"  ⚠ Day {day_num:02d}: 데이터 없음, 건너뜀")
            continue

        html = generate_day_html(day_num)
        if html is None:
            continue

        filepath = os.path.join(OUTPUT_DIR, data["filename"])

        # Day 01은 이미 수동 완성 — 덮어쓰지 않음
        if day_num == 1 and os.path.exists(filepath):
            print(f"  ⏭ Day 01: 이미 존재 (수동 완성본 유지)")
            continue

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)

        is_full = has_full_content(data)
        tag = "FULL" if is_full else "SKELETON"
        print(f"  ✅ Day {day_num:02d}: {data['title_ko']} [{tag}] → {data['filename']}")
        generated += 1
        if is_full:
            full += 1
        else:
            skeleton += 1

    print()
    print(f"═══ 완료: {generated}개 생성 (FULL: {full}, SKELETON: {skeleton}) ═══")
    print(f"상세 콘텐츠 추가: curriculum_data.py에 deriv_steps, params, quiz 등을 추가한 후 재실행")
    print(f"또는 Claude에게 'Day N 상세 생성해줘'라고 요청하면 됩니다.")


if __name__ == "__main__":
    main()
