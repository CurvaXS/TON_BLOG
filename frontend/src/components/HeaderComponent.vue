<template>
    <header>
        <div class="header__wrapper">

            <!-- <div class="header__logo">
                
                <div class="logo"></div>
                <p class="logo__text">
                    Lorem<span>Ipsum</span>
                </p>
            </div> -->


            <div class="header__nav">
                <img src="../assets/img/logo.png" alt="">
                <nav>
                    <RouterLink to="/">Home</RouterLink>
                    <RouterLink to="/about">About</RouterLink>
                    <RouterLink to="/about">About</RouterLink>
                    <a href="#faq">FAQ</a>

                </nav>

                <div class="nav__more">
                    <div class="header__connect-wallet" id="connect">
                    </div>
                    <!--  <div class="dropdown">
                        <div class="dropdown__click">
                            <p>More</p> <span> < </span>
                        </div>

                        <ul class="dropdown-menu" style="">
                    <RouterLink to="/" class="dropdown-item">Home</RouterLink>
                    <RouterLink to="/about" class="dropdown-item">About</RouterLink>
                    <RouterLink to="/about" class="dropdown-item">About</RouterLink>
                    <RouterLink to="/about" class="dropdown-item">About</RouterLink>
                  </ul> 
                    </div>-->

                </div>
            </div>
            <!-- 
            <div class="header__switch-lang">
                <img src="../assets/img/Web.png" alt="">
                <p>Eng</p>
            </div> -->


        </div>
    </header>
</template>

<script setup>
import { onMounted } from 'vue';
import { RouterLink, RouterView } from 'vue-router'

import { TonConnectUI } from '@tonconnect/ui';

onMounted(() => {
    document.addEventListener('DOMContentLoaded', () => {
        new TonConnectUI({
            manifestUrl: './tonconnect-manifest.json',
            buttonRootId: 'connect',
        });
    });
});
</script>