<template>
  <div>
    <h1>데이터 수정 페이지</h1>
    <p>이름 : {{detailInfo.name}}</p>
    <p>잔고 : {{detailInfo.balance}}</p>
    <button @click="store.updateBalance(detailInfo.name)">+</button>
  </div>
</template>

<script setup>
import { useBalanceStore } from '@/stores/balance';
import { useRoute } from 'vue-router';

const store = useBalanceStore()
const route = useRoute()

// console.log(store.detailInfo(route.params.name))
const detailInfo = store.detailInfo(route.params.name)

</script>

<style lang="scss" scoped>

</style>