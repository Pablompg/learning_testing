import {createRouter, createWebHistory} from 'vue-router';
import Login from '../components/Login.vue';
import Welcome from '../components/Welcome.vue';
import NotFound from "@/components/NotFound.vue";

export const routes = [
  { path: '/', component: Login },
  { path: '/login', component: Login },
  { path: '/welcome', component: Welcome},
  // { path: '/', redirect: '/login' },
  { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound },
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});
