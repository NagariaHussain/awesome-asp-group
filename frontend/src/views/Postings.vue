<template>
	<div>
		<p v-if="loading">Loading...</p>

		<div
			v-if="!loading && postings && postings.length === 0"
			class="text-center"
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				class="mx-auto h-12 w-12 text-gray-400"
				viewBox="0 0 24 24"
				fill="none"
				stroke="currentColor"
				stroke-width="2"
				stroke-linecap="round"
				stroke-linejoin="round"
			>
				<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
				<circle cx="12" cy="7" r="4" />
			</svg>
			<h3 class="mt-2 text-sm font-medium text-gray-900">
				No Job Listings
			</h3>
			<p class="mt-1 text-sm text-gray-500">
				Get started by creating a new one.
			</p>
			<div class="mt-6">
				<button
					type="button"
					class="inline-flex items-center rounded-md border border-transparent bg-sky-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-sky-700 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:ring-offset-2"
				>
					<PlusIcon class="-ml-1 mr-2 h-5 w-5" aria-hidden="true" />
					New Job Posting
				</button>
			</div>
		</div>

		<pre v-for="posting in postings" :key="posting.id">
			{{ posting }}
		</pre
		>
	</div>
</template>

<script>
import { PlusIcon } from '@heroicons/vue/solid';
export default {
	components: {
		PlusIcon,
	},
	data() {
		return {
			postings: null,
			loading: false,
		};
	},
	mounted() {
		this.fetchJobPostings();
	},
	inject: ['$api'],
	methods: {
		async fetchJobPostings() {
			this.loading = true;
			await this.$api.get('job-postings').then((response) => {
				this.postings = response.data;
			});
			this.loading = false;
		},
	},
};
</script>
