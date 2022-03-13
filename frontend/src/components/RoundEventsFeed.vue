<script setup>
import {
	ChatAltIcon,
	UserCircleIcon,
	PaperClipIcon,
	CalendarIcon,
} from '@heroicons/vue/solid';
import { inject, ref } from 'vue';
import { parseISO, formatDistanceToNow } from 'date-fns';
import TextareaInput from './TextareaInput.vue';

const api = inject('$api');
const loading = ref(false);
const props = defineProps({
	roundId: Number,
});
const commentValue = ref('');

let activity = ref(null);
let round = ref(null);

async function fetchRoundDetails() {
	const roundDetails = await api.get(`/interview/rounds/${props.roundId}`);
	activity.value = roundDetails.data.interview_events;
	round.value = roundDetails.data.interview_round;
}

// Fetch for the first time
await fetchRoundDetails();

function getSenderName(communication) {
	return `${communication.sender.first_name} ${communication.sender.last_name}`;
}

function getFormattedRelativeDate(dateString) {
	return formatDistanceToNow(parseISO(dateString));
}

async function commentSubmitted() {
	loading.value = true;

	try {
		await api.post('/interview/post_comment', {
			comment: commentValue.value,
		});
		loading.value = false;
		await fetchRoundDetails();
		commentValue.value = '';
	} catch (e) {
		console.error(e);
		loading.value = false;
	}
}
</script>

<template>
	<div class="flow-root">
		<ul role="list" class="-mb-8">
			<li
				v-for="(activityItem, activityItemIdx) in activity"
				:key="activityItem.id"
			>
				<div
					class="relative pb-8"
					v-if="
						[
							'internal_comment',
							'file_attached',
							'started',
						].includes(activityItem.type)
					"
				>
					<span
						v-if="activityItemIdx !== activity.length - 1"
						class="absolute top-5 left-5 -ml-px h-full w-0.5 bg-gray-200"
						aria-hidden="true"
					/>
					<div class="relative flex items-start space-x-3">
						<template
							v-if="
								activityItem.type === 'internal_comment' &&
								activityItem.communication
							"
						>
							<div class="relative">
								<img
									class="flex h-10 w-10 items-center justify-center rounded-full bg-gray-400 ring-8 ring-white"
									src="
										https://frappe.io/files/reema%202019-01-08%2014:48:53.JPG
									"
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
											:href="`/users/${activityItem.communication.sender.username}`"
											class="font-medium text-gray-900"
											>{{
												getSenderName(
													activityItem.communication
												)
											}}</a
										>
									</div>
									<p class="mt-0.5 text-sm text-gray-500">
										Commented
										{{
											getFormattedRelativeDate(
												activityItem.created_at
											)
										}}
										ago
									</p>
								</div>
								<div class="mt-2 text-sm text-gray-700">
									<p>
										{{ activityItem.communication.body }}
									</p>
								</div>
							</div>
						</template>
						<template v-else-if="activityItem.type === 'started'">
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
										>{{ round.name }}</a
									>
									{{ ' ' }}
									started
									{{ ' ' }}

									<span class="whitespace-nowrap">{{
										getFormattedRelativeDate(
											activityItem.created_at
										)
									}}</span>
								</div>
							</div>
						</template>

						<!-- <template v-else>
							<pre>{{ activityItem }}</pre>
						</template> -->
					</div>
				</div>
			</li>
		</ul>
	</div>

	<TextareaInput
		v-model="commentValue"
		@submit="commentSubmitted"
		:loading="loading"
		class="my-12"
	/>
</template>
