<script lang="ts" setup>
import { computed } from 'vue';

import { UserCircleIcon, ExclamationCircleIcon } from '@heroicons/vue/24/solid';
import GPTIcon from './icon/GPTIcon.vue';
import { Role } from '../types';
import md from '../plugins/markdown-it';

interface Props {
  role: Role;
  content: string;
  generating?: boolean;
  errorMessage?: string;
}

const props = defineProps<Props>();

const parsedContent = computed<string>(() => {
  if (props.role === 'user') {
    return props.content;
  } else {
    return md.render(props.content);
  }
});
</script>

<template>
  <div
    :class="{
      'flex py-6 w-full': true,
      'bg-gray-50': role === 'assistant',
    }"
  >
    <div class="flex mx-auto gap-4 p-4 container">
      <div>
        <GPT-icon class="h-6 w-6" v-if="role === 'assistant'" />
        <user-circle-icon class="h-6 w-6" v-if="role === 'user'" />
      </div>
      <div class="w-[calc(100%-50px)] lg:w-[calc(100%-115px)]">
        <div
          v-if="errorMessage"
          class="flex flex-row items-center rounded-md bg-red-200 p-2 min-w-max text-red-700"
        >
          <exclamation-circle-icon class="h-4 w-4 mr-2" />
          {{ errorMessage }}
        </div>
        <span v-if="role === 'assistant'" v-html="parsedContent"></span>
        <span v-else>
          {{ parsedContent }}
        </span>
        <span v-show="generating" class="generating" />
      </div>
    </div>
  </div>
</template>

<style lang="css" scoped>
.generating {
  display: inline-block;
  width: 8px;
  height: 18px;
  vertical-align: text-top;
  background-color: #000;
  animation: blink 1s linear infinite;
}

@keyframes blink {
  0% {
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
</style>
