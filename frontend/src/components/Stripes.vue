<template>
    <div class="strp">

      <div class="strp__item blue">
        <p class="c-white">
          <span class="no-flex-word">ONLY $WAY</span>
          <span class="border-word" data-text="PRESALE"> PRESALE </span>
  
          <span class="no-flex-word">ONLY $WAY</span>
          <span class="border-word" data-text="PRESALE"> PRESALE </span>
  
          <span class="no-flex-word">ONLY $WAY</span>
          <span class="border-word" data-text="PRESALE"> PRESALE </span>
  
          <span class="no-flex-word">ONLY $WAY</span>
          <span class="border-word" data-text="PRESALE"> PRESALE </span>
  
          <span class="no-flex-word">ONLY $WAY</span>
          <span class="border-word" data-text="PRESALE"> PRESALE </span>
  
          <span class="no-flex-word">ONLY $WAY</span>
          <span class="border-word" data-text="PRESALE"> PRESALE </span>
  
          <span class="no-flex-word">ONLY $WAY</span>
          <span class="border-word" data-text="PRESALE"> PRESALE </span>
        </p>
      </div>

      <div class="strp__item purple">
        <p>
          <span class="no-flex-word">ONLY $WAY</span>
          <span class="border-word" data-text="PRESALE"> PRESALE </span>
  
          <span class="no-flex-word">ONLY $WAY</span>
          <span class="border-word" data-text="PRESALE"> PRESALE </span>
  
          <span class="no-flex-word">ONLY $WAY</span>
          <span class="border-word" data-text="PRESALE"> PRESALE </span>
  
          <span class="no-flex-word">ONLY $WAY</span>
          <span class="border-word" data-text="PRESALE"> PRESALE </span>
  
          <span class="no-flex-word">ONLY $WAY</span>
          <span class="border-word" data-text="PRESALE"> PRESALE </span>
  
          <span class="no-flex-word">ONLY $WAY</span>
          <span class="border-word" data-text="PRESALE"> PRESALE </span>
  
          <span class="no-flex-word">ONLY $WAY</span>
          <span class="border-word" data-text="PRESALE"> PRESALE </span>
        </p>
      </div>

      <div class="bc-blur"></div>

    </div>
  </template>
  
  <style lang="scss" scoped>
  .strp {
    transition: all 0.2s ease-in-out;
    width: 100%;
    // border: 3px solid red;
    overflow: hidden;
    height: 400px;
    padding-top: 50px;
    position: relative;
    z-index: 1;

    .bc-blur{
      position: absolute;
      width: 100%;
      height: 100%;
      background-color: transparent;
      z-index: 0;
      top: 0;
    }
  
    .strp__item {
      width: 120%;
      margin-left: -15px;
      color: #000;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      font-weight: 700;
      font-size: 32px;
      border-radius: 10px;
      margin-top: -5px;
      p {
        display: flex;
        flex-wrap: nowrap;
        padding: 13px 0;
        .border-word {
          margin: 0 10px;
          -webkit-text-stroke: 1.5px #000000;
          -webkit-text-fill-color: transparent;
        }
        .no-flex-word {
          min-width: 185px;
        }
      }
      .c-white {
        .border-word {
          -webkit-text-stroke: 1.5px #fff;
        }
      }
    }
  
    .purple {
      background-color: #7F35FF;
      transform: rotate(4deg);
      transform-origin: left;
      animation: slideInLeft 2s forwards;
      margin-top: -35px;
    }
  
    .blue {
      background-color: #388BFF;
      transform: rotate(-4.5deg);
      transform-origin: right;
      margin-left: -35px;
      animation: slideInRight 2s forwards;
      
    }
  
    .c-white {
      color: #FFF !important;
    }
  }
  
  @keyframes slideInLeft {
    0% {
      filter: blur(5px);
      transform: translateX(-100%) rotate(0deg);
    }
    100% {
      filter: blur(0px);
      transform: translateX(0) rotate(4deg);
    }
  }
  
  @keyframes slideInRight {
    0% {
      filter: blur(5px);
      transform: translateX(100%) rotate(0deg);
    }
    100% {
      filter: blur(0px);
      transform: translateX(0) rotate(-4.5deg);
    }
  }
  
  @media (max-width: 1440px) {
    .strp {
      height: 330px;
      .strp__item {
        font-size: 26px;
        p {
          .border-word {
            margin: 0 5px;
          }
          .no-flex-word {
            min-width: 150px;
          }
        }
      }
      .purple {
        margin-top: -35px;
        transform: rotate(8deg);
      }
      .blue {
        transform: rotate(-8deg);
      }
    }
  }
  @media (max-width: 1000px) {
    .strp {
      height: 270px;
      .strp__item {
        font-size: 22px;
        p {
          .border-word {
            margin: 0 5px;
          }
          .no-flex-word {
            min-width: 130px;
          }
        }
      }
    }
  }
  @media (max-width: 650px) {
    .strp {
      height: 150px;
      .strp__item {
        font-size: 18px;
        p {
          .border-word {
            margin: 0 5px;
          }
          .no-flex-word {
            min-width: 105px;
          }
        }
      }
    }
  }
  @media (max-width: 520px) {
    .strp{
      padding-top: 0px !important;
    }
  }
  @media (max-width: 450px) {
    .strp {
      .strp__item {
        font-size: 15px;
        p {
          .border-word {
            margin: 0 5px;
            -webkit-text-stroke: 1px #000000;
          }
          .no-flex-word {
            min-width: 85px;
          }
        }
        .c-white {
          .border-word {
            -webkit-text-stroke: 1px #fff;
          }
        }
      }
    }
  }
  </style>
  