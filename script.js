const tigerData = [
  { year: 2009, value: 121 },
  { year: 2013, value: 198 },
  { year: 2018, value: 235 },
  { year: 2022, value: 355 },
  { year: 2026, value: 429 },
];

const forestTimeline = [
  { year: 2009, value: 39.6 },
  { year: 2013, value: 39.1 },
  { year: 2018, value: 44.74 },
  { year: 2022, value: 44.0 },
  { year: 2026, value: 40.36 },
];

const parkChangeData = [
  { name: "Chitwan", change: 17 },
  { name: "Parsa", change: 30 },
  { name: "Banke", change: 26 },
  { name: "Shuklaphanta", change: 14 },
  { name: "Bardiya", change: -13 },
];

function createSvg(width, height) {
  const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svg.setAttribute("width", width);
  svg.setAttribute("height", height);
  svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
  return svg;
}

function addText(svg, x, y, content, options = {}) {
  const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
  text.setAttribute("x", x);
  text.setAttribute("y", y);
  text.setAttribute("text-anchor", options.anchor || "middle");
  text.setAttribute("font-size", options.fontSize || "11");
  text.setAttribute("font-weight", options.fontWeight || "500");
  text.setAttribute("fill", options.fill || "#f5f7fb");
  text.textContent = content;
  svg.appendChild(text);
}

function renderTimelineChart() {
  const container = document.getElementById("timelineChart");
  if (!container) return;

  const width = 460;
  const height = 280;
  const padding = { top: 30, right: 44, bottom: 52, left: 48 };
  const svg = createSvg(width, height);
  svg.setAttribute("style", "display:block;width:100%;height:auto;");

  const innerWidth = width - padding.left - padding.right;
  const innerHeight = height - padding.top - padding.bottom;
  const xScale = (year) => padding.left + ((year - 2009) / (2026 - 2009)) * innerWidth;
  const tigerScale = (value) => padding.top + innerHeight - ((value - 100) / 350) * innerHeight;
  const forestScale = (value) => padding.top + innerHeight - ((value - 39) / 6) * innerHeight;

  const bg = document.createElementNS("http://www.w3.org/2000/svg", "rect");
  bg.setAttribute("x", 0);
  bg.setAttribute("y", 0);
  bg.setAttribute("width", width);
  bg.setAttribute("height", height);
  bg.setAttribute("fill", "#09131d");
  bg.setAttribute("rx", 14);
  svg.appendChild(bg);

  for (let i = 0; i <= 4; i += 1) {
    const y = padding.top + (i * innerHeight) / 4;
    const grid = document.createElementNS("http://www.w3.org/2000/svg", "line");
    grid.setAttribute("x1", padding.left);
    grid.setAttribute("y1", y);
    grid.setAttribute("x2", width - padding.right);
    grid.setAttribute("y2", y);
    grid.setAttribute("stroke", "rgba(255,255,255,0.12)");
    grid.setAttribute("stroke-width", "1");
    svg.appendChild(grid);
  }

  const axisX = document.createElementNS("http://www.w3.org/2000/svg", "line");
  axisX.setAttribute("x1", padding.left);
  axisX.setAttribute("y1", height - padding.bottom);
  axisX.setAttribute("x2", width - padding.right);
  axisX.setAttribute("y2", height - padding.bottom);
  axisX.setAttribute("stroke", "#f5f7fb");
  axisX.setAttribute("stroke-width", "1.2");
  svg.appendChild(axisX);

  const axisY = document.createElementNS("http://www.w3.org/2000/svg", "line");
  axisY.setAttribute("x1", padding.left);
  axisY.setAttribute("y1", padding.top);
  axisY.setAttribute("x2", padding.left);
  axisY.setAttribute("y2", height - padding.bottom);
  axisY.setAttribute("stroke", "#f5f7fb");
  axisY.setAttribute("stroke-width", "1.2");
  svg.appendChild(axisY);

  const tigerPoints = tigerData.map((item) => ({ x: xScale(item.year), y: tigerScale(item.value), item }));
  const forestPoints = forestTimeline.map((item) => ({ x: xScale(item.year), y: forestScale(item.value), item }));

  const area = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
  const areaPoints = tigerPoints.map((p) => `${p.x},${p.y}`).join(" ");
  area.setAttribute("points", `${areaPoints} ${tigerPoints[tigerPoints.length - 1].x},${height - padding.bottom} ${tigerPoints[0].x},${height - padding.bottom}`);
  area.setAttribute("fill", "rgba(135,240,177,0.2)");
  svg.appendChild(area);

  const tigerLine = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
  tigerLine.setAttribute("points", tigerPoints.map((p) => `${p.x},${p.y}`).join(" "));
  tigerLine.setAttribute("fill", "none");
  tigerLine.setAttribute("stroke", "#87f0b1");
  tigerLine.setAttribute("stroke-width", "3.2");
  svg.appendChild(tigerLine);

  const forestLine = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
  forestLine.setAttribute("points", forestPoints.map((p) => `${p.x},${p.y}`).join(" "));
  forestLine.setAttribute("fill", "none");
  forestLine.setAttribute("stroke", "#38bdf8");
  forestLine.setAttribute("stroke-width", "2.6");
  forestLine.setAttribute("stroke-dasharray", "6 4");
  svg.appendChild(forestLine);

  tigerPoints.forEach((point) => {
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", point.x);
    circle.setAttribute("cy", point.y);
    circle.setAttribute("r", "5.2");
    circle.setAttribute("fill", "#87f0b1");
    circle.setAttribute("stroke", "#09131d");
    circle.setAttribute("stroke-width", "1.6");
    svg.appendChild(circle);
  });

  forestPoints.forEach((point) => {
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", point.x);
    circle.setAttribute("cy", point.y);
    circle.setAttribute("r", "4.2");
    circle.setAttribute("fill", "#38bdf8");
    circle.setAttribute("stroke", "#09131d");
    circle.setAttribute("stroke-width", "1.4");
    svg.appendChild(circle);
  });

  tigerData.forEach((item, index) => {
    const point = tigerPoints[index];
    addText(svg, point.x, height - 16, item.year, { fontSize: "10", fill: "#e2e8f0" });
    addText(svg, point.x + 8, point.y - 10, item.value, { fontSize: "10", anchor: "start", fill: "#e2e8f0" });
  });

  addText(svg, 18, 18, "Tiger count", { anchor: "start", fontSize: "11", fill: "#87f0b1" });
  addText(svg, width - 92, 18, "Forest cover %", { anchor: "start", fontSize: "11", fill: "#38bdf8" });
  addText(svg, 18, 28, "Clear recovery despite a narrow forest band", { anchor: "start", fontSize: "10", fill: "#cbd5e1" });

  container.appendChild(svg);
}

