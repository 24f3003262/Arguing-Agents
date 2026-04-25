<script setup lang="ts">
import { ref, computed } from 'vue'

interface NegotiationResult {
  round: number
  buyer_offer: number
  seller_offer: number
}

interface NegotiationResponse {
  status: string
  item: string
  agreed_price: number | null
  rounds: NegotiationResult[]
}

interface NegotiationRequest {
  item: string
  start_price: number
  min_price: number
  max_price: number
  personality: string
}

// State
const isLoading = ref(false)
const error = ref('')
const negotiationData = ref<NegotiationResponse | null>(null)

// Form data
const form = ref<NegotiationRequest>({
  item: '',
  start_price: 0,
  min_price: 0,
  max_price: 0,
  personality: 'balanced'
})

// Computed values
const hasAgreement = computed(() => negotiationData.value?.status === 'agreed')
const contractId = computed(() => {
  if (!negotiationData.value) return ''
  return '0x' + Math.random().toString(16).slice(2, 10).toUpperCase() + '...' + Math.random().toString(16).slice(2, 6).toUpperCase()
})

const settlementPrice = computed(() => {
  if (!negotiationData.value?.agreed_price) return '0.000'
  return negotiationData.value.agreed_price.toFixed(3)
})

const asset = computed(() => ({
  name: negotiationData.value?.item || 'No item selected',
  standard: 'ERC-721',
  network: 'Ethereum'
}))

const counterparty = computed(() => ({
  id: '0x3F',
  name: 'Agent_Sigma_V9',
  reputation: '98.4%'
}))

const confidenceScore = computed(() => {
  if (!negotiationData.value) return 0
  const rounds = negotiationData.value.rounds.length
  return Math.min(85 + (rounds * 2), 99)
})


const transcript = computed(() => {
  if (!negotiationData.value) return []
  return negotiationData.value.rounds.map((r, i) => ({
    time: `14:0${i + 1}:${Math.floor(Math.random() * 60).toString().padStart(2, '0')}`,
    sender: i % 2 === 0 ? 'LOCAL_NODE' : 'AGENT_0x3F',
    message: i % 2 === 0 
      ? `SUBMIT_BID (Amount: ${r.buyer_offer.toFixed(2)} ETH)`
      : `COUNTER_OFFER (Amount: ${r.seller_offer.toFixed(2)} ETH)`,
    type: i === negotiationData.value!.rounds.length - 1 ? 'accept' : 'info'
  }))
})


const navItems = [
  { label: 'Marketplace', href: '#', active: false },
  { label: 'Negotiations', href: '#', active: true },
  { label: 'Dashboard', href: '#', active: false }
]

const sideNavItems = [
  { icon: 'sensors', label: 'Network Status', href: '#' },
  { icon: 'memory', label: 'Agent Nodes', href: '#' },
  { icon: 'shield_with_heart', label: 'Security Mesh', href: '#' },
  { icon: 'account_balance_wallet', label: 'Ledger', href: '#', active: true }
]

// API call to Python backend
async function startNegotiation() {
  if (!form.value.item || form.value.start_price <= 0 || form.value.min_price <= 0 || form.value.max_price <= 0) {
    error.value = 'Please fill in all fields'
    return
  }

  isLoading.value = true
  error.value = ''

  try {
    const response = await fetch('http://localhost:8000/start-negotiation', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(form.value)
    })

    if (!response.ok) {
      throw new Error('Failed to start negotiation')
    }

    negotiationData.value = await response.json()
  } catch (e) {
    error.value = e instanceof Error ? e.message : 'An error occurred'
    // Fallback to mock data for demo
    negotiationData.value = {
      status: 'agreed',
      item: form.value.item,
      agreed_price: (form.value.start_price + form.value.min_price) / 2,
      rounds: [
        { round: 1, buyer_offer: form.value.min_price, seller_offer: form.value.start_price },
        { round: 2, buyer_offer: form.value.min_price * 1.2, seller_offer: form.value.start_price * 0.9 },
        { round: 3, buyer_offer: form.value.min_price * 1.5, seller_offer: form.value.start_price * 0.8 }
      ]
    }
  } finally {
    isLoading.value = false
  }
}

