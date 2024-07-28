<template>
    <div class="u">
        <!-- <img src="../assets/img/2.gif" alt="miami__background.png"> -->
        <img src="../assets/img/miami__background.png" alt="">
        <!-- <div class="dark"></div> -->
    </div>
</template>

<style lang="scss">
.u {
    position: relative;
    width: 100%;
    overflow-x: hidden;
    overflow-y: hidden;

    img {
        width: 100%;
        display: block;
        opacity: 0.5;
        /* Убедитесь, что изображение блочный элемент */
    }

    .dark {
        width: 150%;
        height: 63%;

        position: absolute;
        bottom: -33%;
        left: 50%;
        /* Центрируем элемент по горизонтали */
        transform: translateX(-50%);
        /* Смещаем элемент на половину его ширины влево */

        z-index: 5;

        background: #000;
        filter: blur(70px);
    }
}

@media (max-width:1440px) {
    .u {
        img {
            transform: scale(1.5);
        }
    }
}
@media (max-width:1000px) {
    .u {
        img {
            transform: scale(1.9);
        }
        .dark{
            height: 20% !important;
        }
    }
}

@media (max-width:750px) {
    .u {
        img {
            transform: scale(3);
        }
        .dark{
            height: 20% !important;
        }
    }
}

</style>