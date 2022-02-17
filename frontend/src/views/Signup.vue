<template>
	<div class="flex min-h-full flex-col justify-center py-12 sm:px-6 lg:px-8">
		<div class="sm:mx-auto sm:w-full sm:max-w-md">
			<h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
				Sign up for a new account
			</h2>
		</div>

		<div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
			<div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
				<form class="space-y-6" @submit.prevent="signup">
					<div class="grid grid-cols-2 gap-2">
						<div>
							<label
								for="firstname"
								class="block text-sm font-medium text-gray-700"
							>
								First Name
							</label>
							<div class="mt-1">
								<input
									id="firstname"
									v-model="firstName"
									type="text"
									autocomplete="off"
									required="true"
									class="w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
								/>
							</div>
						</div>

						<div>
							<label
								for="username"
								class="block text-sm font-medium text-gray-700"
							>
								Last Name
							</label>
							<div class="mt-1">
								<input
									v-model="lastName"
									type="text"
									id="lastname"
									autocomplete="off"
									class="w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
								/>
							</div>
						</div>
					</div>

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
								type="text"
								autocomplete="off"
								required="true"
								class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
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
								type="password"
								autocomplete="off"
								required="true"
								class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
							/>
						</div>
					</div>

					<div>
						<label
							for="password"
							class="block text-sm font-medium text-gray-700"
						>
							Confirm Password
						</label>
						<div class="mt-1">
							<input
								v-model="passwordRepeat"
								name="password"
								type="password"
								autocomplete="none"
								required="true"
								class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
							/>
						</div>
					</div>

					<RadioGroup v-model="userType" class="mt-2">
						<RadioGroupLabel class="sr-only">
							Choose a user type
						</RadioGroupLabel>
						<div class="grid grid-cols-1 gap-3 sm:grid-cols-2">
							<RadioGroupOption
								as="template"
								v-for="option in userOptions"
								:key="option"
								:value="option"
								v-slot="{ active, checked }"
							>
								<div
									:class="[
										'cursor-pointer focus:outline-none',
										active
											? 'ring-2 ring-gray-500 ring-offset-2'
											: '',
										checked
											? 'border-transparent bg-gray-600 text-white hover:bg-gray-700'
											: 'border-gray-200 bg-white text-gray-900 hover:bg-gray-50',
										'flex items-center justify-center rounded-md border py-3 px-3 text-sm font-medium uppercase sm:flex-1',
									]"
								>
									<RadioGroupLabel as="p">
										{{ option }}
									</RadioGroupLabel>
								</div>
							</RadioGroupOption>
						</div>
					</RadioGroup>

					<div v-if="errorMessage" class="rounded-md bg-red-50 p-4">
						<div class="flex">
							<div class="flex-shrink-0">
								<XCircleIcon
									class="h-5 w-5 text-red-400"
									aria-hidden="true"
								/>
							</div>

							<div class="ml-2 text-sm text-red-700">
								{{ errorMessage }}
							</div>
						</div>
					</div>

					<div>
						<button
							type="submit"
							class="flex w-full justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
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
							Sign up
						</button>
					</div>
				</form>
			</div>
		</div>
	</div>
</template>

<script>
import { mapStores } from 'pinia';
import useUser from '../stores/useUser';
import { XCircleIcon } from '@heroicons/vue/solid';
import { RadioGroup, RadioGroupLabel, RadioGroupOption } from '@headlessui/vue';

export default {
	data() {
		return {
			username: '',
			password: '',
			firstName: '',
			lastName: '',
			passwordRepeat: '',
			loading: false,
			errorMessage: null,
			userOptions: ['Company', 'Individual'],
			userType: 'Company',
		};
	},

	components: {
		XCircleIcon,
		RadioGroup,
		RadioGroupLabel,
		RadioGroupOption,
	},

	computed: {
		...mapStores(useUser),
	},
	methods: {
		async signup() {
			const {
				username,
				password,
				passwordRepeat,
				firstName,
				lastName,
				userType,
			} = this;

			if (password !== passwordRepeat) {
				this.errorMessage = 'Passwords does not match';
				return;
			}

			this.loading = true;
			this.errorMessage = null;

			try {
				await this.userStore.signup({
					username,
					password,
					firstName,
					lastName,
					userType,
				});

				this.$router.push('/login');
			} catch (error) {
				this.errorMessage = this.getErrorMessage(error);
			} finally {
				this.loading = false;
			}

			this.loading = false;
		},

		getErrorMessage(error) {
			let message = '';
			console.log('Status code: ', Object.keys(error.response));
			let statusCode = error.response.status;

			if (statusCode === 500) {
				message = 'Internal server error';
			} else if (statusCode === 400) {
				const { data } = error.response;

				for (const key in data) {
					if (data.hasOwnProperty(key)) {
						message += `${data[key]}\n`;
					}
				}
			} else {
				message = 'Something went wrong';
			}

			return message;
		},
	},

	watch: {
		userType(newType) {
			console.log(newType);
		},
	},
};
</script>
