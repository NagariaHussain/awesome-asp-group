import './main.css';

import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import { createPinia, defineStore } from 'pinia';

// Setup Vue Router
import { createRouter, createWebHistory } from 'vue-router';
import routes from './routes';

const router = createRouter({
	history: createWebHistory(),
	routes,
});
const api = axios.create({
	baseURL: '/api/',
});
const app = createApp(App);

app.use(router);
app.use(createPinia()); // Store
app.provide('$api', api);
app.mount('#app');

export const useAccountInfo = defineStore('account', {
	state: () => {
		return {
			isLoggedIn: false,
			user: {
				username: null,
				email: null,
			},
		};
	},
});

router.beforeEach((to, from, next) => {
	const accountStore = useAccountInfo();

	if (to.meta.requiresAuth && !accountStore.isLoggedIn) {
		next('/login');
	} else {
		next();
	}
});
