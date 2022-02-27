<template>
	<div class="flow-root">
		<ul role="list" class="-mb-8">
			<li
				v-for="(activityItem, activityItemIdx) in activity"
				:key="activityItem.id"
			>
				<div class="relative pb-8">
					<span
						v-if="activityItemIdx !== activity.length - 1"
						class="absolute top-5 left-5 -ml-px h-full w-0.5 bg-gray-200"
						aria-hidden="true"
					/>
					<div class="relative flex items-start space-x-3">
						<template v-if="activityItem.type === 'comment'">
							<div class="relative">
								<img
									class="flex h-10 w-10 items-center justify-center rounded-full bg-gray-400 ring-8 ring-white"
									:src="activityItem.imageUrl"
									alt=""
								/>

								<span
									class="absolute -bottom-0.5 -right-1 rounded-tl bg-white px-0.5 py-px"
								>
									<ChatAltIcon
										class="h-5 w-5 text-gray-400"
										aria-hidden="true"
									/>
								</span>
							</div>
							<div class="min-w-0 flex-1">
								<div>
									<div class="text-sm">
										<a
											:href="activityItem.person.href"
											class="font-medium text-gray-900"
											>{{ activityItem.person.name }}</a
										>
									</div>
									<p class="mt-0.5 text-sm text-gray-500">
										Commented {{ activityItem.date }}
									</p>
								</div>
								<div class="mt-2 text-sm text-gray-700">
									<p>
										{{ activityItem.comment }}
									</p>
								</div>
							</div>
						</template>
						<template
							v-else-if="activityItem.type === 'assignment'"
							condition="activityItem.type === 'assignment'"
						>
							<div>
								<div class="relative px-1">
									<div
										class="flex h-8 w-8 items-center justify-center rounded-full bg-gray-100 ring-8 ring-white"
									>
										<UserCircleIcon
											class="h-5 w-5 text-gray-500"
											aria-hidden="true"
										/>
									</div>
								</div>
							</div>
							<div class="min-w-0 flex-1 py-1.5">
								<div class="text-sm text-gray-500">
									<a
										:href="activityItem.person.href"
										class="font-medium text-gray-900"
										>{{ activityItem.person.name }}</a
									>
									{{ ' ' }}
									assigned
									{{ ' ' }}
									<a
										:href="activityItem.assigned.href"
										class="font-medium text-gray-900"
										>{{ activityItem.assigned.name }}</a
									>
									{{ ' ' }}
									<span class="whitespace-nowrap">{{
										activityItem.date
									}}</span>
								</div>
							</div>
						</template>
						<template
							v-else-if="activityItem.type === 'tags'"
							condition="activityItem.type === 'tags'"
						>
							<div>
								<div class="relative px-1">
									<div
										class="flex h-8 w-8 items-center justify-center rounded-full bg-gray-100 ring-8 ring-white"
									>
										<PaperClipIcon
											class="h-5 w-5 text-gray-500"
											aria-hidden="true"
										/>
									</div>
								</div>
							</div>
							<div class="min-w-0 flex-1 py-0">
								<div class="text-sm leading-8 text-gray-500">
									<span class="mr-0.5">
										<a
											:href="activityItem.person.href"
											class="font-medium text-gray-900"
											>{{ activityItem.person.name }}</a
										>
										{{ ' ' }}
										attached file
									</span>
									{{ ' ' }}
									<span class="mr-0.5">
										<template
											v-for="tag in activityItem.tags"
											:key="tag.name"
										>
											<a
												:href="tag.href"
												class="relative inline-flex items-center rounded-full border border-gray-300 px-3 py-0.5 text-sm"
											>
												<span
													class="font-medium text-gray-900"
													>{{ tag.name }}</span
												>
											</a>
											{{ ' ' }}
										</template>
									</span>
									<span class="whitespace-nowrap">{{
										activityItem.date
									}}</span>
								</div>
							</div>
						</template>
						<template
							v-else-if="activityItem.type === 'event'"
							condition="activityItem.type === 'event'"
						>
							<div>
								<div class="relative px-1">
									<div
										class="flex h-8 w-8 items-center justify-center rounded-full bg-gray-100 ring-8 ring-white"
									>
										<CalendarIcon
											class="h-5 w-5 text-gray-500"
											aria-hidden="true"
										/>
									</div>
								</div>
							</div>
							<div class="min-w-0 flex-1 py-1.5">
								<div class="text-sm text-gray-500">
									<a
										href="#"
										class="font-medium text-gray-900"
										>{{ activityItem.title }}</a
									>
									{{ ' ' }}
									started
									{{ ' ' }}

									<span class="whitespace-nowrap">{{
										activityItem.date
									}}</span>
								</div>
							</div>
						</template>
					</div>
				</div>
			</li>
		</ul>
	</div>
</template>

<script setup>
import {
	ChatAltIcon,
	UserCircleIcon,
	PaperClipIcon,
	ClockIcon,
	CalendarIcon,
} from '@heroicons/vue/solid';

const activity = [
	{
		id: 0,
		type: 'event',
		title: 'Round 1',
		date: '10 days ago',
	},
	{
		id: 1,
		type: 'comment',
		person: { name: "Sydel D'souza", href: '#' },
		imageUrl: 'https://frappe.io/files/sydel.jpg',
		comment:
			"The candidate has submitted the flask test. Let's schedule a call next week, Reema?",
		date: '6d ago',
	},
	{
		id: 2,
		type: 'assignment',
		person: { name: "Sydel D'souza", href: '#' },
		assigned: { name: 'Reema Mehta', href: '#' },
		date: '6d ago',
	},
	{
		id: 3,
		type: 'tags',
		person: { name: 'Reema Mehta', href: '#' },
		tags: [{ name: 'resume.pdf', href: '#', color: 'bg-emerald-500' }],
		date: '6h ago',
	},
	{
		id: 4,
		type: 'comment',
		person: { name: 'Rushabh Mehta', href: '#' },
		imageUrl: 'https://frappe.io/files/rushabhd82db2.jpg',
		comment: 'What do you think about the candidate @netchampfaris?',
		date: '2h ago',
	},
];
</script>
