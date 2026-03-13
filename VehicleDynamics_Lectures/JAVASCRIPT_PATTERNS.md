# JavaScript Event Handler Patterns
## Vehicle Dynamics Lectures - Complete JS Code Reference

---

## 1. ACCORDION EVENT HANDLER

### Complete Implementation
```javascript
// Global event listener for all accordions
document.addEventListener('click', function(e) {
  var hdr = e.target.closest('.accordion-header, .accordion-toggle');
  if (hdr) {
    var content = hdr.nextElementSibling;
    if (content) {
      // Toggle the open class
      content.classList.toggle('open');
      var nowOpen = content.classList.contains('open');

      // Rotate or change arrow
      var arrow = hdr.querySelector('.accordion-arrow, span:last-child');
      if (arrow) {
        if (arrow.textContent === '+' || arrow.textContent === '−') {
          // If arrow is +/−, change it
          arrow.textContent = nowOpen ? '−' : '+';
        } else {
          // If arrow is ▼, rotate it
          arrow.style.transform = nowOpen ? 'rotate(180deg)' : 'rotate(0deg)';
        }
      }
    }
  }
});
```

### How It Works
1. Listens for any click on the page
2. Uses `.closest()` to find if click target is accordion header
3. Gets next sibling (the `.accordion-content` div)
4. Toggles `.open` class on the content
5. Updates arrow visual (rotation or text change)

### Usage Notes
- Works with **any class name** containing "accordion-header" or "accordion-toggle"
- Arrow automatically detects symbol type (+/− vs ▼)
- Pure CSS handles open/closed display (no JS show/hide)
- **Event delegation** = single listener handles all accordions

---

## 2. CANVAS SIMULATION SETUP PATTERN

### Full IIFE Template
```javascript
(function(){
  // ═══ CANVAS & CONTEXT ═══
  const canvas = document.getElementById('sim-day30');  // Change day number
  const ctx = canvas.getContext('2d');
  const W = 700, H = 350;

  // ═══ CONTROL BOXES ═══
  const ctrlBox = document.getElementById('sim-day30-controls');
  const metricBox = document.getElementById('sim-day30-metrics');

  // ═══ SLIDER CREATION HELPER ═══
  function addSlider(label, min, max, value, step, id) {
    const g = document.createElement('div');
    g.className = 'sim-slider-group';
    g.innerHTML = '<label>' + label + '</label>' +
                  '<input type="range" min="'+min+'" max="'+max+'" value="'+value+'" step="'+step+'" id="'+id+'">' +
                  '<div class="sim-readout" id="'+id+'-val">'+value+'</div>';
    ctrlBox.appendChild(g);

    const inp = document.getElementById(id);
    inp.oninput = function(){
      document.getElementById(id+'-val').textContent = this.value;
      draw();  // Redraw on slider change
    };
    return inp;
  }

  // ═══ BUTTON CREATION HELPER ═══
  function addBtn(label, fn) {
    const b = document.createElement('button');
    b.className = 'sim-btn';
    b.textContent = label;
    b.onclick = fn;
    ctrlBox.appendChild(b);
  }

  // ═══ METRICS DISPLAY HELPER ═══
  function setMetrics(arr) {
    // arr = [['Label1', 'Value1'], ['Label2', 'Value2'], ...]
    metricBox.innerHTML = arr.map(m =>
      '<div class="sim-metric"><strong>'+m[0]+':</strong>&nbsp;'+m[1]+'</div>'
    ).join('');
  }

  // ═══ CREATE CONTROLS ═══
  const sl_z = addSlider('감쇠비 ζ', 0.1, 0.5, 0.3, 0.01, 'sim30-z');

  // ═══ MAIN DRAWING FUNCTION ═══
  function draw() {
    // Clear canvas with dark background
    ctx.fillStyle = '#0a0c10';
    ctx.fillRect(0, 0, W, H);

    // Get current slider values
    const z = +sl_z.value;  // Convert string to number
    const ms = 300, ks = 20000;
    const wn = Math.sqrt(ks/ms);

    // ─── Draw Analytical Response ───
    ctx.strokeStyle = '#C9A84C';  // Gold color
    ctx.lineWidth = 2;
    ctx.beginPath();

    for(let i = 0; i <= 400; i++) {
      const t = i * 2 / 400;
      const x = 0.05 * Math.exp(-z*wn*t) * Math.cos(wn*Math.sqrt(1-z*z)*t);
      const px = i * W / 400;
      const py = H/2 - x*H*7;

      if(i) ctx.lineTo(px, py);
      else ctx.moveTo(px, py);
    }
    ctx.stroke();

    // ─── Draw SIMPACK Response (with noise) ───
    ctx.strokeStyle = '#4A9EBF';  // Blue color
    ctx.lineWidth = 1.5;
    ctx.setLineDash([4, 2]);  // Dashed line
    ctx.beginPath();

    for(let i = 0; i <= 400; i++) {
      const t = i * 2 / 400;
      const noise = 1 + 0.02*Math.sin(50*t);
      const x = 0.05 * Math.exp(-z*wn*t) * Math.cos(wn*Math.sqrt(1-z*z)*t) * noise;
      const px = i * W / 400;
      const py = H/2 - x*H*7;

      if(i) ctx.lineTo(px, py);
      else ctx.moveTo(px, py);
    }
    ctx.stroke();
    ctx.setLineDash([]);  // Reset dash

    // ─── Draw Center Line ───
    ctx.strokeStyle = 'rgba(255,255,255,0.15)';
    ctx.beginPath();
    ctx.moveTo(0, H/2);
    ctx.lineTo(W, H/2);
    ctx.stroke();

    // ─── Draw Legend ───
    ctx.fillStyle = '#C9A84C';
    ctx.font = '12px monospace';
    ctx.fillText('— 해석해 (Analytical)', 10, 20);

    ctx.fillStyle = '#4A9EBF';
    ctx.fillText('- - - SIMPACK', 10, 40);
  }

  // ═══ INITIAL DRAW ═══
  draw();

})();  // End IIFE
```

