<template>
    <header>
        <div class="header__wrapper">
            <div class="header__nav">

                <img src="../assets/img/logo.png" alt="">
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