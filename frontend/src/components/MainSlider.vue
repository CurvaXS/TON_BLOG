<script>
import Page1 from '../components/SliderPages/Page1.vue';

import { Pagination, A11y } from 'swiper/modules';

import { Swiper, SwiperSlide } from 'swiper/vue';

import 'swiper/css';
import 'swiper/css/pagination';


export default {
  components: {
    Swiper,
    SwiperSlide,
    Page1
  },
  setup() {
    const onSwiper = (swiper) => {
      console.log(swiper);
    };
    const onSlideChange = () => {
      console.log('slide change');
    };
    return {
      onSwiper,
      onSlideChange,
      modules: [Pagination, A11y],
    };
  },
};
</script>

<template>
  <swiper :modules="modules" :slides-per-view="1" :space-between="50" :pagination="{ clickable: true }"
    :scrollbar="{ draggable: true }" @swiper="onSwiper" @slideChange="onSlideChange">
    <swiper-slide>

      <Page1></Page1>

    </swiper-slide>
    <swiper-slide>

      <Page1></Page1>

    </swiper-slide>
    <swiper-slide>

      <Page1></Page1>

    </swiper-slide>
  </swiper>
</template>


<style scoped>
.swiper-slide {
  background: transparent;
}

</style>