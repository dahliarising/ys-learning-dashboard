# HTML Patterns Audit Report
## Vehicle Dynamics Lectures - Pattern Analysis

**Generated**: 2026-03-13
**Files Analyzed**:
- Day01_운동방정식유도.html
- Day15_Part2복습.html
- Day30_QuarterCar구현.html

---

## 1. ACCORDION / EXPANDABLE SECTIONS

### HTML Structure Pattern

#### Full Accordion Container
```html
<div class="accordion">
  <button class="accordion-toggle">
    <span>💡 왜 자중(mg)이 운동방정식에 없는가?</span>
    <span class="accordion-arrow">▼</span>
  </button>
  <div class="accordion-content" id="deepdive1">
    <div class="accordion-inner">
      <h4 style="color:var(--gold-light);margin-bottom:12px;">정적평형점 기준 좌표계의 핵심</h4>
      <p>운동방정식 mẍ + cẋ + kx = F(t)를 보면, 중력 mg 항이 없습니다...</p>
    </div>
  </div>
</div>
```

### CSS Patterns for Accordion

```css
.accordion {
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
}

.accordion-toggle {
  width: 100%;
  background: var(--surface);
  border: none;
  padding: 18px 24px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: var(--text-bright);
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 15px;
  font-weight: 400;
}

.accordion-toggle:hover {
  background: var(--surface2);
}

.accordion-arrow {
  color: var(--gold);
  font-size: 18px;
  transition: transform 0.3s;
}

.accordion-content {
  display: none;
  background: var(--surface);
  padding: 0;
}

.accordion-content.open {
  display: block;
  padding: 0;
}

.accordion-inner {
  padding: 0 24px 24px;
}

.accordion-inner p {
  font-size: 14px;
  margin-bottom: 10px;
}

.accordion-inner .deriv-equation {
  margin-top: 12px;
}
```

### JavaScript Event Handler

```javascript
document.addEventListener('click', function(e) {
  var hdr = e.target.closest('.accordion-header, .accordion-toggle');
  if (hdr) {
    var content = hdr.nextElementSibling;
    if (content) {
      content.classList.toggle('open');
      var nowOpen = content.classList.contains('open');
      var arrow = hdr.querySelector('.accordion-arrow, span:last-child');
      if (arrow) {
        if (arrow.textContent === '+' || arrow.textContent === '−') {
          arrow.textContent = nowOpen ? '−' : '+';
        } else {
          arrow.style.transform = nowOpen ? 'rotate(180deg)' : 'rotate(0deg)';
        }
      }
    }
  }
});
```

### Key Features
- **Container**: `.accordion` with border and rounded corners
- **Toggle Button**: `.accordion-toggle` with flex layout
- **Arrow Indicator**: `.accordion-arrow` with rotation transition
- **Content**: `.accordion-content` with `open` class toggle
- **Inner Wrapper**: `.accordion-inner` provides padding for content
- **Default State**: `display: none` (collapsed)
- **Expanded State**: `display: block` with `.open` class

---

## 2. CANVAS/SIMULATION SECTIONS

### HTML Structure Pattern

```html
<!-- INTERACTIVE SIMULATION -->
<div class="section-card" style="margin-top:32px">
  <div class="section-label">INTERACTIVE SIMULATION</div>
  <h2 class="section-title">🎮 1-DOF 자유진동 시뮬레이터</h2>
  <div class="sim-container">
    <div class="sim-canvas-wrap">
      <canvas id="sim-day01" width="700" height="350"></canvas>
    </div>
    <div id="sim-day01-controls" class="sim-controls"></div>
    <div id="sim-day01-metrics" class="sim-metrics"></div>
  </div>
  <script>
  (function(){
    // Canvas setup and simulation code
  })();
  </script>
</div>
```

### CSS Patterns for Canvas/Simulation

