<template>
  <div class="body">

    <!-- hamburger -->
    <input type="checkbox" id="navi-toggle" class="checkbox" />
    <label for="navi-toggle" class="button">
      <span class="icon">&nbsp;</span>
    </label>
    <div class="background">&nbsp;</div>

    <!-- nav -->
    <nav class="nav">
      <ul class="list">
        <li class="item"> <a class="link"> Link 1 </a> </li>
        <li class="item"> <a class="link"> Link 2 </a> </li>
        <li class="item"> <a class="link"> Link 4 </a> </li>
        <li class="item"> <a class="link"> Link 5 </a> </li>
        <li class="item"> <a class="link"> Link 6 </a> </li>
      </ul>
    </nav>

    <div class="socials">

      <a href="https://x.com/token_way">
        <img src="../assets/img/twitter_elon musk_twitter new logo_icon.png" alt="">
      </a>

      <a href="https://t.me/token_way">
        <img src="../assets/img/telegram_plane_icon.png" alt="">
      </a>

    </div>

  </div>
</template>

<style lsng="scss" scoped>
/* page styling */
.body {
  background: linear-gradient(90deg, #7bed9f, #3498db);
}

.socials {
  display: none;
  animation: out 0.8s ease-in-out;
}

section {
  max-width: 900px;
  margin: 0 auto;
}

section h1 {
  font-size: 46px;
  text-align: center;
}

section p {
  font-size: 26px;
  text-align: center;
}

/* hamburger */
.checkbox {
  display: none;
}

.button {
  position: relative;
  background-color: white;
  height: 3rem;
  width: 3rem;
  border-radius: 25%;
  position: fixed;
  top: 8px;
  right: 16px;
  z-index: 8000;
  box-shadow: 0 1rem 3rem black;
  text-align: center;
  cursor: pointer;
}

.background {
  height: 2rem;
  width: 2rem;
  border-radius: 50%;
  position: fixed;
  top: 8px;
  right: 16px;
  background: linear-gradient(90deg, rgb(188, 62, 108) 0%, rgb(120, 16, 54) 50%, rgb(188, 62, 108) 100%);
  z-index: 7000;

  transition: transform 0.8s cubic-bezier(0.86, 0, 0.07, 1);
}

.nav {
  height: 100vh;
  position: fixed;
  top: 0;
  right: -100vh;
  z-index: 7998;
  opacity: 0;
  width: 0;
  transition: all 0.8s;
}

.list {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  list-style: none;
  text-align: center;
  width: 100%;
  z-index: 7999;
}

.item {
  margin: 1rem;
  font-size: 36px;
}

.link:link,
.link:visited {
  display: inline-block;
  font-size: 3rem;
  font-weight: 300;
  padding: 1rem 2rem;
  color: white;
  text-decoration: none;
  text-transform: uppercase;
  background-image: linear-gradient(120deg,
      transparent 0%,
      transparent 50%,
      white 50%);
  background-size: 220%;
  transition: all 0.4s;
}

.link:hover,
.link:active {
  color: lightgreen;
  cursor: pointer;
}

/* functionality */
.checkbox:checked~.background {
  transform: scale(80);
}

.checkbox:checked~.nav {
  opacity: 1;
  width: 100%;
  right: 0;
}

.checkbox:checked~.socials {
  animation: in 0.8s ease-in-out;

  display: block;

  position: absolute;
  top: 8px;
  left: -7px;

  width: 100px;
  height: 64px;

  z-index: 30000;

  border-radius: 20px;
  backdrop-filter: blur(20px);
  background: rgba(255, 255, 255, 0.85);

  display: flex;
  justify-content: space-around;
  align-items: center;

  a {
    width: 25px;
    position: relative;
    z-index: 3001;

    img {
      max-width: 64px;
      max-height: 64px;
      position: relative;
      z-index: 3002;
      width: 25px;
    }
  }

}

@keyframes in{
  0%{
    opacity: 0;
  }
  100%{
    opacity: 1;
  }
}
@keyframes out{
  0%{
    opacity: 1;
  }
  100%{
    opacity: 0;
  }
}
/*  */
/* styling hamb ICON */
.icon {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.icon,
.icon::before,
.icon::after {
  width: 2rem;
  height: 2px;
  background-color: gray;
  display: inline-block;
}

.icon::before,
.icon::after {
  content: "";
  position: absolute;
  left: 0;
  transition: all 0.2s;
}

.icon::before {
  top: -0.8rem;
}

.icon::after {
  top: 0.8rem;
}

.button:hover icon:before {
  top: -1rem;
}

.button:hover icon::after {
  top: 1rem;
}

.checkbox:checked+.button .icon {
  background-color: transparent;
}

.checkbox:checked+.button .icon::before {
  top: 0;
  transform: rotate(135deg);
}

.checkbox:checked+.button .icon::after {
  top: 0;
  transform: rotate(-135deg);
}

/* @media (max-width: 450px) {
  .socials {
        
        position: absolute;
        top: 32px;
        right: 50px;

        width: 100px;
        height: 64px;

        z-index: 3000;

        border-radius: 20px;
        backdrop-filter: blur(20px);
        background: rgba(255, 255, 255, 0.5);

        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;

        a {
            width: 25px;
            position: relative;
            z-index: 3001;

            img {
                max-width: 64px;
                max-height: 64px;
                position: relative;
                z-index: 3002;
                width: 25px;
            }
        }

    }
} */
</style>