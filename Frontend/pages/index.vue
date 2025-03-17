<script setup lang="ts">
import { ref } from "vue";
const name = ref("BrainPath");
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <NavBar />
    <div class="container mx-auto py-8 px-4">
      <h1 class="text-4xl font-bold text-teal-600 mb-6">
        {{ name }}
      </h1>
      <p class="text-xl text-gray-700 mb-8">
        Alzheimer hastalığı tespiti için yapay zeka destekli görüntü analizi
        platformu
      </p>

      <div class="bg-white p-6 rounded-lg shadow-md mb-8">
        <h2 class="text-2xl font-bold text-teal-600 mb-4">
          MR Görüntü Analizi
        </h2>
        <UploadForm />
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Ana sayfa stillemesi */
</style>
