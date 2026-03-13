# HTML Pattern Audit Checklist
## Quick Reference for Identifying & Fixing Patterns

---

## ACCORDION SECTION (심화 학습)

### ✓ CORRECT Pattern
```html
<div class="accordion">
  <button class="accordion-toggle">
    <span>💡 Title Text</span>
    <span class="accordion-arrow">▼</span>
  </button>
  <div class="accordion-content" id="deepdive1">
    <div class="accordion-inner">
      <h4 style="color:var(--gold-light);">Heading</h4>
      <p>Content paragraph</p>
    </div>
  </div>
</div>
```

### ❌ COMMON MISTAKES

#### Mistake 1: Wrong Button Class
```html
<!-- ❌ WRONG -->
<button class="accordion-btn">
  <span>Title</span>
  <span class="accordion-arrow">▼</span>
</button>

<!-- ✅ FIX -->
<button class="accordion-toggle">
  <span>Title</span>
  <span class="accordion-arrow">▼</span>
</button>
```

#### Mistake 2: Missing accordion-inner Div
```html
<!-- ❌ WRONG -->
<div class="accordion-content" id="deepdive1">
  <p>Content directly here</p>
</div>

<!-- ✅ FIX -->
<div class="accordion-content" id="deepdive1">
  <div class="accordion-inner">
    <p>Content inside accordion-inner</p>
  </div>
</div>
```

#### Mistake 3: Content Not Sibling of Button
```html
<!-- ❌ WRONG -->
<div class="accordion">
  <button class="accordion-toggle">...</button>
  <div class="some-wrapper">
    <div class="accordion-content">...</div>
  </div>
</div>

<!-- ✅ FIX -->
<div class="accordion">
  <button class="accordion-toggle">...</button>
  <div class="accordion-content">...</div>
</div>
```

#### Mistake 4: Extra Styling in Accordion Content
```html
<!-- ❌ WRONG (styled box inside accordion) -->
<div class="accordion-content" id="deepdive1">
  <div class="accordion-inner">
    <div style="background:linear-gradient(...);">
      <h4>Title</h4>
      <p>Content</p>
    </div>
  </div>
</div>

<!-- ✅ FIX (plain content only) -->
<div class="accordion-content" id="deepdive1">
  <div class="accordion-inner">
    <h4 style="color:var(--gold-light);">Title</h4>
    <p>Content</p>
  </div>
</div>
```

### Audit Checklist for Accordion
- [ ] Button has `class="accordion-toggle"` (NOT `accordion-btn`)
- [ ] Button contains exactly 2 `<span>` (text + arrow)
- [ ] Arrow span has `class="accordion-arrow"`
- [ ] Arrow is `▼` character (not `+`, `-`, or icon)
- [ ] Next sibling of button is `class="accordion-content"`
- [ ] Content div has `id="deepdive{N}"` format
- [ ] Inside content is `class="accordion-inner"` div
- [ ] Inner padding is NOT in deep-styled gradient boxes
- [ ] Parent `.accordion` div has NO additional styling
- [ ] JavaScript listener exists: `e.target.closest('.accordion-toggle')`

---

## CANVAS SIMULATION SECTION

### ✓ CORRECT Pattern
```html
<div class="sim-container">
  <div class="sim-canvas-wrap">
    <canvas id="sim-day01" width="700" height="350"></canvas>
  </div>
  <div id="sim-day01-controls" class="sim-controls"></div>
  <div id="sim-day01-metrics" class="sim-metrics"></div>
</div>

<script>
(function(){
  const canvas = document.getElementById('sim-day01');
  const ctx = canvas.getContext('2d');
  const W = 700, H = 350;
  const ctrlBox = document.getElementById('sim-day01-controls');
  const metricBox = document.getElementById('sim-day01-metrics');

  function addSlider(label, min, max, value, step, id) {
    const g = document.createElement('div');
    g.className = 'sim-slider-group';
    g.innerHTML = '<label>'+label+'</label>'+
      '<input type="range" min="'+min+'" max="'+max+'" value="'+value+'" step="'+step+'" id="'+id+'">'+
      '<div class="sim-readout" id="'+id+'-val">'+value+'</div>';
    ctrlBox.appendChild(g);
    const inp = document.getElementById(id);
    inp.oninput = function(){ document.getElementById(id+'-val').textContent = this.value; draw(); };
    return inp;
  }

  function draw() {
    ctx.fillStyle = '#0a0c10';
    ctx.fillRect(0, 0, W, H);
    // ... draw simulation ...
  }

  const sl_m = addSlider('질량 m (kg)', 1, 50, 10, 1, 'sim01-m');
  draw();
})();
</script>
```

### ❌ COMMON MISTAKES

