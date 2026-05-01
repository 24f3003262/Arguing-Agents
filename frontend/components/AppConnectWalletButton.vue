<script setup lang="ts">
import { computed } from 'vue'
import { useAccount, useConnect, useDisconnect } from '@wagmi/vue'

const props = withDefaults(defineProps<{
  variant?: 'marketplace' | 'negotiation'
}>(), {
  variant: 'marketplace'
})

const { address, isConnected, isConnecting } = useAccount()
const { connect, connectors } = useConnect()
const { disconnect } = useDisconnect()

const walletLabel = computed(() => {
  if (!address.value) return 'Connect Wallet'
  const value = address.value
  return `${value.slice(0, 6)}...${value.slice(-4)}`
})

const buttonClass = computed(() => {
  if (props.variant === 'negotiation') {
    return "font-['Space_Grotesk'] uppercase chromatic-border-hover tracking-widest text-sm text-cyan-400 border border-cyan-400 px-4 py-2 hover:bg-cyan-400/10 transition-colors"
  }

  return 'border border-cyan-400/50 bg-cyan-950/30 text-cyan-400 font-label-caps px-4 py-2 hover:bg-cyan-900/50 hover:border-cyan-400 transition-all shadow-[0_0_10px_rgba(0,255,255,0.1)] hover:shadow-[0_0_15px_rgba(0,255,255,0.3)] uppercase'
})

function handleClick() {
  if (isConnected.value) {
    disconnect()
    return
  }

  const connector = connectors.value[0]
  if (!connector) return
  connect({ connector })
}
</script>

<template>
  <button :class="buttonClass" @click="handleClick" :disabled="isConnecting">
    {{ isConnecting ? 'Connecting...' : walletLabel }}
  </button>
</template>
