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
            </div>
        </div>
    </div>
</template>

<script setup>
import Timer from './Timer.vue'
</script>

<style scoped lang="scss">
.main__block {
    margin-top: -100px;

    width: 100%;
    min-height: 1850px;

    background: url("../assets/img/miami__background-2.png") no-repeat center;
    background-size: cover;

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
            }

            p.timer {
                margin-top: 14px;
                color: rgb(127, 53, 255);
                font-size: 80px;
                font-weight: 700;
                line-height: 96px;
            }

            .steps {
                display: flex;
                align-items: center;
                justify-content: space-between;
                margin-top: 20px;

                .step__item {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center
                }
                .step__line{
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
        }
    }
}
</style>