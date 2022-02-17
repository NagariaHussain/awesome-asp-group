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

		async signup(userInfo) {
			let response = null;

			try {
				response = await api.post('/signup', userInfo);
			} catch (err) {
				throw err;
			}

			return this.fetchAccount();
		},
		logout() {
			return api.get('/logout');
		},
		async fetchAccount() {
			try {
				let { data } = await api.get('/account');
				if (data) {
					this.isLoggedIn = true;
					this.account.username = data.username;
					this.account.email = data.email;
					this.account.first_name = data.first_name;
					this.account.last_name = data.last_name;
					this.account.userType =
						data.profile.user_type === 'I'
							? 'Individual'
							: 'Company';
				}
			} catch (e) {
				console.error(e);
			}
		},
	},
});
