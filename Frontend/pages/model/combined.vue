<script setup lang="ts">
import { ref } from "vue";
import { predictionCombined } from "~/store/model";

const prediction = ref<{
  prediction: string;
  probability: number;
  handwriting_probability: number;
  mr_probability: number;
  timestamp: string;
} | null>(null);

const fileHandwritting = ref<File | null>(null);
const fileMR = ref<File | null>(null);

const loading = ref(false);
const error = ref<string | null>(null);

async function handleAnalysis(fileHandwritting: File, fileMR: File) {
  loading.value = true;
  error.value = null;

  try {
    prediction.value = await predictionCombined(fileHandwritting, fileMR);
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

    <div class="flex flex-col w-full xl:px-40">
      <div class="flex flex-col lg:flex-row gap-4">
        <div class="container py-8 px-4">
          <div class="bg-white p-6 rounded-lg shadow-md">
  
            <UploadForm
              type="file"
              @file-selected="(selectedFile) => (fileHandwritting = selectedFile)"
            />
          </div>
        </div>

        <div class="container mx-auto py-8 px-4">
          <div class="bg-white p-6 rounded-lg shadow-md">
    
            <UploadForm
              type="goruntu"
              @file-selected="(selectedFile) => (fileMR = selectedFile)"
            />
          </div>
        </div>
      </div>
      <UButton
        class="flex w-40 mb-2 justify-center bg-teal-500 hover:bg-teal-400"
        size="xl"
        variant="outline"
        icon="ant-design-radius-setting-outlined"
        color="neutral"
        @click="
          fileMR && fileHandwritting
            ? handleAnalysis(fileHandwritting, fileMR)
            : (error = 'Lütfen iki dosya seçin!')
        "
      >
        Analiz et
      </UButton>

      <!-- Sonuclar -->
      <div
        v-if="prediction"
        class="p-6 bg-white rounded-lg shadow-md text-black"
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
            {{ prediction.probability }}
          </p>
          <p class="text-lg">
            <span class="font-medium">El Yazısı Olasılığı:</span>
            {{ prediction.handwriting_probability }}
          </p>
          <p class="text-lg">
            <span class="font-medium">MR Olasılığı:</span>
            {{ prediction.mr_probability }}
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
