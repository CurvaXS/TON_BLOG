<template>
  <div class="body-tablet">
    <div class="midstream"></div>
    <div class="loops">
      <div class=" loop"></div>
      <div class="loop"></div>
    </div>
    <div class="table-hor" @click="SwingHor">

      <p id="1"> PRESALE - Don't miss out! $WAY presale starts now. Be among the first.</p>
      <p id="2"> DEX - $WAY becomes available for trading on DEXs</p>
      <p id="3"> NFT - Creation of collectible NFTs powered by the Ton blockchain.</p>
      <p id="4"> Stake - Showering our $WAY holders with love and appreciation! Exclusive rewards and giveaways await!
      </p>
      <p id="5">Нажми на меня</p>
      <p id="6">Нажми на меня</p>
    </div>
  </div>

</template>

<script setup>
const SwingHor = (event) => {
  const tableH = event.target.closest('.table-hor');
  if (tableH) {
    tableH.classList.add("swing-h");

    setTimeout(() => {
      tableH.classList.remove("swing-h");
    }, 1500);
  }
};
</script>

<style scoped>
* {
  color: #000;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.midstream {
  width: 464px;
  height: 11px;
  background: rgb(30, 33, 38);
}

.loops {
  width: 377px;
  margin-left: 66px;

  display: flex;
  justify-content: space-between;
}

.loops .loop {
  height: 17px;
  width: 17px;

  background: rgb(27, 20, 31);
}

.body-tablet {
  perspective: 800px;
}

.table-hor {
  margin-left: 38px;
  width: 430px;
  height: 114px;

  border-radius: 6px;
  background: rgb(13, 17, 20);
  border: 3px solid rgb(30, 33, 38);

  display: flex;
  align-items: center;
  justify-content: center;

  transition: all 0.2s ease-in-out;
  transform-origin: top;

}

.table-hor:hover {
  /* background: rgb(188, 62, 108); */
  background: linear-gradient(90deg, rgb(94, 31, 54) 0%, rgb(120, 16, 54) 50%, rgb(114, 8, 47) 100%);

  p {
    color: #fff;
  }

}

.table-hor p {
  color: rgb(111, 100, 99);
  font-family: 'DrukWideCyr-Bold';
  font-size: 18px;
  font-weight: 700;
  line-height: 20px;
  padding: 1em;
}

p[id="1"],
p[id="2"],
p[id="3"],
p[id="4"],
p[id="5"],
p[id="6"] {
  display: none;
}

.swing-h {
  animation: swing-h 1.5s alternate;
}

@keyframes swing-h {
  0% {
    transform: rotate3d(-1, 0, 0, 0deg);
  }

  25% {
    transform: rotate3d(-1, 0, 0, 30deg);
  }

  50% {
    transform: rotate3d(-1, 0, 0, -20deg);
  }

  75% {
    transform: rotate3d(-1, 0, 0, 10deg);
  }

  100% {
    transform: rotate3d(-1, 0, 0, 0deg);
  }
}

@media (max-width: 770px) {
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
    font-size: 13px !important;
  }
}

@media (max-width: 500px) {
  .midstream {
    width: 150px;
    height: 9px;
  }

  .loops {
    width: 100px;
    margin-left: 20px;
  }

  .table-hor {
    margin-left: 10px;
    width: 120px;
    height: 50px;
  }

  .table-hor p {
    font-size: 11px !important;
  }
}
</style>