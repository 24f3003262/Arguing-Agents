<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  variant?: 'primary' | 'secondary'
}>(), {
  variant: 'secondary'
})

const linkClass = computed(() => {
  if (props.variant === 'primary') {
    return 'bg-primary-container text-on-primary-fixed font-label-caps px-md py-sm border border-transparent group-hover:bg-primary-fixed group-hover:shadow-[0_0_10px_rgba(0,251,251,0.5)] transition-all'
  }

  return 'bg-surface-dim text-primary-container font-label-caps px-md py-sm border border-primary-container hover:bg-primary-container hover:text-on-primary-container transition-all cyber-hover-effect'
})
</script>

<template>
  <NuxtLink to="/negotiation" :class="linkClass">
    Negotiate
  </NuxtLink>
</template>