```css
/* Simulation Container */
.sim-container {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 24px;
  margin: 24px 0;
  overflow: hidden;
}

.sim-title {
  font-family: 'Cormorant Garamond', serif;
  font-weight: 600;
  font-size: 20px;
  color: var(--text-bright);
  margin-bottom: 16px;
}

/* Canvas Wrapper */
.sim-canvas-wrap {
  background: #0A0C10;
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 8px;
  margin-bottom: 16px;
  text-align: center;
}

.sim-canvas-wrap canvas {
  max-width: 100%;
  border-radius: 8px;
}

/* Controls Section */
.sim-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 16px;
}

/* Slider Groups */
.sim-slider-group {
  flex: 1;
  min-width: 200px;
  background: var(--surface2);
  border-radius: 10px;
  padding: 12px 16px;
}

.sim-slider-group label {
  display: block;
  font-size: 12px;
  color: var(--text-dim);
  margin-bottom: 6px;
  font-family: 'JetBrains Mono', monospace;
}

.sim-slider-group input[type=range] {
  width: 100%;
  accent-color: var(--gold);
  margin: 4px 0;
}

.sim-slider-group .sim-value {
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
  color: var(--gold-light);
  text-align: right;
}

/* Metrics Display */
.sim-metrics {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 8px;
}

.sim-metric {
  background: var(--surface2);
  border-radius: 8px;
  padding: 10px 14px;
  text-align: center;
}

.sim-metric .sm-label {
  font-size: 11px;
  color: var(--text-dim);
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 1px;
}

.sim-metric .sm-value {
  font-family: 'JetBrains Mono', monospace;
  font-size: 18px;
  color: var(--gold-light);
  font-weight: 500;
  display: block;
  margin-top: 4px;
}

/* Buttons */
.sim-btn {
  background: var(--gold);
  color: var(--dark);
  border: none;
  border-radius: 8px;
  padding: 10px 16px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 500;
}

.sim-btn:hover {
  opacity: 0.9;
}

.sim-btn-secondary {
  background: var(--surface2);
  color: var(--text);
  border: 1px solid var(--border);
}

.sim-btn-secondary:hover {
  border-color: var(--gold);
  color: var(--gold);
}
```

### JavaScript Canvas Pattern - Minimal Example

```javascript
(function(){
  const canvas = document.getElementById('sim-day01');
  const ctx = canvas.getContext('2d');
  const W = 700, H = 350;
  const ctrlBox = document.getElementById('sim-day01-controls');
  const metricBox = document.getElementById('sim-day01-metrics');

  // Slider creation helper
  function addSlider(label, min, max, value, step, id) {
    const g = document.createElement('div');
    g.className = 'sim-slider-group';
    g.innerHTML = '<label>' + label + '</label><input type="range" min="'+min+'" max="'+max+'" value="'+value+'" step="'+step+'" id="'+id+'"><div class="sim-readout" id="'+id+'-val">'+value+'</div>';
    ctrlBox.appendChild(g);
    const inp = document.getElementById(id);
    inp.oninput = function(){
      document.getElementById(id+'-val').textContent = this.value;
      draw();
    };
    return inp;
  }

  // Button creation helper
  function addBtn(label, fn) {
    const b = document.createElement('button');
    b.className = 'sim-btn';
    b.textContent = label;
    b.onclick = fn;
    ctrlBox.appendChild(b);
  }

  // Metrics display helper
  function setMetrics(arr) {
    metricBox.innerHTML = arr.map(m =>
      '<div class="sim-metric"><strong>'+m[0]+':</strong>&nbsp;'+m[1]+'</div>'
    ).join('');
  }

  // Create sliders
  const sl_m = addSlider('질량 m (kg)', 1, 50, 10, 1, 'sim01-m');
  const sl_k = addSlider('강성 k (N/m)', 100, 5000, 1000, 100, 'sim01-k');
  const sl_z = addSlider('감쇠비 ζ', 0, 2, 0.1, 0.01, 'sim01-z');
  const sl_x0 = addSlider('초기변위 x₀ (m)', 0.01, 0.1, 0.05, 0.005, 'sim01-x0');

  // Main drawing function
  function draw() {
    ctx.fillStyle = '#0a0c10';
    ctx.fillRect(0, 0, W, H);

    const m = +sl_m.value;
    const k = +sl_k.value;
    const z = +sl_z.value;
    const x0 = +sl_x0.value;

    const wn = Math.sqrt(k/m);
    const wd = wn * Math.sqrt(Math.max(0, 1 - z*z));
    const T = 4*Math.PI / (wd || 1);
    const dt = T / 500;

    // Draw oscillation response
    ctx.strokeStyle = '#C9A84C';
    ctx.lineWidth = 2;
    ctx.beginPath();

    const scX = W / T;
    const scY = H * 0.4 / x0;

    for(let i = 0; i < 500; i++) {
      const t = i * dt;
      let x;
      if(z < 1) {
        x = x0 * Math.exp(-z*wn*t) * Math.cos(wd*t);
      } else if(z === 1) {
        x = x0 * (1 + wn*t) * Math.exp(-wn*t);
      } else {
        const s1 = wn*(-z + Math.sqrt(z*z-1));
        const s2 = wn*(-z - Math.sqrt(z*z-1));
        x = x0*(s1*Math.exp(s2*t)-s2*Math.exp(s1*t))/(s1-s2);
      }

      const px = i * W / 500;
      const py = H/2 - x*scY;
      if(i) ctx.lineTo(px, py);
      else ctx.moveTo(px, py);
    }
    ctx.stroke();
  }

  draw();
})();
```

