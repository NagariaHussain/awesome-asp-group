<template>
	<form @submit.prevent="saveJobPosting">
		<div
			class="border-b border-gray-200 pb-5 sm:flex sm:items-center sm:justify-between"
		>
			<h3 class="text-lg font-medium leading-6 text-gray-900">
				Job Postings
			</h3>
			<div class="mt-3 space-x-2 sm:mt-0 sm:ml-4">
				<Button @click="$router.push('/postings')"> Cancel </Button>

				<input
					role="button"
					type="submit"
					value="Save"
					class="inline-flex items-center rounded-md border border-transparent bg-sky-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-sky-700 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:ring-offset-2"
				/>
			</div>
		</div>

		<div class="space-y-6 sm:space-y-5">
			<div
				class="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:border-t sm:border-gray-200 sm:pt-5"
			>
				<label
					for="job-title"
					class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2"
				>
					Job Title
				</label>
				<div class="mt-1 sm:col-span-2 sm:mt-0">
					<input
						v-model="jobPosting.job_title"
						required
						type="text"
						name="job-title"
						id="job-title"
						class="block w-full max-w-lg rounded-md border-gray-300 shadow-sm focus:border-sky-500 focus:ring-sky-500 sm:max-w-xs sm:text-sm"
						placeholder="e.g. Senior Frontend Engineer"
					/>
				</div>
			</div>

			<div
				class="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:border-t sm:border-gray-200 sm:pt-5"
			>
				<label
					for="location"
					class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2"
				>
					Location
				</label>
				<div class="mt-1 sm:col-span-2 sm:mt-0">
					<input
						v-model="jobPosting.location"
						required
						type="text"
						name="location"
						id="location"
						autocomplete="false"
						class="block w-full max-w-lg rounded-md border-gray-300 shadow-sm focus:border-sky-500 focus:ring-sky-500 sm:max-w-xs sm:text-sm"
						placeholder="e.g. New York, NY"
					/>
				</div>
			</div>
			<div>
				<label
					for="description"
					class="block text-sm font-medium text-gray-700 sm:items-start sm:gap-4 sm:border-t sm:border-gray-200 sm:pt-5"
					>Add job description</label
				>
				<div class="mt-1">
					<textarea
						v-model="jobPosting.description"
						required
						rows="4"
						name="description"
						id="description"
						class="block w-full rounded-md border-gray-300 shadow-sm focus:border-sky-500 focus:ring-sky-500 sm:text-sm"
					/>
				</div>
			</div>
		</div>
	</form>
</template>

<script>
import Button from '../components/Button.vue';

export default {
	data() {
		return {
			jobPosting: {
				job_title: '',
				location: '',
				description: '',
			},
			loading: false,
		};
	},
	inject: ['$api'],
	components: {
		Button,
	},
	methods: {
		async saveJobPosting() {
			this.loading = true;
			let responseData = null;
			try {
				responseData = await this.$api.post(
					'/job-postings/new',
					this.jobPosting
				);
			} catch (e) {
				console.log(e.response);
				console.error('Something went wrong while saving.');
			}

			if (responseData) {
				this.$router.replace('/postings');
			}

			this.loading = false;
		},
	},
};
</script>
