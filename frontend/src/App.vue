<template>
	<div>
		<Navbar />
		<!-- route outlet -->
		<!-- component matched by the route will render here -->
		<div class="mx-3 mt-3">
			<router-view></router-view>
		</div>
	</div>
</template>

<script>
import Navbar from './components/Navbar.vue';
import useUser from './stores/useUser';
import { mapStores } from 'pinia';

export default {
	data() {
		return {};
	},
	mounted() {
		this.userStore.fetchAccount();
	},
	computed: {
		...mapStores(useUser),
	},
	inject: ['$api'],
	methods: {},
	components: { Navbar },
};
</script>
