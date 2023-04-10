import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  build: {
    manifest: true,
    emptyOutDir: true,
    assetsDir: '',
    rollupOptions: {
      input: './src/main.ts',
    },
  },

  server: {
    origin: 'http://127.0.0.1:8000',
  },
});
