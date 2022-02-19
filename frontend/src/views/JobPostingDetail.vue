<template>
	<div>
		<div v-if="loading">
			<Button :loading="loading">Loading...</Button>
		</div>
		<div v-else-if="!loading && jobPosting">
			<div
				class="border-b border-gray-200 pb-5 sm:flex sm:items-center sm:justify-between"
			>
				<h3 class="text-lg font-medium leading-6 text-gray-900">
					{{ jobPosting.job_title }}
				</h3>
				<div class="mt-3 space-x-2 sm:mt-0 sm:ml-4">
					<Button
						role="button"
						class="inline-flex items-center rounded-md border border-transparent bg-sky-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-sky-700 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:ring-offset-2"
					>
						<PencilAltIcon
							class="-ml-1 mr-1 h-5 w-5"
							aria-hidden="true"
						/>
						Edit</Button
					>

					<Button
						type="primary"
						role="button"
						class="inline-flex items-center rounded-md border border-transparent bg-sky-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-sky-700 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:ring-offset-2"
					>
						<CheckIcon
							class="-ml-1 mr-1 h-5 w-5"
							aria-hidden="true"
						/>
						Publish</Button
					>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import Button from '../components/Button.vue';
import { PencilAltIcon, CheckIcon } from '@heroicons/vue/solid';

export default {
	props: ['id'],
	inject: ['$api'],
	data() {
		return {
			loading: false,
			jobPosting: null,
		};
	},
	mounted() {
		console.log('JobPostingDetail mounted');
		console.log(this.id);
		this.getJobPosting(this.id).then((response) => {
			this.jobPosting = response.data;
			this.loading = false;
		});
	},
	methods: {
		async getJobPosting(id) {
			this.loading = true;
			const response = await this.$api.get(`/job-postings/${id}`);
			this.loading = false;
			return response;
		},
	},
	components: { Button, CheckIcon, PencilAltIcon },
};
</script>
