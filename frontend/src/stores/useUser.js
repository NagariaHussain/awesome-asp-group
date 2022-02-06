import { defineStore } from 'pinia';
import axios from 'axios';

const api = axios.create({
	baseURL: '/api/',
	headers: {
		'X-CSRFToken': getCSRFToken(),
	},
});

export default defineStore('user', {
	state: () => {
		return {
			account: {},
			isLoggedIn: false,
		};
	},
	actions: {
		async login(username, password) {
			await api.post('/login', { username, password });
			return this.fetchAccount();
		},
		async logout() {
			await api.get('/logout');
		},
		async fetchAccount() {
			console.log('fetchAccount');
			try {
				let accountData = await api.get('/account');
				if (accountData) {
					this.isLoggedIn = true;
					this.account.username = accountData.username;
					this.account.email = accountData.email;
					this.account.first_name = accountData.first_name;
				}
			} catch (e) {}
		},
	},
});

function getCSRFToken() {
	const cookie = Object.fromEntries(
		document.cookie
			.split('; ')
			.map((part) => part.split('='))
			.map((d) => [d[0], decodeURIComponent(d[1])])
	);

	return cookie.csrftoken;
}
