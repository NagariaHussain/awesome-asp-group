<template>
	<div
		:class="{
      'flex space-x-4': variant === 'horizontal',
    }"
	>
		<ul
			class="list-none  p-1.5 rounded-lg text-center overflow-auto whitespace-nowrap"
			:class="{
        'flex items-center mb-6': variant === 'vertical',
      }"
		>
			<li
				v-for="(tab, index) in tabList"
				:key="index"
				class="w-full px-4 py-1.5 rounded-lg"
				:class="{
          'text-slate-600 bg-white bg-slate-100': index + 1 === activeTab
        }"
			>
				<div class="flex py-2 justify-items-start">
					<component
						:is="tab.icon"
						:class="[
								activeTab
									? 'text-gray-500'
									: 'text-gray-400 group-hover:text-gray-500',
								'-ml-1 mr-3 h-6 w-6 flex-shrink-0',
							]"
						aria-hidden="true"
					/>
					<label
						:for="`${_uid}${index}`"
						v-text="tab.name"
						class="cursor-pointer w-full text-left block ml-3 text-slate-600"
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
		<template v-for="(tab, index) in tabList" class="ml-5">
			<div
				:key="index"
				v-if="index + 1 === activeTab"
				class="flex-grow bg-white rounded-lg  p-4"
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
			required: true
		},
		variant: {
			type: String,
			required: false,
			default: () => "vertical",
			validator: (value) => ["horizontal", "vertical"].includes(value)
		}
	},
	data() {
		return {
			activeTab: 1
		};
	}
};
</script>
