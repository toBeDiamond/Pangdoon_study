<template>
  <div class="card">
    <h1>가수 이름</h1>
    <img src="@/assets/singer.jpg" alt="singer">
    <p>가수 소개글</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
</script>

<style scoped>
  img {
    width: 200px;
    border-radius: 50%;
  }
  div {border: 1px solid black;}
  div{
      text-align: center;
    }
  .card {
    display:inline-block;
    width: 40%;
    margin: 20px;
  }
</style>