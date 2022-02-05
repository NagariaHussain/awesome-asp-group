<!-- This example requires Tailwind CSS v2.0+ -->
<template>
	<Disclosure as="nav" class="bg-white shadow" v-slot="{ open }">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="flex h-16 justify-between">
				<div class="flex">
					<div class="flex flex-shrink-0 items-center">
						<img
							class="block h-8 w-auto lg:hidden"
							src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg"
							alt="Workflow"
						/>
						<img
							class="hidden h-8 w-auto lg:block"
							src="https://tailwindui.com/img/logos/workflow-logo-indigo-600-mark-gray-800-text.svg"
							alt="Workflow"
						/>
					</div>
					<div class="hidden sm:ml-6 sm:flex sm:space-x-8">
						<router-link
							v-for="navItem in navItems"
							:to="navItem.href"
							:key="navItem.href"
							v-slot="{ href, isActive }"
							custom
						>
							<a
								:href="href"
								class="inline-flex items-center border-b-2 px-1 pt-1 text-sm font-medium"
								:class="
									isActive
										? 'border-indigo-500 text-gray-900'
										: 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700'
								"
							>
								{{ navItem.name }}
							</a>
						</router-link>
					</div>
				</div>
				<div class="hidden sm:ml-6 sm:flex sm:items-center">
					<!-- Profile dropdown -->
					<Menu as="div" class="relative ml-3">
						<div>
							<MenuButton
								class="flex rounded-full bg-white text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
							>
								<span class="sr-only">Open user menu</span>
								<img
									class="h-8 w-8 rounded-full"
									src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
									alt=""
								/>
							</MenuButton>
						</div>
						<transition
							enter-active-class="transition ease-out duration-200"
							enter-from-class="transform opacity-0 scale-95"
							enter-to-class="transform opacity-100 scale-100"
							leave-active-class="transition ease-in duration-75"
							leave-from-class="transform opacity-100 scale-100"
							leave-to-class="transform opacity-0 scale-95"
						>
							<MenuItems
								class="absolute right-0 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
							>
								<MenuItem v-slot="{ active }">
									<a
										href="#"
										:class="[
											active ? 'bg-gray-100' : '',
											'block px-4 py-2 text-sm text-gray-700',
										]"
										>Your Profile</a
									>
								</MenuItem>
								<MenuItem v-slot="{ active }">
									<a
										href="#"
										:class="[
											active ? 'bg-gray-100' : '',
											'block px-4 py-2 text-sm text-gray-700',
										]"
										>Settings</a
									>
								</MenuItem>
								<MenuItem v-slot="{ active }">
									<a
										href="#"
										:class="[
											active ? 'bg-gray-100' : '',
											'block px-4 py-2 text-sm text-gray-700',
										]"
										>Sign out</a
									>
								</MenuItem>
							</MenuItems>
						</transition>
					</Menu>
				</div>
				<div class="-mr-2 flex items-center sm:hidden">
					<!-- Mobile menu button -->
					<DisclosureButton
						class="inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500"
					>
						<span class="sr-only">Open main menu</span>
						<MenuIcon
							v-if="!open"
							class="block h-6 w-6"
							aria-hidden="true"
						/>
						<XIcon
							v-else
							class="block h-6 w-6"
							aria-hidden="true"
						/>
					</DisclosureButton>
				</div>
			</div>
		</div>

		<DisclosurePanel class="sm:hidden">
			<div class="space-y-1 pt-2 pb-3">
				<!-- Current: "bg-indigo-50 border-indigo-500 text-indigo-700", Default: "border-transparent text-gray-500 hover:bg-gray-50 hover:border-gray-300 hover:text-gray-700" -->
				<DisclosureButton
					as="a"
					href="#"
					class="block border-l-4 border-indigo-500 bg-indigo-50 py-2 pl-3 pr-4 text-base font-medium text-indigo-700"
					>Home</DisclosureButton
				>
				<DisclosureButton
					as="a"
					href="#"
					class="block border-l-4 border-transparent py-2 pl-3 pr-4 text-base font-medium text-gray-500 hover:border-gray-300 hover:bg-gray-50 hover:text-gray-700"
					>Jobs</DisclosureButton
				>
				<DisclosureButton
					as="a"
					href="#"
					class="block border-l-4 border-transparent py-2 pl-3 pr-4 text-base font-medium text-gray-500 hover:border-gray-300 hover:bg-gray-50 hover:text-gray-700"
					>Support</DisclosureButton
				>
			</div>
			<div class="border-t border-gray-200 pt-4 pb-3">
				<div class="flex items-center px-4">
					<div class="flex-shrink-0">
						<img
							class="h-10 w-10 rounded-full"
							src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
							alt=""
						/>
					</div>
					<div class="ml-3">
						<div class="text-base font-medium text-gray-800">
							Tom Cook
						</div>
						<div class="text-sm font-medium text-gray-500">
							tom@example.com
						</div>
					</div>
				</div>
				<div class="mt-3 space-y-1">
					<DisclosureButton
						as="a"
						href="#"
						class="block px-4 py-2 text-base font-medium text-gray-500 hover:bg-gray-100 hover:text-gray-800"
						>Your Profile</DisclosureButton
					>
					<DisclosureButton
						as="a"
						href="#"
						class="block px-4 py-2 text-base font-medium text-gray-500 hover:bg-gray-100 hover:text-gray-800"
						>Settings</DisclosureButton
					>
					<DisclosureButton
						as="a"
						href="#"
						class="block px-4 py-2 text-base font-medium text-gray-500 hover:bg-gray-100 hover:text-gray-800"
						>Sign out</DisclosureButton
					>
				</div>
			</div>
		</DisclosurePanel>
	</Disclosure>
</template>

<script>
import {
	Disclosure,
	DisclosureButton,
	DisclosurePanel,
	Menu,
	MenuButton,
	MenuItem,
	MenuItems,
} from '@headlessui/vue';
import { BellIcon, MenuIcon, XIcon } from '@heroicons/vue/outline';

export default {
	components: {
		Disclosure,
		DisclosureButton,
		DisclosurePanel,
		Menu,
		MenuButton,
		MenuItem,
		MenuItems,
		BellIcon,
		MenuIcon,
		XIcon,
	},
	data() {
		return {
			navItems: [
				{
					name: 'Home',
					href: '/',
				},
				{
					name: 'Jobs',
					href: '/jobs',
				},
				{
					name: 'About Us',
					href: '/about',
				},
			],
		};
	},
};
</script>