function renderParkChangeChart() {
  const container = document.getElementById("parkChart");
  if (!container) return;

  const width = 460;
  const height = 280;
  const padding = { top: 30, right: 28, bottom: 54, left: 48 };
  const svg = createSvg(width, height);
  svg.setAttribute("style", "display:block;width:100%;height:auto;");

  const bg = document.createElementNS("http://www.w3.org/2000/svg", "rect");
  bg.setAttribute("x", 0);
  bg.setAttribute("y", 0);
  bg.setAttribute("width", width);
  bg.setAttribute("height", height);
  bg.setAttribute("fill", "#09131d");
  bg.setAttribute("rx", 14);
  svg.appendChild(bg);

  const maxValue = Math.max(...parkChangeData.map((d) => Math.abs(d.change)));
  const zeroY = height - padding.bottom;
  const innerHeight = height - padding.top - padding.bottom;
  const barWidth = 46;
  const gap = 24;

  const axis = document.createElementNS("http://www.w3.org/2000/svg", "line");
  axis.setAttribute("x1", padding.left);
  axis.setAttribute("y1", zeroY);
  axis.setAttribute("x2", width - padding.right);
  axis.setAttribute("y2", zeroY);
  axis.setAttribute("stroke", "#f5f7fb");
  axis.setAttribute("stroke-width", "1.2");
  svg.appendChild(axis);

  const midpoint = document.createElementNS("http://www.w3.org/2000/svg", "line");
  midpoint.setAttribute("x1", padding.left);
  midpoint.setAttribute("y1", zeroY - innerHeight / 2);
  midpoint.setAttribute("x2", width - padding.right);
  midpoint.setAttribute("y2", zeroY - innerHeight / 2);
  midpoint.setAttribute("stroke", "rgba(255,255,255,0.24)");
  midpoint.setAttribute("stroke-width", "1");
  midpoint.setAttribute("stroke-dasharray", "4 4");
  svg.appendChild(midpoint);

  parkChangeData.forEach((item, index) => {
    const x = padding.left + index * (barWidth + gap) + 8;
    const barHeight = (Math.abs(item.change) / maxValue) * (innerHeight * 0.82);
    const y = item.change >= 0 ? zeroY - barHeight : zeroY;
    const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    rect.setAttribute("x", x);
    rect.setAttribute("y", y);
    rect.setAttribute("width", barWidth);
    rect.setAttribute("height", barHeight);
    rect.setAttribute("fill", item.change >= 0 ? "#87f0b1" : "#fb7185");
    rect.setAttribute("rx", 8);
    svg.appendChild(rect);

    addText(svg, x + barWidth / 2, zeroY + 22, item.name, { fontSize: "10", fill: "#e2e8f0" });
    addText(svg, x + barWidth / 2, y - 8, `${item.change}`, { fontSize: "10", fill: item.change >= 0 ? "#87f0b1" : "#fb7185" });
  });

  addText(svg, 18, 18, "Park-level change", { anchor: "start", fontSize: "11", fill: "#87f0b1" });
  addText(svg, 18, 28, "Most parks show positive movement", { anchor: "start", fontSize: "10", fill: "#cbd5e1" });

  container.appendChild(svg);
}

