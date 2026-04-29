<template>
  <div class="min-h-screen flex flex-col overflow-x-hidden selection:bg-primary-container selection:text-on-primary-container bg-surface-dim">
    <header class="flex justify-between items-center w-full px-8 py-4 sticky top-0 z-50 bg-neutral-950/90 backdrop-blur-md border-b border-cyan-500/20 shadow-[0_4px_20px_rgba(0,255,255,0.05)] relative after:content-[''] after:absolute after:inset-0 after:bg-[linear-gradient(rgba(18,16,16,0)_50%,rgba(0,0,0,0.25)_50%),linear-gradient(90deg,rgba(255,0,0,0.06),rgba(0,255,0,0.02),rgba(0,0,255,0.06))] after:bg-[length:100%_2px,3px_100%] after:pointer-events-none">
      <div class="text-xl font-bold text-cyan-400 tracking-tighter italic z-10 font-['Space_Grotesk']">
        Arguing Agents?
      </div>
      
      <nav class="hidden md:flex gap-8 z-10">
        <NuxtLink 
          v-for="item in navItems" 
          :key="item.label" 
          :to="item.to"
          class="font-['Space_Grotesk'] uppercase tracking-widest text-sm transition-all duration-300 chromatic-hover"
          :class="isActive(item.to) ? 'text-cyan-400 border-b border-cyan-400 pb-1' : 'text-neutral-500 hover:text-neutral-300'"
        >
          {{ item.label }}
        </NuxtLink>
      </nav>

      <div class="z-10 hidden md:block">
        <AppConnectWalletButton variant="negotiation" />
      </div>
    </header>

    <div class="flex flex-1 relative w-full">
      <aside class="fixed left-0 top-[73px] bottom-0 flex flex-col pt-6 bg-neutral-950 h-full w-64 border-r border-cyan-900/30 hidden md:flex before:content-[''] before:absolute before:inset-0 before:bg-[linear-gradient(rgba(18,19,21,0)_50%,rgba(0,255,255,0.02)_50%)] before:bg-[length:100%_4px] z-40">
        <div class="px-6 mb-8 relative z-10">
          <h2 class="text-cyan-500 font-black font-['Space_Grotesk'] text-lg tracking-widest">SYSTEM_CTRL</h2>
          <p class="font-['Space_Grotesk'] text-xs font-medium text-neutral-500 mt-1">V.2.0.4-STABLE</p>
        </div>
        
        <nav class="flex flex-col w-full relative z-10">
          <NuxtLink
            v-for="item in sideNavItems"
            :key="item.label"
            :to="item.to"
            class="font-['Space_Grotesk'] text-xs font-medium flex items-center gap-3 px-4 py-3 transition-all chromatic-hover"
            :class="isActive(item.to) 
              ? 'bg-cyan-500/10 text-cyan-400 border-r-2 border-cyan-400' 
              : 'text-neutral-600 hover:bg-neutral-900 hover:text-cyan-200'"
          >
            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 0;">{{ item.icon }}</span>
            {{ item.label }}
          </NuxtLink>
        </nav>
      </aside>

      <main class="flex-1 md:ml-64 p-gutter lg:p-margin relative scanline-bg min-h-full">
        <slot />
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
const route = useRoute()

const navItems = [
  { label: 'Marketplace', to: '/marketplace' },
  { label: 'Negotiations', to: '/negotiation' },
  { label: 'Dashboard', to: '/' }
]

const sideNavItems = [
  { icon: 'sensors', label: 'Network Status', to: '#' },
  { icon: 'memory', label: 'Agent Nodes', to: '#' },
  { icon: 'shield_with_heart', label: 'Security Mesh', to: '#' },
  { icon: 'account_balance_wallet', label: 'Ledger', to: '/negotiation' }
]

const isActive = (path: string) => {
  if (path === '/') return route.path === '/'
  return route.path.startsWith(path)
}
</script>

<style>
/* 1. Base Scanline Overlay */
.scanline-bg::after {
  content: '';
  position: absolute;
  inset: 0;
  /* Use a slightly higher contrast for the lines */
  background: linear-gradient(
    rgba(18, 16, 16, 0) 50%,
    rgba(0, 251, 251, 0.04) 50%
  );
  background-size: 100% 4px;
  pointer-events: none;
  z-index: 10;
}

/* 2. Precise Text Chromatic Aberration */
.chromatic-hover {
  transition: all 0.1s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.chromatic-hover:hover {
  /* Magenta on left (-2px), Cyan on right (2px) */
  text-shadow: 
    -2px 0 0 rgba(254, 0, 254, 0.7), 
     2px 0 0 rgba(0, 251, 251, 0.7);
  transform: scale(1.01) translateX(1px);
}

/* 3. Intense Jitter on Click (The "Exact" Look) */
.chromatic-hover:active,
.chromatic-border-hover:active {
  text-shadow: 
    -4px 1px 0 rgba(254, 0, 254, 0.9), 
     4px -1px 0 rgba(0, 251, 251, 0.9);
  transform: translate(-1px, 1px);
  filter: brightness(1.2) contrast(1.1);
}

/* 4. Perfected Border Glitch */
.chromatic-border-hover {
  position: relative;
  transition: border 0.1s ease, box-shadow 0.1s ease;
  border: 1px solid rgba(0, 251, 251, 0.4);
}

.chromatic-border-hover:hover {
  border-color: transparent;
  /* Box shadow aberration matches text shadow offset */
  box-shadow: 
    -3px 0 0 rgba(254, 0, 254, 0.8), 
     3px 0 0 rgba(0, 251, 251, 0.8);
  animation: glitch-skew 0.3s infinite linear alternate-reverse;
}

/* 5. The Skew Jitter */
@keyframes glitch-skew {
  0% { transform: skew(0deg) translateX(0); }
  25% { transform: skew(-0.5deg) translateX(-1px); }
  75% { transform: skew(0.5deg) translateX(1px); }
  100% { transform: skew(0deg) translateX(0); }
}
</style>