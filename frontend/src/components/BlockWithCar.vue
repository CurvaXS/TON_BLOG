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

        <div class="bg-absolute">
            <BG></BG>
        </div>


        <!-- <div class="car car-st">
            <div class="smoke"></div>
            <img src="../assets/img/car-crop.png" alt="">
        </div>

        <div class="lights car-st">
            <img src="../assets/img/car__blur.png" alt="">
        </div> -->

        <!-- <div class="black-bc"></div> -->

    </div>
</template>

<script setup>
import HorizontalTablet from './Tablets/HorizontalTablet.vue'
import VerticalTablet from './Tablets/VerticalTablet.vue'
import BG from '../components/BackgroundForBlockWithCar/BG.vue'
</script>

<style lang="scss">
.main__block-car {
    position: relative;

    margin-top: 0;

    width: 100%;
    min-height: 1595px;

    // background: url('../assets/img/miami__background-4.gif') no-repeat center;
    // background-size: cover;
    // background-position: bottom;

    .black-bc {
        position: absolute;
        width: 100%;
        height: 100%;
        background-color: rgb(0, 0, 0, 0.65);
        z-index: 0;
        top: 0;
    }

    .bg-absolute {
        position: absolute;
        top: 0;
        height: 100%;
    }

    .tablets {
        position: relative;
        z-index: 2010;

        .first-h {
            position: absolute;
            // padding-top: 30px;
            top: 30px;
            z-index: 2010;

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

                p[id="1"] {
                    display: block;
                }
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

                p[id="2"] {
                    display: block;
                }
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

                p[id="3"] {
                    display: block;
                }
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
                height: 188px;

                p[id="4"] {
                    display: block;
                }
            }
        }

        .first-v {
            position: absolute;
            top: 30px;
            right: 0;

            p[id="1"] {
                display: block;
            }
        }

        .second-v {
            position: absolute;
            top: 1030px;
            left: 100px;

            flex-direction: column-reverse !important;

            .midstream {
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
                height: 180px;
                width: 153px;

                p {
                    max-width: 90%;
                    font-size: 12px;
                    padding-left: 5px;

                    writing-mode: horizontal-tb;
                }

                p[id="2"] {
                    display: block;
                }
            }
        }
    }

    .car {
        z-index: 1;
        // max-height: 22em;
        // overflow: hidden;
    }

    .lights {
        z-index: 0;
        // max-height: 350px;
        // overflow: hidden;
    }

    .car-st {
        position: absolute;

        bottom: 0em;
        left: 50%;
        transform: translateX(-44%);

        animation: flicker 1.5s infinite;


        width: 33%;

        img {
            width: 100%;
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

@media (max-width: 1440px) {
    .main__block-car {
        .car-st {
            overflow: hidden;
            left: 50%;
            width: 478px;

            transform: translateX(-44%);

            img {
                display: block;
            }
        }
    }
}

@media (max-width: 1280px) {
    .main__block-car {}
}

@media (max-width: 770px) {
    .main__block-car {
        // background-size: 200%;
        min-height: 1000px;
        margin-top: 0;

        .tablets {
            .first-h {
                top: 20px !important;
                z-index: 5 !important;

                .midstream {
                    width: 300px;
                    height: 9px;
                }

                .loops {
                    width: 250px;
                    margin-left: 40px;
                }

                .table-hor {
                    margin-left: 38px;
                    width: 270px;
                    height: 85px;
                }

                .table-hor p {
                    font-size: 22px;
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
                margin-top: 130px;


                .midstream {
                    width: 300px !important;
                }

                .loops {
                    width: 210px;
                    margin-right: 40px;
                }

                .table-hor {
                    margin-right: 5px;
                    height: 430px;
                    height: 114px;
                }
            }

            .fourth-h {
                display: none;
            }

            .first-v {
                position: absolute;
                top: 30px;
                right: 0;
            }

            .second-v {
                position: absolute;
                top: 400px;
                left: 100px;

                .midstream {
                    width: 200px;
                    height: 11px;

                    margin-left: -109px;
                }

                .loops-right {
                    width: 80px;
                }

                .table {
                    height: 180px;
                    width: 153px;

                    p {
                        font-size: 11px;
                        padding: 10px;
                    }
                }
            }
        }

        .car-st {
            width: 295px;
            transform: translateX(-45.5%);
        }
    }
}

@media (max-width: 500px) {
    .main__block-car {
        // background-size: 200%;
        min-height: 1000px;
        // margin-top: -75px;

        .tablets {
            .first-h {
                top: 20px !important;
                z-index: 5 !important;

                .midstream {
                    width: 200px;
                    height: 9px;
                }

                .loops {
                    width: 140px;
                }

                .table-hor {
                    margin-left: 18px;
                    width: 220px;
                    height: 85px;
                }

                .table-hor p {
                    font-size: 16px;
                }
            }

            .third-h {
                .midstream {
                    width: 150px !important;
                }
                .loops {
                    width: 100px;
                }
                .table-hor{
                    width: 150px;
                }
            }

            .first-v {
                position: absolute;
                top: 30px;
                right: 0;

                .loops-right {
                    height: 150px !important;
                }

                .table {
                    width: 50px;
                    height: 250px;

                    p {
                        font-size: 16px;
                    }
                }
            }

            .second-v {
                left: 15px;

                .table {
                    p {
                        line-height: 15px !important;
                    }
                }
            }
        }

    }
}
</style>