function createParticles() {
  const layer = document.querySelector('.hero__particle-layer');
  if (!layer) return;
  for (let i = 0; i < 16; i += 1) {
    const particle = document.createElement('span');
    particle.className = 'hero__particle';
    particle.style.left = `${Math.random() * 100}%`;
    particle.style.top = `${Math.random() * 100}%`;
    particle.style.animationDelay = `${Math.random() * 4}s`;
    particle.style.opacity = `${0.3 + Math.random() * 0.6}`;
    layer.appendChild(particle);
  }
}

function addTiltEffect() {
  const cards = document.querySelectorAll('.tilt-card');
  cards.forEach((card) => {
    card.addEventListener('pointermove', (event) => {
      const rect = card.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;
      const rotateY = ((x / rect.width) - 0.5) * 10;
      const rotateX = ((0.5 - (y / rect.height))) * 10;
      card.style.transform = `perspective(900px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
    });
    card.addEventListener('pointerleave', () => {
      card.style.transform = '';
    });
  });
}

window.addEventListener('DOMContentLoaded', () => {
  createParticles();
  addTiltEffect();
});
