<template>
  <div class="wrapper">
    <HeaderComponent></HeaderComponent>
    <HeaderPresale></HeaderPresale>
    <!-- <HeaderBanner></HeaderBanner> -->
    <!-- <img class="header__background-line" src="../assets/img/header__background-line.png" alt=""> -->
    <!-- <img class="header__background-top" src="../assets/img/miami__background.png" alt=""> -->


    <!-- <div class="block__partners"></div>
        <MainSlider></MainSlider> -->
    <HeaderBackgroundTop class="header__background-top"></HeaderBackgroundTop>
    <!-- <img class="header__background-top" src="../assets/img/miami__background.png" alt=""> -->
    <img class="header__background" src="../assets/img/header__background.png" alt="">

    <MainBlock></MainBlock>

    <div class="gradient-background">
      <div class="scrolling-text">
        <p>
          $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY
          $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY $WAY
        </p>
      </div>
    </div>

    <BlockWithCar></BlockWithCar>


    <div class="line"></div>
    <div class="block_faq">
      <div class="faq__wrapper">
        <h2 id="faq">FAQ</h2>
        <h1 class="faq__title">HAVE ANY QUESTIONS?</h1>
        <div class="accordion__wrapper">
          <Accordion></Accordion>
        </div>

      </div>
    </div>
    <div class="line-footer"></div>
    <footer>
      <div class="footer__wrapper">
        <div class="socials-footer">
          <a href="https://x.com/token_way">
            <img src="../assets/img/twitter_elon musk_twitter new logo_icon.png" alt="">
          </a>
          <a href="https://t.me/token_way">
            <img src="../assets/img/telegram_plane_icon.png" alt="">
          </a>
        </div>
        <h2>SweetDesign</h2>
        <p>made with love <3 </p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import HeaderComponent from '../components/HeaderComponent.vue';
import HeaderPresale from '../components/HeaderPresale.vue';

import HeaderBanner from '../components/HeaderBanner.vue';
import MainSlider from '../components/MainSlider.vue';
import HeaderBackgroundTop from '../components/HeaderBackgroundTop.vue';

import MainBlock from '../components/MainBlock.vue';
import BlockWithCar from '../components/BlockWithCar.vue';
import Accordion from '../components/Accordion.vue';
</script>

<style scoped>
.faq__wrapper {
  padding: 100px 0;
  background: url('../assets/img/faq__back.png') center;
  background-size: cover;
}

#faq {
  padding-top: 60px;
  text-align: center;
  font-family: Inter;
  color: rgb(188, 62, 108);
  font-size: 30px;
  font-weight: 700;
}

.faq__title {
  text-align: center;
  font-family: Inter;
  color: rgb(255, 255, 255);
  font-size: 40px;
  font-weight: 700;
}

.accordion__wrapper {
  max-width: 732px;
  margin: 39px auto 0;

  padding-bottom: 73px;
}

@keyframes textScroll {
  0% {
    transform: translateX(-5%);
  }

  50% {
    transform: translateX(0);
  }

  100% {
    transform: translateX(-5%);
  }

  /* 75% {
    transform: translateX(0);
  }
  100%{
    transform: translateX(-50%);
  } */
}

.gradient-background {
  width: 100%;
  height: 100px;
  background: rgba(56, 139, 255, 0.56);

  display: flex;
  align-items: center;
  position: relative;
  overflow: hidden;

  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-weight: 700;
  font-size: 32px;
}

.gradient-background .scrolling-text {
  position: absolute;
  white-space: nowrap;
  /* animation: textScroll 45s linear infinite; */
  font-size: 2em;
  color: white;
}

@media (max-width: 500px) {
  .gradient-background {
    margin-top: -122px;
    height: 50px;
    font-size: 20px;
  }

  .gradient-background .scrolling-text {
    animation: textScroll 30s linear infinite;
  }
}

.socials-footer {
  width: 100px;
  height: 64px;

  margin: 30px auto 20px;

  border-radius: 20px;
  backdrop-filter: blur(20px);
  background: rgba(255, 255, 255, 0.75);

  display: flex;
  justify-content: space-around;
  align-items: center;
}

.socials-footer a {
  width: 25px;
  position: relative;
}

.socials-footer a img {
  width: 25px;
}

@media (max-width:1440px) {
  .socials-footer {
    width: 70px;
    height: 44px;
  }

  .socials-footer a,
  .socials-footer a img {
    width: 18px;
  }
}

@media (max-width:1250px) {
  .socials-footer {
    /* width: 46px;
    height: 93px; */
  }
}
</style>