<script setup lang="ts">
import { computed, ref, watch } from 'vue';

interface Props {
  modelValue: string;
}

interface Emit {
  (e: 'update:modelValue', value: string): void;
  (e: 'submit'): void;
}

const props = defineProps<Props>();
const emits = defineEmits<Emit>();

const textareaElement = ref<HTMLTextAreaElement | null>(null);

const query = computed({
  get: () => props.modelValue,
  set: (val: string) => emits('update:modelValue', val),
});

const canSubmit = computed(() => {
  return props.modelValue.length > 0;
});

watch(query, () => {
  if (textareaElement.value) {
    textareaElement.value.style.height = 'auto';
    textareaElement.value.style.height = `${textareaElement.value.scrollHeight}px`;
  }
});

const handleSubmit = () => {
  if (canSubmit) {
    emits('submit');
  }
};

const handleTextareaKeydown = (event: KeyboardEvent) => {
  if (event.ctrlKey || event.metaKey) {
    handleSubmit();
  }
};
</script>

<template>
  <div>
    <form
      @submit.prevent="handleSubmit"
      class="flex flex-row items-end justify-center w-full h-max py-2 shadow-sm rounded-md border border-black/10 gap-2"
    >
      <div class="flex w-full min-h-[40px] items-center">
        <textarea
          ref="textareaElement"
          class="w-full pl-4 pr-2 resize-none bg-transparent focus:outline-0 focus:ring-0 focus-visible:ring-0 max-h-[200px] overflow-y-hidden"
          rows="1"
          v-model="query"
          @keydown.enter="handleTextareaKeydown"
          placeholder="Send a message..."
        />
      </div>
      <button
        class="h-10 px-4 py-2 mr-2 rounded-md bg-primary text-white disabled:bg-opacity-50 disabled:cursor-not-allowed"
        type="submit"
        :disabled="!canSubmit"
      >
        Send
      </button>
    </form>
    <p class="text-gray-700 text-sm mt-2 px-4">
      Press <kbd class="text-sm">Ctrl</kbd> +
      <kbd class="text-sm">Enter</kbd> or <kbd class="text-sm">Command</kbd> +
      <kbd class="text-sm">Enter</kbd> to submit.
    </p>
  </div>
</template>

<style scoped>
kbd {
  border-radius: 3px;
  padding: 1px 2px 0;
  border: 1px solid black;
}
</style>
