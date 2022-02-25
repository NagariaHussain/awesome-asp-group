<template>
	<div>
		<div v-if="loading">
			<Button :loading="loading">Loading...</Button>
		</div>
		<div v-else-if="!loading && jobPosting">
			<div
				class="border-b border-gray-200 pb-5 sm:flex sm:items-center sm:justify-between"
			>
				<div class="gap-2">
					<h3 class="text-lg font-medium leading-6 text-gray-900">
						{{ jobPosting.job_title }}
					</h3>
					<h4 class="text-sm text-gray-600">
						{{ jobPosting.department }}
					</h4>
				</div>
				<div class="mt-3 space-x-2 sm:mt-0 sm:ml-4">
					<Button
						role="button"
					>
						Edit</Button
					>

					<Button
						v-if="!jobPosting.is_published"
						type="primary"
						role="button"
						:loading="publishLoading"
						@click="publishJobPosting"
						class="inline-flex items-center rounded-md border border-transparent bg-sky-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-sky-700 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:ring-offset-2"
					>
						Publish</Button
					>

					<Button
						v-else
						type="primary"
						role="button"
						:loading="publishLoading"
						@click="unlistJobPosting"
						class="inline-flex items-center rounded-md border border-transparent bg-sky-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-sky-700 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:ring-offset-2"
					>
						Unlist</Button
					>
				</div>
			</div>

			<div class="mt-3">
				<p class="text-base text-gray-500">
					<strong>Location: </strong>
					<span> {{ jobPosting.location }}</span>
				</p>
				<p class="text-base text-gray-500">
					<strong>Job Description: </strong>
					<span> {{ jobPosting.description }}</span>
				</p>
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
			publishLoading: false,
		};
	},
	mounted() {
		console.log('JobPostingDetail mounted');
		console.log(this.id);
		this.fetchJobPosting();
	},
	methods: {
		async fetchJobPosting() {
			this.loading = true;
			const response = await this.$api.get(`/job-postings/${this.id}`);
			this.loading = false;
			this.jobPosting = response.data;
		},
		async publishJobPosting() {
			this.publishLoading = true;
			const response = await this.$api.get(
				`/job-postings/${this.id}/publish`
			);
			this.publishLoading = false;
			this.fetchJobPosting();
			return response;
		},
		async unlistJobPosting() {
			this.publishLoading = true;
			const response = await this.$api.get(
				`/job-postings/${this.id}/unlist`
			);
			this.publishLoading = false;
			this.fetchJobPosting();
			return response;
		},
	},
	components: { Button, CheckIcon, PencilAltIcon },
};
</script>