### Key Patterns Explained

#### Slider Creation
```javascript
inp.oninput = function(){
  document.getElementById(id+'-val').textContent = this.value;
  draw();  // Redraw simulation
};
```
- **`oninput`** event (not onChange) fires while dragging
- Updates the readout/value display
- **Calls `draw()` to re-render canvas**

#### Value Updates
```javascript
const z = +sl_z.value;  // + prefix converts string to number
```
- Input values are always strings
- Prefix `+` is shorthand for `Number()`
- Alternative: `parseInt()`, `parseFloat()`

#### Canvas Drawing
```javascript
ctx.beginPath();
// ... lines of moveTo/lineTo ...
ctx.stroke();
```
- Always bracket draw operations with `beginPath()` and `stroke()`
- Colors set with `ctx.strokeStyle` before `beginPath()`
- Line width set with `ctx.lineWidth`

#### Dashed Lines
```javascript
ctx.setLineDash([4, 2]);  // 4px line, 2px gap
// ... draw ...
ctx.setLineDash([]);  // Reset to solid
```

---

## 3. QUIZ ANSWER HANDLER PATTERN

### Full Implementation
```javascript
document.addEventListener('click', function(e) {
  var opt = e.target.closest('.quiz-opt');
  if (opt) {
    var card = opt.closest('.quiz-card');
    if (card && card.dataset.correct !== undefined) {
      var options = card.querySelectorAll('.quiz-opt');
      var correctIdx = parseInt(card.dataset.correct);
      var selectedIdx = Array.from(options).indexOf(opt);

      // Mark all options as disabled
      options.forEach(o => {
        o.classList.add('disabled');
      });

      // Show feedback
      var feedbackDiv = card.querySelector('.quiz-feedback');
      if (feedbackDiv) {
        feedbackDiv.classList.add('show');
        if (selectedIdx === correctIdx) {
          feedbackDiv.classList.add('correct-fb');
          feedbackDiv.classList.remove('wrong-fb');
          feedbackDiv.textContent = '✓ 정답입니다!';
          opt.classList.add('correct');
        } else {
          feedbackDiv.classList.add('wrong-fb');
          feedbackDiv.classList.remove('correct-fb');
          feedbackDiv.textContent = '✗ 다시 생각해보세요. 정답은 ' +
            (correctIdx + 1) + '번입니다.';
          opt.classList.add('wrong');
          options[correctIdx].classList.add('correct');
        }
      }

      // Show solution
      var solPanel = card.querySelector('.solution-panel');
      if (solPanel) {
        solPanel.classList.add('show');
      }
    }
  }
});
```

### Key Features
- **`data-correct`** attribute: 0-based index of correct answer
- **Array.from()**: Converts NodeList to array for indexOf()
- **classList methods**: Add/remove/toggle classes dynamically
- **Feedback types**: `.correct-fb` vs `.wrong-fb`
- **Solution reveal**: `.solution-panel.show` class enables animation

---

## 4. LATEX/KATEX AUTO-RENDER SETUP

