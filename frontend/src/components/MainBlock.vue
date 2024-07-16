<template>
    <div class="main__block">
        <div class="darken"></div>
        <div class="main__block-wrapper">
            <div class="block__info">
                <h1 class="name">LAUNCH ON</h1>
                <Timer></Timer>
                <div class="steps">
                    <div class="step__item">
                        <div class="item">
                            <img src="../assets/img/wallet.png" alt="">
                        </div>
                        <p>Set up wallet</p>
                    </div>
                    <img src="../assets/img/step_line.png" alt="" class="step__line">
                    <div class="step__item">
                        <div class="item">
                            <img src="../assets/img/line_top.png" alt="">

                        </div>
                        <p>x100</p>
                    </div>
                    <img src="../assets/img/step_line.png" alt="" class="step__line">
                    <div class="step__item">
                        <div class="item">
                            <img src="../assets/img/data_base.png" alt="">

                        </div>
                        <p>Rich guy</p>
                    </div>
                </div>
                <button class="btn btn-main">View More</button>
            </div>
            <div class="block__tablets">
                <div class="tablet-horizontal">
                    <HorizontalTablet></HorizontalTablet>
                </div>
                <div class="tablet-vertical">
                    <VerticalTablet></VerticalTablet>
                </div>
            </div>
            <div class="block__components">
                <div class="item">
                    <div class="component">
                        <p class="percents">20%</p>
                        <p class="naming">lorem ipsum</p>
                    </div>
                    <div class="component component-right">
                        <p class="percents">10%</p>
                        <p class="naming">lorem ipsum</p>
                    </div>
                </div>
                <div class="item">
                    <div class="component">
                        <p class="percents">27%</p>
                        <p class="naming">lorem ipsum</p>
                    </div>
                    <div class="component component-right">
                        <p class="percents">33%</p>
                        <p class="naming">lorem ipsum</p>
                    </div>
                </div>
                <div class="item-logo">
                    <svg width="315" height="207" viewBox="0 0 315 207" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M310.035 3.00003L254.386 117.714L66.9308 117.714L5.02781 3L310.035 3.00003Z"
                            fill="#EED1FF" stroke="#EED1FF" stroke-width="6" />
                        <path d="M258.559 144L223.822 205L105.276 205L66.6344 144L258.559 144Z" fill="#EED1FF"
                            stroke="#EED1FF" stroke-width="4" />
                    </svg>
                </div>
            </div>
        </div>

    </div>
</template>

<script setup>
import Timer from './Timer.vue'
import HorizontalTablet from './Tablets/HorizontalTablet.vue'
import VerticalTablet from './Tablets/VerticalTablet.vue'

</script>

<style scoped lang="scss">
.main__block {
    margin-top: -100px;

    width: 100%;
    min-height: 1850px;

    background: url("../assets/img/miami__background-2.png") no-repeat center;
    background-size: cover;

    .darken {
        position: absolute;
        width: 100%;
        height: 282px;
        background: url(../assets/img/darken.png) no-repeat center;
        background-size: cover;
        top: 2250px;
    }

    .main__block-wrapper {
        padding: 170px 0;

        .block__info {
            width: 1045px;
            margin: 0 auto;

            text-align: center;
            font-family: Lato;

            h1.name {
                color: rgb(218, 218, 218);
                font-size: 60px;
                font-weight: 600;
                line-height: 72px;
                margin-bottom: 14px;
            }

            .steps {
                display: flex;
                align-items: center;
                justify-content: space-between;
                margin-top: 44px;

                .step__item {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center
                }

                .step__line {
                    margin-bottom: 25px;
                }

                .item {
                    display: flex;
                    flex-wrap: nowrap;
                    align-items: center;
                    justify-content: center;

                    background: url('../assets/img/step__item-back.png') no-repeat center;

                    width: 235px;
                    height: 235px;

                }

                p {
                    margin-top: 25px;
                    color: rgb(255, 255, 255);
                    font-family: Inter;
                    font-size: 25px;
                    font-weight: 700;
                    line-height: 30px;
                }
            }

            button.btn-main {
                margin: 57px auto 0;
                padding: 16px 24px;

                border-radius: 14px;
                background-color: rgb(109, 40, 217);

                transition: all 0.2s ease-in-out;

                color: #FFF;
            }

            button.btn-main:hover {
                background-color: rgba(108, 40, 217, 0.85);
            }

            button.btn-main:active {
                transform: scale(0.9);
            }


        }

        .block__tablets {
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: -45px;
        }

        .block__components {
            width: 95%;
            margin: 0 auto;
            position: relative;

            .item {
                margin-top: 125px;

                display: flex;
                align-items: center;
                justify-content: space-between;

                color: #eed1ff;
                font-weight: 700;
                font-family: 'DrukWideCyr-Bold';

                .component {
                    width: 33%;
                    border-bottom: 5px solid #eed1ff;

                    p.percents {
                        font-size: 50px;
                        line-height: 61px;
                    }

                    p.naming {
                        margin-top: 7px;
                        font-size: 30px;
                        line-height: 36px;
                        padding-bottom: 20px;
                        text-transform: uppercase;
                    }
                }

                .component-right {
                    text-align: right;
                }
            }

            .item-logo {
                position: absolute;
                top: -20%;

                left: calc((100% - 40%) / 2);
                width: 40%;
                padding-top: 40%;
                /* Это создаст круг */

                display: flex;
                align-items: center;
                justify-content: center;

                border-radius: 50%;
                border: 5px solid rgb(238, 209, 255);
                backdrop-filter: blur(1515151px);
                background: linear-gradient(180.00deg, rgba(142, 71, 140, 0.2), rgba(87, 57, 44, 0.2) 100%);

                svg {
                    position: absolute;
                    width: 75%;
                    height: 100%;

                    top: 0;
                }
            }

            @media (max-width: 1575px) {
                .item-logo {
                    top: -5%;
                }
            }

            @media (max-width: 1375px) {
                .item-logo {
                    top: 0;
                }
            }

            @media (max-width: 1300px) {
                .item {
                    margin-top: 125px;

                    .component {
                        width: 40%;

                        p.percents {
                            font-size: 50px;
                        }

                        p.naming {
                            margin-top: 7px;
                            font-size: 30px;
                            padding-bottom: 20px;
                        }
                    }
                }
            }
        }
    }
}
</style>