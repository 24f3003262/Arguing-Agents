<script setup lang="ts">
interface NavItem {
  label: string
  to: string
}

defineProps<{
  items: NavItem[]
  containerClass: string
  baseClass: string
  activeClass: string
  inactiveClass: string
}>()
</script>

<template>
  <nav :class="containerClass">
    <NuxtLink
      v-for="item in items"
      :key="item.label"
      :to="item.to"
      custom
      v-slot="{ href, navigate, isExactActive }"
    >
      <a
        :href="href"
        @click="navigate"
        :class="[baseClass, isExactActive ? activeClass : inactiveClass]"
      >
        {{ item.label }}
      </a>
    </NuxtLink>
  </nav>
</template>
