<template>
    <div class="header__presale">
        <!--<img class="particles__logo" src="../assets/img/particles__logo.png" alt=""> -->
        <div class="particle__logo">
            <img src="../assets/img/particles__logo.png" alt="">
        </div>
        <div class="lighting"></div>
        <Stripes></Stripes>
        <!-- <img class="stripes" src="../assets/img/Stripe.png" alt=""> -->
        <!-- <img class="darken" src="../assets/img/darken-top.png" alt=""> -->
    </div>
</template>

<script setup>
import Stripes from './Stripes.vue'
</script>

<style scoped lang="scss">
.header__presale {
    position: relative;

    .lighting {
        position: absolute;
        left: -28px;
        top: 87.11px;

        width: 262.25px;
        height: 351.6px;

        z-index: 9;

        transform: rotate(60.00deg);

        // border: 6px solid red;

        filter: blur(189.97px);
        background: linear-gradient(132.90deg,
                rgba(195, 174, 255, 0.2) 26.834%,
                rgba(92, 62, 188, 0.2) 26.842%,
                rgba(62, 154, 222, 0.2) 26.85%,
                rgba(51, 100, 229, 0.2) 108.423%);
    }
}

.particle__logo {
    // position: absolute;
    // top: 138px;
    // left: -58px;

    // z-index: 10;

    // width: 150px;
    // height: 150px;

    // border-radius: 50%;
    // border: 2.5px solid rgb(255, 255, 255);
    // backdrop-filter: blur(33.6px);
    // background: transparent;

    // display: flex;
    // justify-content: center;
    // align-items: center;

    // transform: rotate(-26deg);
    display: none;
}

@media (max-width:1100px) {
    .header__presale{
       padding-top: 180px
    }
}

@media (max-width:770px) {
    .header__presale{
        padding-top: 130px
    }
}
@media (max-width:450px) {
    .header__presale{
        padding-top: 100px
    }
}
@media (max-width:400px) {
    .header__presale{
        padding-top: 70px;
    }
}
</style>