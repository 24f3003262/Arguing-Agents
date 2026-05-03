<script setup lang="ts">
import { ref, onMounted } from 'vue'

interface MarketItem {
  id: number
  item: string
  starting_price: number
  description?: string
  seller_wallet: string
  status: string
}

const items = ref<MarketItem[]>([])
const isLoading = ref(true)

async function fetchItems() {
  try {
    const res = await fetch('http://localhost:3001/items')
    const data = await res.json()
    
    // Filter out any broken items or ensure they have default values
    items.value = data.map((item: any) => ({
      ...item,
      seller_wallet: item.seller_wallet || '', // Ensure it's at least an empty string
      status: item.status || 'AVAILABLE'
    }))
  } catch (e) {
    console.error("Failed to sync with market ledger:", e)
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  fetchItems()
})
</script>

<template>
  <div class="relative z-20">
    <header class="mb-xl border-b border-surface-variant pb-md flex justify-between items-end">
      <div>
        <h1 class="font-h1 text-on-surface mb-unit italic tracking-tighter">Asset Exchange</h1>
        <p class="font-code-sm text-on-surface-variant uppercase tracking-widest">
          Procure resources for autonomous agent execution.
        </p>
      </div>

      <!-- GLITCHY CREATE BUTTON -->
      <NuxtLink 
        to="/create_items"
        class="font-label-caps text-label-caps px-xl py-md border border-primary-container text-primary-container negotiation-chromatic-btn transition-all flex items-center gap-sm group"
      >
        <span class="material-symbols-outlined text-sm group-hover:rotate-90 transition-transform">add</span>
        Initialize_New_Asset
      </NuxtLink>
    </header>

    <!-- LOADING STATE -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center py-20 text-primary-container animate-pulse">
      <span class="material-symbols-outlined text-6xl animate-spin">sync</span>
      <p class="font-code-sm mt-md">SYNCHRONIZING_WITH_LEDGER...</p>
    </div>

    <!-- DYNAMIC GRID -->
    <div v-else class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-gutter items-stretch">
      <article 
        v-for="item in items" 
        :key="item.id"
        class="bg-surface-container-low border border-outline-variant p-lg flex flex-col h-full group relative overflow-hidden cyber-card-base"
      >
        <div class="absolute top-0 right-0 p-unit bg-primary-container/10 border-b border-l border-outline-variant text-primary-container font-label-caps text-[10px]">
          {{ item.status }}
        </div>
        
        <div class="mb-lg">
          <span class="material-symbols-outlined text-4xl text-primary-fixed-dim mb-sm block">
            {{ item.status === 'SOLD' ? 'lock' : 'deployed_code' }}
          </span>
          <h3 class="font-h3 text-on-surface uppercase">{{ item.item || item.name || 'Unknown Asset' }}</h3>
          <p class="font-code-sm text-on-surface-variant mt-xs h-12 line-clamp-2">
            Origin: {{ item.seller_wallet?.slice(0, 10) || '0x0000...0000' }}
          </p>
        </div>
        
        <div class="flex-1 grid grid-cols-2 gap-sm mb-lg font-code-sm border-t border-surface-variant pt-sm">
          <div class="col-span-2">
            <div class="text-outline uppercase">Registry_ID</div>
            <div class="text-on-surface font-bold text-[10px]">{{ item.id }}</div>
          </div>
        </div>

        <div class="mt-auto flex items-center justify-between pt-md border-t border-surface-variant">
          <div class="font-h2 text-on-surface">
            {{ item.starting_price ?? item.price ?? '0.00' }} 
            <span class="font-body-md text-outline">ETH</span>
          </div>
          
          <!-- Route to negotiation with the specific item ID -->
          <NuxtLink 
            v-if="item.status !== 'SOLD'"
            :to="{ path: '/negotiation', query: { id: item.id } }"
            class="negotiation-chromatic-btn px-lg py-sm font-label-caps text-label-caps text-cyan-400"
>
            Negotiate
          </NuxtLink>
          <div v-else class="text-outline font-label-caps">COMPLETED</div>
        </div>
      </article>
    </div>
  </div>
</template>

<style scoped>
/* Card Hover Effect */
.cyber-card-base {
  transition: all 0.3s ease;
}
.cyber-card-base:hover {
  box-shadow: 
    2px 0 0 rgba(254, 0, 254, 0.4), 
    -2px 0 0 rgba(0, 251, 251, 0.4), 
    0 0 15px rgba(0, 251, 251, 0.1);
  transform: translate(-1px, -1px);
}

/* REPLICATED NEGOTIATION CHROMATIC ABERRATION 
  This specifically targets the buttons for that magenta/cyan shift.
*/
.negotiation-chromatic-btn {
  position: relative;
  transition: all 0.2s ease;
  overflow: hidden;
  border: 1px solid rgba(0, 251, 251, 0.4);
}

.negotiation-chromatic-btn:hover {
  /* The spread radius (15px) creates the soft outer glow */
  box-shadow: 
    -3px 0 0 #fe00fe, 
     3px 0 0 #00fbfb, 
     0 0 15px rgba(0, 251, 251, 0.5); /* This is the glow */
  background-color: #00fbfb;
  color: #000;
  animation: glitch-skew 0.3s infinite linear alternate-reverse;
}
.negotiation-chromatic-btn:active {
  box-shadow:
    -5px 2px 0 #fe00fe,
     5px -2px 0 #00fbfb;
  transform: translateY(1px);
}
.cyber-card-base:hover {
  border-color: rgba(0, 251, 251, 0.5);
  box-shadow: 0 0 20px rgba(0, 251, 251, 0.1);
}
@keyframes glitch-skew {
  0% { transform: skew(0deg); }
  20% { transform: skew(-1deg); }
  40% { transform: skew(1deg); }
  100% { transform: skew(0deg); }
}
</style>