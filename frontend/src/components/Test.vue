<template>
  <div class="strp">
    <div class="strp__item blue c-white">
      <p>
        ONLY $WAY
        <img src="../assets/img/PRESALE.png" alt="">
        ONLY $WAY
        <img src="../assets/img/PRESALE.png" alt="">
        ONLY $WAY
        <img src="../assets/img/PRESALE.png" alt="">
        ONLY $WAY
        <img src="../assets/img/PRESALE.png" alt="">
        ONLY $WAY
      </p>
    </div>
    <div class="strp__item purple">
      <p>
        ONLY $WAY
        <span class="border-word" data-text="PRESALE"> PRESALE </span>
        ONLY $WAY
        <span class="border-word" data-text="PRESALE"> PRESALE </span>
        ONLY $WAY
        <span class="border-word" data-text="PRESALE"> PRESALE </span>
        ONLY $WAY
        <span class="border-word" data-text="PRESALE"> PRESALE </span>
        ONLY $WAY
      </p>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.strp {
  width: 100%;

  .strp__item {
    width: 120%;

    margin-left: -15px;

    color: #000;
    font-family: 'Inter';
    font-weight: 700;
    font-size: 32px;

    p {
      padding: 10px 0;

      // .border-word {
      //   color: #7F35FF;
      //   position: relative;
      //   display: inline-block;
      // }

      // .border-word::before {
      //   content: attr(data-text);
      //   position: absolute;
      //   left: 0;
      //   top: 0;
      //   color: black;
      //   z-index: -1;
      //   filter: blur(2px);
      //   opacity: 1;
      // }
    }
  }

  .purple {
    background-color: #7F35FF;
    transform: rotate(5deg);
    transform-origin: left;
  }

  .blue {
    background-color: #388BFF;
    transform: rotate(-5deg);
    transform-origin: right;
  }

  .c-white {
    color: #FFF !important;
  }
}
</style>