<script setup lang="ts">
import { ref, computed } from "vue";

// Yeni bir prop tanımlıyoruz
const props = defineProps<{
  type: "goruntu" | "file";
}>();

const emit = defineEmits(["file-selected"]);

const selectedFile = ref<File | null>(null);
const loading = ref(false);

// Dosya seçildiğinde çalışacak fonksiyon
function handleFileChange(event: Event) {
  const input = event.target as HTMLInputElement;
  if (input.files && input.files[0]) {
    selectedFile.value = input.files[0];
    emit("file-selected", selectedFile.value);
  }
}

// props.type ve selectedFile'e göre previewUrl'ü ayarlayan computed property
const previewUrl = computed(() => {
  if (selectedFile.value) {
    if (props.type === "file") {
      return "/csvimg.png"; // CSV dosyaları için varsayılan resim
    }
    return URL.createObjectURL(selectedFile.value);
  }
  return null;
});
</script>

<template>
  <UCard class="bg-white p-6">
    <!-- Başlık, prop değerine göre değişiyor -->
    <h2 class="text-2xl font-bold text-teal-600 mb-4">
      {{
        props.type === "goruntu"
          ? "Beyin MR Görüntüsü Yükleme"
          : "El Yazısı Yükleme"
      }}
    </h2>
    <div class="mb-4">
      <label class="block mb-2 text-gray-700">Görüntü Seçin:</label>
      <input
        type="file"
        class="border border-gray-300 rounded p-2 w-full text-black"
        placeholder="Görüntü seç"
        @change="handleFileChange"
        :accept="props.type === 'goruntu' ? 'image/png, image/jpeg' : '.csv'"
      />
    </div>
    <div v-if="selectedFile" class="mb-4">
      <p class="text-gray-700">Seçilen dosya: {{ selectedFile.name }}</p>
      <img
        v-if="previewUrl"
        :src="previewUrl"
        class="mt-2 max-w-full h-auto max-h-64"
      />
    </div>

    <div v-if="loading" class="mt-4 text-center">
      <UAlert type="info" class="text-teal-600"> İşleniyor... </UAlert>
    </div>
  </UCard>
</template>
