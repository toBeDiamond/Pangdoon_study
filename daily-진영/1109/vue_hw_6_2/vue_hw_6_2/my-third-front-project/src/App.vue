<template>
  <div>
    <MainPage />
  <nav>
    <RouterLink :to="{name: 'some'}">Some</RouterLink>
    <RouterLink :to="{name: 'other'}">Other</RouterLink>
  </nav>
  </div>

<RouterView />
</template>

<script setup>
import MainPage from '@/components/MainPage.vue';


</script>

<style scoped>
a {margin: 20px;}
</style>