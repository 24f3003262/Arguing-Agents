<script setup lang="ts">
// Logic for handling marketplace interactions can go here
</script>

<template>
  <div class="relative z-20">
    <header class="mb-xl border-b border-surface-variant pb-md flex justify-between items-end">
      <div>
        <h1 class="font-h1 text-on-surface mb-unit">Asset Exchange</h1>
        <p class="font-code-sm text-on-surface-variant">Procure resources for autonomous agent execution. Live market rates applied.</p>
      </div>
      <div class="flex items-center gap-md font-code-sm text-primary-container">
        <span class="w-2 h-2 rounded-full bg-primary-container animate-pulse"></span>
        MARKET: ONLINE
      </div>
    </header>

    <div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-gutter items-stretch">
      
      <article class="bg-surface-container-low border border-outline-variant p-lg flex flex-col h-full group relative overflow-hidden cyber-card-base">
        <div class="absolute top-0 right-0 p-unit bg-primary-container/10 border-b border-l border-outline-variant text-primary-container font-label-caps text-[10px]">TIER 1</div>
        <div class="mb-lg">
          <span class="material-symbols-outlined text-4xl text-primary-fixed-dim mb-sm block">memory</span>
          <h3 class="font-h3 text-on-surface">Neural Net Processors</h3>
          <p class="font-code-sm text-on-surface-variant mt-xs h-12 line-clamp-2">High-throughput tensor cores for deep learning inference.</p>
        </div>
        
        <div class="flex-1 grid grid-cols-2 gap-sm mb-lg font-code-sm border-t border-surface-variant pt-sm">
          <div>
            <div class="text-outline">Compute</div>
            <div class="text-on-surface font-bold">12.4 TFLOPS</div>
          </div>
          <div>
            <div class="text-outline">Latency</div>
            <div class="text-on-surface font-bold">~4ms</div>
          </div>
          <div class="col-span-2">
            <div class="text-outline">Availability</div>
            <div class="text-primary-container">99.98%</div>
          </div>
        </div>

        <div class="mt-auto flex items-center justify-between pt-md border-t border-surface-variant">
          <div class="font-h2 text-tertiary">2.5 <span class="font-body-md text-outline">ETH</span></div>
          <MarketplaceNegotiateLink variant="primary" class="negotiation-chromatic-btn glow-cyan" />
        </div>
      </article>

      <article class="bg-surface-container-low border border-outline-variant p-lg flex flex-col h-full group relative overflow-hidden cyber-card-base">
        <div class="absolute top-0 right-0 p-unit bg-primary-container/10 border-b border-l border-outline-variant text-primary-container font-label-caps text-[10px]">HIGH DEMAND</div>
        <div class="mb-lg">
          <span class="material-symbols-outlined text-4xl text-primary-fixed-dim mb-sm block">route</span>
          <h3 class="font-h3 text-on-surface">Logistics Arrays</h3>
          <p class="font-code-sm text-on-surface-variant mt-xs h-12 line-clamp-2">Optimized routing algorithms for supply chain management.</p>
        </div>
        
        <div class="flex-1 grid grid-cols-2 gap-sm mb-lg font-code-sm border-t border-surface-variant pt-sm">
          <div>
            <div class="text-outline">Nodes</div>
            <div class="text-on-surface font-bold">10,000+</div>
          </div>
          <div>
            <div class="text-outline">Update Freq</div>
            <div class="text-on-surface font-bold">Real-time</div>
          </div>
          <div class="col-span-2">
            <div class="text-outline">Protocol</div>
            <div class="text-on-surface">Dijkstra+</div>
          </div>
        </div>

        <div class="mt-auto flex items-center justify-between pt-md border-t border-surface-variant">
          <div class="font-h2 text-tertiary">1,200 <span class="font-body-md text-outline">USDC</span></div>
          <MarketplaceNegotiateLink variant="primary" class="negotiation-chromatic-btn glow-cyan" />
        </div>
      </article>

      <article class="bg-surface-container-low border border-outline-variant p-lg flex flex-col h-full group relative overflow-hidden cyber-card-base">
        <div class="mb-lg">
          <span class="material-symbols-outlined text-4xl text-primary-fixed-dim mb-sm block">cyclone</span>
          <h3 class="font-h3 text-on-surface">Compute Cycles</h3>
          <p class="font-code-sm text-on-surface-variant mt-xs h-12 line-clamp-2">Raw distributed processing power for general tasks.</p>
        </div>

        <div class="flex-1 grid grid-cols-2 gap-sm mb-lg font-code-sm border-t border-surface-variant pt-sm">
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
          <MarketplaceNegotiateLink variant="primary" class="negotiation-chromatic-btn glow-cyan" />
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