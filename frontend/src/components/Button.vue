<template>
	<button
		v-if="type === 'primary'"
		:disabled="loading"
		type="button"
		class="inline-flex items-center rounded-md border border-transparent bg-sky-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-sky-700 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:ring-offset-2"
	>
		<!-- Animated Loading Spinner -->
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
		<slot> </slot>
	</button>

	<button
		v-else
		type="button"
		class="rounded-md border border-gray-300 bg-white py-2 px-4 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:ring-offset-2"
	>
		<slot> </slot>
	</button>
</template>

<script>
export default {
	props: {
		loading: {
			type: Boolean,
			default: false,
		},
		type: {
			type: String,
			default: 'secondary',
		},
	},
};
</script>
