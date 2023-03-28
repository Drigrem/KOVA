const ftnEl = document.getElementById('.title__about')

function fadeIn() {
    ftnEl.forEach(element => {
      if (isElementView(element)) {
        element.style.opacity = 1;
        element.style.transform = 'translateY(0px)';
      }
    });
  }

function isElementView(element) {
    const rect = element.getBoundingClientRect()
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
      );
}

window.addEventListener('scroll', fadeIn);