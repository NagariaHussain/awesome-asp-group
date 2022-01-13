<template>
	<div class="p-5">
		<h2>Job Listings:</h2>

		<ul v-if="jobListings">
			<li v-for="jl in jobListings" :key="jl.id">{{ jl.job_title }}</li>
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
};
</script>
