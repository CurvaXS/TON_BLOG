<template>
  <div data-v-0904fc8e="" class="main__block-wrapper">
    <div data-v-0904fc8e="" class="block__info">
      <div data-v-0904fc8e="" class="steps">
        <div data-v-0904fc8e="" class="step__item">
          <div data-v-6f8f7279="" data-v-0904fc8e="" class="container">
            <div class="box" data-v-6f8f7279=""><img src="/src/assets/img/wallet.png" alt="" data-v-6f8f7279=""><span
                style="--i:1;" data-v-6f8f7279=""></span><span style="--i:2;" data-v-6f8f7279=""></span><span
                style="--i:3;" data-v-6f8f7279=""></span></div>
          </div>
          <p data-v-0904fc8e="">Set up wallet</p>
        </div><img data-v-0904fc8e="" src="/src/assets/img/step_line.png" alt="" class="step__line">
        <div data-v-0904fc8e="" class="step__item">
          <div data-v-57b11441="" data-v-0904fc8e="" class="container">
            <div class="box" data-v-57b11441="">
              <img src="/src/assets/img/line_top.png" alt="" data-v-57b11441=""><span
                style="--i:1;" data-v-57b11441="">
              </span>
              <span style="--i:2;" data-v-57b11441=""></span>
              <span
                style="--i:3;" data-v-57b11441=""></span>
              </div>
          </div>
          <p data-v-0904fc8e="">x100</p>
        </div><img data-v-0904fc8e="" src="/src/assets/img/step_line.png" alt="" class="step__line">
        <div data-v-0904fc8e="" class="step__item">
          <div data-v-f146446a="" data-v-0904fc8e="" class="container">
            <div class="box" data-v-f146446a=""><img src="/src/assets/img/data_base.png" alt="" data-v-f146446a=""><span
                style="--i:1;" data-v-f146446a=""></span><span style="--i:2;" data-v-f146446a=""></span><span
                style="--i:3;" data-v-f146446a=""></span></div>
          </div>
          <p data-v-0904fc8e="">Rich guy</p>
        </div>
      </div><button data-v-0904fc8e="" class="btn btn-main">PRE-SALE</button>
    </div>
  </div>
</template>

<script setup>
import Timer from './Timer.vue';
import RippleWallet from './Ripple/RippleWallet.vue';
import RippleLineTop from './Ripple/RippleLineTop.vue';
import RippleDataBase from './Ripple/RippleDataBase.vue';
</script>

<style scoped lang="scss">
@media (max-width: 1575px) {
  .main__block .main__block-wrapper .block__components .item-logo[data-v-561215b6] {
    top: 5em
  }
}

@media (max-width: 1375px) {
  .main__block .main__block-wrapper .block__components .item-logo[data-v-561215b6] {
    top: 6em
  }
}

@media (max-width: 1300px) {
  .main__block .main__block-wrapper .block__components .item[data-v-561215b6] {
    margin-top: 125px
  }

  .main__block .main__block-wrapper .block__components .item .component[data-v-561215b6] {
    padding: 1.5em
  }

  .main__block .main__block-wrapper .block__components .item .component p.percents[data-v-561215b6] {
    font-size: 50px
  }

  .main__block .main__block-wrapper .block__components .item .component p.naming[data-v-561215b6] {
    margin-top: 7px;
    font-size: 30px;
    padding-bottom: 20px
  }

  .main__block .main__block-wrapper .block__components .item-logo[data-v-561215b6] {
    left: 40%;
    width: 20%;
    padding-top: 17%
  }
}

@media (max-width: 760px) {
  .main__block .main__block-wrapper .block__components .item-logo[data-v-561215b6] {
    top: 4em;
    padding-top: 16%
  }
}

@media (max-width: 500px) {
  .main__block .main__block-wrapper .block__components .item-logo[data-v-561215b6] {
    top: 3.5em
  }
}

@media (max-width: 1700px) {
  .main__block[data-v-561215b6] {
    margin-top: -18em
  }
}

