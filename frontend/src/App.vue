<template>
	<div>
		<Navbar />
		<!-- route outlet -->
		<!-- component matched by the route will render here -->
		<router-view></router-view>
	</div>
</template>

<script>
import Navbar from './components/Navbar.vue';
export default {
	data() {
		return {
			jobListings: null,
		};
	},
	mounted() {
		this.$api
			.get('/')
			.then((d) => {
				console.log(d);
				this.jobListings = d.data;
			})
			.catch((e) => console.log(e));
	},
	inject: ['$api'],
	methods: {
		publishJob(id) {
			console.log('Publish job clicked.');
			this.$api
				.get(`/publish-jp/${id}`)
				.then((d) => {
					this.fetchData();
				})
				.catch((e) => console.log(e));
		},
		fetchData() {
			this.$api
				.get('/')
				.then((d) => {
					console.log(d);
					this.jobListings = d.data;
				})
				.catch((e) => console.log(e));
		},
	},
	components: { Navbar },
};
</script>
