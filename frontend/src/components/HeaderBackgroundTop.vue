<template>
    <div class="u">
        <!-- <img src="../assets/img/2.gif" alt="miami__background.png"> -->
        <!-- <h1>WAY</h1> -->
        <div class="socials">

            <a href="https://x.com/token_way">
                <img src="../assets/img/twitter_elon musk_twitter new logo_icon.png" alt="">
            </a>

            <a href="https://t.me/token_way">
                <img src="../assets/img/telegram_plane_icon.png" alt="">
            </a>

        </div>
        <svg>
            <symbol id="s-text">
                <text text-anchor="middle" x="50%" y="60%">WAY</text>
            </symbol>
            <g class="g-ants">
                <use href="#s-text" class="text-copy"></use>
                <use href="#s-text" class="text-copy"></use>
                <use href="#s-text" class="text-copy"></use>
                <use href="#s-text" class="text-copy"></use>
                <use href="#s-text" class="text-copy"></use>
            </g>
        </svg>
        <img class="miami__background" src="../assets/img/miami__background.png" alt="">
        <!-- <div class="dark"></div> -->
    </div>
</template>

<style lang="scss">
.u {
    position: relative;
    width: 100%;
    overflow-x: hidden;
    overflow-y: hidden;

    .socials {
        position: absolute;
        top: 32px;
        right: 50px;

        width: 100px;
        height: 64px;

        z-index: 3000;

        border-radius: 20px;
        backdrop-filter: blur(20px);
        background: rgba(255, 255, 255, 0.5);

        display: flex;
        justify-content: space-around;
        align-items: center;

        a {
            width: 25px;
            position: relative;
            z-index: 3001;

            img {
                // max-width: 64px;
                // max-height: 64px;
                position: relative;
                z-index: 3002;
                width: 25px;
            }
        }

    }

    h1 {
        text-align: center;
        font-family: 'DrukWideCyr-Bold';
        font-size: 60px;
        position: absolute;

        top: calc((100% - 70px)/2);
        left: calc((100% - 176px)/2);
    }

    svg {
        display: block;
        font-family: 'DrukWideCyr-Bold';
        font-size: 100px;
        width: 100%;
        height: 100%;
        margin: 0 auto;
        position: absolute;
    }

    .text-copy {
        fill: none;
        stroke: white;
        stroke-dasharray: 6% 29%;
        stroke-width: 5px;
        stroke-dashoffset: 0%;
        animation: stroke-offset 5.5s infinite linear;
    }

    .text-copy:nth-child(1) {
        stroke: #4D163D;
        animation-delay: -1s;
    }

    .text-copy:nth-child(2) {
        stroke: #840037;
        animation-delay: -2s;
    }

    .text-copy:nth-child(3) {
        stroke: #BD0034;
        animation-delay: -3s;
    }

    .text-copy:nth-child(4) {
        stroke: #BD0034;
        animation-delay: -4s;
    }

    .text-copy:nth-child(5) {
        stroke: #FDB731;
        animation-delay: -5s;
    }

    @keyframes stroke-offset {
        100% {
            stroke-dashoffset: -35%;
        }
    }

    .miami__background {
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
        .miami__background {
            transform: scale(1.5);
        }

        .socials {
            top: 45px;
            right: 10px;

            width: 70px;
            height: 44px;

            a {
                width: 18px;

                img {
                    width: 18px;
                }
            }

        }
    }
}

@media (max-width:1250px) {
    .u {
        .socials {
            width: 46px;
            height: 93px;
            flex-direction: column;
        }
    }
}

@media (max-width:1000px) {
    .u {
        svg {
            font-size: 70px;
            height: 80%;
        }

        .miami__background {
            transform: scale(1.9);
        }

        .dark {
            height: 20% !important;
        }
    }
}
@media (max-width:900px) {
    .u {
        .socials {
           top: 100px;
        }
    }
}
@media (max-width:770px) {
    .u {
        .socials {
           top: 45px;
        }
    }
}
@media (max-width:750px) {
    .u {
        svg {
            font-size: 50px;
            height: 70%;
        }

        .miami__background {
            transform: scale(3);
        }

        .dark {
            height: 20% !important;
        }
    }
}

@media (max-width:500px) {
    .u {
        svg {
            font-size: 50px;
            height: 60%;
        }
    }
}
@media (max-width:450px) {
    .u {
        .socials {
           display: none;
        }
    }
}
</style>