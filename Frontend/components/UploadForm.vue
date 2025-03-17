<template>
  <div class="bg-white p-6 rounded-lg shadow-md">
    <h2 class="text-2xl font-bold text-teal-600 mb-4">
      Beyin MR Görüntüsü Yükleme
    </h2>
    <form @submit.prevent="handleSubmit">
      <div class="mb-4">
        <label class="block mb-2 text-gray-700">Görüntü Seçin:</label>
        <input
          type="file"
          accept="image/*"
          @change="handleFileChange"
          class="w-full p-2 border border-gray-300 rounded"
        />
      </div>
      <div v-if="selectedFile" class="mb-4">
        <p class="text-gray-700">Seçilen dosya: {{ selectedFile.name }}</p>
        <img
          :src="previewUrl"
          v-if="previewUrl"
          class="mt-2 max-w-full h-auto max-h-64"
        />
      </div>
      <button
        type="submit"
        class="bg-teal-600 text-white py-2 px-4 rounded hover:bg-teal-700 disabled:opacity-50"
        :disabled="!selectedFile"
      >
        Analiz Et
      </button>
    </form>
    <div v-if="loading" class="mt-4 text-center">
      <p>İşleniyor...</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const selectedFile = ref<File | null>(null);
const previewUrl = ref<string | null>(null);
const loading = ref(false);

function handleFileChange(event: Event) {
  const input = event.target as HTMLInputElement;
  if (input.files && input.files.length > 0) {
    selectedFile.value = input.files[0];
    createPreview();
  }
}

function createPreview() {
  if (selectedFile.value) {
    const reader = new FileReader();
    reader.onload = (e) => {
      previewUrl.value = e.target?.result as string;
    };
    reader.readAsDataURL(selectedFile.value);
  }
}

function handleSubmit() {
  if (!selectedFile.value) return;

  loading.value = true;
  // Burada API entegrasyonu yapılacak
  setTimeout(() => {
    loading.value = false;
    // Sonuç işleme
  }, 2000);
}
</script>

<style scoped>
/* Form stillemesi */
</style>
