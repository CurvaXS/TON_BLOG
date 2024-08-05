<template>
    <div class="main__block">

        <div class="main__block-wrapper">
            <div class="block__info">
                <h1 class="name">LAUNCH ON</h1>
                <Timer></Timer>
                <div class="steps">
                    <div class="step__item">
                        <RippleWallet></RippleWallet>
                        <p>Set up wallet</p>
                    </div>
                    <img src="../assets/img/step_line.png" alt="" class="step__line">
                    <div class="step__item">
                        <RippleLineTop></RippleLineTop>
                        <p>x100</p>
                    </div>
                    <img src="../assets/img/step_line.png" alt="" class="step__line">
                    <div class="step__item">
                        <RippleDataBase></RippleDataBase>
                        <p>Rich guy</p>
                    </div>
                </div>
                <button class="btn btn-main">PRE-SALE</button>
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
                <div class="componets__header">
                    <h1>Token way</h1>
                    <div class="item-logo">
                        <svg width="315" height="207" viewBox="0 0 315 207" fill="none"
                            xmlns="http://www.w3.org/2000/svg">
                            <path d="M310.035 3.00003L254.386 117.714L66.9306 117.714L5.02763 3L310.035 3.00003Z"
                                fill="#EED1FF" stroke="#EED1FF" stroke-width="6" />
                            <path d="M243.83 144L214.738 205L111.695 205L78.8484 144L243.83 144Z" fill="#EED1FF"
                                stroke="#EED1FF" stroke-width="4" />
                        </svg>
                    </div>
                </div>
                <div class="item">
                    <div class="component">
                        <p class="percents">30%</p>
                        <p class="naming">Liquidity</p>
                    </div>
                    <div class="connect-line"></div>
                    <div class="connect-line component-right"></div>
                    <div class="component component-right">
                        <p class="percents">5%</p>
                        <p class="naming">Marketing</p>
                    </div>
                </div>
                <div class="item">
                    <div class="component">
                        <p class="percents">10%</p>
                        <p class="naming">Team</p>
                    </div>
                    <div class="connect-line"></div>
                    <div class="connect-line component-right"></div>
                    <div class="component component-right">
                        <p class="percents">30%</p>
                        <p class="naming">Development</p>
                    </div>
                </div>
                <div class="item">
                    <div class="component">
                        <p class="percents">15%</p>
                        <p class="naming">Presale</p>
                    </div>
                    <div class="connect-line"></div>
                    <div class="connect-line component-right"></div>
                    <div class="component component-right">
                        <p class="percents">10%</p>
                        <p class="naming">Community</p>
                    </div>
                </div>
                <div class="vertical-line"></div>
                <!-- <div class="item-logo-back"></div> -->
            </div>
        </div>

    </div>
</template>

<script setup>
import Timer from './Timer.vue'
import HorizontalTablet from './Tablets/HorizontalTablet.vue'
import VerticalTablet from './Tablets/VerticalTablet.vue'

import RippleWallet from './Ripple/RippleWallet.vue'
import RippleDataBase from './Ripple/RippleDataBase.vue'
import RippleLineTop from './Ripple/RippleLineTop.vue'
</script>

