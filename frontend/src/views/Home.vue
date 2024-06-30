<template>
      <div class="wrapper">
        <HeaderComponent></HeaderComponent>
        <HeaderBanner></HeaderBanner>
        <img class="header__background-line" src="../assets/img/header__background-line.png" alt="">
        <img class="header__background" src="../assets/img/header__background.png" alt="">
        <div class="block__partners"></div>
        <MainSlider></MainSlider>
        <div class="line"></div>
        <div class="line-footer"></div>
        <footer>
          <div class="footer__wrapper">
            <h2>SweetDesign</h2>
            <p>made with love <3 </p>
          </div>
        </footer>
      </div>
</template>

<script setup>
import HeaderComponent from '../components/HeaderComponent.vue';
import HeaderBanner from '../components/HeaderBanner.vue';
import MainSlider from '../components/MainSlider.vue';
</script>