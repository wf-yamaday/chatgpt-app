/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./templates/index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'primary': '#7286D3',
        'info': '#d7e7af'
      },
    },
  },
  plugins: [],
}

