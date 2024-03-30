// test-utils.js
import { render } from '@testing-library/vue';
import { createRouter, createWebHistory } from 'vue-router';
import { routes } from '../src/router';

function createTestRouter() {
  return createRouter({
    history: createWebHistory(),
    routes,
  });
}

// Custom render that includes Vue Router
export function renderWithRouter(ui: any, { route = '/', ...options } = {}) {
  const router = createTestRouter();

  // Ensure the router is in the correct state before rendering the UI
  router.push(route).catch(err => {});

  return render(ui, {
    global: {
      plugins: [router],
    },
    ...options,
  });
}