function resetNegotiation() {
  negotiationData.value = null
  form.value = {
    item: '',
    start_price: 0,
    min_price: 0,
    max_price: 0,
    personality: 'balanced'
  }
}
</script>

<template>
  <div class="min-h-screen flex flex-col overflow-x-hidden selection:bg-primary-container selection:text-on-primary-container">
    <!-- TopNavBar -->
    <header class="flex justify-between items-center w-full px-8 py-4 sticky top-0 z-50 bg-neutral-950/90 backdrop-blur-md docked full-width border-b border-cyan-500/20 shadow-[0_4px_20px_rgba(0,255,255,0.05)] relative after:content-[''] after:absolute after:inset-0 after:bg-[linear-gradient(rgba(18,16,16,0)_50%,rgba(0,0,0,0.25)_50%),linear-gradient(90deg,rgba(255,0,0,0.06),rgba(0,255,0,0.02),rgba(0,0,255,0.06))] after:bg-[length:100%_2px,3px_100%] after:pointer-events-none">
      <div class="text-xl font-bold text-cyan-400 tracking-tighter italic z-10 font-['Space_Grotesk']">Arguing Agents?</div>
      <nav class="hidden md:flex gap-8 z-10">
        <a 
          v-for="item in navItems" 
          :key="item.label"
          :href="item.href"
          class="font-['Space_Grotesk'] uppercase tracking-widest text-sm transition-all duration-300 hover:shadow-[0_0_8px_#00FFFF]"
          :class="item.active 
            ? 'text-cyan-400 border-b border-cyan-400 pb-1 hover:text-cyan-300' 
            : 'text-neutral-500 hover:text-neutral-300'"
        >
          {{ item.label }}
        </a>
      </nav>
      <div class="z-10 hidden md:block">
        <button class="font-['Space_Grotesk'] uppercase tracking-widest text-sm text-cyan-400 border border-cyan-400 px-4 py-2 hover:bg-cyan-400/10 transition-colors">
          Connect Wallet
        </button>
      </div>
    </header>

    <div class="flex flex-1 relative w-full">
      <!-- SideNavBar -->
      <aside class="fixed left-0 top-[73px] bottom-0 flex flex-col pt-6 bg-neutral-950 h-full w-64 border-r border-cyan-900/30 hidden md:flex before:content-[''] before:absolute before:inset-0 before:bg-[linear-gradient(rgba(18,19,21,0)_50%,rgba(0,255,255,0.02)_50%)] before:bg-[length:100%_4px] z-40">
        <div class="px-6 mb-8 relative z-10">
          <h2 class="text-cyan-500 font-black font-['Space_Grotesk'] text-lg tracking-widest">SYSTEM_CTRL</h2>
          <p class="font-['Space_Grotesk'] text-xs font-medium text-neutral-500 mt-1">V.2.0.4-STABLE</p>
        </div>
        <nav class="flex flex-col w-full relative z-10">
          <a 
            v-for="item in sideNavItems" 
            :key="item.label"
            :href="item.href"
            class="font-['Space_Grotesk'] text-xs font-medium flex items-center chromatic-hover gap-3 px-4 py-3 hover:bg-neutral-900 hover:text-cyan-200 transition-all"
            :class="item.active 
              ? 'bg-cyan-500/10 text-cyan-400 border-r-2 border-cyan-400' 
              : 'text-neutral-600'"
          >
            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 0;">{{ item.icon }}</span>
            {{ item.label }}
          </a>
        </nav>
      </aside>

      <!-- Main Canvas -->
      <main class="flex-1 md:ml-64 p-gutter lg:p-margin relative scanline-bg bg-surface-dim min-h-full">
        
        <!-- Negotiation Form (when no data) -->
        <div v-if="!negotiationData" class="max-w-2xl mx-auto pt-lg">
          <div class="bg-surface-container border border-outline-variant p-lg">
            <h2 class="font-h2 text-h2 text-on-surface mb-lg">Start New Negotiation</h2>
            
            <form @submit.prevent="startNegotiation" class="flex flex-col gap-lg">
              <div>
                <label class="font-label-caps text-label-caps text-on-surface-variant block mb-sm">ITEM NAME</label>
                <input 
                  v-model="form.item"
                  type="text" 
                  placeholder="e.g., Bored Ape Yacht Club #4211"
                  class="w-full bg-surface-container-low border border-outline-variant text-on-surface px-md py-sm rounded-DEFAULT focus:border-primary-container focus:outline-none"
                />
              </div>
              
              <div class="grid grid-cols-1 md:grid-cols-3 gap-md">
                <div>
                  <label class="font-label-caps text-label-caps text-on-surface-variant block mb-sm">START PRICE</label>
                  <input 
                    v-model.number="form.start_price"
                    type="number" 
                    step="0.01"
                    placeholder="0.00"
                    class="w-full bg-surface-container-low border border-outline-variant text-on-surface px-md py-sm rounded-DEFAULT focus:border-primary-container focus:outline-none"
                  />
                </div>
                <div>
                  <label class="font-label-caps text-label-caps text-on-surface-variant block mb-sm">MIN PRICE</label>
                  <input 
                    v-model.number="form.min_price"
                    type="number" 
                    step="0.01"
                    placeholder="0.00"
                    class="w-full bg-surface-container-low border border-outline-variant text-on-surface px-md py-sm rounded-DEFAULT focus:border-primary-container focus:outline-none"
                  />
                </div>
                <div>
                  <label class="font-label-caps text-label-caps text-on-surface-variant block mb-sm">MAX PRICE</label>
                  <input 
                    v-model.number="form.max_price"
                    type="number" 
                    step="0.01"
                    placeholder="0.00"
                    class="w-full bg-surface-container-low border border-outline-variant text-on-surface px-md py-sm rounded-DEFAULT focus:border-primary-container focus:outline-none"
                  />
                </div>
              </div>
              
              <div>
                <label class="font-label-caps text-label-caps text-on-surface-variant block mb-sm">PERSONALITY</label>
                <select 
                  v-model="form.personality"
                  class="w-full bg-surface-container-low border border-outline-variant text-on-surface px-md py-sm rounded-DEFAULT focus:border-primary-container focus:outline-none"
                >
                  <option value="balanced">Balanced</option>
                  <option value="aggressive">Aggressive</option>
                  <option value="conservative">Conservative</option>
                </select>
              </div>
              
              <div v-if="error" class="text-error font-code-sm">{{ error }}</div>
              
              <button 
                type="submit" 
                :disabled="isLoading"
                class="bg-primary-container text-on-primary-container font-label-caps text-label-caps py-md px-lg rounded-DEFAULT chromatic-border-hover uppercase tracking-widest border border-transparent hover:bg-transparent hover:text-primary-container hover:border-primary-container transition-all duration-300 flex items-center justify-center gap-sm disabled:opacity-50"
              >
                <span v-if="isLoading" class="material-symbols-outlined text-[16px] animate-spin">sync</span>
                <span v-else class="material-symbols-outlined text-[16px]">play_arrow</span>
                {{ isLoading ? 'Processing...' : 'Start Negotiation' }}
              </button>
            </form>
          </div>
        </div>

        <!-- Results View (when data exists) -->
        <div v-else>
          <!-- Contextual Header -->
          <div class="mb-lg flex items-center justify-between relative z-10">
            <div>
              <div class="font-label-caps text-label-caps text-primary-container mb-unit flex items-center gap-sm">
                <span class="material-symbols-outlined text-[16px]">receipt_long</span>
                CONTRACT ID: {{ contractId }}
              </div>
              <h1 class="font-h2 text-h2 text-on-surface">Outcome Resolution</h1>
            </div>
            <div class="px-md py-sm border border-primary-container bg-primary-container/10 text-primary-container font-label-caps text-label-caps flex items-center gap-sm shadow-[0_0_12px_rgba(0,251,251,0.15)]">
              <span class="material-symbols-outlined text-[14px]">check_circle</span>
              {{ hasAgreement ? 'AGREEMENT REACHED' : 'NEGOTIATION FAILED' }}
            </div>
          </div>

          <!-- Hero Bento Grid -->
          <div class="grid grid-cols-1 lg:grid-cols-3 gap-gutter mb-xl relative z-10">
            <!-- Primary Outcome Card -->
            <div class="lg:col-span-2 bg-surface-container-low border border-outline-variant p-lg flex flex-col justify-between relative overflow-hidden group">
              <div class="absolute inset-0 bg-gradient-to-br from-primary-container/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
              <div class="mb-xl">
                <h3 class="font-label-caps text-label-caps text-on-surface-variant mb-md tracking-widest">FINAL SETTLEMENT PRICE</h3>
                <div class="font-h1 text-h1 text-primary-container drop-shadow-[0_0_24px_rgba(0,251,251,0.4)] flex items-baseline gap-md">
                  <span>{{ settlementPrice }}</span>
                  <span class="font-h3 text-h3 text-primary-fixed-dim">ETH</span>
                </div>
                <p class="font-code-sm text-code-sm text-outline mt-sm">Status: {{ negotiationData.status }}</p>
              </div>
              <div class="flex gap-md mt-auto pt-lg border-t border-surface-variant">
                <button class="flex-1 bg-primary-container text-on-primary-container chromatic-border-hover font-label-caps text-label-caps py-md px-lg rounded-DEFAULT uppercase tracking-widest border border-transparent hover:bg-transparent hover:text-primary-container hover:border-primary-container transition-all duration-300 chromatic-border-hover flex items-center justify-center gap-sm">
                  <span class="material-symbols-outlined text-[16px]">draw</span>
                  Finalize Contract
                </button>
                <button @click="resetNegotiation" class="flex-1 bg-surface-container text-on-surface font-label-caps text-label-caps py-md px-lg rounded-DEFAULT uppercase tracking-widest border border-outline-variant hover:border-secondary-container hover:text-secondary-container transition-all duration-300 chromatic-hover flex items-center justify-center gap-sm">
                  <span class="material-symbols-outlined text-[16px]">restart_alt</span>
                  New Negotiation
                </button>
              </div>
            </div>

            <!-- Asset & Counterparty Detail -->
            <div class="bg-surface-container border border-outline-variant p-lg flex flex-col gap-lg relative z-10">
              <div>
                <h4 class="font-label-caps text-label-caps text-on-surface-variant mb-sm border-b border-surface-variant pb-sm">ASSET TARGET</h4>
                <div class="font-body-md text-body-md text-on-surface font-semibold">{{ asset.name }}</div>
                <div class="font-code-sm text-code-sm text-outline mt-unit">{{ asset.standard }} • {{ asset.network }}</div>
              </div>
              <div>
                <h4 class="font-label-caps text-label-caps text-on-surface-variant mb-sm border-b border-surface-variant pb-sm">COUNTERPARTY NODE</h4>
                <div class="flex items-center gap-md">
                  <div class="w-10 h-10 bg-secondary-container/20 border border-secondary-container rounded-full flex items-center justify-center text-secondary-container font-code-sm">
                    {{ counterparty.id }}
                  </div>
                  <div>
                    <div class="font-code-sm text-code-sm text-secondary-fixed">{{ counterparty.name }}</div>
                    <div class="font-label-caps text-[10px] text-outline mt-xs">REPUTATION: {{ counterparty.reputation }}</div>
                  </div>
                </div>
              </div>
              <div class="mt-auto pt-md">
                <div class="w-full h-1 bg-surface-variant rounded-full overflow-hidden">
                  <div class="h-full bg-primary-container shadow-[0_0_8px_#00fbfb]" :style="{ width: confidenceScore + '%' }"></div>
                </div>
                <div class="font-label-caps text-[10px] text-primary-container text-right mt-sm tracking-widest">CONFIDENCE SCORE: {{ confidenceScore }}%</div>
              </div>
            </div>
          </div>

          <!-- Transcript Ledger -->
          <div class="bg-surface-container-lowest border border-outline-variant relative z-10">
            <div class="p-md border-b border-outline-variant flex items-center justify-between bg-surface-container-low">
              <h3 class="font-label-caps text-label-caps text-on-surface flex items-center gap-sm">
                <span class="material-symbols-outlined text-[16px]">terminal</span>
                NEGOTIATION HISTORY
              </h3>
              <span class="font-code-sm text-code-sm text-outline text-[12px]">Rounds: {{ negotiationData.rounds.length }}</span>
            </div>
            <div class="p-lg flex flex-col gap-sm font-code-sm text-code-sm overflow-y-auto max-h-[400px]">
              <div 
                v-for="(entry, index) in transcript" 
                :key="index"
                class="flex gap-md py-sm border-b border-surface-variant/50 hover:bg-surface-container-low transition-colors"
                :class="{
                  'bg-primary-container/5': index === transcript.length - 1 && hasAgreement,
                  'bg-secondary-container/5 border-l-2 border-primary-container': index === transcript.length - 1
                }"
              >
                <span class="text-outline w-24 shrink-0">[{{ entry.time }}]</span>
                <span 
                  class="w-32 shrink-0"
                  :class="entry.sender === 'LOCAL_NODE' ? 'text-primary-fixed' : 'text-secondary-fixed'"
                >
                  {{ entry.sender }}
                </span>
                <span 
                  class="text-on-surface"
                  :class="{
                    'font-bold': index === transcript.length - 1,
                    'text-error': entry.type === 'reject'
                  }"
                >
                  {{ entry.message }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </main> 
    </div>
  </div>
</template>

<style scoped>
.scanline-bg {
  position: relative;
}
.scanline-bg::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(transparent 50%, rgba(0, 251, 251, 0.03) 50%);
  background-size: 100% 4px;
  pointer-events: none;
  z-index: 0;
}
.chromatic-hover {
  transition: all 0.1s ease;
}

