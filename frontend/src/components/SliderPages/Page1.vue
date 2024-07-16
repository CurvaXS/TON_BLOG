<template>
    <div class="page__wrapper">
        <div class="page__container">
            <div class="item">
                <div class="item__block">

                    <div class="top">
                        <p>1ST STEP</p>
                        <p>USE IT</p>
                    </div>
                    <div class="dotted-line"></div>

                    <div class="block__wrapper">
                        <div class="circle"></div>
                        <h2 class="name">Lorem ipsum</h2>
                        <p class="description">Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
                        <button type="button">
                            <img src="@/assets/img/eye.png" alt="">
                            SEARCH ON DEX
                        </button>
                    </div>

                    <div class="item__mini-border item__mini-border-top-left"></div>
                    <div class="item__mini-border item__mini-border-top-right"></div>
                    <div class="item__mini-border item__mini-border-bottom-left"></div>
                    <div class="item__mini-border item__mini-border-bottom-right"></div>
                </div>
                <div class="item__btn purple">
                    Lorem ipsum
                </div>
                <div class="item__btn blue">
                    Dolor sit amet
                </div>
            </div>
            <div class="item">
                <div class="item__block item__block-full">

                    <div class="block__wrapper">
                        <div class="circle-orbita">
                            <div class="circle"></div>
                            <img src="@/assets/img/orbita.png" alt="">
                            <img src="@/assets/img/orbita-2.png" alt="">
                        </div>
                        <h2 class="name">Lorem ipsum</h2>
                        <p class="description">Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>

                        <div class="btns">
                            <button class="mini">USE</button>
                            <button class="mini">-</button>
                            <button class="mini">-</button>
                            <button class="mini">-</button>
                            <button class="mini">-</button>
                            <button class="mini">-</button>
                            <button class="mini">-</button>
                            <button class="mini">-</button>
                        </div>
                    </div>



                    <div class="item__achieve">
                        <img src="@/assets/img/fire.png" alt="">
                    </div>
                    <div class="item__mini-border item__mini-border-top-left"></div>
                    <div class="item__mini-border item__mini-border-top-right"></div>
                    <div class="item__mini-border item__mini-border-bottom-left"></div>
                    <div class="item__mini-border item__mini-border-bottom-right"></div>
                </div>
            </div>
            <div class="item">
                <div class="item__block item__block-medium">
                    <div class="block__wrapper-other"></div>
                    <div class="block__wrapper">
                        <div class="circle"></div>
                        <h2 class="name">UNO</h2>
                        <span>Dos Tres • Quatro</span>
                        <div class="medium-btn">
                            <button class="medium">
                                <img src="@/assets/img/i.png" alt="">
                                info
                            </button>
                        </div>
                        <p class="description description-medium">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
                            labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitationullamco
                            laboris nisi ut aliquip ex ea commodo consequat
                        </p>

                    </div>

                    <div class="item__mini-border item__mini-border-top-left"></div>
                    <div class="item__mini-border item__mini-border-top-right"></div>
                    <div class="item__mini-border item__mini-border-bottom-left"></div>
                    <div class="item__mini-border item__mini-border-bottom-right"></div>
                </div>
                <div class="item__block item__block-small">

                    <div class="block__wrapper">
                        <h2 class="name">Settings</h2>
                        <form action="">
                            <input type="checkbox" name="a">
                            <input type="checkbox" name="a">
                            <input type="checkbox" name="a">

                        </form>

                    </div>
                    <div class="item__mini-border item__mini-border-top-left"></div>
                    <div class="item__mini-border item__mini-border-top-right"></div>
                    <div class="item__mini-border item__mini-border-bottom-left"></div>
                    <div class="item__mini-border item__mini-border-bottom-right"></div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
.swiper-slide {
    background: transparent;
}

.page__wrapper {
    background: transparent;
    padding: 58px;
    width: 90.5%;
    margin: 0 auto;
}

.page__container {
    width: 100%;
    height: 666px;
    background: transparent;
    display: grid;
    grid-template-columns: 37% 33% 21.5%;
    grid-template-rows: repeat(1, 100%);
    justify-content: space-between;
    align-content: space-between;
}

.item {
    background-color: transparent;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
    align-items: center;
    flex-wrap: wrap;

    font-family: 'Inter';
}

.item .item__block {
    width: 100%;
    height: 455px;

    border: 1px solid rgba(195, 174, 255, 0.4);
    border-radius: 12px;
    background: rgba(4, 11, 21, 0.4);

    position: relative;
}

.item .item__block .top {
    width: 100%;
    padding: 5px 15px;

    display: flex;
    justify-content: space-between;
    align-items: center;

    font-size: 15.44px;
    font-weight: 700;
    line-height: 26.16px;
    color: rgb(195, 174, 255);
}

.item .item__block .dotted-line {
    border: 1px dashed rgba(195, 174, 255, 0.4);
    background: rgba(195, 174, 255, 0.4);
    width: 100%;
    height: 1px;
}

.item .item__block .item__achieve {
    position: absolute;
    top: -45px;
    right: -45px;
    z-index: 2;

    width: 90px;
    height: 90px;

    border: 2px solid rgba(255, 255, 255, 0.12);
    border-radius: 50%;
    backdrop-filter: blur(20px);
    background: rgba(255, 255, 255, 0.1);

    display: flex;
    justify-content: center;
    align-items: center
}

