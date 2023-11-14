import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', () => {
  const balances = ref([
    {
      name: '김하나',
      balance: 100000
      },
      {
      name: '김두리',
      balance: 10000
      },
      {
      name: '김서이',
      balance: 100
      },
  ])
  
  const detailInfo = computed(() => { 
    return (name) => balances.value.find((item) => item.name === name) 
  })

  const updateBalance = function(name) {
    balances.value = balances.value.map((item) => {
      if(item.name === name){
        item.balance += 1000
      }
      return item
    })
  }

  return { balances, detailInfo, updateBalance }
})
