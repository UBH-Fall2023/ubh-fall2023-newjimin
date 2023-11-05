let cookie = document.getElementById('cookie');
let scoreDisplay = document.querySelector('.score');
let cookies = 0;
let autoClickActive = false;
let upgradeClickActive = false;
let studyingActive = false;
let autoClickInterval; 

function updateScore() {
  scoreDisplay.textContent = `Cookies Earned = ${cookies}`;
}

cookie.addEventListener('click', () => {
  if (upgradeClickActive) {
    cookies += 10; 
  } else {
    cookies++; 
  }
  updateScore();
  if (cookies > 50) {
    changeImg2();
  }
  if (cookies > 100) {
    changeImg3();
  }
  if (cookies > 200) {
    getquote(api_url);
  }
});
function changeImg2() {
  cookie.src = "images/closed_cookie_2.svg";
}

function changeImg3() {
  cookie.src = "images/final_cookie.svg";
}

const createParticle = (x, y) => {
  const cookieClicks = document.querySelector(".cookie-clicks");
  const particle = document.createElement("img");
  particle.setAttribute("src", "images/closed_cookie_1.svg");
  particle.setAttribute("class", "cookie-particle");
  particle.style.left = x + "px";
  particle.style.top = y + "px";
  cookieClicks.appendChild(particle);

  setTimeout(() => {
    cookieClicks.removeChild(particle);
  }, 3000);
}

cookie.addEventListener("click", (e) => {
  createParticle(e.clientX, e.clientY);

});

function cookieClicked() {
  cookies++;
  updateScore();
  if (cookies > 50) {
    changeImg2();
  }
  if (cookies > 100) {
    changeImg3();
  }
  if (cookies > 200) {
    getquote(api_url);
  }
}

document.getElementById('auto-click').addEventListener('click', () => {
  if (cookies >= 100 && !autoClickActive) {
    cookies -= 100;
    autoClickActive = true;
    updateScore();
    startAutoClick();
  }
});

function startAutoClick() {
  autoClickInterval = setInterval(() => {
    cookies += 1; // Perform 100 clicks
    updateScore();
  }, 1000);
}

document.getElementById('upgrade-click').addEventListener('click', () => {
  if (cookies >= 50 && !upgradeClickActive) {
    cookies -= 50;
    upgradeClickActive = true;
    updateScore();
  }
});

document.getElementById('studying-click').addEventListener('click', () => {
  if (cookies >= 500 && !studyingActive) {
    cookies -= 500;
    studyingActive = true;
    updateScore();
    startStudying();
  }
});

function startStudying() {
  location.href = "timer.html"; 
}

updateScore();
const quote = document.getElementById("quote");
const author = document.getElementById("author");
const api_url = "https://api.quotable.io/random";

async function getquote(url){
  const response = await fetch(url);
  var data = await response.json();
  quote.innerHTML = data.content; 
  author.innerHTML = data.author;
}