function renderForestGauge() {
  const container = document.getElementById("forestGauge");
  if (!container) return;

  const width = 320;
  const height = 220;
  const centerX = width / 2;
  const centerY = height / 2;
  const radius = 72;
  const svg = createSvg(width, height);

  const track = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  track.setAttribute("cx", centerX);
  track.setAttribute("cy", centerY);
  track.setAttribute("r", radius);
  track.setAttribute("fill", "none");
  track.setAttribute("stroke", "rgba(255,255,255,0.16)");
  track.setAttribute("stroke-width", "18");
  svg.appendChild(track);

  const progress = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  progress.setAttribute("cx", centerX);
  progress.setAttribute("cy", centerY);
  progress.setAttribute("r", radius);
  progress.setAttribute("fill", "none");
  progress.setAttribute("stroke", "#87f0b1");
  progress.setAttribute("stroke-width", "18");
  progress.setAttribute("stroke-linecap", "round");
  progress.setAttribute("stroke-dasharray", `${2 * Math.PI * radius}`);
  progress.setAttribute("stroke-dashoffset", `${2 * Math.PI * radius * 0.58}`);
  progress.setAttribute("transform", `rotate(-90 ${centerX} ${centerY})`);
  svg.appendChild(progress);

  addText(svg, centerX, centerY - 8, "~42%", { fontSize: "24", fontWeight: "700", fill: "#f8fafc" });
  addText(svg, centerX, centerY + 16, "forest cover", { fontSize: "12", fill: "#cbd5e1" });
  addText(svg, centerX, centerY + 48, "stable, but not yet enough to guarantee future expansion", { fontSize: "10", fill: "#cbd5e1" });

  container.appendChild(svg);
}

function createParticles() {
  const layer = document.querySelector(".hero__particle-layer");
  if (!layer) return;
  for (let i = 0; i < 16; i += 1) {
    const particle = document.createElement("span");
    particle.className = "hero__particle";
    particle.style.left = `${Math.random() * 100}%`;
    particle.style.top = `${Math.random() * 100}%`;
    particle.style.animationDelay = `${Math.random() * 4}s`;
    particle.style.opacity = `${0.3 + Math.random() * 0.6}`;
    layer.appendChild(particle);
  }
}

function addTiltEffect() {
  const cards = document.querySelectorAll(".tilt-card");
  cards.forEach((card) => {
    card.addEventListener("pointermove", (event) => {
      const rect = card.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;
      const rotateY = ((x / rect.width) - 0.5) * 10;
      const rotateX = ((0.5 - (y / rect.height))) * 10;
      card.style.transform = `perspective(900px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
    });

    card.addEventListener("pointerleave", () => {
      card.style.transform = "";
    });
  });
}

window.addEventListener("DOMContentLoaded", () => {
  renderTimelineChart();
  renderParkChangeChart();
  renderForestGauge();
  createParticles();
  addTiltEffect();
});
