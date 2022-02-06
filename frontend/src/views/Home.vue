<!-- This example requires Tailwind CSS v2.0+ -->
<template>
	<div class="grid grid-cols-4 gap-2">
		<nav class="space-y-1" aria-label="Sidebar">
			<router-link
				custom
				v-for="item in navigation"
				:key="item.name"
				:to="item.href"
				v-slot="{ href, isExactActive, navigate }"
			>
				<a
					@click="navigate"
					:href="href"
					:class="[
						isExactActive
							? 'bg-gray-100 text-gray-900'
							: 'text-gray-600 hover:bg-gray-50 hover:text-gray-900',
						'group flex items-center rounded-md px-3 py-2 text-sm font-medium',
					]"
					:aria-current="isExactActive ? 'page' : undefined"
				>
					<component
						:is="item.icon"
						:class="[
							item.current
								? 'text-gray-500'
								: 'text-gray-400 group-hover:text-gray-500',
							'-ml-1 mr-3 h-6 w-6 flex-shrink-0',
						]"
						aria-hidden="true"
					/>
					<span class="truncate">
						{{ item.name }}
					</span>
					<span
						v-if="item.count"
						:class="[
							item.current
								? 'bg-white'
								: 'bg-gray-100 group-hover:bg-gray-200',
							'ml-auto inline-block rounded-full py-0.5 px-3 text-xs',
						]"
					>
						{{ item.count }}
					</span>
				</a>
			</router-link>
		</nav>
		<div class="col-span-3 bg-slate-200 p-4">
			<router-view></router-view>
		</div>
	</div>
</template>

<script setup>
import {
	FolderIcon,
	HomeIcon,
	InboxIcon,
	UsersIcon,
} from '@heroicons/vue/outline';
import { reactive, onActivated } from 'vue';

const navigation = reactive([
	{
		name: 'Dashboard',
		href: '/',
		icon: HomeIcon,
		count: '5',
	},
	{
		name: 'Job Postings',
		href: '/postings',
		icon: UsersIcon,
	},
	{
		name: 'Applicants',
		href: '/applicants',
		icon: FolderIcon,
		count: '19',
	},
	{ name: 'Company', href: '/company', icon: InboxIcon, current: false },
]);

onActivated(() => {
	this.$router.replace({ path: '/dashboard' });
});
</script>