### Key Features
- **Canvas ID Pattern**: `sim-day{N}` where N is day number
- **Wrapper Divs**:
  - `sim-canvas-wrap` - dark background canvas container
  - `sim-day{N}-controls` - dynamically populated slider/button area
  - `sim-day{N}-metrics` - dynamically populated metrics display
- **Dynamic Creation**: Sliders and buttons are created via JavaScript
- **Rendering Loop**: Direct canvas 2D context drawing (no requestAnimationFrame for simple plots)
- **Metrics**: 2-element arrays `[label, value]` rendered to HTML

---

## 3. STYLED BOX SECTIONS (Non-Accordion Content)

### "심화 학습" (Deep Learning) Section Header

```html
<div class="section">
  <div class="section-label">DEEP DIVE</div>
  <h2 class="section-title">심화 학습</h2>
  <!-- Multiple accordion items below -->
</div>
```

### Memory Hook Box Pattern

```html
<div class="memory-hook"
  style="background:linear-gradient(135deg,rgba(138,106,191,.08),rgba(138,106,191,.02));
         border:1px solid rgba(138,106,191,.2);
         border-radius:16px;
         padding:24px;
         margin:20px 0;">
  <h3 style="color:var(--purple);margin-bottom:12px;">🧠 기억 앵커: "MCK 삼총사"</h3>
  <p style="font-size:15px;line-height:1.9;">운동방정식의 세 주인공을 기억하는 이미지:</p>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:16px 0;text-align:center;">
    <div style="background:var(--surface);padding:16px;border-radius:12px;">
      <div style="font-size:32px;margin-bottom:8px;">🦏</div>
      <div style="color:var(--gold-light);font-family:'JetBrains Mono';font-size:18px;font-weight:500;">m (Mass)</div>
      <div style="color:var(--text-dim);font-size:13px;margin-top:4px;">코뿔소처럼 무거워서<br>쉽게 안 움직임 = <strong>관성</strong></div>
    </div>
    <!-- More cards... -->
  </div>
</div>
```

### CSS for Memory Hook

```css
.memory-hook {
  background: linear-gradient(135deg, rgba(201,168,76,.1), rgba(201,168,76,.03));
  border: 1px solid rgba(201,168,76,.2);
  border-radius: 12px;
  padding: 16px 20px;
  margin: 16px 0;
  font-size: 14px;
}

.memory-hook strong {
  color: var(--gold-light);
}
```

### Vehicle Example Box Pattern

