<template>
  <div class="u">
    <img src="../assets/img/miami__background.png" alt="">
    <div class="dark"></div>
  </div>
</template>

<style lang="scss">


.u {
  position: relative;
  width: 100%;
  overflow-x: hidden;

  img {
    width: 100%;
    display: block; /* Убедитесь, что изображение блочный элемент */
  }

  .dark {
    width: 150%;
    height: 63%;

    position: absolute;
    bottom: -33%;
    left: 50%; /* Центрируем элемент по горизонтали */
    transform: translateX(-50%); /* Смещаем элемент на половину его ширины влево */

    background: #000;
    filter: blur(70px);
  }
}
</style>