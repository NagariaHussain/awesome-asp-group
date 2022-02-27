<template>
	<div class="flex justify-center">
		<div class="flex flex-col px-3 mt-5">
			<label for="search" class="sr-only">Search</label>
			<div class="mt-1 relative rounded-md">
				<div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none" aria-hidden="true">
					<SearchIcon class="mr-3 h-4 w-4 text-gray-400" aria-hidden="true" />
				</div>
				<input type="text" v-on:keyup.enter="searching" name="search" id="search"
					   class="w-96 focus:ring-sky-500 focus:border-sky-500 block pl-9 sm:text-sm border-gray-300 rounded-md"
					   placeholder="Search" />
			</div>
		</div>
	</div>
	<div class="flex justify-center mt-5">
		<div class="flex flex-col basis-3/12 gap-4" v-if="published_jobs && published_jobs.length > 0">
			<div class="bg-white  py-8 px-4 shadow sm:rounded-lg sm:px-10" v-for="job in published_jobs"
				 :key="job.id">
				<div class="flex flex-row gap-3">
					<img class="w-12"
						 :src="job.department === 'Design'? 'src/assets/letter-d.png' : job.department === 'Leadership' ?
					'src/assets/letter-l.png' : job.department === 'Marketing' ?
					'src/assets/letter-m.png' : 'src/assets/letter-e.png'"
						 alt="department">
					<div class="font-semibold text-lg">
						<div class="">
							{{ job.job_title }}
						</div>
						<div class="text-gray-500 text-sm">{{ job.company_name ?? "Company-Name" }}, {{ job.location
							}}
						</div>
					</div>
				</div>
				<div class="mt-4">{{ shorten_description(job.description) }}</div>
				<div class="flex flex-row mt-5 content-center justify-between">
					<div class="flex flex-row text-gray-500" style="align-items: center">
						<div class="mr-1">
							<CalendarIcon class="h-5 w-5 flex-shrink-0" />
						</div>
						<div>
							{{ days_ago(job.created_at) != 0 ? days_ago(job.created_at) + " day(s) ago" : "Today" }}
						</div>
					</div>
					<div class="flex flex-row-reverse gap-2">
						<div>
							<Button type="primary" :class="applied_job_id.includes(job.id) ? 'disabled:opacity-50' : ''"
									:disabled="applied_job_id.includes(job.id)" @click="apply(job)">
								{{ applied_job_id.includes(job.id) ? "Applied" : "Apply" }}
							</Button>
						</div>
						<div>
							<Button type="secondary" @click="moreInfo(job)">More Info</Button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import api from "../libs/api";
import Button from "../components/Button.vue";
import {
	CalendarIcon,
	SearchIcon
} from "@heroicons/vue/outline";
import { mapStores } from "pinia";
import useUser from "../stores/useUser";

export default {
	data() {
		return {
			username: null,
			published_jobs: null,
			applied_job_id: []
		};
	},
	computed: {
		...mapStores(useUser)
	},
	mounted() {
		this.username = this.userStore.account.username;
		this.fetch_published_jobs("");
		this.fetch_applied_jobs();
	},
	methods: {
		async fetch_published_jobs(param) {
			const jobs = await api.get(`/job-published-postings?title=${param}`);
			this.published_jobs = jobs.data;
		},
		async fetch_applied_jobs() {
			const applied_jobs = await api.get(`v1/applied/${this.username}`);
			this.applied_job_id = applied_jobs.data.map(e => e.applied_job_id);
		},
		async apply(element) {
			const payload = { "username": this.username, "applied_job_id": element.id };
			await api.post(`v1/apply`, payload);
			this.applied_job_id.push(element.id);
		},
		async moreInfo(element) {
			console.log(element.target.value);
		},
		shorten_description(text) {
			if (text.length > 20) {
				text = text.substring(0, 250) + "...";
			}
			return text;
		},
		days_ago(val) {
			const now = new Date(Date.now());
			const date = new Date(val);
			const diff = Math.abs(now.getUTCDate() - date.getUTCDate());
			return diff;
		},
		async searching(e) {
			await this.fetch_published_jobs(e.target.value);
		}
	},
	components: {
		Button,
		CalendarIcon,
		SearchIcon
	}
};
</script>