```html
<div class="vehicle-example"
  style="background:linear-gradient(135deg,rgba(201,168,76,.04),rgba(74,158,191,.04));
         border:1px solid rgba(201,168,76,.15);
         border-radius:16px;
         padding:24px;
         margin:20px 0;">
  <h4 style="color:var(--gold-light);margin-bottom:16px;">🚗 레퍼런스 C-SUV — 프론트 1/4 차량</h4>

  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:16px;">
    <div style="background:var(--surface);padding:12px;border-radius:10px;text-align:center;">
      <div style="color:var(--text-dim);font-size:12px;">스프렁 매스 (1/4)</div>
      <div style="color:var(--gold-light);font-size:22px;font-family:'JetBrains Mono';font-weight:500;">340 kg</div>
      <div style="color:var(--text-dim);font-size:11px;">공차중량 1,360 kg 기준</div>
    </div>
    <!-- More data cards... -->
  </div>
</div>
```

### CSS for Vehicle Example

```css
.vehicle-example {
  background: linear-gradient(135deg, rgba(74,158,191,.08), rgba(74,158,191,.02));
  border: 1px solid rgba(74,158,191,.25);
  border-radius: 12px;
  padding: 20px 24px;
  margin-top: 20px;
}

.vehicle-example h4 {
  font-family: 'Cormorant Garamond', serif;
  font-weight: 600;
  font-size: 17px;
  color: var(--blue);
  margin-bottom: 12px;
}

.vehicle-example p {
  font-size: 13px;
  margin-bottom: 6px;
}

.vehicle-example .calc {
  font-family: 'JetBrains Mono', monospace;
  color: var(--gold-light);
  font-size: 13px;
  background: #0D1017;
  padding: 6px 12px;
  border-radius: 6px;
  display: inline-block;
  margin: 4px 0;
}
```

### Warning/Info Box Pattern

```css
.sp-warn {
  background: rgba(191,106,74,0.1);
  border: 1px solid rgba(191,106,74,0.3);
  border-radius: 8px;
  padding: 10px 14px;
  margin-top: 8px;
  font-size: 12px;
  color: var(--orange);
}
```

---

## 4. QUIZ SECTIONS

### Quiz Card HTML Pattern

```html
<div class="quiz-card" data-correct="1">
  <div class="quiz-num">QUESTION 01 — 모델 구성</div>
  <p class="quiz-q">Quarter-Car 2DOF 모델의 자유도는 어떤 물리량인가?</p>
  <div class="quiz-options" id="q1">
    <div class="quiz-opt">A. 스프링 변형량, 댐퍼 변형량</div>
    <div class="quiz-opt">B. 차체 변위(zs), 휠 변위(zu)</div>
    <div class="quiz-opt">C. 차체 가속도, 휠 가속도</div>
    <div class="quiz-opt">D. 전륜 변위, 후륜 변위</div>
  </div>
  <div class="quiz-feedback" id="q1-fb"></div>
  <div class="solution-panel" id="q1-sol">
    <div class="sol-header">SOLUTION</div>
    <!-- Solution steps... -->
  </div>
</div>
```

### CSS for Quiz

