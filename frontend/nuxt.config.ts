// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },

  plugins: ['~/plugins/wagmi.ts'],

  //Tailwind Module
  modules: ['@nuxtjs/tailwindcss'],

  //main CSS file 
  css: ['~/assets/css/main.css'],


  build: {
    transpile: ['@wagmi/vue', '@tanstack/vue-query', 'viem']
  },


  vite: {
    optimizeDeps: {
      include: [
        'eventemitter3',
        '@vue/devtools-core',
        '@vue/devtools-kit',
        'buffer',
        'process'
      ]
    }
  }
})