<!-- This example requires Tailwind CSS v2.0+ -->
<template>
	<div class="overflow-hidden bg-white shadow sm:rounded-md">
		<ul role="list" class="divide-y divide-gray-200">
			<li v-for="position in postings" :key="position.id">
				<a href="#" class="block hover:bg-gray-50">
					<div class="flex items-center px-4 py-4 sm:px-6">
						<div
							class="min-w-0 flex-1 sm:flex sm:items-center sm:justify-between"
						>
							<div class="truncate">
								<div class="flex text-sm">
									<p
										class="truncate font-medium text-sky-600"
									>
										{{ position.job_title }}
									</p>
									<p
										class="ml-1 flex-shrink-0 font-normal text-gray-500"
									>
										in {{ position.department }}
									</p>
								</div>
								<div class="mt-2 flex">
									<div
										class="flex items-center text-sm text-gray-500"
									>
										<!-- Add Later -->
										<!-- <CalendarIcon
											class="mr-1.5 h-5 w-5 flex-shrink-0 text-gray-400"
											aria-hidden="true"
										/>
										<p>
											Closing on
											{{ ' ' }}
											<time
												:datetime="position.created_at"
											></time>
										</p> -->
									</div>
								</div>
							</div>
						</div>
						<!-- Add Later -->
						<div class="ml-5 flex-shrink-0">
							<p class="text-sm text-gray-600">
								{{ position.location }}
							</p>
							<!-- <ChevronRightIcon
								class="h-5 w-5 text-gray-400"
								aria-hidden="true"
							/> -->
						</div>
					</div>
				</a>
			</li>
		</ul>
	</div>
</template>

<script>
import { CalendarIcon, ChevronRightIcon } from '@heroicons/vue/solid';

export default {
	components: {
		CalendarIcon,
		ChevronRightIcon,
	},
	props: {
		postings: {
			type: Array,
			required: true,
		},
	},
};
</script>
