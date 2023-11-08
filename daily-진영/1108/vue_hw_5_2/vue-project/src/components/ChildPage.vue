<template>
  <div>
    <p>자식 페이지입니다.</p>
    <p>이름 : {{ child.name }}</p>
    <p>나이 : {{ child.age }}</p>
  </div>
</template>

<script setup>
  defineProps({
    child: Object
  })
</script>

<style scoped>
  div {
    margin: 10px;
    border: 1px solid black;
    padding: 10px;
  }
</style>