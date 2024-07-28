<template>
    <header id="top">
        <div class="header__wrapper">
            <div class="header__nav">

                <!-- <img src="../assets/img/logo.png" alt=""> -->
                <div class="logo">
                    <a href="#top">
                        <svg width="40" height="26.29" viewBox="0 0 315 207" fill="none"
                            xmlns="http://www.w3.org/2000/svg">
                            <path d="M310.035 3.00003L254.386 117.714L66.9306 117.714L5.02763 3L310.035 3.00003Z"
                                fill="#FFF" stroke="#FFF" stroke-width="6" />
                            <path d="M243.83 144L214.738 205L111.695 205L78.8484 144L243.83 144Z" fill="#FFF"
                                stroke="#FFF" stroke-width="4" />
                        </svg>
                    </a>
                </div>

                <nav class="menu">
                    <RouterLink to="/">Home</RouterLink>
                    <RouterLink to="/about">Other</RouterLink>
                    <a href="#faq">FAQ</a>
                </nav>
                <div class="nav__more">
                    <div class="header__connect-wallet" id="connect">
                    </div>
                </div>

                <div class="burger">
                    <BurgerMenu></BurgerMenu>
                </div>
            </div>
        </div>
    </header>
</template>

<script setup>
import { onMounted } from 'vue';
import { RouterLink, RouterView } from 'vue-router'

import BurgerMenu from './BurgerMenu.vue'

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