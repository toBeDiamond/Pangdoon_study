<template>
  <div>
    <h1>가수 목록</h1>
    <SingerDetail />
  </div>
</template>

<script setup>
import SingerDetail from '@/components/singers/SingerDetail.vue'
import { ref } from 'vue'
</script>

<style scoped>
    div{
      text-align: center;
    }
</style>