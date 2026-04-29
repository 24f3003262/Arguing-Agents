<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';

interface Contract {
  tx_hash: string;
  counterparty: string;
  asset_class: string;
  value: number;
  status: string;
  timestamp: string;
}

const contracts = ref<Contract[]>([]);
const isLoading = ref(true);
const error = ref('');

onMounted(async () => {
  try {
    const response = await axios.get('/api/contracts'); // Replace with actual API endpoint
    contracts.value = response.data;
  } catch (err) {
    error.value = 'Failed to load contract data.';
  } finally {
    isLoading.value = false;
  }
});
</script>

<template>
  <div class="pt-16 md:pl-64 min-h-screen bg-surface-lowest">
    <div class="p-gutter md:p-margin max-w-container-max mx-auto space-y-8">
      <!-- Header Section -->
      <div class="flex flex-col md:flex-row md:items-end justify-between border-b border-surface-variant pb-4 gap-4">
        <div>
          <h1 class="font-headline-lg text-primary uppercase tracking-tighter glitch-hover inline-block">Deal History</h1>
          <p class="font-code-label text-on-surface-variant mt-2 uppercase flex items-center gap-2">
            <span class="inline-block w-2 h-2 bg-tertiary-fixed-dim animate-pulse"></span>
            Archive // System_Query_Executed
          </p>
        </div>
        <div class="flex gap-4 font-code-label">
          <button class="bg-primary-container text-on-primary-container px-4 py-2 uppercase tracking-widest font-bold hover:shadow-[2px_0_0_#ff00ff,-2px_0_0_#00ffff] hover:translate-x-px hover:-translate-y-px transition-all">
            Export Data
          </button>
        </div>
      </div>

      <!-- Stats Bento Grid -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-unit">
        <div class="bg-surface-container-low border border-surface-variant p-6 glitch-card relative overflow-hidden group">
          <div class="font-code-label text-on-surface-variant uppercase mb-2">Total Volume (Settled)</div>
          <div class="font-headline-lg text-primary tracking-tighter">84,092</div>
          <div class="font-code-label text-tertiary-fixed mt-2 flex items-center gap-1">
            <span class="material-symbols-outlined text-[14px]">arrow_upward</span>
            +12.4% vs prev cycle
          </div>
        </div>
        <div class="bg-surface-container-low border border-surface-variant p-6 glitch-card relative overflow-hidden group">
          <div class="font-code-label text-on-surface-variant uppercase mb-2">Avg Closing Speed</div>
          <div class="font-headline-lg text-primary tracking-tighter">1.4s</div>
          <div class="font-code-label text-secondary mt-2 flex items-center gap-1">
            <span class="material-symbols-outlined text-[14px]">arrow_downward</span>
            -0.2s latency drop
          </div>
        </div>
        <div class="bg-surface-container-low border border-surface-variant p-6 glitch-card relative overflow-hidden group">
          <div class="font-code-label text-on-surface-variant uppercase mb-2">Disputed Contracts</div>
          <div class="font-headline-lg text-primary tracking-tighter">03</div>
          <div class="font-code-label text-error mt-2 flex items-center gap-1">
            <span class="material-symbols-outlined text-[14px]">warning</span>
            Requires Operator Review
          </div>
        </div>
      </div>

      <!-- Data Table Section -->
      <div class="bg-surface-container border border-surface-variant overflow-hidden">
        <div class="border-b border-surface-variant p-4 flex justify-between items-center bg-surface-container-high">
          <div class="font-code-label text-primary uppercase tracking-widest font-bold">Contract Ledger</div>
          <div class="flex gap-2 font-code-label">
            <input
              class="bg-surface text-on-surface border-b border-surface-variant border-t-0 border-l-0 border-r-0 focus:ring-0 focus:border-primary-fixed focus:bg-surface-bright placeholder:text-tertiary-fixed/50 font-mono text-xs w-48 transition-colors"
              placeholder="SEARCH_HASH..."
              type="text"
            />
            <button class="text-surface-variant hover:text-primary transition-colors">
              <span class="material-symbols-outlined text-xl">filter_alt</span>
            </button>
          </div>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse font-body-sm">
            <thead>
              <tr class="font-code-label text-on-surface-variant border-b border-surface-variant bg-surface-container">
                <th class="p-4 font-normal uppercase">Tx_Hash</th>
                <th class="p-4 font-normal uppercase">Counterparty</th>
                <th class="p-4 font-normal uppercase">Asset Class</th>
                <th class="p-4 font-normal uppercase">Value (Units)</th>
                <th class="p-4 font-normal uppercase">Status</th>
                <th class="p-4 font-normal uppercase text-right">Timestamp</th>
              </tr>
            </thead>
            <tbody class="font-mono text-sm">
              <tr
                v-for="contract in contracts"
                :key="contract.tx_hash"
                class="border-b border-surface-variant/50 hover:bg-surface-bright glitch-hover group cursor-crosshair transition-colors"
              >
                <td class="p-4 text-primary-fixed group-hover:text-primary transition-colors">{{ contract.tx_hash }}</td>
                <td class="p-4 text-on-surface font-body-sm">{{ contract.counterparty }}</td>
                <td class="p-4 text-on-surface-variant">{{ contract.asset_class }}</td>
                <td class="p-4 text-primary font-bold">{{ contract.value }}</td>
                <td class="p-4">
                  <span
                    :class="{
                      'inline-block px-2 py-1 text-xs font-code-label uppercase': true,
                      'bg-tertiary-fixed-dim/10 border border-tertiary-fixed-dim text-tertiary-fixed-dim': contract.status === 'Settled',
                      'bg-error/10 border border-error text-error animate-[pulse_2s_infinite]': contract.status === 'Disputed',
                    }"
                  >
                    {{ contract.status }}
                  </span>
                </td>
                <td class="p-4 text-on-surface-variant text-right">{{ contract.timestamp }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- Pagination Footer -->
        <div
          class="border-t border-surface-variant p-4 flex justify-between items-center bg-surface-container-high font-code-label text-on-surface-variant"
        >
          <div>Showing [ 1 - 5 ] of [ 4,208 ] Records</div>
          <div class="flex gap-2">
            <button
              class="px-2 py-1 border border-surface-variant hover:border-primary-fixed hover:text-primary-fixed transition-colors disabled:opacity-50"
              disabled
            >
              &lt; PREV
            </button>
            <button
              class="px-2 py-1 border border-surface-variant hover:border-primary-fixed hover:text-primary-fixed transition-colors"
            >
              NEXT &gt;
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Add any additional scoped styles here */
</style>