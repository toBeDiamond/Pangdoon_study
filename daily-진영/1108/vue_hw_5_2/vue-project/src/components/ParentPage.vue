<template>
  <div class="parentsDiv">
    <h1>부모 페이지입니다.</h1>
    <div v-for="child in children">
      <Childpage :child="child"/>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import Childpage from '@/components/Childpage.vue'
const children = ref(
  [
    {
    name:'김하나', age: 30
    },
    {
    name:'김두리', age: 20
    },
    {
    name:'김서이', age: 10
    }
  ])

</script>

<style scoped>
  .parentsDiv {
    border: 1px solid black;
    padding: 30px;
  }
</style>