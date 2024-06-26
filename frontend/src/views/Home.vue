
<template>
    <main>
        <header>
        
        <div class="wrapper">
          <nav>
            <RouterLink to="/">Home</RouterLink>
            <RouterLink to="/about">About</RouterLink>
          </nav>
        </div>
      </header>
    
      <RouterView />
        <h1>TEST</h1>
      </main>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>


