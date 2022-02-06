import './main.css';

import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import { createPinia } from 'pinia';

// Setup Vue Router
import { createRouter, createWebHistory } from 'vue-router';
import routes from './routes';
import useUser from './stores/useUser';

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

router.beforeEach(async (to, from, next) => {
	const accountStore = useUser();

	// Trying to visit login page
	if (to.meta.isLoginPage) {
		console.log('Visit login page');
		await accountStore.fetchAccount();

		if (accountStore.isLoggedIn) {
			next('/');
		} else {
			next();
		}
	} else if (to.meta.requiresAuth) {
		if (!accountStore.isLoggedIn) {
			next('/login');
		} else {
			next();
		}
	} else {
		next();
	}
});
