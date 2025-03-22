<script setup lang="ts">
import { ref } from "vue";
const name = ref("BrainPath");

definePageMeta({
  title: "Ana Sayfa",
  description:
    "Alzheimer hastalığı tespiti için yapay zeka destekli görüntü analizi platformu",
});
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <NavBar />
    <div class="container mx-auto py-8 px-4">
      <h1 class="text-4xl font-bold text-teal-600">
        {{ name }}
      </h1>

      <p class="text-xl text-gray-700 mb-8">
        Alzheimer hastalığı tespiti için yapay zeka destekli görüntü analizi
        platformu
      </p>

      <div class="bg-white p-6 rounded-lg shadow-md">
        <h2 class="text-2xl font-bold text-teal-600 mb-4">
          Yapay Zeka Modelimiz
        </h2>
        <p class="text-gray-700 mb-4">
          BrainPath'in temelinde, son teknoloji derin öğrenme mimarisi
          kullanılarak geliştirilmiş bir yapay zeka modeli bulunur. Modelimiz,
          beyin MR görüntülerindeki Alzheimer belirtilerini yüksek doğrulukla
          tespit edebilmektedir.
        </p>

        <h2 class="text-2xl font-bold text-teal-600 mb-4 mt-8">
          Teknik Detaylar
        </h2>
        <ul class="list-disc pl-5 text-gray-700">
          <li class="mb-2">Convolutional Neural Network (CNN) mimarisi</li>
          <li class="mb-2">%95'in üzerinde doğruluk oranı</li>
          <li class="mb-2">1000+ MR görüntüsü ile eğitilmiş model</li>
          <li class="mb-2">Hızlı analiz ve sonuç üretme kapasitesi</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Ana sayfa stillemesi */
</style>