```css
.quiz-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 24px 28px;
  margin-bottom: 16px;
}

.quiz-num {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--gold);
  letter-spacing: 2px;
  margin-bottom: 10px;
}

.quiz-q {
  font-size: 15px;
  color: var(--text-bright);
  margin-bottom: 16px;
  font-weight: 400;
}

.quiz-options {
  display: grid;
  gap: 8px;
}

.quiz-opt {
  background: var(--surface2);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 12px 16px;
  cursor: pointer;
  font-size: 14px;
  color: var(--text);
  transition: all 0.2s;
}

.quiz-opt:hover {
  border-color: var(--gold);
  color: var(--text-bright);
}

.quiz-opt.correct {
  background: rgba(74,191,138,.12);
  border-color: var(--green);
  color: var(--green);
}

.quiz-opt.wrong {
  background: rgba(191,74,74,.12);
  border-color: #bf4a4a;
  color: #bf4a4a;
}

.quiz-opt.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.quiz-feedback {
  margin-top: 10px;
  padding: 10px 14px;
  border-radius: 8px;
  font-size: 13px;
  display: none;
}

.quiz-feedback.show {
  display: block;
}

.quiz-feedback.correct-fb {
  background: rgba(74,191,138,.08);
  color: var(--green);
}

.quiz-feedback.wrong-fb {
  background: rgba(191,74,74,.08);
  color: #bf4a4a;
}

/* Solution Panel */
.solution-panel {
  display: none;
  margin-top: 16px;
  background: linear-gradient(135deg, rgba(201,168,76,.06), rgba(201,168,76,.02));
  border: 1px solid rgba(201,168,76,.2);
  border-radius: 12px;
  overflow: hidden;
  animation: solReveal 0.4s ease;
}

.solution-panel.show {
  display: block;
}

@keyframes solReveal {
  from {
    opacity: 0;
    transform: translateY(-8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.sol-header {
  background: rgba(201,168,76,.1);
  padding: 12px 20px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  color: var(--gold);
  font-weight: 500;
  letter-spacing: 1px;
  border-bottom: 1px solid rgba(201,168,76,.15);
}

.sol-step {
  padding: 10px 20px;
  font-size: 13px;
  color: var(--text);
  border-bottom: 1px solid rgba(201,168,76,.08);
  display: flex;
  align-items: baseline;
  gap: 12px;
}

.sol-step:last-of-type {
  border-bottom: none;
}

.sol-num {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--gold);
  font-weight: 500;
  min-width: 50px;
  letter-spacing: 1px;
  flex-shrink: 0;
}

.sol-step.highlight-step {
  background: rgba(201,168,76,.08);
}
```

### Key Attributes

- **data-correct**: Index of correct answer (0-based)
- **ID Pattern**: `q{N}` for options, `q{N}-fb` for feedback, `q{N}-sol` for solution
- **Quiz Number Format**: "QUESTION {N} — {Topic}"

---

## 5. SUMMARY TABLE: EXACT PATTERNS

| Component | Class | Purpose | Default State |
|-----------|-------|---------|----------------|
| Accordion Container | `.accordion` | Wrapper for expandable section | Border + overflow hidden |
| Accordion Button | `.accordion-toggle` | Clickable header (flex layout) | Cursor pointer, 18px 24px padding |
| Arrow Indicator | `.accordion-arrow` | Visual toggle indicator | `▼` or rotatable symbol |
| Content Area | `.accordion-content` | Hidden/shown via `.open` class | `display: none` |
| Content Padding | `.accordion-inner` | Inner margin/padding | `0 24px 24px` |
| Canvas Wrapper | `.sim-canvas-wrap` | Dark box around canvas | `#0A0C10` background |
| Simulation Container | `.sim-container` | Entire sim section | `var(--surface)` background |
| Slider Group | `.sim-slider-group` | Single slider + label | Flex 1, min-width 200px |
| Metrics Display | `.sim-metrics` | Grid of metric boxes | `grid: repeat(auto-fit, minmax(140px, 1fr))` |
| Metric Item | `.sim-metric` | Single metric card | Centered, monospace font |
| Memory Hook | `.memory-hook` | Gradient box for memory tips | Gold gradient background |
| Vehicle Example | `.vehicle-example` | Gradient box for examples | Blue gradient background |
| Quiz Card | `.quiz-card` | Question container | `var(--surface)` background |
| Quiz Option | `.quiz-opt` | Answer choice | `var(--surface2)` background |
| Solution Panel | `.solution-panel` | Hidden solution reveal | Gold gradient, animation |

---

## 6. CREATION CHECKLIST

Use this checklist to identify/audit patterns in HTML files:

