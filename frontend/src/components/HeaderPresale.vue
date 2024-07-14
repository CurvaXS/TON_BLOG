<template>
    <div class="header__presale">
        <!-- <img class="particles__logo" src="../assets/img/particles__logo.png" alt=""> -->
        <div class="particle__logo">
            <img src="../assets/img/particles__logo.png" alt="">
        </div>
        <img class="stripes" src="../assets/img/Stripe.png" alt="">
    </div>
</template>

<style scoped lang="scss">
.particle__logo {
    position: absolute;
    top: 138px;
    left: -58px;

    z-index: -1;

    width: 150px;
    height: 150px;

    border-radius: 50%;
    border: 2.5px solid rgb(255, 255, 255);
    backdrop-filter: blur(33.6px);
    background: rgba(217, 217, 217, 0.2);

    display: flex;
    justify-content: center;
    align-items: center;

    transform: rotate(-26deg);

}


</style>