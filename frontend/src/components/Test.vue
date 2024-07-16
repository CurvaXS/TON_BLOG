<template>
    <div class="body">
        <div class="table" @click="Swing">
            <!-- Ваша табличка -->
            <p>Нажми на меня</p>
        </div>
    </div>
</template>

<script setup>


const Swing = () => {
    const table = document.querySelector(".table");
    table.classList.add("swing");

    setTimeout(() => {
        table.classList.remove("swing");
    }, 1500);
};
</script>

<style scoped>
* {
    color: black;
    cursor: pointer;
}

.body{
    perspective: 800px;
}

.table {
  width: 200px;
  height: 100px;
  background-color: #f0f0f0;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.2s ease-in-out;
  transform-origin: right;
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
  50%{
    transform: rotate3d(0, 1, 0, 20deg);
  }
  75% {
    transform: rotate3d(0, 1, 0, -10deg);
  }
  100% {
    transform: rotate3d(0, 1, 0, 0deg);
  }
}
</style>