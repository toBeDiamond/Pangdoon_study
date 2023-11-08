<template>
  <div>
    <p>자식 페이지입니다.</p>
    <p>이름 : {{ child.name }}</p>
    <p>나이 : {{ child.age }}</p>
    <p>용돈 : {{ child.balance }}</p>
    <button @click="buttonClick">용돈주세요</button>
  </div>
</template>

<script setup>
  const props = defineProps({
    child: Object
  })

  const emit = defineEmits(['giveMeAllowance'])
  const buttonClick = function () {
    emit('giveMeAllowance', props.child)
  }

</script>

<style scoped>
  div {
    margin: 10px;
    border: 1px solid black;
    padding: 10px;
  }
</style>