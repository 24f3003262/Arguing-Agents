<script setup lang="ts">
const navItems = [
  { label: 'Marketplace', to: '/marketplace' },
  { label: 'Negotiations', to: '/negotiation' },
  { label: 'Dashboard', to: '/' }
]

const navBaseClass = "font-['Space_Grotesk'] uppercase tracking-widest text-sm transition-all duration-300 hover:text-cyan-300 hover:shadow-[0_0_8px_#00FFFF]"
const navActiveClass = 'text-cyan-400 border-b border-cyan-400 pb-1 hover:text-cyan-300'
const navInactiveClass = 'text-neutral-500 hover:text-neutral-300'
</script>

<template>
  <div class="min-h-screen flex flex-col bg-background text-on-surface font-body-md antialiased">
    <!-- TopNavBar -->
    <nav class="bg-neutral-950/90 backdrop-blur-md docked full-width top-0 border-b border-cyan-500/20 shadow-[0_4px_20px_rgba(0,255,255,0.05)] relative flex justify-between items-center w-full px-8 py-4 sticky top-0 z-50">
      <div class="flex items-center gap-12">
        <div class="text-xl font-bold text-cyan-400 tracking-tighter italic font-['Space_Grotesk'] uppercase tracking-widest text-sm">
          NEGO_OS
        </div>
        <AppNavLinks
          :items="navItems"
          container-class="hidden md:flex items-center gap-8"
          :base-class="navBaseClass"
          :active-class="navActiveClass"
          :inactive-class="navInactiveClass"
        />
      </div>
      <div class="flex items-center gap-6 z-10 relative">
        <button class="text-neutral-500 hover:text-cyan-300 transition-colors">
          <span class="material-symbols-outlined">search</span>
        </button>
        <AppConnectWalletButton />
      </div>
    </nav>
    <div class="flex flex-1 relative overflow-hidden">
      <!-- SideNavBar -->
      <aside class="hidden md:flex bg-neutral-950 docked left-0 h-full w-64 border-r border-cyan-900/30 fixed left-0 top-[73px] bottom-0 flex flex-col pt-6 z-40 before:content-[''] before:absolute before:inset-0 before:bg-[linear-gradient(rgba(18,19,21,0)_50%,rgba(0,255,255,0.02)_50%)] before:bg-[length:100%_4px]">
        <div class="px-6 mb-8 z-10 relative">
          <div class="text-cyan-500 font-black font-['Space_Grotesk'] tracking-wider">SYSTEM_CTRL</div>
          <div class="text-[10px] text-neutral-500 font-['JetBrains_Mono'] mt-1">V.2.0.4-STABLE</div>
        </div>
        <nav class="flex flex-col gap-1 z-10 relative w-full">
          <a class="font-['Space_Grotesk'] text-xs font-medium text-neutral-600 flex items-center gap-3 px-4 py-3 hover:bg-neutral-900/50 hover:text-cyan-200 transition-all" href="#"><span class="material-symbols-outlined text-sm">sensors</span>Network Status</a>
          <a class="font-['Space_Grotesk'] text-xs font-medium text-neutral-600 flex items-center gap-3 px-4 py-3 hover:bg-neutral-900/50 hover:text-cyan-200 transition-all" href="#"><span class="material-symbols-outlined text-sm">memory</span>Agent Nodes</a>
          <a class="font-['Space_Grotesk'] text-xs font-medium text-neutral-600 flex items-center gap-3 px-4 py-3 hover:bg-neutral-900/50 hover:text-cyan-200 transition-all" href="#"><span class="material-symbols-outlined text-sm">shield_with_heart</span>Security Mesh</a>
          <a class="font-['Space_Grotesk'] text-xs font-medium text-neutral-600 flex items-center gap-3 px-4 py-3 hover:bg-neutral-900/50 hover:text-cyan-200 transition-all" href="#"><span class="material-symbols-outlined text-sm">account_balance_wallet</span>Ledger</a>
        </nav>
      </aside>
      <!-- Main Content Canvas -->
      <main class="flex-1 md:ml-64 p-margin xl:p-xl relative scanlines bg-surface-container-lowest min-h-screen">
        <header class="mb-xl border-b border-surface-variant pb-md relative z-20 flex justify-between items-end">
          <div>
            <h1 class="font-h1 text-on-surface mb-unit">Asset Exchange</h1>
            <p class="font-code-sm text-on-surface-variant">Procure resources for autonomous agent execution. Live market rates applied.</p>
          </div>
          <div class="flex items-center gap-md font-code-sm text-primary-container">
            <span class="w-2 h-2 rounded-full bg-primary-container animate-pulse"></span>
            MARKET: ONLINE
          </div>
        </header>
        <!-- Grid Layout -->
        <div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-gutter relative z-20">
          <!-- Card 1: Neural Net Processors -->
          <article class="bg-surface-container-low border border-outline-variant p-lg cyber-hover-effect flex flex-col group relative overflow-hidden">
            <div class="absolute top-0 right-0 p-unit bg-primary-container/10 border-b border-l border-outline-variant text-primary-container font-label-caps">TIER 1</div>
            <div class="mb-lg">
              <span class="material-symbols-outlined text-4xl text-primary-fixed-dim mb-sm block">memory</span>
              <h3 class="font-h3 text-on-surface">Neural Net Processors</h3>
              <p class="font-code-sm text-on-surface-variant mt-xs">High-throughput tensor cores for deep learning inference.</p>
            </div>
            <div class="grid grid-cols-2 gap-sm mb-lg font-code-sm border-t border-surface-variant pt-sm">
              <div>
                <div class="text-outline">Compute</div>
                <div class="text-on-surface font-bold">12.4 TFLOPS</div>
              </div>
              <div>
                <div class="text-outline">Latency</div>
                <div class="text-on-surface font-bold">~4ms</div>
              </div>
              <div>
                <div class="text-outline">Availability</div>
                <div class="text-primary-container">99.98%</div>
              </div>
            </div>
            <div class="mt-auto flex items-center justify-between pt-md border-t border-surface-variant">
              <div class="font-h2 text-tertiary">2.5 <span class="font-body-md text-outline">ETH</span></div>
              <MarketplaceNegotiateLink variant="primary" />
            </div>
          </article>
          <!-- Card 2: Logistics Arrays -->
          <article class="bg-surface-container-low border border-outline-variant p-lg cyber-hover-effect flex flex-col group relative overflow-hidden">
            <div class="absolute top-0 right-0 p-unit bg-secondary/10 border-b border-l border-outline-variant text-secondary font-label-caps">HIGH DEMAND</div>
            <div class="mb-lg">
              <span class="material-symbols-outlined text-4xl text-secondary mb-sm block">route</span>
              <h3 class="font-h3 text-on-surface">Logistics Arrays</h3>
              <p class="font-code-sm text-on-surface-variant mt-xs">Optimized routing algorithms for supply chain management.</p>
            </div>
            <div class="grid grid-cols-2 gap-sm mb-lg font-code-sm border-t border-surface-variant pt-sm">
              <div>
                <div class="text-outline">Nodes</div>
                <div class="text-on-surface font-bold">10,000+</div>
              </div>
              <div>
                <div class="text-outline">Update Freq</div>
                <div class="text-on-surface font-bold">Real-time</div>
              </div>
              <div>
                <div class="text-outline">Protocol</div>
                <div class="text-on-surface">Dijkstra+</div>
              </div>
            </div>
            <div class="mt-auto flex items-center justify-between pt-md border-t border-surface-variant">
              <div class="font-h2 text-tertiary">1,200 <span class="font-body-md text-outline">USDC</span></div>
              <MarketplaceNegotiateLink />
            </div>
          </article>
          <!-- Card 3: Compute Cycles -->
          <article class="bg-surface-container-low border border-outline-variant p-lg cyber-hover-effect flex flex-col group relative overflow-hidden">
            <div class="mb-lg">
              <span class="material-symbols-outlined text-4xl text-tertiary-fixed mb-sm block">cyclone</span>
              <h3 class="font-h3 text-on-surface">Compute Cycles</h3>
              <p class="font-code-sm text-on-surface-variant mt-xs">Raw distributed processing power for general tasks.</p>
            </div>
            <div class="grid grid-cols-2 gap-sm mb-lg font-code-sm border-t border-surface-variant pt-sm">
              <div>
                <div class="text-outline">Allocation</div>
                <div class="text-on-surface font-bold">Dynamic</div>
              </div>
              <div>
                <div class="text-outline">Base Cost</div>
                <div class="text-on-surface font-bold">Spot</div>
              </div>
              <div class="col-span-2">
                <div class="text-outline">Cluster Size</div>
                <div class="text-on-surface">Scalable (1 - 100x)</div>
              </div>
            </div>
            <div class="mt-auto flex items-center justify-between pt-md border-t border-surface-variant">
              <div class="font-h2 text-tertiary">0.05 <span class="font-body-md text-outline">ETH/hr</span></div>
              <MarketplaceNegotiateLink />
            </div>
          </article>
        </div>
      </main>
    </div>
  </div>
</template>

<style scoped>
.cyber-hover-effect {
  transition: all 0.3s ease;
}
.cyber-hover-effect:hover {
  box-shadow: 2px 0 0 rgba(254, 0, 254, 0.4), -2px 0 0 rgba(0, 251, 251, 0.4), 0 0 15px rgba(0, 251, 251, 0.2);
  transform: translate(-1px, -1px);
}
.scanlines::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(rgba(18, 19, 21, 0) 50%, rgba(0, 251, 251, 0.02) 50%);
  background-size: 100% 4px;
  pointer-events: none;
  z-index: 10;
}
</style>
