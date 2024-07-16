<template>
  <div class="body">
    <div class="midstream"></div>
    <div class="loops">
      <div class=" loop"></div>
      <div class="loop"></div>
    </div>
    <div class="table-hor" @click="SwingHor">
      <p>Нажми на меня</p>
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
}

.midstream {
  width: 464px;
  height: 11px;
  background: rgb(27, 20, 31);
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

.body {
  perspective: 800px;
}

.table-hor {
  margin-left: 38px;
  width: 430px;
  height: 114px;

  border-radius: 6px;
  background: rgb(13, 17, 20);
  border: 3px solid rgb(27, 20, 31);

  display: flex;
  align-items: center;
  justify-content: center;

  transition: transform 0.2s ease-in-out;
  transform-origin: top;
}

.table-hor p {
  color: rgb(111, 100, 99);
  font-family: 'DrukWideCyr-Bold';
  font-size: 27px;
  font-weight: 700;
  line-height: 33px;
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
</style>