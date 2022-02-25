<template>
	<div
		:class="{
			'grid grid-cols-5 space-x-4': variant === 'horizontal',
		}"
	>
		<ul
			class="list-none overflow-auto whitespace-nowrap rounded-lg p-1.5 text-center col-span-2"
			:class="{
				'mb-6 flex items-center': variant === 'vertical',
			}"
		>
			<li
				v-for="(tab, index) in tabList"
				:key="index"
				class="w-full rounded-lg py-1.5"
				:class="{
					'bg-slate-100 text-slate-600': index + 1 === activeTab,
				}"
			>
				<div class="flex justify-items-start py-2">
					<component
						:is="tab.icon"
						:class="[
							activeTab
								? 'text-gray-500'
								: 'text-gray-400 group-hover:text-gray-500',
							'h-5 w-5 flex-shrink-0',
						]"
						aria-hidden="true"
					/>
					<label
						:for="`${_uid}${index}`"
						v-text="tab.name"
						class="text-sm ml-3 block w-full cursor-pointer text-left text-slate-600"
					/>

					<input
						:id="`${_uid}${index}`"
						type="radio"
						:name="`${_uid}-tab`"
						:value="index + 1"
						v-model="activeTab"
						class="hidden"
					/>
				</div>
			</li>
		</ul>
		<template v-for="(tab, index) in tabList">
			<div
				:key="index"
				v-if="index + 1 === activeTab"
				class="flex-grow rounded-lg bg-white p-4 col-span-3"
			>
				<slot :name="`tabPanel-${index + 1}`" />
			</div>
		</template>
	</div>
</template>

<script>
export default {
	props: {
		tabList: {
			type: Array,
			required: true,
		},
		variant: {
			type: String,
			required: false,
			default: () => 'vertical',
			validator: (value) => ['horizontal', 'vertical'].includes(value),
		},
	},
	data() {
		return {
			activeTab: 1,
		};
	},
};
</script>