#### Mistake 1: Wrong Canvas ID Pattern
```html
<!-- ❌ WRONG -->
<canvas id="simulation" width="700" height="350"></canvas>
<div id="controls" class="sim-controls"></div>
<div id="metrics" class="sim-metrics"></div>

<!-- ✅ FIX -->
<canvas id="sim-day01" width="700" height="350"></canvas>
<div id="sim-day01-controls" class="sim-controls"></div>
<div id="sim-day01-metrics" class="sim-metrics"></div>
```

#### Mistake 2: Sliders Created as HTML Instead of JavaScript
```html
<!-- ❌ WRONG -->
<div class="sim-controls">
  <div class="sim-slider-group">
    <label>质量 m (kg)</label>
    <input type="range" id="sim01-m" min="1" max="50" value="10">
    <div class="sim-readout" id="sim01-m-val">10</div>
  </div>
</div>

<!-- ✅ FIX (create dynamically) -->
<div id="sim-day01-controls" class="sim-controls"></div>
<script>
  function addSlider(label, min, max, value, step, id) {
    // ... JavaScript creates HTML ...
  }
</script>
```

#### Mistake 3: Canvas Missing Width/Height Attributes
```html
<!-- ❌ WRONG -->
<canvas id="sim-day01"></canvas>

<!-- ✅ FIX -->
<canvas id="sim-day01" width="700" height="350"></canvas>
```

#### Mistake 4: Draw Function Not Called on Slider Change
```javascript
// ❌ WRONG
inp.oninput = function(){
  document.getElementById(id+'-val').textContent = this.value;
  // Missing draw() call!
};

// ✅ FIX
inp.oninput = function(){
  document.getElementById(id+'-val').textContent = this.value;
  draw();  // Re-render canvas
};
```

#### Mistake 5: Metrics Not Using Array Mapping
```javascript
// ❌ WRONG
metricBox.innerHTML = '<div class="sim-metric">m: 10</div>';

// ✅ FIX
function setMetrics(arr) {
  metricBox.innerHTML = arr.map(m =>
    '<div class="sim-metric"><strong>'+m[0]+':</strong>&nbsp;'+m[1]+'</div>'
  ).join('');
}
setMetrics([['Mass', '10 kg'], ['Stiffness', '1000 N/m']]);
```

### Audit Checklist for Canvas
- [ ] Canvas ID follows `sim-day{N}` pattern
- [ ] Canvas has explicit `width="700" height="350"`
- [ ] Container div has `class="sim-container"`
- [ ] Canvas wrapped in `class="sim-canvas-wrap"`
- [ ] Controls div has `id="sim-day{N}-controls"` class=`"sim-controls"`
- [ ] Metrics div has `id="sim-day{N}-metrics"` class=`"sim-metrics"`
- [ ] JavaScript is inside IIFE `(function(){...})()`
- [ ] First line gets canvas: `getElementById('sim-day{N}')`
- [ ] Gets 2D context: `getContext('2d')`
- [ ] Defines W and H variables
- [ ] `addSlider()` function exists and creates HTML
- [ ] `draw()` function redraws canvas
- [ ] Sliders call `draw()` on input
- [ ] `draw()` initializes canvas with `fillRect()`
- [ ] Canvas draws with `ctx.strokeStyle` and `ctx.stroke()`

---

## STYLED BOXES (Memory Hook, Vehicle Example)

### ✓ CORRECT Patterns

#### Memory Hook Box
```html
<div class="memory-hook"
  style="background:linear-gradient(135deg,rgba(138,106,191,.08),rgba(138,106,191,.02));
         border:1px solid rgba(138,106,191,.2);
         border-radius:16px;
         padding:24px;
         margin:20px 0;">
  <h3 style="color:var(--purple);margin-bottom:12px;">🧠 기억 앵커</h3>
  <p>Memory text</p>
</div>
```

#### Vehicle Example Box
```html
<div class="vehicle-example"
  style="background:linear-gradient(135deg,rgba(201,168,76,.04),rgba(74,158,191,.04));
         border:1px solid rgba(201,168,76,.15);
         border-radius:16px;
         padding:24px;
         margin:20px 0;">
  <h4 style="color:var(--gold-light);margin-bottom:16px;">🚗 레퍼런스</h4>
  <p>Example content</p>
</div>
```

### ❌ COMMON MISTAKES

#### Mistake 1: Using Styled Box Inside Accordion
```html
<!-- ❌ WRONG -->
<div class="accordion-content" id="deepdive1">
  <div class="accordion-inner">
    <div class="memory-hook" style="...">
      <h3>Title</h3>
      <p>Content</p>
    </div>
  </div>
</div>

<!-- ✅ FIX (simple content in accordion) -->
<div class="accordion-content" id="deepdive1">
  <div class="accordion-inner">
    <h4 style="color:var(--gold-light);">Title</h4>
    <p>Content</p>
  </div>
</div>

<!-- Then separate styled box OUTSIDE accordion -->
<div class="memory-hook" style="...">
  <h3 style="color:var(--purple);">Title</h3>
  <p>Content</p>
</div>
```

