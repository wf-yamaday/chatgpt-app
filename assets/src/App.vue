<script setup lang="ts">
import { ref, reactive } from 'vue';
import ChatInput from './components/ChatInput.vue';
import TheHeader from './components/TheHeader.vue';
import ChatMessageItem from './components/ChatMessageItem.vue';

import { ChatMessage } from './types';

const query = ref<string>('');
const chats = reactive<ChatMessage[]>([]);

const read = async (
  reader: ReadableStreamDefaultReader,
  decoder: TextDecoder
): Promise<any> => {
  const { value, done } = await reader.read();
  if (done) {
    chats[chats.length - 1].generating = false;
    reader.releaseLock();
    return;
  }

  const chunk = decoder.decode(value, { stream: true });
  chats[chats.length - 1].content = chats[chats.length - 1].content + chunk;
  return read(reader, decoder);
};

const handleSubmit = async () => {
  const userMessage = query.value;
  query.value = '';
  chats.push({ role: 'user', content: userMessage });
  const messages = [...chats];
  chats.push({ role: 'assistant', content: '', generating: true });

  fetch('/api/chat/stream/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query: userMessage, messages }),
  })
    .then((res) => {
      if (!res.ok) {
        chats[chats.length - 1].generating = false;
        chats[
          chats.length - 1
        ].errorMessage = `Error ${res.status} ${res.statusText}`;
      }

      return res.body;
    })
    .then(async (stream) => {
      if (stream) {
        const decoder = new TextDecoder('utf-8');
        const reader = stream?.getReader();
        await read(reader, decoder);
      }
    })
    .catch((error) => {
      console.log(error);
      chats[chats.length - 1].generating = false;
      chats[chats.length - 1].errorMessage = 'Network Error';
    });
};
</script>

<template>
  <div class="min-h-screen flex flex-col">
    <the-header />
    <main class="flex-grow items-center">
      <div class="flex flex-col gap-4 w-full text-gray-800">
        <div
          v-show="chats.length === 0"
          class="mt-8 mx-auto w-4/5 p-4 rounded-lg bg-info"
        >
          <p class="mb-2 font-bold text-xl">New Chat</p>
          If you have any questions or something you'd like to talk about, feel
          free to start a conversation with me in the text area below.
        </div>

        <chat-message-item
          v-for="(chat, i) in chats"
          :key="i"
          :content="chat.content"
          :role="chat.role"
          :generating="chat.generating"
          :error-message="chat.errorMessage"
        />
      </div>
    </main>
    <chat-input @submit="handleSubmit" v-model="query" class="p-6" />
  </div>
</template>
