<template>
      <div class="wrapper">
        <HeaderComponent></HeaderComponent>
        <HeaderPresale></HeaderPresale>
        <!-- <HeaderBanner></HeaderBanner> -->
        <!-- <img class="header__background-line" src="../assets/img/header__background-line.png" alt=""> -->
        <!-- <img class="header__background-top" src="../assets/img/miami__background.png" alt=""> -->
       
        
        <!-- <div class="block__partners"></div>
        <MainSlider></MainSlider> -->

        <MainBlock></MainBlock>
        <BlockWithCar></BlockWithCar>

        <div class="header__background-top"></div>
        <img class="header__background" src="../assets/img/header__background.png" alt="">

        <div class="line"></div>
        <div class="block_faq">
          <div class="faq__wrapper">
            <h2 id="faq">FAQ</h2>
            <h1 class="faq__title">Lorem ipsum dolor amet</h1>
            <div class="accordion__wrapper">
              <Accordion></Accordion>
            </div>
            
          </div>
        </div>
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
import HeaderPresale from '../components/HeaderPresale.vue';

import HeaderBanner from '../components/HeaderBanner.vue';
import MainSlider from '../components/MainSlider.vue';

import MainBlock from '../components/MainBlock.vue';
import BlockWithCar from '../components/BlockWithCar.vue';
import Accordion from '../components/Accordion.vue';
</script>

<style scoped>
#faq{
  text-align: center;
  font-family: Inter;
  color: rgb(110, 139, 253);
  font-size: 30px;
  font-weight: 700;
}
.faq__title{
  text-align: center;
  font-family: Inter;
  color: rgb(255, 255, 255);
  font-size: 40px;
  font-weight: 700;
}
.accordion__wrapper{
  max-width: 732px;
  margin: 39px auto 73px;
}
</style>