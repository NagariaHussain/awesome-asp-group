<script setup>
import RoundEventsFeed from '../components/RoundEventsFeed.vue';
import Button from '../components/Button.vue';
import { CheckCircleIcon } from '@heroicons/vue/solid';

// TODO: Later, get these from the API
const steps = [
	{ name: 'Round 1: Resume Review', href: '#', status: 'complete' },
	{ name: 'Round 2: Flask Test', href: '#', status: 'current' },
	{ name: 'Round 3: Culture Fit', href: '#', status: 'upcoming' },
];
</script>

<template>
	<div class="grid grid-cols-1 md:grid-cols-3 xl:grid-cols-4">
		<div>
			<nav class="mb-3 flex" aria-label="Progress">
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

		<div class="col-span-2 xl:col-span-3">
			<Suspense>
				<!-- component with nested async dependencies -->
				<RoundEventsFeed :roundId="1" />
				<!-- loading state via #fallback slot -->
				<template #fallback>
					<Button :loading="true">Loading...</Button>
				</template>
			</Suspense>
		</div>
	</div>
</template>
