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

            <div class="lights-wrapper">
                <div class="lights">
                    <div class="light"></div>
                    <div class="light"></div>
                </div>
            </div>

            <div class="smoke"></div>

            <img src="../assets/img/car.png" alt="">

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
    min-height: 1566px;

    background: url("../assets/img/miami__background-3.png") no-repeat center;
    background-size: cover;

    .tablets {
        position: relative;

        .first-h {
            padding-top: 30px;

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
            margin-top: 95px;

            .midstream {
                width: 220px;
            }

            .loops {
                width: 170px;
                margin-left: 30px;
            }

            .table-hor {
                margin-left: 5px;
                width: 231px;
                height: 114px;
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
            top: 430px;
            left: 0;

            flex-direction: row !important;
        }
    }

    .car {
        position: absolute;
        bottom: 113px;
        left: -9px;

        .lights-wrapper {
            position: relative;

            .lights {
                position: absolute;
                top: 315px;
                left: 237px;
                width: 569px;
                transform: rotate(-2.5deg);

                animation: flicker 1.5s infinite;

                display: flex;
                align-items: center;
                justify-content: space-between;

                .light {
                    width: 110px;
                    height: 120px;
                    background: radial-gradient(50% 50% at 50% 50%, rgba(255, 85, 0, 0.838), rgba(0, 0, 0, 0) 100%);
                    border-radius: 5px;
                }
            }
        }


        img {
            width: 1000px;
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