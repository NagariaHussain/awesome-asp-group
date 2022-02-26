<!-- This example requires Tailwind CSS v2.0+ -->
<template>
	<div v-if="!id">
		<Button :loading="true">Loading...</Button>
	</div>
	<div v-else class="mx-auto max-w-7xl md:px-3">
		<div>
			<nav aria-label="Back to dashboard">
				<router-link to="/" replace>
					<a
						class="flex cursor-pointer items-center text-sm font-medium text-gray-500 hover:text-gray-700"
					>
						<ChevronLeftIcon
							class="-ml-1 mr-1 h-5 w-5 flex-shrink-0 text-gray-400"
							aria-hidden="true"
						/>
						Back to dashboard
					</a>
				</router-link>
			</nav>
		</div>

		<div class="mt-2 md:flex md:items-center md:justify-between">
			<div class="min-w-0 flex-1">
				<h2
					class="text-2xl font-bold leading-7 text-gray-900 sm:truncate sm:text-3xl"
				>
					Application
					<span class="text-2xl text-slate-700/70"> #{{ id }} </span>
				</h2>
				<p class="mt-2">
					<Badge>In Progress</Badge>
				</p>
			</div>
			<div
				class="mt-4 flex flex-shrink-0 flex-col items-end md:mt-0 md:ml-4"
			>
				<Menu as="div" class="relative inline-block text-left">
					<div>
						<MenuButton
							class="inline-flex w-full justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:ring-offset-2 focus:ring-offset-gray-100"
						>
							Actions
							<ChevronDownIcon
								class="-mr-1 ml-2 h-5 w-5"
								aria-hidden="true"
							/>
						</MenuButton>
					</div>

					<transition
						enter-active-class="transition ease-out duration-100"
						enter-from-class="transform opacity-0 scale-95"
						enter-to-class="transform opacity-100 scale-100"
						leave-active-class="transition ease-in duration-75"
						leave-from-class="transform opacity-100 scale-100"
						leave-to-class="transform opacity-0 scale-95"
					>
						<MenuItems
							class="absolute right-0 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
						>
							<div class="py-1">
								<MenuItem v-slot="{ active }">
									<a
										href="#"
										:class="[
											active
												? 'bg-gray-100 text-gray-900'
												: 'text-gray-700',
											'block px-4 py-2 text-sm',
										]"
										>Put on hold</a
									>
								</MenuItem>
								<MenuItem v-slot="{ active }">
									<a
										href="#"
										:class="[
											active
												? 'bg-gray-100 text-gray-900'
												: 'text-gray-700',
											'block px-4 py-2 text-sm',
										]"
										>Proceed to offer</a
									>
								</MenuItem>
								<MenuItem v-slot="{ active }">
									<a
										href="#"
										:class="[
											active
												? 'bg-gray-100 text-gray-900'
												: 'text-gray-700',
											'block px-4 py-2 text-sm',
										]"
										>Disqualify</a
									>
								</MenuItem>
							</div>
						</MenuItems>
					</transition>
				</Menu>

				<p class="mt-3 text-sm">
					Applied for
					<a class="text-sky-600 hover:text-sky-800" href="#">
						<span>Software Engineer</span>
					</a>
				</p>
			</div>
		</div>

		<!-- Tabs -->
		<div class="mt-3">
			<div class="sm:hidden">
				<label for="tabs" class="sr-only">Select a tab</label>
				<!-- Use an "onChange" listener to redirect the user to the selected tab URL. -->
				<select
					id="tabs"
					name="tabs"
					class="block w-full rounded-md border-gray-300 py-2 pl-3 pr-10 text-base focus:border-sky-500 focus:outline-none focus:ring-sky-500 sm:text-sm"
				>
					<option
						v-for="tab in tabs"
						:key="tab.name"
						:selected="tab.current"
					>
						{{ tab.name }}
					</option>
				</select>
			</div>
			<div class="hidden sm:block">
				<div class="border-b border-gray-200">
					<nav class="-mb-px flex space-x-8" aria-label="Tabs">
						<a
							v-for="tab in tabs"
							:key="tab.name"
							:href="tab.href"
							:class="[
								tab.current
									? 'border-sky-500 text-sky-600'
									: 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700',
								'whitespace-nowrap border-b-2 py-4 px-1 text-sm font-medium',
							]"
							:aria-current="tab.current ? 'page' : undefined"
						>
							{{ tab.name }}
						</a>
					</nav>
				</div>
			</div>
		</div>

		<div class="grid grid-cols-1 pt-7 md:grid-cols-3">
			<!-- Vertical nav: should be inside the active tab component -->
			<div>
				<nav class="flex" aria-label="Progress">
					<ol role="list" class="space-y-6">
						<li v-for="step in steps" :key="step.name">
							<a
								v-if="step.status === 'complete'"
								:href="step.href"
								class="group"
							>
								<span class="flex items-start">
									<span
										class="relative flex h-5 w-5 flex-shrink-0 items-center justify-center"
									>
										<CheckCircleIcon
											class="h-full w-full text-sky-600 group-hover:text-sky-800"
											aria-hidden="true"
										/>
									</span>
									<span
										class="ml-3 text-sm font-medium text-slate-500 group-hover:text-slate-900"
										>{{ step.name }}</span
									>
								</span>
							</a>
							<a
								v-else-if="step.status === 'current'"
								:href="step.href"
								class="flex items-start"
								aria-current="step"
							>
								<span
									class="relative flex h-5 w-5 flex-shrink-0 items-center justify-center"
									aria-hidden="true"
								>
									<span
										class="absolute h-4 w-4 rounded-full bg-sky-200"
									/>
									<span
										class="relative block h-2 w-2 rounded-full bg-sky-600"
									/>
								</span>
								<span
									class="ml-3 text-sm font-medium text-sky-600"
									>{{ step.name }}</span
								>
							</a>
							<a v-else :href="step.href" class="group">
								<div class="flex items-start">
									<div
										class="relative flex h-5 w-5 flex-shrink-0 items-center justify-center"
										aria-hidden="true"
									>
										<div
											class="h-2 w-2 rounded-full bg-gray-300 group-hover:bg-gray-400"
										/>
									</div>
									<p
										class="ml-3 text-sm font-medium text-gray-500 group-hover:text-gray-900"
									>
										{{ step.name }}
									</p>
								</div>
							</a>
						</li>
					</ol>
				</nav>
			</div>

			<!-- Content for active interview round -->
			<div class="col-span-2"></div>
		</div>
	</div>
</template>

<script setup>
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue';
import { ChevronLeftIcon, ChevronDownIcon } from '@heroicons/vue/solid';
import Button from '../components/Button.vue';
import Badge from '../components/Badge.vue';
import { CheckCircleIcon } from '@heroicons/vue/solid';

const steps = [
	{ name: 'Round 1: Resume Review', href: '#', status: 'complete' },
	{ name: 'Round 2: Flask Test', href: '#', status: 'current' },
	{ name: 'Round 3: Culture Fit', href: '#', status: 'upcoming' },
];

const props = defineProps({
	id: String,
});

const tabs = [
	{ name: 'Applicant Information', href: '#', current: false },
	{ name: 'Interview', href: '#', current: true },
	{ name: 'Communication', href: '#', current: false },
	{ name: 'Onboarding', href: '#', current: false },
];
</script>
