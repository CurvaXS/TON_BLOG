<template>
    <div class="main__block">

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
                <div class="item-logo-back"></div>
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



    .main__block-wrapper {
        padding: 500px 0 170px;

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

                z-index: 3;

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

            .item-logo-back {
                position: absolute;
                top: -20%;

                left: calc((100% - 45%) / 2);
                width: 45%;
                padding-top: 45%;

                border-radius: 50%;

                z-index: 2;

                filter: blur(351.8px);
                background: rgba(73, 80, 207, 0.4);
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

@media (max-width: 1100px) {
    .main__block {
        margin-top: 0px;
    }

    .main__block-wrapper {
        padding: 350px 0 0 !important;

        .block__info {
            width: 750px !important;

            h1.name {
                font-size: 45px !important;
            }

            .steps {
                margin-top: 44px;

                .step__line {
                    margin-bottom: 25px;

                    width: 90px !important;
                }

                .item {
                    width: 200px !important;
                    height: 200px !important;

                    background-size: cover !important;
                }

                p {
                    margin-top: 25px;
                    font-size: 23px !important;
                }
            }
        }

        .block__components {
            .item {
                margin-top: 90px !important;

                .component {
                    p.percents {
                        font-size: 40px !important;
                        line-height: 61px;
                    }

                    p.naming {
                        margin-top: 7px;
                        font-size: 25px !important;
                        padding-bottom: 20px;
                    }
                }
            }
        }
    }
}

@media (max-width: 950px) {


    .main__block-wrapper {
        padding: 275px 0 200px !important;

        .block__info {
            width: 750px !important;

            .steps {
                margin-top: 0px !important;
                flex-direction: column;

                .step__item {
                    width: 100%;
                    flex-direction: row !important;
                    justify-content: flex-start !important;
                }

                .step__item:nth-child(3) {
                    flex-direction: row-reverse !important;
                }

                .step__line {
                    transform: rotate(45deg);
                }

                .step__line:nth-child(4) {
                    transform: rotate(-45deg);
                }

                .item {
                    width: 220px !important;
                    height: 220px !important;
                }
            }
        }

        .block__components {
            .item {
                margin-top: 40px !important;

                .component {
                    p.percents {
                        font-size: 25px !important;
                        line-height: 50px;
                    }

                    p.naming {
                        margin-top: 4px;
                        font-size: 20px !important;
                        padding-bottom: 0px;
                    }
                }
            }
        }
    }
}

@media (max-width: 770px) {


    .main__block-wrapper {
        padding: 275px 0 200px !important;

        .block__info {
            width: 500px !important;
        }

        .block__components {
            .item {
                margin-top: 40px !important;

                .component {
                    p.percents {
                        font-size: 25px !important;
                        line-height: 50px;
                    }

                    p.naming {
                        margin-top: 4px;
                        font-size: 20px !important;
                        padding-bottom: 0px;
                    }
                }
            }
        }
    }
}

@media (max-width: 590px) {
    .main__block-wrapper {
        padding: 200px 0 200px !important;
    }
}

@media (max-width: 500px) {

    .main__block-wrapper {
        padding: 150px 0 200px !important;

        .block__info {
            width: 290px !important;

            .steps {
                margin-top: 44px;

                .step__line {
                    margin-bottom: 18px !important;
                    width: 70px !important;
                }

                .item {

                    width: 180px !important;
                    height: 180px !important;

                }

                p {
                    font-size: 18px !important;
                }
            }
        }

        .block__components {
            .item {
                margin-top: 10px !important;

                .component {
                    p.percents {
                        font-size: 10px !important;
                        line-height: 25px !important;
                    }

                    p.naming {
                        margin-top: 1px !important;
                        font-size: 8px !important;
                        padding-bottom: 0px !important;
                    }
                }
            }
        }
    }
}
</style>