### Implementation
```javascript
(function() {
  var katexJS = document.createElement('script');
  katexJS.src = 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js';
  katexJS.onload = function() {
    var autoRender = document.createElement('script');
    autoRender.src = 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js';
    autoRender.onload = function() {
      renderMathInElement(document.body, {
        delimiters: [
          {left: "$$", right: "$$", display: true},
          {left: "$", right: "$", display: false}
        ]
      });
    };
    document.head.appendChild(autoRender);
  };
  document.head.appendChild(katexJS);
})();
```

### Notes
- **IIFE** prevents global variable pollution
- **Dynamic script loading** ensures dependencies load in order
- **Display math**: `$$...$$ (newline-separated)`
- **Inline math**: `$...$ (in text)`

---

## 5. COMMON PATTERNS & CONVENTIONS

### ID Naming Convention
```
sim-day{N}         → Canvas element
sim-day{N}-controls → Control container
sim-day{N}-metrics  → Metrics display
q{N}               → Quiz options container
q{N}-fb            → Quiz feedback div
q{N}-sol           → Quiz solution div
deepdive{N}        → Accordion content ID
```

### CSS Color Variables Used
```javascript
ctx.strokeStyle = '#C9A84C';   // Gold (main)
ctx.strokeStyle = '#4A9EBF';   // Blue (secondary)
ctx.fillStyle = '#0a0c10';     // Dark background
ctx.strokeStyle = 'rgba(255,255,255,0.15)'; // White 15%
```

### Event Delegation Pattern
```javascript
document.addEventListener('click', function(e) {
  var element = e.target.closest('.selector');
  if (element) {
    // Handle element
  }
});
```
**Why?** Single global listener handles all current AND future elements

### Dynamic Element Creation
```javascript
const div = document.createElement('div');
div.className = 'class-name';
div.innerHTML = '<label>Text</label>';  // Avoid for user input
div.appendChild(someElement);           // Safer for app-generated HTML
parentElement.appendChild(div);
```

---

## 6. DEBUGGING TIPS

### Check if Canvas Exists
```javascript
const canvas = document.getElementById('sim-day01');
console.log('Canvas exists:', !!canvas);
console.log('Canvas size:', canvas.width, 'x', canvas.height);
```

### Check if Accordion Listeners Work
```javascript
document.addEventListener('click', function(e) {
  console.log('Click target:', e.target);
  console.log('Closest .accordion-toggle:', e.target.closest('.accordion-toggle'));
});
```

### Check Slider Values
```javascript
inp.oninput = function(){
  console.log('Slider value:', this.value);
  console.log('Parsed:', +this.value);
  draw();
};
```

### Check Quiz Card Selection
```javascript
var card = opt.closest('.quiz-card');
console.log('Card data-correct:', card.dataset.correct);
console.log('Selected index:', selectedIdx);
console.log('Correct index:', correctIdx);
console.log('Match:', selectedIdx === correctIdx);
```

---

## 7. COMMON MISTAKES TO AVOID

| ❌ Wrong | ✅ Correct |
|---------|----------|
| `event.target` (not closest) | `event.target.closest('.class')` |
| `e.preventDefault()` (for delegated) | Check with `.closest()` first |
| Canvas ID = `sim01` | Canvas ID = `sim-day01` |
| `Math.sqrt(k/m)` without parentheses | `Math.sqrt(k/m)` ✓ |
| `ctx.stroke()` before `ctx.beginPath()` | `ctx.beginPath()` first |
| Multiple global listeners | Use event delegation |
| String values: `sl_m.value` directly | Convert: `+sl_m.value` |
| `classList = 'new-class'` | Use `classList.add('new-class')` |
| Missing `.setLineDash([])` after dashed | Always reset to `[]` |
| Hardcoding canvas size in JS | Use canvas width/height attributes |

---

## 8. CANVAS COORDINATE SYSTEM

```
Canvas coordinates: (0,0) at TOP-LEFT
                    x increases RIGHT
                    y increases DOWN

┌─────────────────┐ (0,0)
│                 │
│                 │ y axis ↓
│                 │
└─────────────────┘
  → x axis

Physics coordinates: y increases UP
Conversion: canvas_y = canvas_height - physics_y
```

### Example: Centered Line Graph
```javascript
const H = 350;
const centerY = H / 2;  // Middle of canvas

// Physics value x ranges from -0.05 to +0.05
// +0.05 should appear at top, -0.05 at bottom
const scale = H * 7;
const py = centerY - x * scale;  // x positive → py smaller (up)
```

---

**Last Updated**: 2026-03-13
**Complete Pattern Reference**: ✅
