import { defineStore } from 'pinia';
import axios from 'axios';

const api = axios.create({
	baseURL: '/api/',
});

export default defineStore('user', {
	state: () => {
		return {
			account: {},
			isLoggedIn: false,
		};
	},
	actions: {
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
