const tigerData = [
  { year: 2009, value: 121 },
  { year: 2013, value: 198 },
  { year: 2018, value: 235 },
  { year: 2022, value: 355 },
  { year: 2026, value: 429 },
];

const forestData = [
  { year: 1994, value: 39 },
  { year: 2010, value: 42 },
  { year: 2015, value: 44 },
  { year: 2021, value: 45 },
];

function createSvg(width, height) {
  const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svg.setAttribute("width", width);
  svg.setAttribute("height", height);
  svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
  return svg;
}

function renderLineChart(containerId, data, color) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const width = 340;
  const height = 220;
  const padding = 30;
  const maxValue = Math.max(...data.map((d) => d.value));
  const svg = createSvg(width, height);

  const axis = document.createElementNS("http://www.w3.org/2000/svg", "line");
  axis.setAttribute("x1", padding);
  axis.setAttribute("y1", height - padding);
  axis.setAttribute("x2", width - padding);
  axis.setAttribute("y2", height - padding);
  axis.setAttribute("stroke", "#111");
  axis.setAttribute("stroke-width", "1.2");
  svg.appendChild(axis);

  const points = data.map((item, index) => {
    const x = padding + (index * (width - padding * 2)) / (data.length - 1);
    const y = height - padding - (item.value / maxValue) * (height - padding * 2);
    return { x, y, item };
  });

  const polyline = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
  polyline.setAttribute("points", points.map((p) => `${p.x},${p.y}`).join(" "));
  polyline.setAttribute("fill", "none");
  polyline.setAttribute("stroke", color);
  polyline.setAttribute("stroke-width", "2.5");
  svg.appendChild(polyline);

  points.forEach((point) => {
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", point.x);
    circle.setAttribute("cy", point.y);
    circle.setAttribute("r", "5");
    circle.setAttribute("fill", color);
    svg.appendChild(circle);

    const label = document.createElementNS("http://www.w3.org/2000/svg", "text");
    label.setAttribute("x", point.x);
    label.setAttribute("y", height - 10);
    label.setAttribute("text-anchor", "middle");
    label.setAttribute("font-size", "11");
    label.setAttribute("fill", "#111");
    label.textContent = point.item.year;
    svg.appendChild(label);
  });

  container.appendChild(svg);
}

function renderForestChart() {
  const container = document.getElementById("forestChart");
  if (!container) return;

  const width = 260;
  const height = 260;
  const centerX = width / 2;
  const centerY = height / 2;
  const radius = 84;
  const svg = createSvg(width, height);

  const segments = [
    { value: 94, color: "#111" },
    { value: 6, color: "#c7c7c2" },
  ];

  let startAngle = -90;
  segments.forEach((segment) => {
    const sliceAngle = (segment.value / 100) * 360;
    const endAngle = startAngle + sliceAngle;

    const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    const largeArc = sliceAngle > 180 ? 1 : 0;
    const start = {
      x: centerX + radius * Math.cos((startAngle * Math.PI) / 180),
      y: centerY + radius * Math.sin((startAngle * Math.PI) / 180),
    };
    const end = {
      x: centerX + radius * Math.cos((endAngle * Math.PI) / 180),
      y: centerY + radius * Math.sin((endAngle * Math.PI) / 180),
    };

    const d = [
      `M ${centerX} ${centerY}`,
      `L ${start.x} ${start.y}`,
      `A ${radius} ${radius} 0 ${largeArc} 1 ${end.x} ${end.y}`,
      "Z",
    ].join(" ");

    path.setAttribute("d", d);
    path.setAttribute("fill", segment.color);
    svg.appendChild(path);
    startAngle = endAngle;
  });

  const innerCircle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  innerCircle.setAttribute("cx", centerX);
  innerCircle.setAttribute("cy", centerY);
  innerCircle.setAttribute("r", 48);
  innerCircle.setAttribute("fill", "#efefeb");
  svg.appendChild(innerCircle);

  const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
  text.setAttribute("x", centerX);
  text.setAttribute("y", centerY - 6);
  text.setAttribute("text-anchor", "middle");
  text.setAttribute("font-size", "18");
  text.setAttribute("font-weight", "700");
  text.setAttribute("fill", "#111");
  text.textContent = "Stable";
  svg.appendChild(text);

  const subtext = document.createElementNS("http://www.w3.org/2000/svg", "text");
  subtext.setAttribute("x", centerX);
  subtext.setAttribute("y", centerY + 18);
  subtext.setAttribute("text-anchor", "middle");
  subtext.setAttribute("font-size", "11");
  subtext.setAttribute("fill", "#5c6670");
  subtext.textContent = "Forest cover remains broadly stable";
  svg.appendChild(subtext);

  container.appendChild(svg);
}

function renderComparisonChart() {
  const container = document.getElementById("comparisonChart");
  if (!container) return;

  const width = 320;
  const height = 180;
  const svg = createSvg(width, height);
  const groups = [
    { label: "World", value: 28, color: "#111" },
    { label: "Nepal", value: 82, color: "#2f6f4f" },
  ];

  groups.forEach((group, index) => {
    const barHeight = (group.value / 100) * 110;
    const x = 70 + index * 110;
    const y = 150 - barHeight;
    const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    rect.setAttribute("x", x);
    rect.setAttribute("y", y);
    rect.setAttribute("width", "40");
    rect.setAttribute("height", barHeight);
    rect.setAttribute("fill", group.color);
    svg.appendChild(rect);

    const label = document.createElementNS("http://www.w3.org/2000/svg", "text");
    label.setAttribute("x", x + 20);
    label.setAttribute("y", 168);
    label.setAttribute("text-anchor", "middle");
    label.setAttribute("font-size", "11");
    label.setAttribute("fill", "#111");
    label.textContent = group.label;
    svg.appendChild(label);
  });

  container.appendChild(svg);
}

window.addEventListener("DOMContentLoaded", () => {
  renderLineChart("tigerChart", tigerData, "#111");
  renderForestChart();
  renderComparisonChart();
});
