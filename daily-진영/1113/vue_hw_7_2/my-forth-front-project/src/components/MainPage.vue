<template>
  <div>
    <h1>pinia 연습하기</h1>
    <ParentPage v-for="people in store.familyinfo" 
    :key="people.familyName" 
    :family="people"/>
  </div>
</template>

<script setup>
  import ParentPage from '@/components/ParentPage.vue';
  import { useCounterStore } from '@/stores/family'
  const store = useCounterStore()

</script>

<style lang="scss" scoped>

</style>