<script setup>
import { TabGroup, TabList, Tab, TabPanels, TabPanel } from '@headlessui/vue';

const tabs = [
	{ name: 'Applicant Information', href: '#', current: false },
	{ name: 'Interview', href: '#', current: true },
	{ name: 'Communication', href: '#', current: false },
	{ name: 'Onboarding', href: '#', current: false },
];
</script>

<template>
	<TabGroup>
		<TabList>
			<Tab v-slot="{ selected }" v-for="tab in tabs" :key="tab.name">
				<a
					:class="[
						selected
							? 'border-sky-500 text-sky-600'
							: 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700',
						'whitespace-nowrap border-b-2 py-4 px-1 text-sm font-medium',
					]"
					:aria-current="selected ? 'page' : undefined"
				>
					{{ tab.name }}
				</a>
			</Tab>
		</TabList>
		<TabPanels>
			<TabPanel v-for="tab in tabs" :key="tab.name">{{
				tab.name
			}}</TabPanel>
		</TabPanels>
	</TabGroup>
</template>
