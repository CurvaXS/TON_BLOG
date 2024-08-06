<template>
    <header id="top">
        <div class="header__wrapper">
            <div class="header__nav">

                <!-- <img src="../assets/img/logo.png" alt=""> -->
                <div class="logo">
                    <a href="#top">
                        <svg width="40" height="22" viewBox="0 0 324 181" fill="none"
                            xmlns="http://www.w3.org/2000/svg">
                            <path d="M0 0H324L277 102H50L0 0Z" fill="#FFF" />
                            <path d="M56 113H272L240 181H88L56 113Z" fill="#FFF" />
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