### Accordion Section Checklist
- [ ] Has `.accordion` container div
- [ ] Contains `.accordion-toggle` button (not class="accordion-btn")
- [ ] Toggle button has two `<span>` elements (text + arrow)
- [ ] Arrow is `.accordion-arrow` with `▼` symbol
- [ ] Content div has `.accordion-content` class
- [ ] Content div has `id="deepdive{N}"` pattern
- [ ] Content inner has `.accordion-inner` div
- [ ] No styled inline `<div style="...">` wrappers in accordion
- [ ] Event listener handles `.accordion-toggle` click
- [ ] Click toggles `.open` class on content

### Canvas Simulation Checklist
- [ ] Wrapped in `.sim-container` div
- [ ] Has `.sim-canvas-wrap` around `<canvas>`
- [ ] Canvas has `id="sim-day{N}"` pattern
- [ ] Has `width="700" height="350"` attributes
- [ ] Controls div has `id="sim-day{N}-controls"`
- [ ] Metrics div has `id="sim-day{N}-metrics"`
- [ ] JavaScript is IIFE `(function(){...})()`
- [ ] Uses `ctx = canvas.getContext('2d')`
- [ ] Has `addSlider()` function for dynamic creation
- [ ] Has `addBtn()` function for dynamic creation
- [ ] Has `draw()` function for rendering
- [ ] Sliders call `draw()` on input

### Styled Box Checklist
- [ ] Memory hook uses gradient: `rgba(201,168,76,.1), rgba(201,168,76,.03)`
- [ ] Vehicle example uses gradient: `rgba(201,168,76,.04), rgba(74,158,191,.04)`
- [ ] Box has `border-radius: 16px`
- [ ] Box has `padding: 24px`
- [ ] Box has `margin: 20px 0`
- [ ] Title has inline color style (gold-light, blue, purple)
- [ ] NO `.memory-hook` or `.vehicle-example` in plain text sections
- [ ] Inner grid uses `display:grid;grid-template-columns:repeat(3,1fr);gap:16px`

### Quiz Checklist
- [ ] Quiz card has `class="quiz-card" data-correct="X"`
- [ ] Quiz number div has `class="quiz-num"` with "QUESTION {N} — {Topic}" format
- [ ] Question text in `<p class="quiz-q">`
- [ ] Options in `<div class="quiz-options" id="q{N}">`
- [ ] Each option is `<div class="quiz-opt">`
- [ ] Feedback div: `<div class="quiz-feedback" id="q{N}-fb">`
- [ ] Solution div: `<div class="solution-panel" id="q{N}-sol">`
- [ ] Solution has `.sol-header` and `.sol-step` elements
- [ ] Event listeners check `data-correct` attribute

---

## 7. NOTES FOR AUDIT/FIX SCRIPTS

### What to Look For (Anti-patterns)
1. `class="accordion-btn"` instead of `class="accordion-toggle"` ❌
2. `.accordion-content` as sibling to non-button elements ❌
3. Canvas wrapped in multiple nested divs ❌
4. Canvas without `id="sim-day{N}"` pattern ❌
5. Sliders created with plain HTML instead of JavaScript ❌
6. Metrics displayed as raw text instead of grid ❌
7. Memory hooks without gradient background ❌
8. Vehicle examples without blue gradient ❌
9. Quiz options without `data-correct` on card ❌
10. Solution panel with hardcoded display:block ❌

### Files Analyzed
1. **Day01_운동방정식유도.html** - 58,184 lines
   - 4 accordion sections (심화 학습)
   - 1 canvas simulation (Day 1 Free Vibration Simulator)
   - 2 memory hooks
   - 1 vehicle example
   - 0 quiz sections (in DEEP DIVE section only)

2. **Day15_Part2복습.html** - (analyzed via grep)
   - Multiple accordion sections
   - Accordion toggle event listeners
   - Quiz sections with solution panels

3. **Day30_QuarterCar구현.html** - (analyzed via grep)
   - 1 canvas simulation (Quarter-Car SIMPACK comparison)
   - 3 quiz cards (Questions 1-3)
   - Complete solution panel structure
   - Memory hooks and vehicle examples

---

**Last Updated**: 2026-03-13
**Pattern Analysis Complete**: ✅