.item .item__block .block__wrapper {
    width: 85%;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;

    .circle {
        margin-top: 27px;
        width: 78px;
        height: 78px;

        border-radius: 50%;
        border: 2px solid rgba(195, 174, 255, 0.68);
        background: rgba(195, 174, 255, 0.1);
    }

    .circle-orbita {
        margin-top: 50px;
        width: 305px;
        height: 175px;

        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;


        .circle {
            width: 120px;
            height: 120px;
            border-radius: 50%;

            background: radial-gradient(62.00% 62.00% at 50% 50%, rgb(109, 94, 234), rgba(255, 255, 255, 0) 99%);
            opacity: 0.39;
        }

        img {
            position: absolute;

            &:nth-child(2) {
                top: 0;
                left: 39px;
            }

            &:nth-child(3) {
                right: 70px;
                bottom: 0;
            }
        }
    }

    .name {
        margin-top: 38px;
        font-family: 'SF Pro Display';
        font-size: 40px;
        font-weight: 700;
        line-height: 26.16px;
        text-transform: uppercase;
    }

    span {
        margin-top: 9px;
        color: rgb(152, 152, 152);
        font-family: Inter;
        font-size: 10px;
        font-weight: 500;
        line-height: 12px;
    }

    .description {
        margin-top: 12px;
        max-width: 333px;
        text-align: center;

        color: rgb(134, 134, 134);
        font-family: 'SF Pro Display';
        font-size: 20px;
        font-weight: 400;
        line-height: 26.16px;
    }

    button {
        margin-top: 27px;
        width: 100%;
        height: 60px;

        border: 1px solid rgb(0, 0, 0);
        border-radius: 10px;
        background: rgba(74, 7, 136, 0.4);

        display: flex;
        justify-content: center;
        align-items: center;

        font-family: SF Pro Display;
        font-size: 37px;
        font-weight: 700;
        line-height: 26.16px;

        img {
            margin-right: 10px;
        }
    }

    .btns {
        margin-top: 21px;
        width: 100%;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;

        .mini {
            margin: 0 0 20px;
            width: 145.05px;
            height: 52.87px;
            border: 1px solid rgba(255, 255, 255, 0.4);
            font-family: 'SF Pro Display Light';
        }
    }

    .medium-btn {
        margin-top: 18px;
        width: 170px;
        height: 35px;
        border-radius: 8px;
        background-color: #FFF;

        button.medium {
            width: 100%;
            height: 100%;
            border-radius: 8px;
            margin-top: -5px;

            border: 1px solid rgb(255, 255, 255);
            border-radius: 8px;

            background: rgb(46, 46, 46);
            font-family: Inter;
            font-size: 20px;
            font-weight: 600;
            line-height: 24px;
        }
    }

    .description-medium {
        margin-top: 60px;
        font-family: Inter;
        font-size: 10px;
        font-weight: 400;
        line-height: 12px;
    }

}

/*.
item .item__block .block__wrapper-other {}
*/

.item .item__mini-border {
    position: absolute;
    border: 2px solid rgb(255, 255, 255);
    width: 18px;
    height: 20px;
}

.item .item__mini-border-top-left {
    border-bottom: transparent;
    border-right: transparent;
    border-top-left-radius: 11px;
    top: -1px;
    left: -1px;
}

.item .item__mini-border-top-right {
    border-bottom: transparent;
    border-left: transparent;
    border-top-right-radius: 11px;
    top: -1px;
    right: -1px;
}

.item .item__mini-border-bottom-right {
    border-top: transparent;
    border-left: transparent;
    border-bottom-right-radius: 11px;
    bottom: -1px;
    right: -1px;
}

.item .item__mini-border-bottom-left {
    border-top: transparent;
    border-right: transparent;
    border-bottom-left-radius: 11px;
    bottom: -1px;
    left: -1px;
}

.item .item__block-full {
    height: 100%;
}

.item .item__block-medium {
    height: 466px;
}

.item .item__block-small {
    height: 175px;

    .block__wrapper {
        align-items: flex-start;

        .name {
            margin-top: 21px;
            text-align: left;
            font-family: Inter;
            font-size: 25px;
            font-weight: 600;
            line-height: 30px;
        }

        form {
            display: flex;
            flex-direction: column;
            z-index: 100;


            input[type=checkbox] {
                width: 0;
                height: 0;
                opacity: 100%;

                cursor: pointer;



                position: inherit;

                margin-bottom: 10px;
            }

            input[type=checkbox]:before {
                content: "";
                display: block;
                width: 20px;
                height: 20px;
                border: 1px solid rgb(195, 174, 255);
                border-radius: 5px;
                background: rgb(5, 32, 54);
            }


        }
    }

}

.item .item__btn {
    width: 100%;
    height: 80px;

    cursor: pointer;

    border: 1px solid rgba(255, 255, 255, 0.4);
    border-radius: 15px;

    font-size: 40px;
    font-weight: 700;
    line-height: 26.16px;
    letter-spacing: -1.05px;
    display: flex;

    align-items: center;
    justify-content: center;
}

.purple {
    background: rgba(74, 7, 136, 0.4);
}

.blue {
    background: rgba(109, 94, 234, 0.4);
}
</style>