<style scoped lang="scss">
.main__block {
    margin-top: -11em;

    width: 100%;
    min-height: 1850px;

    background: url("../assets/img/miami__background-2.png") no-repeat center;
    background-size: cover;



    .main__block-wrapper {
        padding: 500px 0 0;

        .block__info {
            max-width: 1045px;
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

            visibility: hidden;
        }

        .block__components {
            width: 50%;
            margin: -350px auto 0px;
            position: relative;
            padding-bottom: 75px;

            .componets__header {
                display: grid;
                grid-template-columns: 50% 60%;
                grid-template-rows: 145px;
                justify-items: center;
                align-items: center;

                h1 {
                    font-size: 50px;
                    line-height: 61px;
                    color: #eed1ff;
                    font-weight: 700;
                    font-family: 'DrukWideCyr-Bold';
                    text-align: center;
                }
            }

            .item {
                margin-top: 5px;

                display: flex;
                align-items: center;
                justify-content: center;

                color: #eed1ff;
                font-weight: 700;
                font-family: 'DrukWideCyr-Bold';

                .component {
                    min-width: 410px;
                    border: 2px solid rgb(238, 209, 255);
                    border-radius: 10px;
                    background: linear-gradient(180.00deg, rgba(142, 71, 140, 0.2), rgba(87, 57, 44, 0.2) 100%);
                    padding: 2em;

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

                .connect-line {
                    width: 125px;
                    height: 1px;
                    border: 2px solid #EED1FF;
                }

                .component-right {
                    text-align: right;
                    margin-top: 110px;
                }
            }

            .item:nth-child(2) {
                margin-top: 0;
            }

            .item-logo {
                // position: absolute;
                // top: 5em;

                // left: calc((100% - 15%) / 2);
                width: 150px;
                height: 150px;

                // z-index: 3;

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

            .vertical-line {
                position: absolute;
                top: 0;
                left: 49.9%;

                width: 2px;
                height: 100%;
                border: 2px solid #EED1FF;
            }




        }
    }


}

@media (max-width: 1700px) {
    .main__block {
        margin-top: -18em;

        .main__block-wrapper {
            .block__components {
                .item {
                    .component {
                        min-width: 340px;

                        p.percents {
                            font-size: 40px;
                            line-height: 50px;
                        }

                        p.naming {
                            margin-top: 7px;
                            font-size: 25px;
                            line-height: 36px;
                            padding-bottom: 10px;
                        }

                    }

                    .component-right {
                        text-align: right;
                        margin-top: 90px;
                    }
                }
            }
        }
    }
}

@media (max-width: 1440px) {
    .main__block {
        margin-top: -18em;

        .main__block-wrapper {
            .block__components {
                .item {
                    .component {
                        min-width: 300px;

                        p.percents {
                            font-size: 30px;
                            line-height: 40px;
                        }

                        p.naming {
                            margin-top: 4px;
                            font-size: 20px;
                            line-height: 26px;
                            padding-bottom: 5px;
                        }

                    }

                    .component-right {
                        text-align: right;
                        margin-top: 70px;
                    }
                }
            }
        }
    }
}

@media (max-width: 1280px) {
    .main__block {
        margin-top: -18em;

        .main__block-wrapper {
            .block__components {
                .componets__header {
                    grid-template-rows: 100px;

                    h1 {
                        font-size: 35px;
                        line-height: 40px;
                    }
                }

                .item {
                    .component {
                        min-width: 240px;

                        p.percents {
                            font-size: 20px;
                            line-height: 30px;
                        }

                        p.naming {
                            margin-top: 2px;
                            font-size: 15px;
                            line-height: 16px;
                            padding-bottom: 3px;
                        }

                    }

                    .component-right {
                        text-align: right;
                        margin-top: 50px;
                    }
                }

                .item-logo {
                    width: 100px;
                    height: 100px;
                }
            }
        }
    }
}

@media (max-width: 1100px) {
    .main__block {
        .main__block-wrapper {
            .block__info {
                max-width: 750px;

                .steps {
                    margin-top: 0px;
                    flex-direction: column;
                    overflow: hidden;

                    .step__item {
                        width: 100%;
                        flex-direction: row;
                        justify-content: flex-start;
                    }

                    .step__item:nth-child(3) {
                        flex-direction: row-reverse;
                    }

                    .step__line {
                        transform: rotate(45deg);
                    }

                    .step__line:nth-child(4) {
                        transform: rotate(-45deg);
                    }

                    .item {
                        width: 220px;
                        height: 220px;
                    }
                }
            }

            .block__components {
                .componets__header {
                    grid-template-rows: 85px;

                    h1 {
                        font-size: 25px;
                        line-height: 30px;
                    }
                }

                .item {
                    .component {
                        min-width: 200px !important;
                        padding: 0.5em;

                        p.percents {
                            font-size: 18px;
                        }

                        p.naming {
                            font-size: 14px;
                        }

                    }

                    .component-right {
                        text-align: right;
                        margin-top: 35px;
                    }
                }

                .item-logo {
                    width: 85px;
                    height: 85px;
                }
            }
        }
    }
}

@media (max-width:870px) {

    .main__block {
        .main__block-wrapper {
            .block__info {
                max-width: 500px !important;
            }
        }
    }

}

@media (max-width: 590px) {
    .main__block {
        .main__block-wrapper {
            padding: 275px 0 0;
        }
    }
}

@media (max-width: 500px) {
    .main__block {
        .main__block-wrapper {
            padding: 300px 0 0;

            .block__info {
                width: 290px;

                .steps {
                    margin-top: 44px;

                    .step__line {
                        margin-bottom: 18px;
                        width: 70px;
                    }

                    .item {

                        width: 180px;
                        height: 180px;

                    }

                    p {
                        font-size: 18px;
                    }
                }
            }

        }
    }
}
</style>