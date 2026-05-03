<script setup lang="ts">
import { useAccount } from '@wagmi/vue'

const { address } = useAccount()

const form = ref({
  item: '',
  starting_price: 0,
  seller_min_price: 0,
  seller_wallet: address.value, // Automatically bound
  seller_personality: 'balanced'
})

// Update wallet if user switches accounts
watch(address, (newAddr) => {
  form.value.seller_wallet = newAddr
})

async function handleCreate() {
  if (!form.value.item || form.value.seller_min_price <= 0) return
  
  try {
    await fetch('http://localhost:3001/items', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form.value)
    })
    navigateTo('/marketplace')
  } catch (e) {
    console.error("Failed to list item:", e)
  }
}
</script>

<template>
  <!-- UI matches your chromatic aesthetic -->
  <div class="max-w-3xl mx-auto py-20 px-6">
    <div class="bg-neutral-900 border border-cyan-900/30 p-10 relative">
      <h2 class="text-3xl text-cyan-400 font-['Space_Grotesk'] mb-8 italic">REGISTER_ASSET</h2>
      
      <form @submit.prevent="handleCreate" class="space-y-6">
        <div>
          <label class="text-[10px] text-cyan-500/50 uppercase tracking-widest">Asset Name</label>
          <input v-model="form.item" type="text" class="w-full bg-black border border-cyan-900/50 p-4 text-cyan-100 font-mono focus:border-cyan-400 focus:outline-none" />
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="text-[10px] text-cyan-500/50 uppercase tracking-widest">Initial Ask (ETH)</label>
            <input v-model.number="form.starting_price" type="number" step="0.01" class="w-full bg-black border border-cyan-900/50 p-4 text-cyan-100 font-mono focus:border-cyan-400 focus:outline-none" />
          </div>
          <div>
            <label class="text-[10px] text-cyan-500/50 uppercase tracking-widest">Minimum Acceptable (ETH)</label>
            <input v-model.number="form.seller_min_price" type="number" step="0.01" class="w-full bg-black border border-cyan-900/50 p-4 text-cyan-100 font-mono focus:border-cyan-400 focus:outline-none" />
          </div>
        </div>

        <div>
          <label class="text-[10px] text-cyan-500/50 uppercase tracking-widest">Seller Wallet Node</label>
          <div class="p-4 bg-cyan-950/20 border border-cyan-900/30 text-cyan-700 font-mono text-xs">
            {{ address || 'NOT_CONNECTED' }}
          </div>
        </div>

        

        <button type="submit" class="w-full chromatic-border-hover bg-cyan-500 text-black py-4 font-black uppercase tracking-widest">
          INITIALIZE_LEDGER_ENTRY
        </button>
      </form>
    </div>
  </div>
</template>