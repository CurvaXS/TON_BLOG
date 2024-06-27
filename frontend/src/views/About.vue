<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <h1>About</h1>
      <div class="wrapper">
      <header>
        <div class="header__wrapper">
          <div class="header__nav">
            <nav>
              <RouterLink to="/">Home</RouterLink>
              <RouterLink to="/about">About</RouterLink>
            </nav>
          </div>
        </div>
      </header>
      </div>
</template>




