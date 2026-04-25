/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./app.vue",
    "./components/**/*.{vue,js,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
  ],
  theme: {
    extend: {
      colors: {
        'primary-container': '#00fbfb', 
        'on-primary-container': '#000000',
        'primary-fixed': '#00fbfb',
        'primary-fixed-dim': '#00cccc',
        'secondary-container': '#fe00fe', 
        'secondary-fixed': '#fe00fe',
        'surface-dim': '#050505',
        'surface-container': '#0f0f0f',
        'surface-container-low': '#151515',
        'surface-container-lowest': '#020202',
        'on-surface': '#ffffff',
        'on-surface-variant': '#9ca3af',
        'outline': '#4b5563',
        'outline-variant': 'rgba(0, 251, 251, 0.2)',
        'error': '#ff0055',
      },
      spacing: {
        'unit': '4px',
        'sm': '8px',
        'md': '16px',
        'lg': '24px',
        'xl': '32px',
        'gutter': '24px',
        'margin': '40px',
      },
      borderRadius: {
        'DEFAULT': '2px', 
      }
    },
  },
  plugins: [],
}