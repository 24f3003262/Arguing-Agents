import { http, createConfig, cookieStorage, createStorage } from '@wagmi/vue'
import { mainnet, sepolia } from '@wagmi/vue/chains'
import { injected } from '@wagmi/vue/connectors'
import { WagmiPlugin } from '@wagmi/vue'
import { QueryClient, VueQueryPlugin } from '@tanstack/vue-query'

export default defineNuxtPlugin((nuxtApp) => {
  const config = createConfig({
    chains: [mainnet, sepolia],
    connectors: [injected()], // Connects to MetaMask/Agent Wallets
    storage: createStorage({
      storage: cookieStorage,
    }),
    transports: {
      [mainnet.id]: http(),
      [sepolia.id]: http(),
    },
  })

  const queryClient = new QueryClient()

  nuxtApp.vueApp.use(WagmiPlugin, { config })
  nuxtApp.vueApp.use(VueQueryPlugin, { queryClient })
})