<script setup lang="ts">
import { predictMR } from "~/store/model";

const prediction = ref<{
  prediction: string;
  probability: number;
  timestamp: string;
} | null>(null);

const file = ref<File | null>();
const loading = ref(false);
const error = ref<string | null>(null);

async function handleAnalysis(file: File) {
  loading.value = true;
  error.value = null;

  try {
    prediction.value = await predictMR(file);
  } catch (err) {
    error.value =
      "Analiz sırasında bir hata oluştu: " +
      (err instanceof Error ? err.message : err);
  } finally {
    loading.value = false;
  }
}
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <NavBar />

    <div class="container mx-auto py-8 px-4">
      <h1 class="text-4xl font-bold text-teal-600 mb-6">Model</h1>

      <UploadForm
        type="goruntu"
        @file-selected="(selectedFile) => (file = selectedFile)"
      />
      <UButton
        class="my-10 bg-teal-500 hover:bg-teal-400"
        size="xl"
        variant="outline"
        icon="ant-design-radius-setting-outlined"
        color="neutral"
        :loading="loading"
        :disabled="loading"
        @click="
          file ? handleAnalysis(file) : (error = 'Lütfen bir dosya seçin!')
        "
      >
        Analiz et
      </UButton>

      <!-- Sonuç Gösterimi -->
      <div
        v-if="prediction"
        class=" p-6 bg-white rounded-lg shadow-md text-black"
      >
        <h2 class="text-2xl font-semibold mb-4">Analiz Sonucu</h2>
        <div class="space-y-2">
          <p class="text-lg">
            <span class="font-medium">Tahmin:</span>
            <span
              :class="
                prediction.prediction === 'Sağlıklı'
                  ? 'text-green-600'
                  : 'text-red-600'
              "
            >
              {{ prediction.prediction }}
            </span>
          </p>
          <p class="text-lg">
            <span class="font-medium">Olasılık:</span>
            {{ (prediction.probability * 100).toFixed(2) }}%
          </p>
          <p class="text-lg">
            <span class="font-medium">Tarih:</span>
            {{ prediction.timestamp }}
          </p>
        </div>
      </div>

      <!-- Hata Mesajı -->
      <div v-if="error" class="mt-4 p-4 bg-red-100 text-red-700 rounded-lg">
        {{ error }}
      </div>
    </div>
  </div>
</template>
