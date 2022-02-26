<template>
	<span
		class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-100 text-emerald-800"
	>
		<slot></slot>
	</span>
</template>

<script setup>
const props = defineProps({
	type: {
		type: String,
		default: 'default',
	},
});
</script>
