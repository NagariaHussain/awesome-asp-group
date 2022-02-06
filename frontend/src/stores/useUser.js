import { defineStore } from 'pinia';
import api from '../libs/api';

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
		logout() {
			return api.get('/logout');
		},
		async fetchAccount() {
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
