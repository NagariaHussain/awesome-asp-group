import './main.css';

import App from './App.vue';
import { createApp } from 'vue';
import axiosApi from './libs/api';
import { createPinia } from 'pinia';
import useUser from './stores/useUser';

// Setup Vue Router
import routes from './routes';
import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
	history: createWebHistory(),
	routes,
});

const app = createApp(App);

app.use(router);
app.use(createPinia()); // Store
app.provide('$api', axiosApi); // API
app.mount('#app');

router.beforeEach(async (to, from, next) => {
	const accountStore = useUser();

	// Trying to visit login page
	if (to.meta.isLoginPage) {
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