#### Mistake 2: Wrong Gradient Colors
```html
<!-- ❌ WRONG (memory hook with gold gradient) -->
<div class="memory-hook"
  style="background:linear-gradient(135deg,rgba(201,168,76,.1),rgba(201,168,76,.03));">

<!-- ✅ FIX (memory hook with purple gradient) -->
<div class="memory-hook"
  style="background:linear-gradient(135deg,rgba(138,106,191,.08),rgba(138,106,191,.02));">

<!-- ✅ FIX (vehicle example with blue/gold gradient) -->
<div class="vehicle-example"
  style="background:linear-gradient(135deg,rgba(201,168,76,.04),rgba(74,158,191,.04));">
```

#### Mistake 3: Missing Box Styling
```html
<!-- ❌ WRONG -->
<div class="vehicle-example">
  <h4>Title</h4>
  <p>Content</p>
</div>

<!-- ✅ FIX (include inline gradient styling) -->
<div class="vehicle-example"
  style="background:linear-gradient(135deg,rgba(201,168,76,.04),rgba(74,158,191,.04));
         border:1px solid rgba(201,168,76,.15);
         border-radius:16px;
         padding:24px;
         margin:20px 0;">
  <h4 style="color:var(--gold-light);">Title</h4>
  <p>Content</p>
</div>
```

### Audit Checklist for Styled Boxes
- [ ] Memory hook has `.memory-hook` class
- [ ] Memory hook gradient uses purple: `rgba(138,106,191,...)`
- [ ] Vehicle example has `.vehicle-example` class
- [ ] Vehicle example gradient uses blue/gold: `rgba(201,168,76,...)` + `rgba(74,158,191,...)`
- [ ] Box has `border-radius: 16px`
- [ ] Box has `padding: 24px` (or similar)
- [ ] Box has `margin: 20px 0`
- [ ] Title color is `color:var(--gold-light)` or `color:var(--purple)`
- [ ] Styled boxes are NOT inside accordion sections
- [ ] Gradient inline style includes ALL 3 properties (background, border, border-radius)

---

## QUIZ SECTION

### ✓ CORRECT Pattern
```html
<div class="quiz-card" data-correct="1">
  <div class="quiz-num">QUESTION 01 — 주제</div>
  <p class="quiz-q">질문 텍스트?</p>
  <div class="quiz-options" id="q1">
    <div class="quiz-opt">A. 선택지 1</div>
    <div class="quiz-opt">B. 선택지 2</div>
    <div class="quiz-opt">C. 선택지 3</div>
    <div class="quiz-opt">D. 선택지 4</div>
  </div>
  <div class="quiz-feedback" id="q1-fb"></div>
  <div class="solution-panel" id="q1-sol">
    <div class="sol-header">SOLUTION</div>
    <div class="sol-step"><span class="sol-num">1️⃣</span> Step 1</div>
    <div class="sol-step"><span class="sol-num">2️⃣</span> Step 2</div>
  </div>
</div>
```

### ❌ COMMON MISTAKES

#### Mistake 1: Missing data-correct Attribute
```html
<!-- ❌ WRONG -->
<div class="quiz-card">
  <div class="quiz-q">Question?</div>

<!-- ✅ FIX -->
<div class="quiz-card" data-correct="1">
  <div class="quiz-q">Question?</div>
```

#### Mistake 2: Wrong ID Naming
```html
<!-- ❌ WRONG -->
<div class="quiz-options" id="question-1">
<div class="quiz-feedback" id="feedback-1">

<!-- ✅ FIX -->
<div class="quiz-options" id="q1">
<div class="quiz-feedback" id="q1-fb">
<div class="solution-panel" id="q1-sol">
```

#### Mistake 3: Quiz Number Format
```html
<!-- ❌ WRONG -->
<div class="quiz-num">Q1: 주제</div>
<div class="quiz-num">1번 문제</div>

<!-- ✅ FIX -->
<div class="quiz-num">QUESTION 01 — 주제</div>
```

#### Mistake 4: Solution Steps Without sol-num
```html
<!-- ❌ WRONG -->
<div class="solution-panel">
  <div class="sol-step">Step 1 text</div>
  <div class="sol-step">Step 2 text</div>
</div>

<!-- ✅ FIX -->
<div class="solution-panel">
  <div class="sol-step">
    <span class="sol-num">1️⃣</span> Step 1 text
  </div>
  <div class="sol-step">
    <span class="sol-num">2️⃣</span> Step 2 text
  </div>
</div>
```

