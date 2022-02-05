import './main.css';

import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';

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
app.provide('$api', api);
app.mount('#app');
