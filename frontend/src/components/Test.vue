<template>
  <div class="container">

    <svg>
      <symbol id="s-text">
        <text text-anchor="middle" x="50%" y="60%">WAY</text>
      </symbol>

      <g class="g-ants">
        <use xlink:href="#s-text" class="text-copy"></use>
        <use xlink:href="#s-text" class="text-copy"></use>
        <use xlink:href="#s-text" class="text-copy"></use>
        <use xlink:href="#s-text" class="text-copy"></use>
        <use xlink:href="#s-text" class="text-copy"></use>
      </g>
    </svg>

    <h1>
      <span class='one'>W</span>
      <span class='two'>A</span>
      <span class='three'>Y</span>
      <!-- <span class='four'>e</span>
      <span class='five'>u</span>
      <span class='six'>p</span> -->
    </h1>

  </div>
</template>


<script setup>

</script>

<style scoped>
* {
  font-family: 'DrukWideCyr-Bold';
}

svg {
  display: block;
  font-family: 'DrukWideCyr-Bold';
  font-size: 100px;
  width: 960px;
  height: 300px;
  margin: 0 auto;
}

.text-copy {
  fill: none;
  stroke: white;
  stroke-dasharray: 6% 29%;
  stroke-width: 5px;
  stroke-dashoffset: 0%;
  animation: stroke-offset 5.5s infinite linear;
}

.text-copy:nth-child(1) {
  stroke: #4D163D;
  animation-delay: -1;
}

.text-copy:nth-child(2) {
  stroke: #840037;
  animation-delay: -2s;
}

.text-copy:nth-child(3) {
  stroke: #BD0034;
  animation-delay: -3s;
}

.text-copy:nth-child(4) {
  stroke: #BD0034;
  animation-delay: -4s;
}

.text-copy:nth-child(5) {
  stroke: #FDB731;
  animation-delay: -5s;
}

@keyframes stroke-offset {
  100% {
    stroke-dashoffset: -35%;
  }
}

h1 {
  color: #4db1bc;
    margin: 0;
    padding-bottom: 6rem;
    grid-column: 1;
    grid-row: 1;
    z-index: 1;
    
    font-size: 10rem;
    text-transform: uppercase;
    animation: glow 2s ease-in-out infinite alternate;
    text-align: center;
  }
  
  @keyframes glow {
    from {
      text-shadow: 0 0 20px #2d9da9;
    }
    to {
      text-shadow: 0 0 30px #34b3c1, 0 0 10px #4dbbc7;
    }
  }
</style>