#### Mistake 5: Solution Panel Visible by Default
```html
<!-- ❌ WRONG (visible immediately) -->
<div class="solution-panel" style="display:block;">

<!-- ✅ FIX (hidden by default, shown via .show class) -->
<div class="solution-panel">
  <!-- JS adds .show class when answer selected -->
</div>
```

### Audit Checklist for Quiz
- [ ] Quiz card has `data-correct="{N}"` (0-based index)
- [ ] Quiz number div: `class="quiz-num"` with "QUESTION {N} — {Topic}" format
- [ ] Question text: `<p class="quiz-q">`
- [ ] Options container: `id="q{N}"` class=`"quiz-options"`
- [ ] Each option: `<div class="quiz-opt">`
- [ ] Feedback div: `id="q{N}-fb"` class=`"quiz-feedback"`
- [ ] Solution div: `id="q{N}-sol"` class=`"solution-panel"`
- [ ] Solution header: `<div class="sol-header">SOLUTION</div>`
- [ ] Solution steps: `class="sol-step"` with nested `class="sol-num"`
- [ ] Data-correct index matches correct answer position (0-based)
- [ ] Solution panel has NO inline `display:block` style
- [ ] JavaScript listener handles quiz-opt click events
- [ ] Listener accesses `card.dataset.correct` to check answer

---

## QUICK FIND-REPLACE COMMANDS

### Fix: accordion-btn → accordion-toggle
```
Find:    class="accordion-btn"
Replace: class="accordion-toggle"
```

### Fix: sim-day{N} Controls and Metrics IDs
```
Find:    <div id="controls"
Replace: <div id="sim-day{N}-controls"

Find:    <div id="metrics"
Replace: <div id="sim-day{N}-metrics"
```

### Fix: Quiz numbering
```
Find:    <div class="quiz-num">Q1:
Replace: <div class="quiz-num">QUESTION 01 —

Find:    <div class="quiz-num">Q2:
Replace: <div class="quiz-num">QUESTION 02 —
```

### Fix: Quiz IDs (Question 1)
```
Find:    <div class="quiz-options" id="question-1">
Replace: <div class="quiz-options" id="q1">

Find:    <div class="quiz-feedback" id="feedback-1">
Replace: <div class="quiz-feedback" id="q1-fb">

Find:    <div class="solution-panel" id="solution-1">
Replace: <div class="solution-panel" id="q1-sol">
```

---

## STRUCTURE TEMPLATE

### Complete Day File Structure
```html
<!DOCTYPE html>
<html>
<head>
  <!-- CSS with all patterns defined -->
</head>
<body>
  <!-- Section 1: Main content -->
  <section>
    <!-- Regular text, equations, diagrams -->
  </section>

  <!-- Section 2: Deep Dive / Accordion -->
  <div class="section">
    <div class="section-label">DEEP DIVE</div>
    <h2 class="section-title">심화 학습</h2>

    <div class="accordion">
      <button class="accordion-toggle">
        <span>💡 Title 1</span>
        <span class="accordion-arrow">▼</span>
      </button>
      <div class="accordion-content" id="deepdive1">
        <div class="accordion-inner">
          <h4>...</h4>
          <p>...</p>
        </div>
      </div>
    </div>
    <!-- More accordions -->
  </div>

  <!-- Section 3: Memory hooks / Vehicle examples -->
  <div class="memory-hook" style="...">...</div>
  <div class="vehicle-example" style="...">...</div>

  <!-- Section 4: Interactive Simulation -->
  <div class="section-card">
    <div class="section-label">INTERACTIVE SIMULATION</div>
    <h2 class="section-title">🎮 Simulator Title</h2>
    <div class="sim-container">
      <div class="sim-canvas-wrap">
        <canvas id="sim-day{N}" width="700" height="350"></canvas>
      </div>
      <div id="sim-day{N}-controls" class="sim-controls"></div>
      <div id="sim-day{N}-metrics" class="sim-metrics"></div>
    </div>
    <script>
      (function(){...})();
    </script>
  </div>

  <!-- Section 5: Quiz -->
  <div class="section">
    <div class="section-label">QUIZ</div>
    <h2 class="section-title">즉시 복습 퀴즈</h2>

    <div class="quiz-card" data-correct="1">
      <div class="quiz-num">QUESTION 01 — Topic</div>
      <p class="quiz-q">Question text?</p>
      <div class="quiz-options" id="q1">
        <div class="quiz-opt">A. Option 1</div>
        <div class="quiz-opt">B. Option 2</div>
      </div>
      <div class="quiz-feedback" id="q1-fb"></div>
      <div class="solution-panel" id="q1-sol">
        <div class="sol-header">SOLUTION</div>
        <div class="sol-step"><span class="sol-num">1️⃣</span> Step</div>
      </div>
    </div>
  </div>
</body>
</html>
```

---

**Last Updated**: 2026-03-13
**Audit Checklist Version**: 1.0
**Status**: Ready for automated validation
