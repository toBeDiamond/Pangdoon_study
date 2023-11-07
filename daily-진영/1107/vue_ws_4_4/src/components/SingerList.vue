<template>
  <div>
    <h1>가수 목록</h1>
    <SingerDetail />
    <SingerDetail />
  </div>
</template>

<script setup>
import SingerDetail from '@/components/singers/SingerDetail.vue'
import { ref } from 'vue'
</script>

<style scoped>
    h1 {
      color: orangered;
    }
    div{
      text-align: center;
    }
</style>