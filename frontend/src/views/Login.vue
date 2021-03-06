<template>
	<div class="flex min-h-full flex-col justify-center py-12 sm:px-6 lg:px-8">
		<div class="sm:mx-auto sm:w-full sm:max-w-md">
			<h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
				Sign in to your account
			</h2>
		</div>

		<div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
			<div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
				<form class="space-y-6" @submit.prevent="login">
					<div>
						<label
							for="username"
							class="block text-sm font-medium text-gray-700"
						>
							Username
						</label>
						<div class="mt-1">
							<input
								v-model="username"
								id="username"
								name="username"
								type="text"
								autocomplete="username"
								required="true"
								class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-sky-500 focus:outline-none focus:ring-sky-500 sm:text-sm"
							/>
						</div>
					</div>

					<div>
						<label
							for="password"
							class="block text-sm font-medium text-gray-700"
						>
							Password
						</label>
						<div class="mt-1">
							<input
								v-model="password"
								id="password"
								name="password"
								type="password"
								autocomplete="current-password"
								required="true"
								class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-sky-500 focus:outline-none focus:ring-sky-500 sm:text-sm"
							/>
						</div>
					</div>

					<div>
						<button
							type="submit"
							class="flex w-full justify-center rounded-md border border-transparent bg-sky-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-sky-700 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:ring-offset-2"
							:disabled="loading"
						>
							<svg
								v-if="loading"
								class="-ml-1 mr-3 h-5 w-5 animate-spin text-white"
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
							>
								<circle
									class="opacity-25"
									cx="12"
									cy="12"
									r="10"
									stroke="currentColor"
									stroke-width="4"
								></circle>
								<path
									class="opacity-75"
									fill="currentColor"
									d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
								></path>
							</svg>
							Sign in
						</button>
					</div>
				</form>

				<div class="mt-6">
					<div class="relative">
						<div class="absolute inset-0 flex items-center">
							<div class="w-full border-t border-gray-300" />
						</div>
						<div class="relative flex justify-center text-sm">
							<span class="bg-white px-2 text-gray-500">
								Or
							</span>
						</div>
					</div>

					<div class="mt-6 grid items-center justify-center">
						<router-link
							to="/signup"
							v-slot="{ href, navigate }"
							custom
						>
							<a
								:href="href"
								@click.stop="navigate"
								role="button"
								class="inline-flex items-center rounded-md border border-transparent bg-sky-100 px-4 py-2 text-sm font-medium text-sky-700 hover:bg-sky-200 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:ring-offset-2"
							>
								Create an account
							</a>
						</router-link>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { mapStores } from 'pinia';
import useUser from '../stores/useUser';

export default {
	data() {
		return {
			username: '',
			password: '',
			loading: false,
		};
	},
	computed: {
		...mapStores(useUser),
	},
	methods: {
		async login() {
			this.loading = true;
			await this.userStore.login(this.username, this.password);
			this.loading = false;

			this.$router.push('/');
		},
	},
};
</script>