.chromatic-hover:hover {
  /* Red offset left, Cyan offset right */
  text-shadow: 
    -2px 0 0 rgba(255, 0, 255, 0.7), 
     2px 0 0 rgba(0, 251, 251, 0.7);
  transform: scale(1.02);
}

.chromatic-hover:active {
  /* Intense jitter on click */
  text-shadow: 
    -4px 1px 0 rgba(255, 0, 255, 0.9), 
     4px -1px 0 rgba(0, 251, 251, 0.9);
  transform: translate(-1px, 1px);
}

/* Border/Box Chromatic Aberration */
.chromatic-border-hover {
  transition: all 0.2s ease;
  position: relative;
}

.chromatic-border-hover:hover {
  box-shadow: 
    -3px 0 0 #fe00fe, 
     3px 0 0 #00fbfb;
}

.chromatic-border-hover:active {
  box-shadow: 
    -5px 2px 0 #fe00fe, 
     5px -2px 0 #00fbfb;
  transform: translateY(1px);
}

/* Optional: Glitch Animation for a "Live" feel */
@keyframes glitch-skew {
  0% { transform: skew(0deg); }
  20% { transform: skew(-1deg); }
  40% { transform: skew(1deg); }
  100% { transform: skew(0deg); }
}

.chromatic-border-hover:hover {
  animation: glitch-skew 0.3s infinite linear alternate-reverse;
}
</style>