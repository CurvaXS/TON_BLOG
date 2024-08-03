<template>
  <div class="body-tablet">
    <div class="midstream"></div>
    <div class="loops-right">
      <div class="loop"></div>
      <div class="loop"></div>
    </div>
    <div class="table" @click="Swing">

      <p id="1"> TOP SECRET!</p>
      <p id="2"> CEX - Get ready to trade $WAY on top exchanges!</p>
    </div>
  </div>
</template>

<script setup>
const Swing = (event) => {
  const table = event.target.closest(".table");
  if (table) {
    table.classList.add("swing");

    setTimeout(() => {
      table.classList.remove("swing");
    }, 1500);
  }
};
</script>

<style scoped>
* {
  cursor: pointer;
}

.midstream {
  display: none;
}

.body-tablet {
  perspective: 800px;

  display: flex;
  flex-direction: row-reverse;
  align-items: flex-start;
  flex-wrap: nowrap;
}

.loops-right {
  height: 195px;
  margin-top: 90px;

  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.loops-right .loop {
  width: 59px;
  height: 17px;
  background: rgb(30, 33, 38);
}

.table {
  width: 70.36px;
  height: 533.86px;


  display: flex;
  align-items: center;
  justify-content: center;

  transition: transform 0.2s ease-in-out;
  transform-origin: right;
}

.table p {
  color: rgba(250, 168, 132, 0.3);
  font-family: 'DrukWideCyr-Bold';
  font-size: 38px;
  font-weight: 700;
  line-height: 26px;

  text-transform: uppercase;
  writing-mode: vertical-lr;
  text-orientation: upright;
}

p[id="1"],
p[id="2"] {
  display: none;
}

.swing {
  animation: swing 1.5s alternate;
}

@keyframes swing {
  0% {
    transform: rotate3d(0, 1, 0, 0deg);
  }

  25% {
    transform: rotate3d(0, 1, 0, -30deg);
  }

  50% {
    transform: rotate3d(0, 1, 0, 20deg);
  }

  75% {
    transform: rotate3d(0, 1, 0, -10deg);
  }

  100% {
    transform: rotate3d(0, 1, 0, 0deg);
  }
}

@media (max-width: 1045px) {

  .loops-right {
    height: 155px;
  }

  .loops-right .loop {
    width: 59px;
    height: 17px;
    background: rgb(30, 33, 38);
  }

  .table {
    width: 95px;
    height: 450px;


    display: flex;
    align-items: center;
    justify-content: center;

    transition: transform 0.2s ease-in-out;
    transform-origin: right;
  }

  .table p {
    font-size: 32px;

    text-transform: uppercase;
    writing-mode: vertical-lr;
    text-orientation: upright;
  }
}

@media (max-width: 770px) {

  .loops-right {
    height: 100px;
  }

  .loops-right .loop {
    width: 40px;
    height: 14px;
  }

  .table {
    width: 70px;
    height: 400px;
  }

  .table p {
    font-size: 27px;
  }
}
</style>