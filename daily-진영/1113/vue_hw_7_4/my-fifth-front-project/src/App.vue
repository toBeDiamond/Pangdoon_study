<template>
  <nav>
    <RouterLink to="/">Main</RouterLink>
  </nav>
  <h1>pinia + router 연습하기</h1>
  
  <RouterView />

</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>
<style lang="scss" scoped>

</style>