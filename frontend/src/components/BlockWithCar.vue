<template>
    <div class="main__block-car">

        <div class="tablets">
            <HorizontalTablet class="first-h"></HorizontalTablet>
            <HorizontalTablet class="second-h"></HorizontalTablet>
            <HorizontalTablet class="third-h"></HorizontalTablet>
            <HorizontalTablet class="fourth-h"></HorizontalTablet>
            <VerticalTablet class="first-v"></VerticalTablet>
            <VerticalTablet class="second-v"></VerticalTablet>
        </div>

        <div class="car">
            <div class="smoke"></div>
            <img src="../assets/img/car.png" alt="">
        </div>
        <div class="lights-wrapper">
            <div class="lights">
                <!-- <div class="light"></div>
                    <div class="light"></div>
                -->
                <img src="../assets/img/car__blur.png" alt="">
            </div>

        </div>

    </div>
</template>

<script setup>
import HorizontalTablet from './Tablets/HorizontalTablet.vue'
import VerticalTablet from './Tablets/VerticalTablet.vue'

</script>

<style lang="scss">
.main__block-car {
    position: relative;

    margin-top: 117px;

    width: 100%;
    min-height: 1595px;

    background: url(/src/assets/img/miami__background-3.png) no-repeat center;
    background-size: cover;
    background-position: bottom;

    .tablets {
        position: relative;

        .first-h {
            position: absolute;
            // padding-top: 30px;
            top: 30px;
            z-index: 10;

            .midstream {
                width: 581px;
            }

            .loops {
                width: 377px;
                margin-left: 135px;
            }

            .table-hor {
                margin-left: 110px;
                width: 430px;
                height: 114px;
            }
        }

        .second-h {
            padding-top: 300px;

            .midstream {
                width: 238px;
                margin-bottom: -63px;
            }

            .loops {
                display: none;
            }

            .table-hor {
                margin-left: 5px;
                width: 220px;
                height: 114px;

                transform-origin: center;
            }
        }

        .third-h {
            // position: absolute;
            margin-top: 230px;
            display: flex;
            flex-direction: column;
            flex-wrap: nowrap;
            align-items: flex-end;

            .midstream {
                width: 450px;
            }

            .loops {
                width: 377px;
                margin-right: 40px;
            }

            .table-hor {
                margin-right: 5px;
                height: 430px;
                height: 114px;
            }
        }

        .fourth-h {
            margin-top: 170px;
            padding-bottom: 30px;
            display: flex;
            flex-direction: column;
            flex-wrap: nowrap;
            align-items: flex-end;

            .midstream {
                width: 303px;
            }

            .loops {
                width: 277px;
                margin-right: 25px;
            }

            .table-hor {
                margin-right: 5px;
                width: 303px;
                height: 114px;
            }
        }

        .first-v {
            position: absolute;
            top: 30px;
            right: 0;
        }

        .second-v {
            position: absolute;
            top: 1030px;
            left: 100px;

            flex-direction: column-reverse !important;
            .midstream{
                display: block;

                width: 257px;
                height: 11px;

                margin-left: -109px;

                background-color: rgb(30, 33, 38);
            }

            .loops-right {
                margin-top: 0;
                width: 100px;
                height: 23px;

                display: flex;
                flex-direction: row;
                justify-content: space-between;

                .loop {
                    width: 10px;
                    height: 23px;
                    background: rgb(30, 33, 38);
                }

                .loop:nth-child(1) {
                    background: transparent;
                }
            }

            .table {
                height: 255px;
                width: 123px;

                p {
                    font-size: 27px;
                    padding: 10px;
                }
            }
        }
    }

    .car {
        position: absolute;

        bottom: 0px;
        left: calc((100% - 71%) / 2);

        width: 80%;

        z-index: -1;

        img {
            width: 100%;
        }
    }

    .lights-wrapper {
        position: relative;
        bottom: 0;
        width: 100%;

        .lights {
            position: absolute;
            top: -428px;
            width: 80%;
            /* left: 14.5%; */
            left: 10%;
            z-index: -2;
            transform: rotate(-2.5deg);
            animation: flicker 1.5s infinite;

            img {
                width: 100%;
            }

            // display: flex;
            // align-items: center;
            // justify-content: space-between;

            // .light {
            //     width: 110px;
            //     height: 120px;
            //     background: radial-gradient(50% 50% at 50% 50%, rgba(255, 85, 0, 0.838), rgba(0, 0, 0, 0) 100%);
            //     border-radius: 5px;
            // }
        }
    }
}

@keyframes flicker {
    0% {
        opacity: 1;
    }

    50% {
        opacity: 0.5;
    }

    100% {
        opacity: 1;
    }
}
</style>