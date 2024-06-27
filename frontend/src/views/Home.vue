<script setup>
import { RouterLink, RouterView } from 'vue-router'

// import 'https://unpkg.com/@tonconnect/ui@latest/dist/tonconnect-ui.min.js';

// const tonConnectUI = new TON_CONNECT_UI.TonConnectUI({
//   manifesturl: 'https://<YOUR_APP_URL>/tonconnect-manifest.json',
//   buttonRootId: '<YOUR CONNECT BUTTON ANCHOR ID>'
// })




</script>

<template> 
      <div class="wrapper">
        <header>
          <div class="header__wrapper">

            <div class="header__logo">
              <!-- <img src="#" alt="logo" class="logo" /> -->
              <div class="logo"></div>
              <p class="logo__text">
                Lorem<span>Ipsum</span>
              </p>
            </div>


            <div class="header__nav">
              <nav>
                <RouterLink to="/">Home</RouterLink>
                <RouterLink to="/about">About</RouterLink>
                <RouterLink to="/about">About</RouterLink>
                <RouterLink to="/about">About</RouterLink>
              </nav>

              <div class="nav__more">

                <div class="dropdown">
                  <div class="dropdown__click">
                    <p>More</p> <span><</span>
                  </div>
                
                  <!-- <ul class="dropdown-menu" style="">
                    <RouterLink to="/" class="dropdown-item">Home</RouterLink>
                    <RouterLink to="/about" class="dropdown-item">About</RouterLink>
                    <RouterLink to="/about" class="dropdown-item">About</RouterLink>
                    <RouterLink to="/about" class="dropdown-item">About</RouterLink>
                  </ul> -->
                </div>

              </div>
            </div>
            
            <div class="header__switch-lang">
              <img src="../assets/img/Web.png" alt="">
              <p>Eng</p>
            </div>
            
            <div class="header__connect-wallet">
              <p>Connect wallet</p>
            </div>
          </div> 
        </header>
        <img class="header__background" src="../assets/img/header__background.png" alt="">
      </div>
</template>




