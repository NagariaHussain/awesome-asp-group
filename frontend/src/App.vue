<template>
	<div class="p-5">
		<h2>Job Listings:</h2>

		<ul v-if="jobListings" class="space-y-2 divide-y-2">
			<li v-for="jl in jobListings" :key="jl.id">
				<div>
					{{ jl.job_title }} - {{ jl.location }} -
					{{ jl.is_published }}
				</div>
				<button
					@click="publishJob(jl.id)"
					class="p-2 bg-indigo-400 text-white"
				>
					Publish
				</button>
			</li>
		</ul>
	</div>
</template>

<script>
export default {
	data() {
		return {
			jobListings: null,
		};
	},
	mounted() {
		this.$api
			.get("/")
			.then((d) => {
				console.log(d);
				this.jobListings = d.data;
			})
			.catch((e) => console.log(e));
	},
	inject: ["$api"],
	methods: {
		publishJob(id) {
			console.log("Publish job clicked.");
			this.$api
				.get(`/publish-jp/${id}`)
				.then((d) => {
					this.fetchData();
				})
				.catch((e) => console.log(e));
		},
		fetchData() {
			this.$api
				.get("/")
				.then((d) => {
					console.log(d);
					this.jobListings = d.data;
				})
				.catch((e) => console.log(e));
		},
	},
};
</script>