@media (max-width: 1100px) {
  .main__block-wrapper[data-v-561215b6] {
    padding: 350px 0 0 !important
  }

  .main__block-wrapper .block__info[data-v-561215b6] {
    width: 750px !important
  }

  .main__block-wrapper .block__info h1.name[data-v-561215b6] {
    font-size: 45px !important
  }

  .main__block-wrapper .block__info .steps[data-v-561215b6] {
    margin-top: 44px
  }

  .main__block-wrapper .block__info .steps .step__line[data-v-561215b6] {
    margin-bottom: 25px;
    width: 90px !important
  }

  .main__block-wrapper .block__info .steps .item[data-v-561215b6] {
    width: 200px !important;
    height: 200px !important;
    background-size: cover !important
  }

  .main__block-wrapper .block__info .steps p[data-v-561215b6] {
    margin-top: 25px;
    font-size: 23px !important
  }

  .main__block-wrapper .block__components .item[data-v-561215b6] {
    margin-top: 90px !important
  }

  .main__block-wrapper .block__components .item .component p.percents[data-v-561215b6] {
    font-size: 30px !important;
    line-height: 61px
  }

  .main__block-wrapper .block__components .item .component p.naming[data-v-561215b6] {
    margin-top: 7px;
    font-size: 20px !important;
    padding-bottom: 0 !important
  }
}

@media (max-width: 950px) {
  .main__block-wrapper[data-v-561215b6] {
    padding: 275px 0 0 !important
  }

  .main__block-wrapper .block__info[data-v-561215b6] {
    width: 750px !important
  }

  .main__block-wrapper .block__info .steps[data-v-561215b6] {
    margin-top: 0 !important;
    flex-direction: column
  }

  .main__block-wrapper .block__info .steps .step__item[data-v-561215b6] {
    width: 100%;
    flex-direction: row !important;
    justify-content: flex-start !important
  }

  .main__block-wrapper .block__info .steps .step__item[data-v-561215b6]:nth-child(3) {
    flex-direction: row-reverse !important
  }

  .main__block-wrapper .block__info .steps .step__line[data-v-561215b6] {
    transform: rotate(45deg)
  }

  .main__block-wrapper .block__info .steps .step__line[data-v-561215b6]:nth-child(4) {
    transform: rotate(-45deg)
  }

  .main__block-wrapper .block__info .steps .item[data-v-561215b6] {
    width: 220px !important;
    height: 220px !important
  }

  .main__block-wrapper .block__components .item[data-v-561215b6] {
    margin-top: 40px !important
  }

  .main__block-wrapper .block__components .item .component[data-v-561215b6] {
    padding: 1.2em !important
  }

  .main__block-wrapper .block__components .item .component p.percents[data-v-561215b6] {
    font-size: 25px !important;
    line-height: 50px
  }

  .main__block-wrapper .block__components .item .component p.naming[data-v-561215b6] {
    margin-top: 4px;
    font-size: 20px !important
  }
}

@media (max-width: 770px) {
  .main__block-wrapper[data-v-561215b6] {
    padding: 275px 0 0 !important
  }

  .main__block-wrapper .block__info[data-v-561215b6] {
    width: 500px !important
  }

  .main__block-wrapper .block__components .item[data-v-561215b6] {
    margin-top: 40px !important
  }

  .main__block-wrapper .block__components .item .component[data-v-561215b6] {
    padding: 1em !important
  }

  .main__block-wrapper .block__components .item .component p.percents[data-v-561215b6] {
    font-size: 18px !important;
    line-height: 20px !important
  }

  .main__block-wrapper .block__components .item .component p.naming[data-v-561215b6] {
    margin-top: 4px;
    font-size: 16px !important;
    padding-bottom: 0
  }
}

@media (max-width: 590px) {
  .main__block-wrapper[data-v-561215b6] {
    padding: 275px 0 0 !important
  }

  .main__block-wrapper .block__components[data-v-561215b6] {
    margin: 15px auto 0 !important
  }
}

@media (max-width: 500px) {
  .main__block-wrapper[data-v-561215b6] {
    padding: 300px 0 0 !important
  }

  .main__block-wrapper .block__info[data-v-561215b6] {
    width: 290px !important
  }

  .main__block-wrapper .block__info .steps[data-v-561215b6] {
    margin-top: 44px
  }

  .main__block-wrapper .block__info .steps .step__line[data-v-561215b6] {
    margin-bottom: 18px !important;
    width: 70px !important
  }

  .main__block-wrapper .block__info .steps .item[data-v-561215b6] {
    width: 180px !important;
    height: 180px !important
  }

  .main__block-wrapper .block__info .steps p[data-v-561215b6] {
    font-size: 18px !important
  }

  .main__block-wrapper .block__components .item[data-v-561215b6] {
    margin-top: 10px !important
  }

  .main__block-wrapper .block__components .item .component[data-v-561215b6] {
    padding: .9em !important
  }

  .main__block-wrapper .block__components .item .component p.percents[data-v-561215b6] {
    font-size: 15px !important;
    line-height: 15px !important
  }

  .main__block-wrapper .block__components .item .component p.naming[data-v-561215b6] {
    margin-top: 1px !important;
    font-size: 12px !important;
    padding-bottom: 0 !important
  }
}
</style>
